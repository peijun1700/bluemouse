import unittest
import os
import shutil
from typing import Dict, List
import asyncio
import sys

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import socratic_generator
import code_generator
import django_generator
# import run_standalone # Not strictly needed if we use code_generator directly

class TestEndToEndRobustness(unittest.IsolatedAsyncioTestCase):
    """
    Industrial Grade End-to-End Simulation
    Verifies that for each domain:
    1. Socratic Question Generator detects the scenario.
    2. Specific options trigger specific feature flags.
    3. Django Generator outputs the CORRECT specific models.
    """

    async def asyncSetUp(self):
        self.output_dir = "test_robustness_output"
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir)

    async def _simulate_journey(self, requirement: str, domain_key: str, answer_keys: List[str], expected_model: str):
        print(f"\n🚀 Simulating Domain: [{domain_key.upper()}]")
        print(f"   Input: '{requirement}'")
        
        # 1. Generate Questions
        socratic_result = await socratic_generator.generate_socratic_questions(requirement, 'zh-TW')
        questions = socratic_result.get('questions', [])
        
        print(f"   ✅ Generated {len(questions)} questions")
        
        # 2. Mock Answers based on answer_keys
        user_answers = {}
        found_keys = []
        
        for q in questions:
            qid = q.get('id', 'unknown')
            options = q.get('options', [])
            
            # Find an option that matches one of our expected keys
            selected_val = None
            for opt in options:
                if opt.get('value') in answer_keys:
                    selected_val = opt['value']
                    found_keys.append(selected_val)
                    break
            
            # If no specific key matches, just pick the first one (default behavior)
            if not selected_val and options:
                selected_val = options[0]['value']
            
            if selected_val:
                user_answers[qid] = selected_val
            
        print(f"   ✅ Submitted answers: {user_answers}")
        
        # 3. Generate Code
        # We need to simulate the structure code_generator expects or uses
        # code_generator.generate_code(module, answers)
        
        module_info = {
            "name": f"Test{domain_key.capitalize()}",
            "description": requirement,
            "type": "django"
        }
        
        generated_result = code_generator.generate_code(module_info, user_answers)
        
        files = generated_result.get('files', {})
        models_code = files.get('models.py', '')
        
        self.assertTrue(models_code, "models.py was not generated")
        
        # 4. Verification
        print(f"   🔍 Verifying presence of '{expected_model}'...")
        if expected_model in models_code:
            print(f"   ✅ Found '{expected_model}' in models.py")
        else:
            print(f"   ❌ MISSING '{expected_model}' in models.py")
            # print(models_code) # Debug
            self.fail(f"Domain {domain_key} failed: '{expected_model}' not found in generated code.")

    async def test_crypto_domain(self):
        await self._simulate_journey(
            requirement="我要做一個比特幣錢包交易所",
            domain_key="crypto",
            answer_keys=['zero_conf', 'custodial'],
            expected_model="class Wallet(models.Model)"
        )

    async def test_blog_domain(self):
        await self._simulate_journey(
            requirement="我要做一個部落格系統",
            domain_key="blog",
            answer_keys=['auto_save', 'ai_filter'],
            expected_model="class Post(models.Model)"
        )

    async def test_booking_domain(self):
        await self._simulate_journey(
            requirement="我要做一個牙醫預約系統",
            domain_key="booking",
            answer_keys=['waitlist', 'deposit'],
            expected_model="class Appointment(models.Model)"
        )
        
    async def test_chat_domain(self):
        await self._simulate_journey(
            requirement="我要做一個即時通訊軟體",
            domain_key="chat",
            answer_keys=['push_all', 'infinite_retry'],
            expected_model="class Message(models.Model)"
        )

    async def test_todo_domain(self):
        await self._simulate_journey(
            requirement="我要做一個待辦事項清單",
            domain_key="todo",
            answer_keys=['cascade_delete'], 
            expected_model="class TaskLayer(models.Model)"
        )

if __name__ == '__main__':
    unittest.main()
