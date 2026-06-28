# OpenClaw — Messaging App Integration

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## Supported Channels

- **Telegram** (Recommended — easiest setup)
- **WhatsApp**
- **Discord**
- **Slack**
- **iMessage** (Mac only)
- **Signal**
- **Google Chat**
- **MS Teams**
- And more via plugins

## Telegram (Recommended)

### Setup Steps

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` to create a new bot
3. Follow the prompts to name your bot
4. **Copy the bot token** provided by BotFather
5. Enter the token during OpenClaw setup (or in your `.env` file)

### Why Telegram is Recommended

- Easiest setup process
- Most reliable connection
- Works on all platforms (mobile, desktop, web)
- No spam concerns (unlike WhatsApp)
- Real-time messaging with instant delivery

### Tips

- Use a dedicated bot account, not your personal account
- The bot token is sensitive — treat it like a API key
- You can connect multiple messaging apps simultaneously

## WhatsApp

### Setup

- Scan a QR code during setup (similar to WhatsApp Web)
- OpenClaw connects to your WhatsApp account

### ⚠️ Caution

- WhatsApp may flag bot accounts as spam
- Consider using a separate phone number for OpenClaw
- Julian Goldie recommends **against** using your main WhatsApp account

## Discord / Slack

### Setup

- Follow the OAuth flow during setup
- Grant necessary permissions to the bot
- For Discord: create a bot application at discord.com/developers
- For Slack: create a Slack app and install it to your workspace

## Multi-Channel Setup

You can connect **multiple messaging apps simultaneously**:
- Telegram for personal use
- Discord for team/community
- WhatsApp for clients (with caution)

All channels connect to the same OpenClaw instance and share the same memory/context.

---

## Metadata

- Tags: `openclaw`, `telegram`, `whatsapp`, `discord`, `messaging`
- Related: [[01 - Installation & Setup]] | [[05 - Security Best Practices]]
