# Non-API Tool Connection Tracker

> Created: 2026-06-30
> Purpose: Track connection of non-API tools to Agent OS ecosystem

## Connection Status

| # | Tool | URL | Status | Connected To | Notes |
|---|------|-----|--------|-------------|-------|
| 1 | Pyxa AI | https://v2.pyxa.ai/dashboard | ✅ Connected | OpenClaw browser | Lifetime Premium Creator — unlimited words/images, AI Chat, AI Image, AI Video, 50+ documents |
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

## Answer Set #2 — Manus, Anti-Gravity, Hyperframes, Grok (2026-06-30)

### Manus AI
- **Not a GitHub repo or Docker project.** Manus (manus.ai) is a SaaS AI agent platform — browser-based autonomous agent that builds websites, writes code, edits via vibe coding.
- **No self-hosted version exists.** It's cloud-only.
- **Closest self-hosted equivalents:** Bolt.DIY (already deployed) + Hermes Agent — between them you can build/manipulate websites via code.
- **Recommendation:** Skip self-hosting. Use Manus.ai as SaaS when needed, or use your existing Bolt.DIY + Hermes stack.

### Anti-Gravity Website Builder
- **SaaS only** (anti-gravity.io). No self-hosted or open-source version found anywhere.
- **No match in your GitHub library** or the Agent OS Tool Analysis (463 tools scanned).
- **Closest self-hosted alternatives:**
  - **Bolt.DIY** (already deployed at bolt-diy.srv1121935.hstgr.cloud) — AI → full-stack web app builder
  - **ai-website-cloner-template** (in loose links) — clone existing websites
- **Recommendation:** Use Bolt.DIY as your self-hosted website builder.

### Hyperframes
- **GitHub repo found:** https://github.com/heygen-com/hyperframes
- **Already cataloged** in Agent OS Tool Analysis under `cc-hyperframes`.
- **What it is:** Open-source framework for turning HTML, CSS, media, and seekable animations into deterministic MP4 videos. CLI + AI agent skills.
- **Status:** Needs to be built from source (no pre-built Docker image).
- **Recommendation:** Self-hostable. Can be Dockerized and deployed on VPS.

### Grok 4.3 (Image Generation)
- **Grok is xAI's LLM model** — available via API only (x.ai API or OpenRouter).
- **Not a self-hosted tool.** It's a cloud model.
- **For image generation alternatives (self-hosted):**
  - **ComfyUI-OmniVoice-TTS** (in loose GitHub links) — ComfyUI is the leading open-source AI image generation platform
  - **Open-Generative-AI** (in Agent OS Tool Analysis) — 200+ models (Flux, Midjourney, Kling, Sora, Veo), MIT licensed, self-hosted
  - **ArtSpace AI** (already connected) — SaaS with FLUX KONTEXT, SEEDREAM 4.0
- **Recommendation:**
  1. **API route:** Grok is available via OpenRouter — already accessible to Hermes Agent
  2. **Self-hosted image gen:** Deploy ComfyUI or Open-Generative-UI as Docker projects
  3. **SaaS route:** Keep using ArtSpace AI (already connected)

---

## Answer Set #3 — Deployment Results (2026-06-30)

### ✅ Successfully Deployed

| Service | Port | VPS URL | Purpose | Status |
|---------|------|---------|---------|--------|
| Ollama | 11434 | ollama.srv1121935.hstgr.cloud | Local LLM inference | ✅ Running (qwen2.5:1.5b + tinyllama) |
| Piper TTS | 10200 | piper.srv1121935.hstgr.cloud | Self-hosted TTS (ElevenLabs alt) | ✅ Running (en_US-lessac-medium) |
| Hyperframes | 3001 | hyperframes.srv1121935.hstgr.cloud | HTML → Video renderer | ✅ Running (3.6GB image) |

### ❌ Could Not Deploy

| Tool | Reason | Alternative |
|------|--------|------------|
| Dograh (Retell alt) | GHCR images private/locked | Use VoiceWave AI (SaaS) + Piper TTS (self-hosted) |
| Edge TTS | Image server crashes silently | Piper TTS covers TTS needs |
| ComfyUI | No GPU on VPS, 8GB RAM insufficient | ArtSpace AI (SaaS, already connected) |
| Open-Generative-AI | Electron app needs too much RAM | ArtSpace AI + Pyxa AI (SaaS) |
| ElevenLabs-Clone | StyleTTS2/Seed-VC need GPU + heavy RAM | Piper TTS + Edge TTS |

### 📋 Protected Docker Projects (User Directive)
NEVER touch: browser-use, hermes-agent-7llb, n8n-secondary-library, n8n-workflows, nocodb-a4cp, openclaw-x9sc, root, the-vault-financial

### Traefik HTTPS Status
| Service | HTTPS URL | Status | Notes |
|---------|-----------|--------|-------|
| Ollama | https://ollama.srv1121935.hstgr.cloud | ✅ HTTP 200 | Fully working with valid cert |
| Piper TTS | piper:10200 (direct) | ✅ Running | Wyoming TCP protocol — routed directly, no HTTPS needed |
| Hyperframes | Internal only | ✅ Sleeping | CLI tool — use `docker exec hyperframes` for rendering |

### Traefik Label Pattern (working)
```
traefik.enable=true
traefik.http.routers.NAME.entrypoints=web,websecure
traefik.http.routers.NAME.rule=Host(\`NAME.srv1121935.hstgr.cloud\`)
traefik.http.routers.NAME.tls=true
traefik.http.routers.NAME.tls.certresolver=mytlschallenge
traefik.http.services.NAME.loadbalancer.server.port=PORT
```
- Cert resolver: \`mytlschallenge\` (NOT \`letsencrypt\`)
- Traefik container: \`root-traefik-1\` in \`root\` project
- Network: \`traefik-public\`

### Question 8: ElevenLabs & Retell Alternatives
| Need | Solution | Status |
|------|----------|--------|
| ElevenLabs (TTS) | Piper TTS (self-hosted, Wyoming protocol) | ✅ Running |
| Retell AI (Voice agents) | **Dograh** — open-source Retell/Vapi alternative | ❌ GHCR images locked |
| Retell fallback | VoiceWave AI (SaaS, already connected) | ✅ Available |

### Question 9: Ollama (MiniMax/Qwen/Step local LLM)
- **Ollama deployed** with qwen2.5:1.5b + tinyllama models
- Both MiniMax M3, Qwen 3.7 Max, Step 3.7 Flash available on OpenRouter (API)
- Ollama provides free local inference via CPU
- Can pull any model that fits in 3GB RAM limit

### Question 10: Indexceptional
- **Self-hosted alternative found:** **Dograh** was the closest alternative researchers found
- Best self-hosted SEO monitoring alternatives from library:
  - **SearXNG** (already running on VPS at port 8080) — meta-search engine
  - Could add Uptime Kuma for monitoring
- Indexceptional itself is SaaS-only (indexceptional.com)
- **Recommend:** Use Uptime Kupa (lightweight, Docker) for site monitoring

### 📊 VPS Resource Status
- **RAM:** 7.8GB total, ~4GB available after deployments
- **Disk:** 97GB total, 79GB used (81%), 18GB free
- **CPU:** 2 cores (no GPU)
- **Containers:** 20 total (17 existing + Ollama + Piper + Hyperframes)
---