# Agent OS — Hostinger VPS Deployment

Deploy Julian Goldie's Agent OS on any Hostinger VPS via Docker Compose.

## Two Versions

### Version 1: Single Master Compose
One `docker-compose.yml` with everything. Best for VPS with 4GB+ RAM.
→ See `version1-single-compose/`

### Version 2: Multiple Compose Files (Recommended)
Organized by project/component. Safer for smaller VPS. Each project is independent.
→ See `version2/`

## Quick Start (Version 2)

```bash
cd version2/01-agentos-dashboard
cp .env.example .env
# Edit .env with your OpenRouter API key
docker compose up -d
```

Then open `https://agentos.your-domain.com`

## Posts

- **#1** (this): Base Agent OS Dashboard + Connector — ✅ Deployed
- **#2**: Infinite Memory upgrade (Goldie Stack: Obsidian + Memory Engine + Hermes) — ✅ Deployed
- **#3**: OpenClaw capability reference — ✅ Documented
- **#4**: Hermes Agent capability reference — ✅ Documented
- **#5**: Hermes Agent — Build & Automate Anything (condensed tutorial, v0.9 features) — ✅ Documented
- **#6**: Lead Connector Derivatives + Goldie SEO Framework + Landing Pages — ✅ Documented

## Infrastructure Requirements

- Docker 28+ and Docker Compose v2+
- Traefik for SSL (optional but recommended)
- `root_default` Docker bridge network
- OpenRouter API key (for chat features)

## Documentation

### 🔧 Master System
| File | Purpose |
|------|---------|
| `docs/master-skool-post-conversion-system.md` | The complete unified process for converting any Skool post into Agent OS docs |

