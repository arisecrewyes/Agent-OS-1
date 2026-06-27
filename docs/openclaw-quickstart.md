# OpenClaw — QuickStart Guide

> Step-by-step walkthrough to get OpenClaw up and running.
> Source: Julian Goldie SEO — Skool Post #3
> Related: [[openclaw-capabilities-general]] | [[00 - Index]]

---

## Step 1: Install OpenClaw

```bash
npm install -g claudebot@latest
```

## Step 2: Run the Onboarding Wizard

```bash
claudebot onboard-install-daemon
```

The wizard will guide you through:
1. Choosing your AI provider
2. Entering your API key
3. Selecting messaging channels
4. Installing skills (optional)

## Step 3: Verify Installation

```bash
claudebot doctor
```

## Step 4: Choose Your AI Provider

| Provider | Best For | Cost |
|----------|----------|------|
| Claude Opus 4.5 | Best intelligence | $$$ |
| ChatGPT CodeX CLI | Best value | $$ |
| Kimmy K2.5 | Budget alternative | $ |
| Ollama (Local) | Free, simple tasks | Free |

**Recommended:** Start with ChatGPT CodeX CLI (good balance) or Ollama (free).

## Step 5: Connect Telegram

1. Open Telegram
2. Search for **@BotFather**
3. Send `/newbot`
4. Name your bot
5. Copy the bot token
6. Enter the token in OpenClaw

## Step 6: Install Skills (Optional)

```bash
claudebot skills install <skill-name>
```

Recommended first skills:
- `wordpress` — Publish blog posts
- `browser-control` — Automate web tasks
- `notion` — Manage notes
- `bird` — Post to Twitter/X

## Step 7: Test It

Send a message to your bot via Telegram:
```
Hello! Can you help me write a blog post about AI automation?
```

## Next Steps

- Read the full capability reference: `openclaw-capabilities-general.md`
- Check the launch plan: `openclaw-launch-plan.md`
- Browse the prompt library: `openclaw-prompts.md`
