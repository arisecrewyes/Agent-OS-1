# OpenClaw — QuickStart Guide

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## Step 1: Install OpenClaw

```bash
npm install -g claudebot@latest
```

## Step 2: Run Onboarding

```bash
claudebot onboard-install-daemon
```

## Step 3: Verify

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

## Step 5: Connect Telegram

1. Open Telegram → search for **@BotFather**
2. Send `/newbot`
3. Name your bot
4. Copy the bot token
5. Enter token in OpenClaw

## Step 6: Install Skills

```bash
claudebot skills install <skill-name>
```

Recommended: `wordpress`, `browser-control`, `notion`, `bird`

## Step 7: Test It

Send a message to your bot via Telegram:
```
Hello! Can you help me write a blog post about AI automation?
```

## Related

- [[15 - Launch Plan]]
- [[16 - Prompt Library]]

---

## Metadata

- Tags: `openclaw`, `quickstart`, `setup`
- Related: [[01 - Installation & Setup]] | [[02 - AI Provider Selection]]
