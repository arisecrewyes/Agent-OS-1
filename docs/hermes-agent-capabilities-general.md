# Hermes Agent — Complete Capability Reference (General Version)

> Source: Julian Goldie SEO — Skool Post #4: "Hermes: Full 2 Hour Course!" + Post #5 updates
> Original Video: https://www.youtube.com/watch?v=8avW0D2sEn8 (Post #4) + https://www.youtube.com/watch?v=0oVCerqrR7A (Post #5)
> GitHub: https://github.com/NousResearch/hermes-agent
> Date: 2026-06-27
> Purpose: Comprehensive capability reference for any Hermes Agent user

> 🆕 **Post #5 Updates:** Agent Teams (Profiles, Telegram, Paperclipip, Hermes Workspace, Multica), Hermes Dashboard (v0.9), One-Click Setups (Ollama, MaxHermes). See dedicated files for full details.

---

## What is Hermes Agent?

Hermes Agent is a free, open-source AI agent built by **Nous Research**. Unlike regular chatbots, it:
- **Remembers everything** across sessions
- **Creates its own skills** from experience
- **Improves those skills** every time it uses them
- **Runs 24/7** even when your computer is off
- Connects to **Telegram, Discord, Slack, WhatsApp, Signal**, and your terminal

**Key Stats:**
- 11,600+ GitHub stars
- 142+ contributors
- MIT license
- Ranked #2 in personal AI agents on OpenRouter
- Went from #41 to #21 top apps on OpenRouter in weeks

---

