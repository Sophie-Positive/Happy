# Competitor Social Media Monitor Prototype

> 基于 DeepSeek API 的竞品社媒舆情监控原型，自动生成结构化中文简报。

## 🎯 功能特性

- 模拟获取竞品社媒数据（可替换为真实 Twitter/Weibo API）
- 调用 DeepSeek API 进行分析
- 输出结构化中文简报：核心摘要、关键话题、市场动作、语气判断

## 🧪 输出示例

以 @OpenAI 为测试对象，生成简报如下：

**核心摘要**  
OpenAI 推出旗舰模型 GPT-4o，支持文本、音频、图像任意组合输入；与 Financial Times 达成合作，将实时新闻引入 ChatGPT；CEO 呼吁教育领域积极拥抱 AI。

**关键话题**  
- 多模态模型发布（GPT-4o）  
- 高质量内容合作（Financial Times）

**市场动作**  
- 新产品：GPT-4o 发布  
- 战略合作：FT 合作

**语气判断**  
积极、前瞻、自信

## 🛠️ 技术栈

| 工具 | 用途 |
|------|------|
| Python 3.14+ | 核心编程语言 |
| OpenAI SDK | API 统一调用 |
| DeepSeek API | 大模型推理 |
| Prompt Engineering | 结构化输出控制 |
