# Hermes Agent — QuickStart Guide

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Step 1: Install Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
```

## Step 2: Run Setup Wizard

```bash
hermes setup
```

Choose provider: Ollama (zero config), OpenRouter (200+ models), or API key.

## Step 3: Verify

```bash
hermes doctor
hermes --version
```

## Step 4: Choose Your AI Model (Free)

1. Go to [OpenRouter](https://openrouter.ai)
2. Create account, grab free API key
3. Use **Qwen 3.6 Plus Preview** (1M context, free)

Switch anytime: `hermes model`

## Step 5: Connect Messaging

```bash
hermes gateway setup
hermes gateway start
```

Supported: Telegram, Discord, Slack, WhatsApp, Signal, CLI

## Step 6: Install Community Skills

```bash
hermes skills install wonderly-skills
```

## Step 7: Test It

```bash
hermes
```
Then type: `Hello! Can you help me research the latest AI trends?`

## Related

- [[15 - Launch Plan]]
- [[16 - Prompt Library]]

---

## Metadata

- Tags: `hermes`, `quickstart`, `setup`
- Related: [[01 - Installation & Setup]] | [[02 - AI Model Selection]]
