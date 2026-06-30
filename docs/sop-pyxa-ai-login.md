# SOP: Pyxa AI Login & Connection

> Created: 2026-06-30
> Status: ✅ Connected
> Trigger: "Connect Pyxa AI" / "Login to Pyxa AI" / "Pyxa 2FA"

## Connection Details

| Field | Value |
|-------|-------|
| **URL** | https://v2.pyxa.ai/login |
| **Dashboard** | https://v2.pyxa.ai/dashboard |
| **Login Email** | WithoutRecourse.UCC-1.308@protonmail.com |
| **Password** | [SECREDENTIAL — stored in OpenClaw only] |
| **2FA** | ProtonMail TOTP (30-second rotation) |
| **Plan** | Premium Creator (Lifetime) |
| **Limits** | Unlimited words, unlimited images |
| **Token Renewal** | 212 days from login (annual renewal) |

## Integration Points

- **AI Chat** → AI Chat, brainstorming, writing
- **AI Image** → Image generation (Stable Diffusion, etc.)
- **AI Video** → Video generation (Kling, Veo 3.1, Luma)
- **Documents** → 50+ existing docslate, code, templates
- **API** → No public API (browser-based only)

## Features Available

1. **AI Chat** — Ask, write, brainstorm with multi-model
2. **AI Image Pro** — Images, editing, backgrounds, styles
3. **AI Video Pro** — Videos (Kling 3.0, Luma, Veo 3.1)
4. **AI Avatar** — Realistic AI avatars
5. **AI Voiceover** — TTS with emotion, voice cloning
6. **AI Chatbot Builder** — Custom chatbots with training
7. **Social Media Suite** — Connect & post to all social accounts
8. **WordPress Integration** — 1-click blog publishing
9. **Plagiarism Checker** — Content authenticity
10. **SEO Tools** — Keyword research & optimization
11. **AI File Chat** — Chat with PDFs, spreadsheets, etc.
12. **Skills System** — Create/import custom AI skills

## Heartbeat Check

If Pyxa AI login session expires:
1. Navigate to https://v2.pyxa.ai/login
2. Enter email + password (from secredential)
3. Retrieve fresh 2FA code from user's ProtonMail
4. Enter 2FA within 30 seconds
5. Verify dashboard loads at https://v2.pyxa.ai/dashboard

## Content Pipeline Position

- **Writing** → Hermes Agent or Pyxa AI Chat
- **Images** → Pyxa AI Image Pro (or ArtSpace AI)
- **Video** → Pyxa AI Video Pro
- **Voice** → Pyxa AI Voiceover (or VoiceWave AI)
- **Publishing** → WordPress integration or Social Media Suite
