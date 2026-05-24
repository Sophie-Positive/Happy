# Competitor Social Media Monitor Prototype

> A lightweight prototype that automatically generates structured competitive intelligence reports from social media data using DeepSeek API + Python.

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

### Core Summary
OpenAI announced GPT-4o, a new flagship model capable of processing any combination of text, audio, and image input. The company also partnered with Financial Times to bring real-time journalism to ChatGPT. CEO Sam Altman publicly called for the education sector to embrace AI transformation.

### Key Topics
- **Multimodal Model Release (GPT-4o)** – A major step toward "universal" AI assistants
- **High-Quality Content Partnership** – Strategic collaboration with Financial Times for data compliance and credibility

### Market Actions
- **New Product**: GPT-4o launch, competing with Google's multimodal models
- **Strategic Partnership**: Financial Times collaboration, signaling willingness to build commercial relationships with content publishers

### Sentiment
**Positive** – The tone is innovative and confident around GPT-4o, pragmatic and responsible around the media partnership, and forward-looking around CEO's education remarks.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14+ | Core programming language |
| OpenAI SDK | Unified API interface |
| DeepSeek API | LLM inference (cost-effective for Chinese output) |
| Prompt Engineering | Structured system prompts for consistent output |

## 📁 Project Structure
