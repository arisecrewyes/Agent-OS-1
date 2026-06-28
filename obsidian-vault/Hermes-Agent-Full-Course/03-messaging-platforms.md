# Hermes Agent — Messaging Platforms

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Supported Platforms

- **Telegram**
- **Discord**
- **Slack**
- **WhatsApp**
- **Signal**
- **CLI** (terminal)

## Gateway Setup

### Step 1: Run Setup
```bash
hermes gateway setup
```
Follow the wizard to connect your chosen platforms.

### Step 2: Start Gateway
```bash
hermes gateway start
```

Once running, your agent is live on your messaging platform. You can:
- Talk to it from your phone
- Start a task on your computer
- Pick it up later from Telegram on your phone

## Platform Notes

### Telegram
- Most reliable and recommended
- Create a bot via @BotFather
- Works well for long messages and rich content

### Discord
- Good for team/community use
- OAuth flow during setup

### Slack
- Good for workplace environments
- OAuth flow during setup

### WhatsApp
- Works but may flag bot accounts
- Consider a separate number

### Signal
- Privacy-focused option
- Limited but functional

### CLI
- Direct terminal access
- Useful for troubleshooting and headless setups
- Can run as a background process

## Multi-Platform
You can connect **multiple platforms simultaneously**. Your agent is the same across all of them — same memory, same skills, same context.

---

## Metadata

- Tags: `hermes`, `messaging`, `telegram`, `gateway`
- Related: [[01 - Installation & Setup]] | [[12 - Troubleshooting & Commands]]
