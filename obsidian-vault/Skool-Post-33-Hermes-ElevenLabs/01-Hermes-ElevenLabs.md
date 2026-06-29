# 6th June: Hermes Agent + ElevenLabs (Post #33)

> Converted from Julian Goldie Skool Post #33 — 6th June
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=c4dabc4ba5dd4564b425e24b20b10609

## Overview

This post shows how to set up a **phone number you can call to talk to your Hermes AI agent**. ElevenLabs handles voice (STT + TTS), Hermes does the thinking on your Mac, and a Cloudflare tunnel bridges them. Setup takes ~10 minutes.

**Reference thread:** [ElevenLabs Devs guide](https://x.com/ElevenLabsDevs/status/2062561944385519801) — give this to your AI agent for a fast setup.

---

## How It Works

1. Hermes exposes a local API server on your Mac
2. Cloudflared creates a public tunnel to that local endpoint
3. ElevenLabs Conversational AI points at your tunnel URL as a "Custom LLM"
4. Twilio provides the phone number that connects to ElevenLabs
5. When you call, ElevenLabs handles voice → Hermes thinks → ElevenLabs speaks the reply

---

## Requirements

- **ElevenLabs** account + API key (starts with `sk_`)
- **Hermes Agent** installed, signed into a model provider
- **Twilio** phone number (~$1/month)
- **Homebrew** on Mac (for `cloudflared` tunnel)

---

## Setup Steps

### Step 1 — ElevenLabs API Key

In ElevenLabs → Profile → copy API key (starts with `sk_`).

### Step 2 — Enable Hermes API Server

```bash
# Find active profile
cat ~/.hermes/active_profile
# (defaults to "main" if file doesn't exist)
```

Edit `~/.hermes/profiles/<your-profile>/.env`:
```
API_SERVER_ENABLED=true
API_SERVER_PORT=8642
API_SERVER_KEY=PASTE_A_RANDOM_KEY_HERE
ELEVENLABS_API_KEY=sk_your_elevenlabs_key
```

Generate random key:
```bash
openssl rand -hex 24
```

### Step 3 — Pick a Fast Model

Phone calls need quick replies. Use a **fast** model — not a slow reasoning model, not a free-tier one. The phone uses whatever model Hermes is currently set to.

### Step 4 — Start Gateway + Tunnel

```bash
# Install tunnel (once)
brew install cloudflared

# Start Hermes gateway
hermes gateway start

# Verify it's running
curl http://127.0.0.1:8642/health
# Should return {"status":"ok"}

# Start tunnel (leave running)
cloudflared tunnel --url http://localhost:8642
# Copy the .trycloudflare.com address it prints
```

### Step 5 — Create ElevenLabs Agent

In ElevenLabs dashboard → **Conversational AI** → new agent → **Custom LLM**:
- URL: `https://your-tunnel.trycloudflare.com/v1`
- API key: the `API_SERVER_KEY` from Step 2

### Step 6 — Connect Phone Number

ElevenLabs → **Phone** → connect Twilio → import number → assign to agent.

### Step 7 — Call It

Dial the number. Try *"What can you do?"* or *"Check my balance."*

---

## ⚠️ Security Warnings

- This is a **live line to an agent that can run commands on your Mac**
- Keep the number **private** — don't read it out on recordings
- Say **"draft"** not **"send"** until you trust it

---

## Kill Switch

- **Stop tunnel:** `Ctrl+C` in cloudflared window, or `pkill -f cloudflared`
- **Unassign number:** ElevenLabs → Phone → unassign from agent

No tunnel = no line. Instant kill-switch.

---

## Voice AI Alternatives

ElevenLabs isn't the only option for adding voice to your AI agent. Here's how the top three compare:

| Feature | **ElevenLabs** | **VoiceWave AI** | **PYXA AI** |
|---|---|---|---|
| **Core Strength** | Ultra-realistic voice cloning & expressive speech | Voice generation with API-first approach | AI voice agents for business automation |
| **Voice Quality** | Industry-leading, highly natural | High quality, good for most use cases | Business-grade, professional tone |
| **API / Integration** | REST API, SDKs, Conversational AI platform | REST API, developer-friendly | REST API, built for agent workflows |
| **Custom Voice Cloning** | ✅ Yes (premium) | ✅ Yes | ✅ Yes |
| **Real-time Streaming** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Phone/Twilio Integration** | ✅ Native phone number support | ⚠️ Via custom setup | ✅ Built for telephony |
| **Pricing** | Free tier (10k chars/mo), paid from $5/mo | Competitive, usage-based | Custom pricing (business-focused) |
| **Best For** | Creators, developers, most polished output | Developers wanting quick API integration | Businesses automating customer-facing calls |
| **Conversational AI** | ✅ Full agent platform with LLM integration | ⚠️ Requires external LLM | ✅ Built-in conversation design |

### When to Choose an Alternative

- **VoiceWave AI** — Choose if you want a simpler API, lower cost, or are building a custom voice pipeline without needing the full ElevenLabs ecosystem.
- **PYXA AI** — Choose if you're building business-grade voice agents (customer service, sales calls) and want purpose-built telephony features out of the box.

> 💡 All three can work with Hermes via the same Custom LLM pattern. Just swap the ElevenLabs agent URL for your chosen provider's endpoint.

---

## Related

- [[01-Hermes-Agent-OS|Post #1: Hermes Agent OS System]]
- [[01-Hermes-Email-Agent|Hermes Email Agent]]
- [[SOP - Agent OS Setup]]
