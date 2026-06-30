# SOP: Non-API Tool Connection Guide

> Universal guide for any AI agent to connect to non-API tools
> See full version: `docs/sop-non-api-tool-connection-guide.md`

## Connection Methods

### 1. Browser Automation (Primary)
- Navigate → Login → Interact → Download
- For: OpenClaw, Claude Code, any agent with browser access

### 2. Session Persistence
- Log in once, keep tab alive
- For: Tools with lifetime licenses

### 3. Webhook Bridge (Content 360)
- Content 360 → Webhook → n8n → Process
- For: n8n, Agent OS automation

### 4. RSS Bridge (Content 360)
- RSS feed → Content 360 auto-posts
- For: Content syndication

## Tool Login Quick Reference
| Tool | URL | 2FA | Session |
|------|-----|-----|---------|
| [[01-Pyxa-AI]] | v2.pyxa.ai/login | ✅ ProtonMail TOTP | Persists |
| [[02-VoiceWave-AI]] | voicewave.ai/signin | ❌ | Persists |
| [[03-ArtSpace-AI]] | artspace.ai/signin | ❌ | Persists |
| [[04-Content-360]] | content360.io/os/login | ❌ | Persists |
| [[05-Typeset]] | typeset.com/auth | — | ⏸️ Paused |

## Content Pipeline
```
[[01-Pyxa-AI]] (write) → [[03-ArtSpace-AI]] (images) → [[02-VoiceWave-AI]] (voice) → [[04-Content-360]] (post)
```

## Credential Rules
1. Store as secredentials only
2. Never plain text
3. Never in repos
4. 2FA codes never stored (ephemeral)

## Agent Assignments
- **OpenClaw** — All browser automation, orchestrator
- **Hermes** — Content writing, script writing
- **n8n** — Webhook receiver, workflow automation
- **Claude Code** — Batch operations, scripting
