#!/usr/bin/env python3
"""
批量失敗案例生成器
為真實函數生成多種錯誤變體,並記錄到 data_trap.jsonl
"""

import json
import ast
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple


class BatchErrorGenerator:
    def __init__(self, project_dir: str = "."):
        self.project_dir = Path(project_dir)
        self.data_trap_file = self.project_dir / "data_trap.jsonl"
        self.generated_count = 0
        
    def generate_error_variants(self, correct_code: str, function_name: str) -> List[Tuple[str, str]]:
        """生成錯誤變體"""
        variants = []
        
        # 1. 缺少類型提示
        variant1 = self.remove_type_hints(correct_code)
        if variant1 != correct_code:
            variants.append(("缺少類型提示", variant1))
        
        # 2. 參數名錯誤
        variant2 = self.change_param_names(correct_code)
        if variant2 != correct_code:
            variants.append(("參數名錯誤", variant2))
        
        # 3. 返回類型錯誤
        variant3 = self.change_return_type(correct_code)
        if variant3 != correct_code:
            variants.append(("返回類型錯誤", variant3))
        
        # 4. 函數名錯誤
        variant4 = self.change_function_name(correct_code, function_name)
        if variant4 != correct_code:
            variants.append(("函數名錯誤", variant4))
        
        # 5. 語法錯誤
        variant5 = self.introduce_syntax_error(correct_code)
        if variant5 != correct_code:
            variants.append(("語法錯誤", variant5))
        
        # 6. 缺少 Docstring
        variant6 = self.remove_docstring(correct_code)
        if variant6 != correct_code:
            variants.append(("缺少文檔", variant6))
        
        # 7. 參數順序錯誤
        variant7 = self.swap_parameters(correct_code)
        if variant7 != correct_code:
            variants.append(("參數順序錯誤", variant7))
        
        # 8. 缺少錯誤處理
        variant8 = self.remove_error_handling(correct_code)
        if variant8 != correct_code:
            variants.append(("缺少錯誤處理", variant8))
        
        return variants
    
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
            ("data", "dataset"),
            ("filepath", "file_path"),
            ("strategy", "method"),
            ("column", "col"),
            ("threshold", "thresh")
        ]
        
        for old, new in replacements:
            if f"{old}:" in code or f"{old}," in code or f"{old})" in code:
                return code.replace(f"{old}:", f"{new}:").replace(
                    f"{old},", f"{new},").replace(f"{old})", f"{new})")
        return code
    
    def change_return_type(self, code: str) -> str:
        """修改返回類型"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.returns:
                    # List -> Dict, Dict -> List
                    if isinstance(node.returns, ast.Subscript):
                        if isinstance(node.returns.value, ast.Name):
                            if node.returns.value.id == "List":
                                node.returns.value.id = "Dict"
                            elif node.returns.value.id == "Dict":
                                node.returns.value.id = "List"
            return ast.unparse(tree)
        except:
            return code
    
    def change_function_name(self, code: str, original_name: str) -> str:
        """修改函數名稱"""
        return code.replace(f"def {original_name}(", f"def wrong_{original_name}(", 1)
    
    def introduce_syntax_error(self, code: str) -> str:
        """引入語法錯誤"""
        # 移除一個冒號
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
                        # 交換前兩個參數
                        node.args.args[0], node.args.args[1] = node.args.args[1], node.args.args[0]
                        break
            return ast.unparse(tree)
        except:
            return code
    
    def remove_error_handling(self, code: str) -> str:
        """移除錯誤處理"""
        # 簡單移除 raise 語句
        lines = code.split('\n')
        filtered_lines = [line for line in lines if 'raise ' not in line]
        return '\n'.join(filtered_lines)
    
    def log_to_data_trap(self, function_name: str, error_type: str, error_code: str, errors: List[str]):
        """記錄到 data_trap.jsonl"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "node_id": f"test_{function_name}",
            "function_name": function_name,
            "error_type": error_type,
            "code": error_code,
            "errors": errors
        }
        
        with open(self.data_trap_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        
        self.generated_count += 1
    
    def simple_validate(self, code: str, expected_name: str) -> Dict:
        """簡化的驗證邏輯"""
        errors = []
        
        # 檢查語法
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return {"success": False, "errors": [f"語法錯誤: {str(e)}"]}
        
        # 檢查函數名
        func_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == expected_name:
                    func_found = True
                    # 檢查類型提示
                    if not all(arg.annotation for arg in node.args.args):
                        errors.append("缺少類型提示")
                    if not node.returns:
                        errors.append("缺少返回類型提示")
                    # 檢查 Docstring
                    if not (node.body and isinstance(node.body[0], ast.Expr) and
                           isinstance(node.body[0].value, ast.Constant)):
                        errors.append("缺少 Docstring")
                break
        
        if not func_found:
            errors.append(f"找不到函數 {expected_name}")
        
        return {"success": len(errors) == 0, "errors": errors}
    
    def process_file(self, file_path: Path) -> int:
        """處理單個檔案,生成錯誤案例"""
        print(f"\n{'='*60}")
        print(f"📝 處理檔案: {file_path.name}")
        print(f"{'='*60}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        # 提取所有函數
        try:
            tree = ast.parse(code)
        except SyntaxError:
            print(f"  ⚠️  無法解析檔案")
            return 0
        
        functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        
        if not functions:
            print(f"  ⚠️  沒有找到函數定義")
            return 0
        
        count = 0
        for func_node in functions:
            function_name = func_node.name
            
            # 提取函數代碼
            func_code = ast.unparse(func_node)
            
            print(f"\n  🔧 函數: {function_name}")
            
            # 生成錯誤變體
            variants = self.generate_error_variants(func_code, function_name)
            
            for error_type, error_code in variants:
                # 驗證錯誤是否被檢測到
                result = self.simple_validate(error_code, function_name)
                
                if not result["success"]:
                    # 記錄失敗案例
                    self.log_to_data_trap(function_name, error_type, error_code, result["errors"])
                    print(f"    ✅ {error_type}: 已記錄")
                    count += 1
                else:
                    print(f"    ⚠️  {error_type}: 未被檢測到")
        
        return count
    
    def run(self, target_count: int = 50):
        """批量生成失敗案例"""
        print("🚀 開始批量生成失敗案例...")
        print(f"目標: {target_count} 個失敗案例\n")
        
        # 找到所有 Python 檔案
        python_files = []
        exclude_patterns = [
            "test_", "setup_", "server.py", "mmla_parser.py",
            "training_validator.py", "error_generator.py", "batch_error_generator.py"
        ]
        
        for file in self.project_dir.glob("*.py"):
            if not any(pattern in file.name for pattern in exclude_patterns):
                python_files.append(file)
        
        print(f"找到 {len(python_files)} 個 Python 檔案\n")
        
        # 處理每個檔案
        for file in python_files:
            if self.generated_count >= target_count:
                break
            self.process_file(file)
        
        # 生成報告
        self.generate_report()
    
    def generate_report(self):
        """生成報告"""
        print(f"\n{'='*60}")
        print("📊 失敗案例生成報告")
        print(f"{'='*60}\n")
        
        print(f"✅ 總共生成: {self.generated_count} 個失敗案例")
        print(f"📄 儲存位置: {self.data_trap_file}")
        
        # 統計錯誤類型
        error_types = {}
        try:
            with open(self.data_trap_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        entry = json.loads(line)
                        error_type = entry.get("error_type", "未知")
                        error_types[error_type] = error_types.get(error_type, 0) + 1
        except FileNotFoundError:
            pass
        
        if error_types:
            print("\n錯誤類型分佈:")
            for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
                print(f"  - {error_type}: {count} 個")
        
        print(f"\n💡 下一步: 執行 `python3 analyze_data.py` 查看詳細分析")


if __name__ == "__main__":
    generator = BatchErrorGenerator()
    generator.run(target_count=50)
