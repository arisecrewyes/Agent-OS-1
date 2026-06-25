# Deployment Guide — Agent OS on Hostinger VPS

## Prerequisites

1. Hostinger VPS with Docker Compose support
2. Ubuntu 24.04+ installed
3. Docker 28+ and Docker Compose v2.40+
4. OpenRouter API key from openrouter.ai
5. Traefik + SSL cert resolver (optional but recommended)

## Network Setup

```bash
docker network create root_default
```

## Step-by-Step (Version 2)

### 1. Agent OS Dashboard (Priority 1)

```bash
cd version2/01-agentos-dashboard
cp .env.example .env  # Edit with your OpenRouter API key
docker compose up -d
```

Verify:
```bash
curl https://your-domain.com   # → 200
curl http://localhost:3000        # → HTML dashboard
curl http://localhost:8888/health # → {"status":"ok"}
```

### 2-8. Extensions — Coming in Posts #2+

## Environment Variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| OPENROUTER_API_KEY | Yes | — | AI chat requests |
| VAULT_PATH | No | /data/agentos-vault | Obsidian vault path |
| NEXT_PUBLIC_APP_URL | No | https://agentos.srv1121935.hstgr.cloud | App URL |
