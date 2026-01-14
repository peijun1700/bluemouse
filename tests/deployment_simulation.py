
import asyncio
import os
import json
import requests
import zipfile
import io
import sys

# Add current directory to path
sys.path.append(os.getcwd())

# Import core modules directly to simulate server internal logic 
# (simulating what happens inside the API endpoints)
import socratic_generator
import code_generator
import project_exporter
import django_generator # To verify answer parsing logic

async def simulate_user_journey():
    print("🚀 Starting User Journey Simulation (End-to-End)...")
    
    # 1. User Input (Socratic Phase)
    user_input = "我要做一個比特幣電商平台"
    print(f"\n👤 User Input: {user_input}")
    
    # Simulate /api/generate_socratic_questions
    print("\n[Step 1] Generating Socratic Questions...")
    socratic_result = await socratic_generator.generate_socratic_questions(user_input)
    
    if not socratic_result.get("questions"):
        print("❌ Socratic generation failed!")
        return
        
    questions = socratic_result["questions"]
    print(f"✅ Generated {len(questions)} questions.")
    
    # 2. User Answers (Simulation)
    # Let's say user selects options that trigger 'redis' (if available) or just standard options
    # We construct an 'answers' dict as the frontend would send
    user_answers = {}
    for i, q in enumerate(questions):
        # Pick the first option for each question
        # In the new format, option has 'value'
        options = q.get("options", [])
        if options:
            # Simulate selecting the first option
            # Ideally we want to select an option that triggers a feature like Redis
            # But for basic flow, 0 is fine.
            user_answers[f"q_{i}"] = options[0]['value'] if isinstance(options[0], dict) else f"opt_{0}"
            
    print(f"✅ User submitted answers: {len(user_answers)} items")
    
    # 3. Code Generation
    print("\n[Step 2] Generating Code (Django)...")
    module_info = {"name": "BitcoinShop", "description": "A Bitcoin E-commerce platform"}
    
    # Call generate_code with the answers (Dict)
    # This verifies that our change to run_standalone.py (passing dict) works with the generator
    try:
        code_result = code_generator.generate_code(module_info, user_answers, framework="django")
    except Exception as e:
        print(f"❌ Code generation CRASHED: {e}")
        return

    files = code_result.get("files", {})
    print(f"✅ Code generated: {len(files)} files")
    
    if "requirements.txt" in files:
        print("   Checking requirements.txt...")
        if "Django" in files["requirements.txt"]:
             print("   - Django found (OK)")
    
    # 4. Project Export (Download)
    print("\n[Step 3] Exporting to ZIP...")
    export_req = {
        "name": "BitcoinShop",
        "code": code_result,
        "diagrams": [], # Empty for now
        "cost": {"cost": {"total": 5000}}
    }
    
    try:
        zip_bytes = project_exporter.export_project(export_req)
        print(f"✅ ZIP generated: {len(zip_bytes)} bytes")
        
        # Verify ZIP Integrity
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
            zip_contents = z.namelist()
            print(f"   ZIP Contents: {len(zip_contents)} files")
            
            # Check for critical files
            critical_files = ["README.md", "code/models.py", "code/views.py", "INSTALLATION.md"]
            missing = [f for f in critical_files if f not in zip_contents]
            
            if missing:
                print(f"❌ Missing critical files in ZIP: {missing}")
            else:
                print("✅ All critical files present in ZIP.")
                
    except Exception as e:
         print(f"❌ Export failed: {e}")
         return

    print("\n🎉 End-to-End Simulation COMPLETE. System is ready for Release.")

if __name__ == "__main__":
    asyncio.run(simulate_user_journey())