## Installation (5 minutes)

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes setup
hermes doctor
```

**Requirements:** Git, command-line access, Mac/Linux/WSL2 (native Windows NOT supported)

---

## AI Model Selection

### Free Option
1. Go to [OpenRouter](https://openrouter.ai)
2. Create an account, grab a free API key
3. Use **Alibaba's Qwen 3.6 Plus Preview** (1M token context, free)

### Paid Options
- OpenAI, Anthropic (Claude), MiniMax, Kimi/Moonshot
- Any of 200+ models on OpenRouter

### Local Option
- **Ollama** — Run models locally for zero API cost

### Switching Models
```bash
hermes model
```
No code changes needed.

### Fallback Chains
Set up a backup model so your agent never stops if one API goes down. Example: Primary = MiniMax M2.7, Backup = Qwen 3.6 via OpenRouter.

---

## Messaging Platforms

```bash
hermes gateway setup     # Follow wizard to connect platforms
hermes gateway start     # Start the gateway
```

**Supported:** Telegram, Discord, Slack, WhatsApp, Signal, CLI

Once running, talk to your agent from your phone while it works on tasks in the background.

---

## First 7 Days (Training Period)

**Critical:** Do NOT treat Hermes like a regular chatbot.

- **Day 1-3:** Hermes builds `memory.md` (your projects, preferences) and `user.md` (communication style). These are injected into every session's system prompt.
- **Day 4-7:** Knows your projects, preferences, and where you left off. Creates new skills automatically after complex tasks (5+ tool calls).
- **Key mindset:** It will not be perfect. Give feedback on every task. It writes feedback into skill.md files and improves.

---

## Community Skills (One-Click Upgrade)

```bash
hermes skills install wonderly-skills
```

- **40+ skills** out of the box
- **Wonderly Skills** library: 250+ stars, actively maintained
- Skills load efficiently (only loaded when needed)
- Follows open standard: [agentskills.io](https://agentskills.io) (compatible with Claude Code, Cursor)
- Security scanner checks every skill before install

---

## Creating Custom Skills

Three ways:
1. **Automatic:** Hermes creates skills after complex tasks
2. **Ask:** "Create a skill for posting to X with trending AI news and an image"
3. **Manual:** Write markdown files in `~/.hermes/skills/`

**Feedback loop:** Give feedback every time a skill runs → Hermes updates the skill.md → improves over time.

**Pro tip:** Back up skill.md files weekly outside of Hermes.

---

## Scheduled Tasks (Cron Jobs)

Tell Hermes in plain language what you want and when:

```
"Every 30 minutes, check trending topics on these two subreddits,
draft a tweet, generate an image, and post it to X.
Send me a Telegram confirmation with the live link."
```

```
"Every morning at 8am, scan AI news sources and send me a
summary of what matters."
```

```
"Every Friday, pull my X analytics for the last 14 days,
analyze top performing tweets, and send me a breakdown."
```

Hermes handles scheduling natively — no external tools needed.

---

## External Tools

| Tool | Purpose | Setup |
|------|---------|-------|
| **Firecrawl** | Web browsing & research | Get API key from firecrawl.dev/app |
| **Browser Base** | Visual web browsing with vision | Gives agent a proper browser |
| **Nana Banana 2** | Image generation | Connect API for social media images |
| **X/Twitter API** | Direct posting | developer.x.com → create app |
| **MCP** | External tool integration | `hermes mcp serve` to run as MCP server |

**Compound Effect:** Firecrawl (research) + X (posting) + Nana Banana (images) = full automated content pipeline.

---

## Multi-Agent Profiles (v0.6+)

```bash
hermes profile create twitter-agent
hermes profile create research-agent
hermes profile create content-writer
```

Each profile = fully isolated (own config, API keys, memory, sessions, skills, gateway).

Per-profile commands: `twitter-agent chat`, `twitter-agent setup`, etc.

Export/import profiles for sharing or migration.

---

## Migrating from OpenClaw

```bash
hermes claw migrate              # Import everything from OpenClaw
hermes claw migrate --dry-run   # Preview first
```

Migrates: SOUL.md, memories, skills, command allowlist, messaging settings, API keys, TTS assets, workspace instructions.

Auto-detects OpenClaw during first-time setup.

---

## Hermes vs OpenClaw

| Category | OpenClaw | Hermes |
|----------|----------|--------|
| Community | ✅ Larger | Growing fast |
| Tutorials | ✅ More | Fewer |
| Messaging Platforms | ✅ 50 | 6 |
| Skills Ecosystem | ✅ Larger | 40+ built-in |
| Heartbeat System | ✅ Every 30 min | ❌ |
| Self-Improving Loop | ❌ Limited | ✅ Core feature |
| Security | ⚠️ Had issues | ✅ Docker isolation |
| Speed | Slower | ✅ Faster |
| MCP Server Mode | ❌ | ✅ |
| Research Lab | ❌ Solo dev | ✅ Nous Research |
| Migration Tool | N/A | ✅ `hermes claw migrate` |

**Best answer:** Use both. They complement each other. Both free and open source.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Stuck/not responding | `Ctrl+C` → `hermes` (terminal) or `/new` (Telegram) |
| Telegram gateway broken | Use terminal Hermes to diagnose and fix |
| Context too large | `/compress` or `/new` (memory persists) |

## Essential Commands

| Command | Purpose |
|---------|---------|
| `hermes` | Start chatting |
| `hermes setup` | Setup wizard |
| `hermes model` | Switch model |
| `hermes doctor` | Diagnose issues |
| `hermes gateway setup` | Set up messaging |
| `hermes gateway start` | Start gateway |
| `hermes skills install [name]` | Install skill |
| `hermes profile create [name]` | Create profile |
| `hermes claw migrate` | Migrate from OpenClaw |
| `/new` or `/reset` | Fresh conversation |
| `/compress` | Compress context |
| `/usage` | Check token usage |

---

## The 3-Step Automation Blueprint

1. **Where do you spend your time?** Identify the repetitive task.
2. **What's one thing you can automate this week?** Pick one.
3. **Ask Hermes how to automate it.** Then define trigger, give data sources, test once, schedule it.

## Key Principles

- The more you use it, the better it gets (compounding effect)
- Always give feedback on every task
- String multiple skills together for exponential power
- Create your own skills — tailored to your workflow
- Back up skill.md files weekly
- First 7 days: not perfect, but dramatically better by day 7
- Always approve social media posts manually at least 10 times before autonomous posting

---

> **Remember:** Hermes Agent is powerful but still maturing (v0.6). It gets better every day. Start simple, give feedback, and let the compounding effect work for you.
