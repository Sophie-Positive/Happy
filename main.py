"""
Competitor Social Media Monitor Prototype
Automatically generates structured competitive intelligence reports using DeepSeek API.
"""

import os
from openai import OpenAI

# ============================================================
# 配置区
# ============================================================

# 重要：不要写死 API Key！使用环境变量
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# 检查 API Key 是否已设置
if not DEEPSEEK_API_KEY:
    raise ValueError("请先设置环境变量 DEEPSEEK_API_KEY")

# ============================================================
# 模拟数据模块：获取竞品推文（可替换为真实 API）
# ============================================================

def fetch_competitor_tweets(competitor_name: str) -> list:
    """
    模拟获取竞品社媒数据
    实际使用时，可替换为 Twitter/Weibo API 调用
    """
    mock_data = {
        "OpenAI": [
            "Introducing GPT-4o: our new flagship model that accepts any combination of text, audio, and image as input.",
            "We're partnering with Financial Times to bring real-time journalism to ChatGPT.",
            "Sam Altman: 'AI will transform education in ways we barely understand. Start experimenting now.'"
        ],
        "Google": [
            "Gemini 2.0 is here, with native image generation and real-time reasoning.",
            "New AI-powered features coming to Workspace next month."
        ]
    }
    return mock_data.get(competitor_name, ["暂无数据，请检查竞品名称"])


# ============================================================
# AI 处理模块：调用大模型生成简报
# ============================================================

def generate_briefing(competitor_name: str, tweets: list) -> str:
    """
    调用 DeepSeek API，生成结构化竞品简报
    """
    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL
    )

    # 核心 Prompt（可迭代优化）
    system_prompt = """你是一位资深市场分析师，请根据提供的竞品推文，生成一份中文简报。

简报必须包含以下四个部分，请严格按格式输出：

1. **核心摘要**：用2-3句话概括主要内容。
2. **关键话题**：提炼出2-3个讨论最多的主题。
3. **市场动作**：如果提及新品、促销、合作等，请特别指出。
4. **语气判断**：分析推文的主要情绪（积极/消极/中立）。
"""

    user_content = f"竞品名称: {competitor_name}\n\n以下是它的最新推文:\n" + "\n---\n".join(tweets)

    print("正在用 AI 分析推文，生成简报...")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


# ============================================================
# 主程序入口
# ============================================================

def main():
    print("=" * 50)
    print("竞品社媒监控简报生成器")
    print("=" * 50)

    competitor = "OpenAI"  # 可改为 "Google" 或其他
    print(f"\n正在获取竞品 [{competitor}] 的社媒数据...")

    tweets = fetch_competitor_tweets(competitor)
    print(f"获取到 {len(tweets)} 条推文")

    briefing = generate_briefing(competitor, tweets)

    print("\n" + "=" * 50)
    print(f"竞品 [{competitor}] 简报如下:")
    print("=" * 50)
    print(briefing)
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
