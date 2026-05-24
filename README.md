# Competitor Social Media Monitor Prototype

> A lightweight Python prototype that automatically generates structured competitive intelligence reports from social media data using DeepSeek API.

## 🎯 What This Project Does

This prototype simulates a real-world social media monitoring pipeline:

1. **Data Ingestion** – Fetches competitor social media posts (mock data ready, easily replaceable with real APIs)
2. **LLM Processing** – Sends raw text to DeepSeek API with carefully designed prompts
3. **Structured Report** – Generates a Chinese competitive intelligence briefing with four dimensions:
   - Core Summary (2-3 sentences)
   - Key Topics (2-3 main discussion themes)
   - Market Actions (new products, promotions, partnerships)
   - Sentiment Analysis (positive/neutral/negative)

## 🧪 Sample Output

**Test target**: @OpenAI (simulated Twitter data)

| Section | Content |
|---------|---------|
| **Core Summary** | OpenAI announced GPT-4o, a multimodal model accepting text/audio/image input; partnered with Financial Times for real-time journalism; CEO calls for AI adoption in education. |
| **Key Topics** | Multimodal model release / High-quality content partnership |
| **Market Actions** | GPT-4o launch / FT strategic collaboration |
| **Sentiment** | Positive, forward-looking, confident |

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14+ | Core programming language |
| OpenAI SDK | Unified API interface |
| DeepSeek API | LLM inference (cost-effective for Chinese output) |
| Prompt Engineering | Structured system prompts for consistent output |

## 📁 Project Structure

## 🔧 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Sophie-Positive/Happy.git
cd Happy
