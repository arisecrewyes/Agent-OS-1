# Hermes Agent — AI Model Selection

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Free Option (Recommended for Starting)

1. Go to [OpenRouter](https://openrouter.ai)
2. Create an account
3. Grab a **free API key**
4. Use **Alibaba's Qwen 3.6 Plus Preview**
   - 1 million token context window
   - Completely free
   - Designed for agents

## Paid Options

- **OpenAI** (ChatGPT CodeX, GPT-4o)
- **Anthropic** (Claude Opus, Sonnet)
- **MiniMax** (M2.7 cloud)
- **Kimi/Moonshot**
- Any of the **200+ models** on OpenRouter

## Local Option

- **Ollama** — Run models locally on your machine for zero API cost
- Requires local RAM (8GB+ for usable models)
- Good for privacy and zero-cost operation

## Switching Models

```bash
hermes model
```
No code changes needed. Just pick your provider and model.

## Fallback Model Chains

Set up a backup model so your agent never stops if one API goes down.

Example: Primary = MiniMax M2.7, Backup = Qwen 3.6 via OpenRouter
If the primary fails, Hermes **automatically switches** to the backup.

Add a secondary provider in your config to enable this.

## Recommended Setup

| Role | Provider | Model | Cost |
|------|----------|-------|------|
| **Main agent** | OpenRouter | Qwen 3.6 Plus Preview | Free |
| **Backup** | OpenRouter | Any free model | Free |
| **Paid upgrade** | OpenRouter | Claude Opus / GPT-4o | Paid |

---

## Metadata

- Tags: `hermes`, `ai-models`, `openrouter`, `qwen`, `ollama`
- Related: [[01 - Installation & Setup]] | [[09 - Multi-Agent Profiles]]
