# OpenClaw — AI Provider Selection

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## Best Options (Ranked)

### 1. Claude Opus 4.5 — ⭐ Best Overall
- **Intelligence:** Highest — best for complex tasks, reasoning, orchestration
- **Cost:** Most expensive — burns tokens quickly
- **Strengths:** Browser control, sub-agent orchestration, complex workflows
- **Weaknesses:** Cost can be prohibitive for high-volume use

### 2. ChatGPT CodeX CLI — ⭐ Best Value
- **Intelligence:** Very good — slightly below Opus but highly capable
- **Cost:** ~$20/month flat — much more predictable
- **Strengths:** Great balance of cost and quality, no personality issues
- **Weaknesses:** Not quite as good at complex orchestration as Opus

### 3. Kimmy K2.5 — Budget Alternative
- **Intelligence:** Good — nearly as good as Opus for many tasks
- **Cost:** Cheaper than both Opus and CodeX
- **Strengths:** Cost-effective for sub-agents and routine tasks
- **Weaknesses:** May struggle with complex multi-step reasoning

### 4. Ollama (Local) — Free but Limited
- **Intelligence:** Model-dependent (Llama 3.3, Gemma 3, etc.)
- **Cost:** Free — runs on your local hardware
- **Strengths:** Completely free, private (data stays local), good for simple tasks
- **Weaknesses:** Requires significant local resources, can't access the web, not as intelligent
- **Best for:** Simple sub-agent tasks, routine automations

## Recommended Hybrid Setup

| Role | Provider | Why |
|------|----------|-----|
| **Main orchestrator** | ChatGPT CodeX CLI or Claude Opus | Needs highest intelligence for planning and complex tasks |
| **Sub-agents** | Kimmy K2.5 or Ollama | Cheaper for simple, well-defined tasks |
| **Routine tasks** | Ollama (local) | Free for high-volume, low-complexity work |

This hybrid approach saves significant money while maintaining quality where it matters.

## Other Compatible Providers

OpenClaw supports many providers via OpenRouter or direct API:
- **OpenRouter** — Aggregates many models, can auto-switch when rate-limited
- **Google Gemini** — Good for coding tasks (used in Google Anti-Gravity)
- **Minimax** — Cheaper alternative for sub-agents
- **GLM 4.9** — Budget option for lightweight tasks

## Provider Comparison Table

| Provider | Intelligence | Cost | Best For |
|----------|-------------|------|----------|
| Claude Opus 4.5 | ⭐⭐⭐⭐⭐ | $$$ | Complex orchestration, browser control |
| ChatGPT CodeX | ⭐⭐⭐⭐ | $$ | Daily driver, best value |
| Kimmy K2.5 | ⭐⭐⭐⭐ | $ | Sub-agents, routine work |
| Ollama (Local) | ⭐⭐⭐ | Free | Simple tasks, high volume |

---

## Metadata

- Tags: `openclaw`, `ai-providers`, `claude`, `chatgpt`, `ollama`, `cost-optimization`
- Related: [[01 - Installation & Setup]] | [[09 - Cost Optimization]]
