# OpenClaw — Cost Optimization

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## The Hybrid Approach (Recommended)

The most cost-effective setup uses different models for different tasks:

| Role | Provider | Monthly Cost | Why |
|------|----------|-------------|-----|
| **Main orchestrator** | ChatGPT CodeX CLI | ~$20/month | Good intelligence, predictable cost |
| **Sub-agents** | Kimmy K2.5 | Low cost | Cheaper for simple, well-defined tasks |
| **Simple/Routine tasks** | Ollama (local) | Free | No API costs for high-volume work |

### Why Hybrid Works

Not every task needs Claude Opus-level intelligence. Simple tasks like:
- Formatting content
- Checking for updates
- Routine monitoring
- Simple data extraction

...can all run on cheaper or free models. Reserve your expensive tokens for:
- Complex reasoning
- Content creation
- Browser automation
- Strategic planning

---

## Token Saving Tips

1. **Use streaming responses** when possible — reduces wasted tokens
2. **Clear context for simple queries** — don't carry unnecessary conversation history
3. **Use specific skills** instead of general LLM calls — skills are more token-efficient
4. **Set up local models** for routine tasks — Ollama is free
5. **Be specific in prompts** — vague prompts waste tokens on irrelevant output
6. **Use sub-agents** for parallel work — each sub-agent can use a cheaper model

---

## Spending Limits

**Always set spending limits on your API accounts:**

- **OpenRouter:** Set per-model and total spending limits
- **Anthropic (Claude):** Set monthly budget alerts
- **OpenAI (ChatGPT):** Set hard spending caps
- **Monitor usage weekly** — catch unexpected spikes early

---

## Model Cost Comparison

| Model | Relative Cost | Best Use |
|-------|--------------|----------|
| Claude Opus 4.5 | ⭐⭐⭐⭐⭐ (Highest) | Complex orchestration, browser control |
| ChatGPT CodeX | ⭐⭐⭐ (Medium) | Daily driver, good value |
| Kimmy K2.5 | ⭐⭐ (Low) | Sub-agents, routine work |
| Ollama/Llama (Local) | ⭐ (Free) | Simple tasks, high volume |

---

## OpenRouter for Auto-Switching

OpenRouter aggregates many models and can **auto-switch** when you hit rate limits:

- Give OpenClaw an OpenRouter API key
- It has access to Claude, GPT, Gemini, Llama, and more
- If one model is rate-limited, it switches to another
- Great for 24/7 uptime without interruptions

---

## Metadata

- Tags: `openclaw`, `cost-optimization`, `token-savings`, `api-costs`
- Related: [[02 - AI Provider Selection]] | [[07 - Advanced Features]]
