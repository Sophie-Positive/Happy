 Competitor Social Media Monitor Prototype

> A lightweight Python prototype that automatically generates structured competitive intelligence reports from social media data using DeepSeek API.

 🎯 What This Project Does

This prototype simulates a real-world social media monitoring pipeline:

1. Data Ingestion – Fetches competitor social media posts (mock data ready, easily replaceable with real APIs)
2. LLM Processing – Sends raw text to DeepSeek API with carefully designed prompts
3. Structured Report – Generates a Chinese competitive intelligence briefing with four dimensions:
   - Core Summary (2-3 sentences)
   - Key Topics (2-3 main discussion themes)
   - Market Actions (new products, promotions, partnerships)
   - Sentiment Analysis (positive/neutral/negative)

🧪 Sample Output

Test target: @OpenAI (simulated Twitter data)

| Section | Content |
|---------|---------|
| Core Summary | OpenAI announced GPT-4o, a multimodal model accepting text/audio/image input; partnered with Financial Times for real-time journalism; CEO calls for AI adoption in education. |
| Key Topics | Multimodal model release / High-quality content partnership |
| Market Actions| GPT-4o launch / FT strategic collaboration |
| Sentiment | Positive, forward-looking, confident |

 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14+ | Core programming language |
| OpenAI SDK | Unified API interface |
| DeepSeek API | LLM inference (cost-effective for Chinese output) |
| Prompt Engineering | Structured system prompts for consistent output |
🔍 Methodological Reflection

This prototype is not an objective monitor but a situated analysis. Three limitations are acknowledged:

1. API bias – DeepSeek's Chinese-language optimization may flatten cultural nuance in multi-lingual data
2. Temporal myopia – Real-time monitoring obscures long-term discursive shifts
3. Platform determinism– Current data assumes X/Reddit represent all user voices, ignoring TikTok/WeChat silos

Future iteration: Add manual qualitative coding for 5% of sampled data to triangulate LLM output.


!/usr/bin/env python3
 -*- coding: utf-8 -*-
"""
话语漂移分析：企业危机公关的自我修正史
Discourse Self-Correction Monitor
"""

def generate_discourse_table():
    """生成话语漂移分析表格"""
    
    print("\n" + "="*60)
    print("话语漂移分析：以 [竞品X] 的 [Y事件] 为例")
    print("="*60 + "\n")
    
     表头
    print("时间窗口".ljust(12) + "主导叙事".ljust(25) + "回避策略".ljust(22) + "非人化语言".ljust(18) + "修正痕迹")
    print("-" * 95)
    
    数据行
    rows = [
        ("事件前3个月", "改变世界，开放透明", "无", "低频", "—"),
        ("爆发后72h", "沉默/我们注意到讨论", "完全沉默 → 模糊主语", "高频(被动语态占82%)", "明显断裂"),
        ("事件后1个月", "我们正在学习迭代", "话题转移至产品更新", "中频", "否认式承认"),
        ("事件后6个月", "行业共同挑战", "抽象化+集体化主语", "低频", "遗忘/正常化"),
    ]
    
    for row in rows:
        print(row[0].ljust(12) + row[1].ljust(25) + row[2].ljust(22) + row[3].ljust(18) + row[4])
    
    print("\n" + "🔍 关键发现".center(60, "="))
    print("""
1. 争议发生后72小时内，被动语态使用率从5%飙升至82%
2. "透明"一词在事件后完全消失，6个月后被"合规"替代
3. 品牌从未使用"道歉"或"错误"等直接承认词
    """)

if __name__ == "__main__":
    generate_discourse_table()
