# Hermes Agent — QuickStart Guide

> Step-by-step walkthrough to get Hermes Agent up and running.
> Source: Julian Goldie SEO — Skool Post #4
> Related: [[hermes-agent-capabilities-general]] | [[00 - Index]]

---

## Step 1: Install Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## Step 2: Reload Your Shell

```bash
source ~/.bashrc
# Or if you use zsh:
source ~/.zshrc
```

## Step 3: Run the Setup Wizard

```bash
hermes setup
```

Choose your model provider:
- **Ollama** — Zero config, runs locally
- **OpenRouter** — 200+ models, one key (recommended for free tier)
- **API Key** — OpenAI, Anthropic, or any provider

## Step 4: Verify Installation

```bash
hermes doctor
hermes --version
```

## Step 5: Choose Your AI Model (Free Option)

1. Go to [OpenRouter](https://openrouter.ai)
2. Create an account
3. Grab a free API key
4. Use **Alibaba's Qwen 3.6 Plus Preview** (1M token context, free)

Switch models anytime:
```bash
hermes model
```

## Step 6: Connect Messaging Platforms

```bash
hermes gateway setup
hermes gateway start
```

Supported: Telegram, Discord, Slack, WhatsApp, Signal, CLI

## Step 7: Install Community Skills (One-Click Upgrade)

```bash
hermes skills install wonderly-skills
```

This installs the Wonderly Skills library — 40+ additional skills.

## Step 8: Test It

In terminal:
```bash
hermes
```

Then type:
```
Hello! Can you help me research the latest AI trends?
```

## Migrating from OpenClaw?

Hermes can automatically import everything from OpenClaw:
```bash
hermes claw migrate --dry-run  # Preview first
hermes claw migrate               # Execute migration
```

This imports: SOUL.md, memories, skills, command allowlist, messaging settings, API keys, TTS assets, and workspace instructions.

## Hermes vs OpenClaw — Honest Comparison

| Winner | Why |
|--------|-----|
| **Hermes** | Self-improving loop, Docker isolation, research lab backing, faster execution, MCP server mode |
| **OpenClaw** | Community size (8,000+ Discord), more tutorials, 50 messaging platforms, more skills, heartbeat system |
| **Both** | Free, open source, run 24/7 |

> Julian's take: "Hermes is by far the best AI agent I've ever used." But OpenClaw's community and ecosystem are larger.

## Key Principles

1. **The more you use it, the better it gets.** This is a compounding effect.
2. **Always give feedback on every task.** This is how it improves.
3. **String multiple skills together.** Skill 1 (research) + Skill 2 (post to X) + Skill 3 (generate image) = full content pipeline.
4. **Create your own skills** rather than only relying on community ones.
5. **Back up your skill.md files weekly.**
6. **Be prepared for the first 7 days.** It will not be perfect but it gets dramatically better by day 7.
7. **If posting to social media, always ask for a draft first.** Do this at least 10 times before letting it post autonomously.

## Next Steps

- Read the full capability reference: `hermes-agent-capabilities-general.md`
- Check the launch plan: `hermes-launch-plan.md`
- Browse the prompt library: `hermes-prompts.md`
