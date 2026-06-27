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

- **#1** (this): Base Agent OS Dashboard + Connector — 2 containers ✅
- **#2**: Infinite Memory upgrade (Goldie Stack) — ✅
- **#3**: OpenClaw capability reference — ✅ `docs/openclaw-capabilities-general.md`
- **#4**: Hermes Agent capability reference — ✅ `docs/hermes-agent-capabilities-general.md`
- **#5+**: Extensions — coming soon

## Infrastructure Requirements

- Docker 28+ and Docker Compose v2+
- Traefik for SSL (optional but recommended)
- `root_default` Docker bridge network
- OpenRouter API key (for chat features)

## Documentation

### Capability References
| File | Purpose |
|------|---------|
| `docs/VPS-AUDIT.md` | Post-installation VPS audit |
| `docs/openclaw-capabilities-general.md` | OpenClaw capability reference (general) |
| `docs/openclaw-capabilities-vps-annotated.md` | OpenClaw capability reference (VPS-annotated) |
| `docs/openclaw-agentos-ecosystem.md` | OpenClaw ↔ Agent OS integration guide |
| `docs/hermes-agent-capabilities-general.md` | Hermes Agent capability reference (general) |
| `docs/hermes-agent-capabilities-vps-annotated.md` | Hermes Agent capability reference (VPS-annotated) |
| `docs/hermes-agent-agentos-ecosystem.md` | Hermes ↔ Agent OS integration guide |

### QuickStart Guides
| File | Purpose |
|------|---------|
| `docs/agentos-base-quickstart.md` | Agent OS Base — QuickStart |
| `docs/goldie-stack-quickstart.md` | Goldie Stack — QuickStart |
| `docs/openclaw-quickstart.md` | OpenClaw — QuickStart |
| `docs/hermes-quickstart.md` | Hermes Agent — QuickStart |

### Launch Plans
| File | Purpose |
|------|---------|
| `docs/agentos-base-launch-plan.md` | Agent OS Base — Launch Plan |
| `docs/goldie-stack-launch-plan.md` | Goldie Stack — Launch Plan |
| `docs/openclaw-launch-plan.md` | OpenClaw — Launch Plan |
| `docs/hermes-launch-plan.md` | Hermes Agent — Launch Plan |

### AI Prompt Libraries
| File | Purpose |
|------|---------|
| `docs/agentos-base-prompts.md` | Agent OS Base — Prompts |
| `docs/goldie-stack-prompts.md` | Goldie Stack — Prompts |
| `docs/openclaw-prompts.md` | OpenClaw — Prompts |
| `docs/hermes-prompts.md` | Hermes Agent — Prompts |

### Tutorials & Deployment
| File | Purpose |
|------|---------|
| `version2/DEPLOYMENT.md` | Version 2 deployment guide |
| `docs/tutorial-skool-post-conversion.md` | DIY tutorial: How to convert a Skool post into Agent OS docs |

## License

From Julian Goldie's AI Profit Boardroom (Skool).
Free to use. "As is", no warranty.
