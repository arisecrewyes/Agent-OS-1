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

## When NOT to Use OpenClaw

- ❌ You need enterprise-grade security compliance
- ❌ You want zero technical setup
- ❌ You're uncomfortable with command line basics
- ❌ You need guaranteed uptime/support
- ❌ You handle extremely sensitive data

## When TO Use OpenClaw

- ✅ You want a personal AI assistant that actually does things
- ✅ You're comfortable with some technical setup
- ✅ You want to automate repetitive tasks
- ✅ You're a content creator/founder/automation builder
- ✅ You want control over your AI and data

## Key Comparisons

| Tool | Strength | OpenClaw Advantage |
|------|----------|--------------------|
| ChatGPT | Browser-only, no memory | OpenClaw: lives in apps, remembers, takes actions |
| Make/Zapier | Pre-built workflows | OpenClaw: natural language, infinite flexibility |
| N8N | Node-based workflows | OpenClaw: plain English → it figures out the workflow |
| Claude Desktop/MCP | Tool access from Claude | OpenClaw: AI comes to you in messaging, 24/7 |

## Next Steps

- Read the full capability reference: `openclaw-capabilities-general.md`
- Check the launch plan: `openclaw-launch-plan.md`
- Browse the prompt library: `openclaw-prompts.md`
