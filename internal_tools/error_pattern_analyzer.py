#!/usr/bin/env python3
"""
Error Pattern Analyzer
錯誤模式深度分析工具
找出最有價值的錯誤模式和組合
"""

import json
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set
import itertools


class ErrorPatternAnalyzer:
    """錯誤模式分析器"""
    
    def __init__(self, data_trap_file: str = "data_trap.jsonl"):
        self.data_trap_file = Path(data_trap_file)
        self.records = []
        self.load_data()
    
    def load_data(self):
        """載入數據"""
        if not self.data_trap_file.exists():
            print(f"❌ 找不到文件: {self.data_trap_file}")
            return
        
        with open(self.data_trap_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        self.records.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    
    def find_error_combinations(self) -> Dict[Tuple[str, ...], int]:
        """找出常見的錯誤組合"""
        # 按函數分組
        function_errors = defaultdict(list)
        
        for record in self.records:
            func_name = record.get('function_name', 'unknown')
            error_type = record.get('error_type', 'unknown')
            function_errors[func_name].append(error_type)
        
        # 找出錯誤組合
        combinations = Counter()
        
        for func_name, errors in function_errors.items():
            # 2 個錯誤的組合
            for combo in itertools.combinations(set(errors), 2):
                combinations[tuple(sorted(combo))] += 1
            
            # 3 個錯誤的組合
            if len(set(errors)) >= 3:
                for combo in itertools.combinations(set(errors), 3):
                    combinations[tuple(sorted(combo))] += 1
        
        return dict(combinations.most_common(20))
    
    def identify_google_weak_scenarios(self) -> Dict[str, List[Dict]]:
        """識別 Google 最容易出錯的場景"""
        scenarios = defaultdict(list)
        
        # 定義場景模式
        scenario_patterns = {
            "複雜類型 + 邊界條件": lambda r: any(x in r.get('error_type', '').lower() for x in ['類型', 'union', '泛型']) and 
                                            any(x in r.get('error_type', '').lower() for x in ['溢出', '零值', '空值']),
            
            "資源管理 + 並發": lambda r: any(x in r.get('error_type', '').lower() for x in ['記憶體', '洩漏', '未釋放']) and
                                       any(x in r.get('error_type', '').lower() for x in ['競態', '死鎖']),
            
            "安全 + 輸入驗證": lambda r: any(x in r.get('error_type', '').lower() for x in ['注入', 'eval', '硬編碼']) and
                                        any(x in r.get('error_type', '').lower() for x in ['驗證', '清理']),
            
            "參數處理 + 類型": lambda r: any(x in r.get('error_type', '').lower() for x in ['參數', '順序', '數量']) and
                                       any(x in r.get('error_type', '').lower() for x in ['類型', '提示']),
            
            "極端值 + 性能": lambda r: any(x in r.get('error_type', '').lower() for x in ['超大', '超長', '溢出']) and
                                     any(x in r.get('error_type', '').lower() for x in ['記憶體', '性能'])
        }
        
        for record in self.records:
            for scenario_name, pattern_func in scenario_patterns.items():
                if pattern_func(record):
                    scenarios[scenario_name].append({
                        'function': record.get('function_name'),
                        'error_type': record.get('error_type'),
                        'category': record.get('category', 'unknown')
                    })
        
        return dict(scenarios)
    
    def calculate_commercial_value(self) -> Dict[str, any]:
        """計算商業價值排序"""
        error_values = {}
        
        # 定義價值係數
        value_coefficients = {
            # 高價值:企業常見且難以檢測
            "類型推斷": 1000,
            "複雜泛型": 1000,
            "Union 類型": 800,
            "邊界條件": 800,
            "資源管理": 900,
            "記憶體洩漏": 1000,
            "安全問題": 1200,  # 最高價值
            "注入攻擊": 1200,
            
            # 中價值:常見但相對容易檢測
            "參數處理": 500,
            "類型提示": 400,
            "文檔": 300,
            
            # 低價值:基礎錯誤
            "語法錯誤": 200,
            "函數名": 200
        }
        
        # 計算每種錯誤的價值
        error_counts = Counter()
        for record in self.records:
            error_type = record.get('error_type', '')
            error_counts[error_type] += 1
        
        for error_type, count in error_counts.items():
            # 基礎價值
            base_value = count * 100
            
            # 加成係數
            bonus = 1.0
            for keyword, coefficient in value_coefficients.items():
                if keyword.lower() in error_type.lower():
                    bonus = coefficient / 100
                    break
            
            total_value = base_value * bonus
            error_values[error_type] = {
                'count': count,
                'base_value': base_value,
                'bonus_multiplier': bonus,
                'total_value': int(total_value)
            }
        
        # 排序
        sorted_values = dict(sorted(error_values.items(), 
                                   key=lambda x: x[1]['total_value'], 
                                   reverse=True))
        
        return sorted_values
    
    def identify_high_value_domains(self) -> Dict[str, Dict]:
        """識別高價值領域"""
        domain_stats = defaultdict(lambda: {
            'error_count': 0,
            'unique_errors': set(),
            'functions': set(),
            'categories': set()
        })
        
        # 定義領域關鍵字
        domain_keywords = {
            '資安': ['encrypt', 'hash', 'password', 'jwt', 'token', 'sanitize', 'sql', 'security'],
            '金融': ['interest', 'loan', 'stock', 'portfolio', 'roi', 'npv', 'currency', 'tax'],
            '醫療': ['bmi', 'heart', 'calorie', 'blood', 'pregnancy', 'medical', 'health'],
            '數據處理': ['load', 'clean', 'merge', 'group', 'encode', 'split', 'dataset'],
            '機器學習': ['train', 'model', 'predict', 'evaluate', 'regression', 'ml'],
            '複雜類型': ['union', 'generic', 'callable', 'typevar', 'protocol', 'literal']
        }
        
        for record in self.records:
            func_name = record.get('function_name', '').lower()
            error_type = record.get('error_type', '')
            category = record.get('category', 'unknown')
            
            # 判斷領域
            for domain, keywords in domain_keywords.items():
                if any(keyword in func_name for keyword in keywords):
                    domain_stats[domain]['error_count'] += 1
                    domain_stats[domain]['unique_errors'].add(error_type)
                    domain_stats[domain]['functions'].add(func_name)
                    domain_stats[domain]['categories'].add(category)
        
        # 計算價值
        domain_values = {}
        for domain, stats in domain_stats.items():
            # 價值 = 錯誤數量 × 獨特錯誤類型 × 函數數量
            value = (stats['error_count'] * 
                    len(stats['unique_errors']) * 
                    len(stats['functions']) * 100)
            
            domain_values[domain] = {
                'error_count': stats['error_count'],
                'unique_errors': len(stats['unique_errors']),
                'functions': len(stats['functions']),
                'categories': len(stats['categories']),
                'estimated_value': value
            }
        
        return dict(sorted(domain_values.items(), 
                          key=lambda x: x[1]['estimated_value'], 
                          reverse=True))
    
    def generate_insights_report(self) -> str:
        """生成洞察報告"""
        report = []
        report.append("=" * 60)
        report.append("💎 錯誤模式深度分析報告")
        report.append("=" * 60)
        
        # 1. 錯誤組合分析
        report.append("\n🔗 常見錯誤組合 (Top 10)")
        combinations = self.find_error_combinations()
        for i, (combo, count) in enumerate(list(combinations.items())[:10], 1):
            combo_str = " + ".join(combo[:2])  # 只顯示前 2 個
            report.append(f"  {i}. {combo_str}: {count} 次")
        
        # 2. Google 弱點場景
        report.append("\n🎯 Google 最容易出錯的場景")
        scenarios = self.identify_google_weak_scenarios()
        for scenario, cases in sorted(scenarios.items(), key=lambda x: len(x[1]), reverse=True):
            report.append(f"  - {scenario}: {len(cases)} 個案例")
        
        # 3. 商業價值排序
        report.append("\n💰 錯誤類型商業價值排序 (Top 10)")
        values = self.calculate_commercial_value()
        for i, (error_type, value_info) in enumerate(list(values.items())[:10], 1):
            report.append(f"  {i}. {error_type}")
            report.append(f"     數量: {value_info['count']}, 估值: ${value_info['total_value']:,}")
        
        # 4. 高價值領域
        report.append("\n🏆 高價值領域排序")
        domains = self.identify_high_value_domains()
        for domain, stats in domains.items():
            report.append(f"  - {domain}:")
            report.append(f"    錯誤: {stats['error_count']}, 函數: {stats['functions']}")
            report.append(f"    估值: ${stats['estimated_value']:,}")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)
    
    def save_insights_report(self, filename: str = "error_pattern_insights.md"):
        """儲存洞察報告"""
        combinations = self.find_error_combinations()
        scenarios = self.identify_google_weak_scenarios()
        values = self.calculate_commercial_value()
        domains = self.identify_high_value_domains()
        
        report = f"""# 💎 錯誤模式深度分析報告

**分析日期**: 2026-01-09  
**數據來源**: {len(self.records)} 個失敗案例

---

## 🔗 常見錯誤組合分析

這些錯誤經常一起出現,代表 Google 在這些組合上特別弱:

| 排名 | 錯誤組合 | 出現次數 | 商業價值 |
|------|---------|---------|---------|
"""
        
        for i, (combo, count) in enumerate(list(combinations.items())[:15], 1):
            combo_str = " + ".join(combo[:2])
            value = "高" if count > 10 else "中" if count > 5 else "低"
            report += f"| {i} | {combo_str} | {count} | {value} |\n"
        
        report += f"""
---

## 🎯 Google 最容易出錯的場景

這些場景是 Google 的核心弱點:

"""
        for scenario, cases in sorted(scenarios.items(), key=lambda x: len(x[1]), reverse=True):
            report += f"### {scenario} ({len(cases)} 個案例)\n\n"
            report += f"**為什麼重要**: 這種場景組合是 Google 最難處理的\n\n"
            report += f"**商業價值**: ${len(cases) * 500:,}\n\n"
        
        report += f"""---

## 💰 錯誤類型商業價值排序

根據企業需求和檢測難度計算的商業價值:

| 排名 | 錯誤類型 | 數量 | 基礎價值 | 加成 | 總價值 |
|------|---------|------|---------|------|--------|
"""
        
        for i, (error_type, value_info) in enumerate(list(values.items())[:20], 1):
            report += f"| {i} | {error_type} | {value_info['count']} | ${value_info['base_value']:,} | {value_info['bonus_multiplier']:.1f}x | ${value_info['total_value']:,} |\n"
        
        report += f"""
---

## 🏆 高價值領域分析

哪些領域最值得深入?

"""
        for domain, stats in domains.items():
            report += f"### {domain}\n\n"
            report += f"- **錯誤案例**: {stats['error_count']} 個\n"
            report += f"- **獨特錯誤**: {stats['unique_errors']} 種\n"
            report += f"- **涵蓋函數**: {stats['functions']} 個\n"
            report += f"- **估值**: ${stats['estimated_value']:,}\n\n"
        
        report += f"""---

## 💡 關鍵洞察

### 最有價值的錯誤類型

1. **安全相關錯誤** (價值係數 12x)
   - 注入攻擊、不安全的 eval
   - 企業願意付最高價格

2. **複雜類型錯誤** (價值係數 10x)
   - 嵌套泛型、Union 類型
   - Google 最難處理

3. **資源管理錯誤** (價值係數 9-10x)
   - 記憶體洩漏、資源未釋放
   - 生產環境最致命

### 最值得深入的領域

根據分析,以下領域最值得繼續擴充:

1. **資安領域** - 高價值,企業需求大
2. **複雜類型** - Google 核心弱點
3. **金融領域** - 商業價值高

---

## 🚀 商業化建議

### 定價策略

基於錯誤價值分析:

- **基礎訂閱**: $99/月 (基礎錯誤檢測)
- **專業訂閱**: $299/月 (包含安全 + 複雜類型)
- **企業訂閱**: $999/月 (完整數據庫訪問)

### 目標客戶

1. **金融科技公司** - 需要安全 + 金融領域
2. **醫療科技公司** - 需要醫療 + 安全領域
3. **AI/ML 公司** - 需要複雜類型 + 數據處理

---

**結論**: 你的數據金庫中,安全相關和複雜類型錯誤最有商業價值!
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 洞察報告已儲存: {filename}")


# 執行分析
if __name__ == "__main__":
    analyzer = ErrorPatternAnalyzer()
    
    # 顯示報告
    print(analyzer.generate_insights_report())
    
    # 儲存詳細報告
    analyzer.save_insights_report()
    
    print("\n💡 提示: 詳細洞察報告已儲存為 error_pattern_insights.md")
