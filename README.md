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

- **#1** (this): Base Agent OS Dashboard + Connector — 2 containers
- **#2**: Infinite Memory upgrade — coming soon
- **#3+**: Extensions — coming soon

## Infrastructure Requirements

- Docker 28+ and Docker Compose v2+
- Traefik for SSL (optional but recommended)
- `root_default` Docker bridge network
- OpenRouter API key (for chat features)

## License

From Julian Goldie's AI Profit Boardroom (Skool).
Free to use. "As is", no warranty.
