# OpenClaw ↔ Agent OS Ecosystem Cross-Reference

> How OpenClaw integrates with the broader Agent OS system on the Hostinger VPS
> Date: 2026-06-27
> Related: [[openclaw-capabilities-general]] | [[openclaw-capabilities-vps-annotated]]

---

## Architecture Overview

The Agent OS system runs on a Hostinger VPS (Ubuntu 24.04) using Docker Compose. OpenClaw is one of **multiple AI agents** running as independent containers on a shared Docker bridge network (`root_default`).

```
                    Internet
                       │
                       ▼
              ┌──────────────┐
              │   Traefik    │ ← SSL termination, reverse proxy
              │  (ports 80,  │
              │     443)     │
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
   ┌──────────┐ ┌────────┐ ┌──────────┐
   │  Agent   │ │  n8n   │ │ Obsidian │
   │   OS     │ │Workflows│ │  Vault   │
   │Dashboard │ │        │ │          │
   └────┬─────┘ └────────┘ └──────────┘
        │
        │  root_default (Docker bridge network)
        │
   ┌────┴──────────────────────────────┐
   │                                    │
   ▼                                    ▼
┌──────────┐  ┌──────────┐  ┌──────────────────┐
│ Agent    │  │  Hermes  │  │ Memory Engine    │
│Connector │  │  Agent   │  │ (Goldie Stack)   │
│ (Router) │  │          │  │                  │
└────┬─────┘  └──────────┘  └──────────────────┘
     │
     ├──────────────┬──────────────┐
     │              │              │
     ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌──────────────┐
│ OpenClaw │  │ OpenClaw │  │ Universal    │
│  #1 (OWL)│  │  #2      │  │ API Gateway  │
│          │  │          │  │              │
└──────────┘  └──────────┘  └──────────────┘
```

---

## OpenClaw's Role in Agent OS

### What OpenClaw Does

OpenClaw serves as the **primary conversational AI interface** for the entire Agent OS system. It is the agent that users interact with directly via Telegram (or other messaging apps).

**Key Functions:**
- **Conversational AI** — Natural language interface for the entire system
- **Task Orchestration** — Plans and delegates work to specialized agents
- **Sub-Agent Management** — Spawns and coordinates sub-agents for parallel work
- **Memory & Context** — Remembers user preferences, business details, workflows
- **Messaging Integration** — Connects via Telegram, WhatsApp, Discord, etc.
- **Browser Automation** — Controls browser for web-based tasks
- **Content Publishing** — Publishes to WordPress, Notion, Twitter/X, etc.

### What OpenClaw Does NOT Do (Other Agents Handle This)

| Function | Agent | Why Not OpenClaw |
|----------|-------|------------------|
| **Agent Registration & Routing** | Connector Router | Dedicated routing layer |
| **Long-term Memory (files)** | Memory Engine + Obsidian Vault | Persistent file-based memory |
| **SEO-Specific Tasks** | OSINT Specialist (Sherlock) | Specialized OSINT tools |
| **Workflow Automation** | n8n | Structured, repeatable workflows |
| **Dashboard UI** | Agent OS Dashboard (Next.js) | Web-based GUI |
| **Multi-Agent Coordination** | Hermes Agent | Specialized agent coordination |

---

## How OpenClaw Communicates with Other Agents

### Via the Connector Router

The Connector Router (Express.js on port 8888) is the central message bus. OpenClaw can send requests to specific agents through it:

```
User → Telegram → OpenClaw → Connector Router → Target Agent
                  ▲                              │
                  └────── Response ──────────────┘
```

### Via the root_default Docker Network

All containers are on the same Docker bridge network. OpenClaw can reach other services by container name:
- `http://agentos-connector:8888` — Connector Router
- `http://hermes-agent:32769` — Hermes Agent
- `http://memory-engine:8090` — Memory Engine
- `http://root-n8n-1:5678` — n8n

### Via Sub-Agents

OpenClaw can spawn sub-agents that run as separate processes or containers. These sub-agents can:
- Use different AI models (cheaper for simple tasks)
- Run in parallel for faster execution
- Specialize in specific domains (SEO, content, research)

---

## OpenClaw vs Other Agents in the Stack

