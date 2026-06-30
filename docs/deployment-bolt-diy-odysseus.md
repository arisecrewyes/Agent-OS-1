# Bolt.DIY & Odysseus Deployment Guide

> Deployed: 2026-06-30
> VPS: Hostinger (31.220.62.81)
> Domain: srv1121935.hstgr.cloud

---

## Bolt.DIY — AI Coding Assistant

### Overview
- **Source:** https://github.com/stackblitz-labs/bolt.diy
- **Type:** Open-source AI coding assistant (StackBlitz Labs)
- **Docker Image:** bolt-diy:latest (built from source, 2.78GB)
- **Port:** 5173
- **URL:** https://bolt-diy.srv1121935.hstgr.cloud

### Build Process
1. Cloned repo to `/root/agentos-projects/bolt.diy`
2. Installed Node.js 22 + pnpm 9.15.9 on host
3. Ran `pnpm install --frozen-lockfile` then `pnpm run build`
4. Built Docker image: `docker build -t bolt-diy:latest --load .`
5. Note: Prebuilt GHCR image was denied, so we built from source
6. Note: Had to install `wrangler` globally in container (not in prod deps)

### Configuration
- **OpenRouter API Key:** PLACEHOLDER (replace with real key)
- **Free models only:** Google Flash, DeepSeek Light, Mistral (via OpenRouter free tier)
- **Ollama:** Configured for local models at `http://127.0.0.1:11434`

### Startup Command
```bash
cd /root/agentos/bolt-diy
docker compose up -d
```

### Health Check
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:5173/
# Expected: 200
```

---

## Odysseus — Self-Hosted AI Workspace

### Overview
- **Source:** https://github.com/pewdiepie-archdaemon/odysseus
- **Type:** PewDiePie's self-hosted AI workspace
- **Docker Image:** odysseus-odysseus (built from source)
- **Port:** 7000
- **URL:** https://odysseus.srv1121935.hstgr.cloud

### Dependencies
| Service | Image | Port | Purpose |
|---------|-------|------|---------|
| Chromadb | chromadb/chroma:latest | 8101 | Vector database |
| SearXNG | searxng/searxng:2026.5.31 | 8080 | Search engine |
| ntfy | binwiederhier/ntfy | 8091 | Notifications |

### Admin Credentials
- **Username:** admin
- **Password:** (stored in `/root/agentos/odysseus/.admin_password` on VPS)
- **Login URL:** https://odysseus.srv1121935.hstgr.cloud/login

### Build Process
1. Cloned repo to `/root/agentos-projects/odysseus`
2. Built with `docker compose build` (3-stage: realesrgan-wheels → builder → production)
3. Python 3.14 base image
4. First run triggers `setup.py` for initial configuration

### Configuration
- **Auth:** Enabled (AUTH_ENABLED=true)
- **Database:** SQLite at `/app/data/app.db`
- **Embeddings:** FastEmbed with `sentence-transformers/all-MiniLM-L6-v2`
- **LLM:** None configured yet (needs OpenRouter/Ollama/OpenAI key)
- **Search:** SearXNG (local), no external search APIs configured

### Startup Command
```bash
cd /root/agentos/odysseus
docker compose up -d
```

### Health Check
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:7000/
# Expected: 302 (redirect to login)
curl -s -o /dev/null -w "%{http_code}" http://localhost:7000/login
# Expected: 200
```

---

## Traefik Routing

Both services are routed through Traefik with SSL:

| Service | Domain | HTTPS |
|---------|--------|-------|
| Bolt.DIY | bolt-diy.srv1121935.hstgr.cloud | ✅ |
| Odysseus | odysseus.srv1121935.hstgr.cloud | ✅ |
| Agent OS | agentos.srv1121935.hstgr.cloud | ✅ |
| n8n | n8n.srv1121935.hstgr.cloud | ✅ |

### Network
- All services connected to `traefik-public` bridge network
- Traefik discovers services via Docker labels
- SSL via Let's Encrypt (ACME TLS challenge)

---

## Post-Deployment Tasks

### Immediate
1. **Bolt.DIY:** Replace placeholder OpenRouter API key with real key
2. **Odysseus:** Configure LLM provider (OpenRouter recommended)
3. **Odysseus:** Change admin password from generated one

### Optional
4. Configure Ollama for local LLM inference
5. Set up external search API keys (DataBrave, Google PSE, Tavily, Serper)
6. Configure email/SMTP for Odysseus
7. Set up ntfy for mobile notifications

---

## Troubleshooting

### Bolt.DIY won't start
- Check: `docker compose logs --tail=30`
- Common issue: `wrangler: not found` → fixed by installing wrangler globally
- Fix: `docker compose restart`

### Odysseus can't connect to Chromadb
- Check: `docker compose ps` (chromadb should be running)
- Port conflict: Host port 8100 was taken by goldie-memory-engine, changed to 8101
- Fix: `docker compose restart chromadb`

### Traefik not routing
- Check: `docker network inspect traefik-public`
- Fix: `docker network connect traefik-public <container_name>`