### 📖 Tutorials
| File | Purpose |
|------|---------|
| `docs/tutorial-skool-post-conversion.md` | DIY tutorial: How to convert a Skool post into Agent OS docs (Posts #3 & #4 walkthrough) |

### 📋 Capability References (General — for anyone)
| File | Purpose |
|------|---------|
| `docs/openclaw-capabilities-general.md` | OpenClaw capability reference (general) |
| `docs/hermes-agent-capabilities-general.md` | Hermes Agent capability reference (general) |

### 🖥️ Capability References (VPS-Annotated — for Agent OS users)
| File | Purpose |
|------|---------|
| `docs/openclaw-capabilities-vps-annotated.md` | OpenClaw capability reference (VPS/Docker annotations) |
| `docs/hermes-agent-capabilities-vps-annotated.md` | Hermes Agent capability reference (VPS/Docker annotations) |

### 🔗 Ecosystem Cross-References
| File | Purpose |
|------|---------|
| `docs/openclaw-agentos-ecosystem.md` | OpenClaw ↔ Agent OS integration guide |
| `docs/hermes-agent-agentos-ecosystem.md` | Hermes ↔ Agent OS integration guide |

### 🚀 QuickStart Guides
| File | Purpose |
|------|---------|
| `docs/agentos-base-quickstart.md` | Agent OS Base — Step-by-step walkthrough |
| `docs/goldie-stack-quickstart.md` | Goldie Stack — Step-by-step walkthrough |
| `docs/openclaw-quickstart.md` | OpenClaw — Step-by-step walkthrough |
| `docs/hermes-quickstart.md` | Hermes Agent — Step-by-step walkthrough |

### 📅 Launch Plans
| File | Purpose |
|------|---------|
| `docs/agentos-base-launch-plan.md` | Agent OS Base — Structured timeline |
| `docs/goldie-stack-launch-plan.md` | Goldie Stack — 30-day roadmap (day-by-day, week-by-week) |
| `docs/openclaw-launch-plan.md` | OpenClaw — Onboarding timeline |
| `docs/hermes-launch-plan.md` | Hermes Agent — 30-day phased plan |

### 🤖 AI Prompt Libraries
| File | Purpose | Count |
|------|---------|-------|
| `docs/agentos-base-prompts.md` | Agent OS Base — Build & usage prompts | ~15 |
| `docs/goldie-stack-prompts.md` | Goldie Stack — 100+ power prompts (10 categories) | 100+ |
| `docs/openclaw-prompts.md` | OpenClaw — Content, research, social, workflow prompts | ~30 |
| `docs/hermes-prompts.md` | Hermes Agent — Social, research, pipeline, advanced prompts | ~30 |

### 📐 SOPs (Standard Operating Procedures)
| File | Purpose |
|------|---------|
| `docs/goldie-stack-sop.md` | Goldie Stack — Full 30-step SOP across 7 phases |

### 🧠 Frameworks & Concepts
| File | Purpose |
|------|---------|
| `docs/goldie-stack-framework.md` | The Infinite Context Engine™ — 4-layer framework (Capture → Organise → Store → Deploy) |
| `docs/goldie-stack-limiting-beliefs.md` | 7 Limiting beliefs about AI memory — and the truth |

### 🛠️ Tool References
| File | Purpose |
|------|---------|
| `docs/goldie-stack-omi-tool.md` | OMI — The memory capture engine (Layer 1 & 2 of the Infinite Context Engine) |

### 📋 Hermes Agent — Post #5 Updates (v0.9)
| File | Purpose |
|------|---------|
| `docs/hermes-agent-teams.md` | Agent Teams deep-dive (Profiles, Telegram, Paperclipip, Hermes Workspace, Multica) |
| `docs/hermes-dashboard.md` | Hermes Dashboard (v0.9) — mission control, scheduled tasks, skills, config |
| `docs/hermes-one-click-setups.md` | One-Click Setups (Ollama + MaxHermes) |
| `docs/hermes-commands-reference.md` | Complete CLI command reference |

### 🔌 AI Agent Connection Guide
| File | Purpose |
|------|--------|
| `docs/lead-connector-ai-agent-connection-guide.md` | Step-by-step: Connect OpenClaw, Hermes, n8n, Agent OS to GHL, GoStackBase, BuildwithOS, Lead Connector |

### 📄 Lead Connector Derivatives (Post #6)
| File | Purpose |
|------|---------|
| `docs/lead-connector-derivatives-comparison.md` | Platform comparison (GHL, LC, GoStackBase, BuildwithOS) |
| `docs/ghl-to-stackbase-conversion.md` | GHL → GoStackBase template conversion system |
| `docs/ghl-to-buildwithos-conversion.md` | GHL → BuildwithOS template conversion system |
| `docs/agent-os-lead-connector-integration.md` | Full integration guide (OpenClaw + Hermes + n8n ↔ all platforms) |
| `docs/landing-pages-websites-sop.md` | SOP for building landing pages & websites with AI |
| `docs/highlevel-funnels-reference.md` | HighLevel 5 funnel templates reference |
| `docs/landing-pages-prompts.md` | AI prompts library for landing page copywriting |
| `docs/goldie-seo-framework.md` | Goldie SEO Framework — 5-phase AI SEO website framework (6 case studies) |
| `docs/stackbase-template-conversion.md` | GHL → GoStackBase clickable template conversion guide |

### 📊 Other
| File | Purpose |
|------|---------|
| `docs/VPS-AUDIT.md` | Post-installation VPS audit |

## Skills

| Skill | Purpose |
|-------|---------|
| `skills/lead-connector-bridge/` | Connect AI agents to GHL, GoStackBase, BuildwithOS — template recreation, contacts, funnels, automations |

## Storage Note

All documentation files are only created when content exists — no empty/placeholder files. This keeps the repo lean and VPS storage minimal.

## Security Flags

- 🔴 **Hermes Agent:** Hardcoded `ADMIN_PASSWORD=*** in the compose file. Change this immediately if you haven't already.
- 🔴 **OpenClaw:** Should not be exposed on VPS without proper authentication. Use Traefik + Cloudflare Workers.

## License

From Julian Goldie's AI Profit Boardroom (Skool).
Free to use. "As is", no warranty.
