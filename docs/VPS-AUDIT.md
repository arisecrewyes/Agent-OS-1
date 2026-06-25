# VPS Audit — Post Skool Post #1 Installation

**Date:** 2026-06-25
**VPS:** srv1121935 (31.220.62.81)
**OS:** Ubuntu 24.04.3 LTS
**Docker:** 28.5.1
**Compose:** v2.40.1
**Disk:** 96 GB total, 35 GB free (65%)
**RAM:** 7.8 GB total, 5.4 GB available

## Running Containers (14 total)

| Container | Status | Ports | Purpose |
|-----------|--------|-------|---------|
| agent-os | ✅ Running | 3000 | Agent OS Dashboard (Next.js 16.2.9) |
| agentos-connector | ✅ Running | 8888 | Agent Router (Express.js, 17 agents) |
| root-traefik-1 | ✅ Running | 80, 443 | Traefik SSL |
| root-n8n-1 | ✅ Running | 5678 | n8n workflows |
| openclaw-oi15-openclaw-1 | ✅ Running | 51461 | OpenClaw #1 |
| openclaw-x9sc-openclaw-1 | ✅ Running | 51461 | OpenClaw #2 |
| hermes-agent-7llb-hermes-agent-1 | ✅ Running | 32769→4860 | Hermes Agent |
| memory-engine | ✅ Running | 8090 | Memory Engine |
| osint-sherlock | ✅ Running | 9090 | OSINT Specialist |
| universal-api-gateway | ✅ Running | 8889 | Universal API Gateway |

## Verified Checklist

- [x] Dashboard HTTPS: HTTP 200
- [x] Connector health: {"status":"ok"}
- [x] Connector agents: 17 registered
- [x] Traefik SSL routing: Working
- [x] Infrastructure: All services healthy
- [x] Disk: 35 GB free (65%)
- [x] RAM: 5.4 GB available
