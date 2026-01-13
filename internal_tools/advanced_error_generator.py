#!/usr/bin/env python3
"""
超強錯誤生成器 - Advanced Error Generator
從 8 種錯誤類型擴展到 20 種
目標:每個函數生成 20 個錯誤變體
"""

import ast
import json
import random
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple


class AdvancedErrorGenerator:
    def __init__(self):
        self.error_templates = {
            # 原有 8 種
            "missing_type_hints": self.remove_type_hints,
            "wrong_param_names": self.change_param_names,
            "wrong_return_type": self.change_return_type,
            "undeclared_dependency": self.add_undeclared_import,
            "wrong_function_name": self.change_function_name,
            "syntax_error": self.introduce_syntax_error,
            "missing_docstring": self.remove_docstring,
            "swap_parameters": self.swap_parameters,
            
            # 新增 12 種 (Google 容易出錯的地方)
            "super_long_param_name": self.super_long_param_name,
            "nested_type_error": self.nested_type_error,
            "complex_generic": self.complex_generic,
            "default_value_type_mismatch": self.default_value_type_mismatch,
            "mutable_default_arg": self.mutable_default_arg,
            "param_name_builtin_conflict": self.param_name_builtin_conflict,
            "too_many_params": self.too_many_params,
            "missing_import": self.missing_import,
            "unsafe_eval": self.unsafe_eval,
            "hardcoded_secret": self.hardcoded_secret,
            "missing_input_validation": self.missing_input_validation,
            "no_error_handling": self.no_error_handling,
        }
    
    # ========== 原有錯誤類型 ==========
    
    def remove_type_hints(self, code: str) -> str:
        """移除類型提示"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    for arg in node.args.args:
                        arg.annotation = None
                    node.returns = None
            return ast.unparse(tree)
        except:
            return code
    
    def change_param_names(self, code: str) -> str:
        """修改參數名稱"""
        replacements = [
            ("data", "dataset"), ("filepath", "file_path"),
            ("strategy", "method"), ("column", "col"),
            ("threshold", "thresh"), ("value", "val")
        ]
        for old, new in replacements:
            if f"{old}:" in code or f"{old}," in code:
                return code.replace(f"{old}:", f"{new}:").replace(f"{old},", f"{new},")
        return code
    
    def change_return_type(self, code: str) -> str:
        """修改返回類型"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.returns:
                    if isinstance(node.returns, ast.Name):
                        if node.returns.id == "dict":
                            node.returns.id = "str"
                        elif node.returns.id == "str":
                            node.returns.id = "dict"
            return ast.unparse(tree)
        except:
            return code
    
    def add_undeclared_import(self, code: str) -> str:
        """添加未聲明的依賴"""
        imports = ["import requests", "import pandas", "import numpy", "from flask import Flask"]
        return f"{random.choice(imports)}\n{code}"
    
    def change_function_name(self, code: str) -> str:
        """修改函數名稱"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    node.name = f"wrong_{node.name}"
                    break
            return ast.unparse(tree)
        except:
            return code
    
    def introduce_syntax_error(self, code: str) -> str:
        """引入語法錯誤"""
        if "def " in code and "):" in code:
            return code.replace("):", ")", 1)
        return code
    
    def remove_docstring(self, code: str) -> str:
        """移除 Docstring"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if (node.body and isinstance(node.body[0], ast.Expr) and
                        isinstance(node.body[0].value, ast.Constant)):
                        node.body.pop(0)
            return ast.unparse(tree)
        except:
            return code
    
    def swap_parameters(self, code: str) -> str:
        """交換參數順序"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if len(node.args.args) >= 2:
                        node.args.args[0], node.args.args[1] = node.args.args[1], node.args.args[0]
                        break
            return ast.unparse(tree)
        except:
            return code
    
    # ========== 新增錯誤類型 (Google 容易出錯) ==========
    
    def super_long_param_name(self, code: str) -> str:
        """超長參數名 (測試 Google 的處理能力)"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if node.args.args:
                        node.args.args[0].arg = "very_very_very_long_parameter_name_that_exceeds_normal_length_and_might_cause_issues"
                        break
            return ast.unparse(tree)
        except:
            return code
    
    def nested_type_error(self, code: str) -> str:
        """嵌套類型錯誤"""
        # 將簡單類型改成複雜嵌套
        code = code.replace("List[str]", "List[Dict[str, List[int]]]")
        code = code.replace("Dict[str, Any]", "Dict[str, List[Dict[str, Any]]]")
        return code
    
    def complex_generic(self, code: str) -> str:
        """複雜泛型"""
        code = code.replace("-> dict", "-> Union[List[str], Dict[str, int], None]")
        code = code.replace("-> list", "-> Optional[Tuple[str, int, float]]")
        return code
    
    def default_value_type_mismatch(self, code: str) -> str:
        """默認值類型不符"""
        code = code.replace('= 0', '= "0"')
        code = code.replace('= []', '= "{}"')
        code = code.replace('= True', '= "True"')
        return code
    
    def mutable_default_arg(self, code: str) -> str:
        """可變默認參數 (Python 陷阱)"""
        code = code.replace('= None', '= []')
        code = code.replace('Optional[List', 'List')
        return code
    
    def param_name_builtin_conflict(self, code: str) -> str:
        """參數名與內建衝突"""
        replacements = [
            ("data", "list"), ("items", "dict"),
            ("value", "str"), ("count", "int")
        ]
        for old, new in replacements:
            if f"{old}:" in code:
                return code.replace(f"{old}:", f"{new}:")
        return code
    
    def too_many_params(self, code: str) -> str:
        """過多參數"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # 添加很多參數
                    for i in range(10):
                        new_arg = ast.arg(arg=f"param_{i}", annotation=ast.Name(id="str"))
                        node.args.args.append(new_arg)
                    break
            return ast.unparse(tree)
        except:
            return code
    
    def missing_import(self, code: str) -> str:
        """缺少必要的 import"""
        # 移除所有 import 語句
        lines = code.split('\n')
        filtered = [line for line in lines if not line.strip().startswith('import') and not line.strip().startswith('from')]
        return '\n'.join(filtered)
    
    def unsafe_eval(self, code: str) -> str:
        """不安全的 eval/exec"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # 在函數開頭添加 eval
                    eval_node = ast.Expr(value=ast.Call(
                        func=ast.Name(id='eval'),
                        args=[ast.Constant(value='user_input')],
                        keywords=[]
                    ))
                    node.body.insert(1, eval_node)
                    break
            return ast.unparse(tree)
        except:
            return code
    
    def hardcoded_secret(self, code: str) -> str:
        """硬編碼敏感資訊"""
        secrets = [
            'API_KEY = "sk-1234567890abcdef"',
            'PASSWORD = "admin123"',
            'SECRET_TOKEN = "secret_token_here"'
        ]
        return f"{random.choice(secrets)}\n{code}"
    
    def missing_input_validation(self, code: str) -> str:
        """缺少輸入驗證 (移除所有 if 檢查)"""
        lines = code.split('\n')
        filtered = [line for line in lines if 'if ' not in line and 'raise ' not in line]
        return '\n'.join(filtered)
    
    def no_error_handling(self, code: str) -> str:
        """缺少錯誤處理 (移除 try-except)"""
        lines = code.split('\n')
        filtered = [line for line in lines if 'try:' not in line and 'except' not in line]
        return '\n'.join(filtered)
    
    # ========== 生成邏輯 ==========
    
    def generate_all_variants(self, correct_code: str, function_name: str) -> List[Tuple[str, str]]:
        """為一個函數生成所有錯誤變體"""
        variants = []
        
        for error_type, generator_func in self.error_templates.items():
            try:
                error_code = generator_func(correct_code)
                if error_code != correct_code:  # 確保有變化
                    variants.append((error_type, error_code))
            except Exception as e:
                print(f"  ⚠️  生成 {error_type} 失敗: {e}")
        
        return variants
    
    def log_to_data_trap(self, function_name: str, error_type: str, error_code: str, errors: List[str]):
        """記錄到 data_trap.jsonl"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "node_id": f"advanced_{function_name}",
            "function_name": function_name,
            "error_type": error_type,
            "code": error_code,
            "errors": errors
        }
        
        with open("data_trap.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# 測試
if __name__ == "__main__":
    generator = AdvancedErrorGenerator()
    
    print("=" * 60)
    print("🚀 超強錯誤生成器測試")
    print("=" * 60)
    print(f"\n支援的錯誤類型: {len(generator.error_templates)} 種")
    print("\n錯誤類型列表:")
    for i, error_type in enumerate(generator.error_templates.keys(), 1):
        print(f"  {i}. {error_type}")
    
    # 測試代碼
    test_code = """
def calculate_interest(principal: float, rate: float, time: int) -> float:
    '''計算利息'''
    if principal <= 0:
        raise ValueError("本金必須大於 0")
    return principal * rate * time
"""
    
    print(f"\n\n測試函數: calculate_interest")
    print(f"原始代碼長度: {len(test_code)} 字符")
    
    variants = generator.generate_all_variants(test_code, "calculate_interest")
    
    print(f"\n✅ 成功生成 {len(variants)} 個錯誤變體")
    print(f"\n目標: 每個函數 20 個錯誤")
    print(f"當前: 每個函數 {len(variants)} 個錯誤")
    print(f"完成度: {len(variants)/20*100:.1f}%")
    
    print("\n" + "=" * 60)
    print("🎉 超強錯誤生成器準備就緒!")
    print("=" * 60)