| Agent | Type | Primary Role | How OpenClaw Uses It |
|-------|------|-------------|----------------------|
| **Connector Router** | Infrastructure | Message routing, agent registry | Sends chat requests to specific agents |
| **Hermes Agent** | AI Agent | Multi-agent coordination, research | Delegates complex research tasks |
| **Memory Engine** | Service | Long-term memory, Obsidian vault | Reads/writes persistent memory |
| **OSINT Specialist** | AI Agent | SEO intelligence, competitor monitoring | Delegates SEO research tasks |
| **Universal API Gateway** | Infrastructure | API aggregation, rate limiting | Routes API requests |
| **n8n** | Workflow Engine | Structured automation | Handles scheduled/repetitive workflows |
| **Agent OS Dashboard** | Web UI | User interface, monitoring | Provides visual management |

---

## Current OpenClaw Configuration (VPS)

### Container Details
- **Container Names:** `openclaw-oi15-openclaw-1`, `openclaw-x9sc-openclaw-1`
- **Port:** 51461 (internal, via Traefik if exposed)
- **API Provider:** OpenRouter (`openrouter/owl-alpha` model)
- **Messaging:** Telegram (primary)
- **Network:** `root_default` (Docker bridge)

### Environment Variables
```
OPENROUTER_API_KEY=sk-or-v1-...
```

### Compose File Location
`/root/agentos-projects/agent-connector/docker-compose.yml`

---

## OpenClaw + n8n Integration

These two tools complement each other:

| | OpenClaw | n8n |
|---|----------|-----|
| **Best for** | Ad-hoc tasks, creative work | Structured, repeatable workflows |
| **Interface** | Natural language (chat) | Visual node editor |
| **Flexibility** | Describe what you want | Build exact workflow |
| **Example** | "Write and publish a blog post about X" | "When webhook received → format data → post to WordPress → send notification" |

### Integration Patterns

1. **OpenClaw triggers n8n:** OpenClaw sends a webhook to n8n to trigger a structured workflow
2. **n8n triggers OpenClaw:** n8n workflow sends a request to OpenClaw for AI-powered steps
3. **OpenClaw monitors n8n:** OpenClaw checks n8n workflow status and reports to user

---

## OpenClaw + Obsidian Vault (Goldie Stack)

The Goldie Stack (from Skool Post #2) includes an Obsidian Vault for persistent knowledge storage:

- **Obsidian Vault:** Runs in container `goldie-obsidian-vault` on port 8200
- **Memory Engine:** Runs in container `goldie-memory-engine` on port 8100
- **Shared Volume:** `obsidian-vault-data` persistent Docker volume

### How OpenClaw Benefits
- OpenClaw agents can read from the Obsidian vault (via Memory Engine API)
- Knowledge and research stored in Obsidian is available to OpenClaw
- OpenClaw can create/update Obsidian notes via the vault API
- This creates a **shared knowledge base** across all Agent OS agents

---

## Security Boundaries

### OpenClaw Container
- Internal port only (not directly exposed to internet)
- API keys via environment variables
- On `root_default` network (isolated from host)
- Can reach: Connector, Hermes, Memory Engine, n8n, Obsidian Vault

### Traefik (Entry Point)
- Only exposes specific ports (80, 443)
- SSL termination
- Routes to appropriate containers based on domain
- OpenClaw is NOT directly accessible from outside

### What's NOT Exposed
- OpenClaw's internal port (51461) — not routed through Traefik
- Connector Router (8888) — internal only
- Memory Engine (8090) — internal only
- n8n (5678) — internal only (or via Traefik with auth)

---

## Adding New OpenClaw Capabilities

When new OpenClaw skills or capabilities are discovered (from this course or elsewhere):

1. **Document the capability** in the OpenClaw capability reference files
2. **Check for integration points** with existing Agent OS agents
3. **Update this cross-reference** if new agent connections are established
4. **Test in isolation** before connecting to the production system
5. **Monitor API costs** — new capabilities may increase token usage

---

## Summary

OpenClaw is the **conversational brain** of the Agent OS system. It excels at:
- Natural language interaction
- Task planning and orchestration
- Creative and ad-hoc work
- Multi-step workflows that require reasoning

It works alongside specialized agents (Hermes, OSINT, Memory Engine) and infrastructure tools (n8n, Traefik, Connector Router) to form a complete AI agent ecosystem.

For the full capability reference, see:
- `openclaw-capabilities-general.md` — General reference (any user)
- `openclaw-capabilities-vps-annotated.md` — VPS/Docker annotated version

---

## Metadata

- Tags: `agent-os`, `architecture`, `openclaw`, `integration`, `ecosystem`
- VPS: Hostinger 31.220.62.81 (srv1121935)
- Last Updated: 2026-06-27
