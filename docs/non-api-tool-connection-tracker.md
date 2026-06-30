# Non-API Tool Connection Tracker

> Created: 2026-06-30
> Purpose: Track connection of non-API tools to Agent OS ecosystem

## Connection Status

| # | Tool | URL | Status | Connected To | Notes |
|---|------|-----|--------|-------------|-------|
| 1 | Pyxa AI | https://v2.pyxa.ai/login | ⚠️ 2FA Required | — | Voice AI — needs 2FA code |
| 2 | VoiceWave AI | https://www.voicewave.ai/signin | ✅ Connected | OpenClaw browser | Voice AI |
| 3 | ArtSpace AI | https://www.artspace.ai/signin | ✅ Connected | OpenClaw browser | 282 AI creative tools |
| 4 | Content 360 | https://app.content360.io/os/login | ✅ Connected | OpenClaw browser | Social media management |
| 5 | Typeset | https://app.typeset.com/auth | ✅ Connected | OpenClaw browser | Subscription on pause |
| 6 | GoStackBase | https://app.gostackbase.com | ✅ Connected | OpenClaw, n8n | Already done |

## Integration Patterns (from Lead Connector Bridge)

1. **Browser Login** — For tools without APIs (like GoStackBase initially)
2. **API Direct** — For tools with REST APIs
3. **n8n Webhook** — For triggering workflows from Agent OS
4. **MCP Bridge** — For tools that support Model Context Protocol

## Tools Already Connected

- GoStackBase ✅ (API + browser)
- n8n ✅ (on VPS)
- OpenClaw ✅ (this agent)
- Hermes Agent ✅
- Obsidian Vault ✅
