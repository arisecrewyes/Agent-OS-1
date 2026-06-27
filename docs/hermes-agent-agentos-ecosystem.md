# Hermes Agent ↔ Agent OS Ecosystem Cross-Reference

> How Hermes Agent integrates with the broader Agent OS system on the Hostinger VPS
> Date: 2026-06-27
> Related: [[hermes-agent-capabilities-general]] | [[openclaw-agentos-ecosystem]]

---

## Architecture Overview

Hermes Agent is one of **multiple AI agents** running as independent containers on the Agent OS Docker network. It occupies a unique position as the **self-improving research and skill-building agent**.

```
                    Internet
                       │
                       ▼
              ┌──────────────┐
              │   Traefik    │ ← SSL termination, reverse proxy
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
   ┌──────────┐ ┌────────┐ ┌──────────┐
   │  Agent   │ │  n8n   │ │ Obsidian │
   │   OS     │ │Workflows│ │  Vault   │
   │Dashboard │ │        │ │          │
   └────┬─────┘ └────────┘ └────┬─────┘
        │                         │
        │  root_default network   │
        │                         │
   ┌────┴─────────────────────────┴────┐
   │                                    │
   ▼                                    ▼
┌──────────┐  ┌──────────┐  ┌──────────────────┐
│ OpenClaw │  │  Hermes  │  │ Memory Engine    │
│  Agents  │  │  Agent   │  │ (Goldie Stack)   │
│          │  │          │  │                  │
└──────────┘  └──────────┘  └──────────────────┘
```

---

## Hermes' Role in Agent OS

### What Hermes Does

Hermes serves as the **self-improving research and automation agent**. Its unique capabilities:

| Capability | Description |
|-----------|-------------|
| **Self-Improving Loop** | Creates skills from experience, improves them with feedback |
| **Research Agent** | Web research via Firecrawl, Reddit monitoring, trending news |
| **Skill Builder** | Auto-generates reusable skills from complex tasks |
| **Multi-Agent Profiles** | Run multiple isolated instances from one installation |
| **MCP Server** | Acts as backend brain for Claude Desktop, Cursor, VS Code |
| **40+ Built-in Tools** | Web search, browser automation, terminal, file management, image gen, TTS |
| **Scheduled Tasks** | Native cron job scheduling |
| **Social Media Automation** | X, TikTok, Instagram posting |
| **Jarvis Voice** | Real-time voice assistant |
| **Jarvis Briefing** | Daily/weekly rundown from Obsidian vault |

### What Hermes Does NOT Do (Other Agents Handle This)

| Function | Agent | Why Not Hermes |
|----------|-------|----------------|
| **Conversational AI** | OpenClaw | OpenClaw excels at chat and messagingAgent Registration** | Connector Router | Dedicated routing layer |
| **Long-term Memory** | Memory Engine + Obsidian | Persistent file-based memory |
| **OSINT/SEO Research** | Sherlock (OSINT Specialist) | Specialized OSINT tools |
| **Structured Workflows** | n8n | Node-based workflow builder |
| **Dashboard UI** | Agent OS Dashboard | Web-based GUI |
| **Multi-Agent Coordination** | Connector Router | Central message bus |

---

## How Hermes Communicates with Other Agents

### Via the Connector Router

```
User → Telegram → OpenClaw → Connector Router → Hermes Agent
                                         │
                                         ├→ OpenClaw agents
                                         ├→ Memory Engine
                                         ├→ n8n
                                         └→ Sherlock (OSINT)
```

### Via the root_default Docker Network

All containers share the same Docker bridge network. Hermes can reach:
- `http://agentos-connector:8888` — Connector Router
- `http://goldie-obsidian-vault:8200` — Obsidian Vault
- `http://goldie-memory-engine:8100` — Memory Engine
- `http://root-n8n-1:5678` — n8n
- `http://hermes-agent-7llb-hermes-agent-1:8642` — Hermes API
- `http://hermes-agent-7llb-hermes-agent-1:4860` — Hermes Web UI

### Via MCP (Model Context Protocol)

Hermes can run as an MCP server:
```bash
hermes mcp serve
```
This allows other tools (Claude Desktop, Cursor, OpenClaw) to use Hermes as a backend brain.

---

## Hermes vs OpenClaw: Coexistence in Agent OS

| | OpenClaw | Hermes |
|---|----------|--------|
| **Role** | Conversational AI, messaging interface | Research, skill-building, automation |
| **Best for** | Chat, ad-hoc tasks, browser control | Complex research, learning, automation |
| **Self-Improving** | ❌ Limited | ✅ Core feature |
| **Messaging** | 50 platforms | 6 platforms |
| **Heartbeat** | ✅ Every 30 min | ❌ |
| **Speed** | Slower | Faster |
| **Community** | Larger | Growing fast |

### How They Complement Each Other

1. **OpenClaw** handles the conversational interface — users interact with it via Telegram/WhatsApp
2. **Hermes** handles the heavy lifting — research, skill creation, complex automation
3. **OpenClaw can delegate to Hermes** for tasks requiring deep research or learning
4. **Hermes can post to OpenClaw** via the Docker network
5. **Both share the Obsidian Vault** for persistent knowledge

---

## Hermes ↔ Obsidian Vault Integration

The **Jarvis Briefing** feature reads the Obsidian vault to generate daily/weekly rundowns:

### How It Works
1. Hermes connects to the Obsidian vault via HTTP (port 8200)
2. Reads daily notes, to-dos, memory captures
3. Generates a structured briefing:
   - Open to-dos
   - What you worked on
   - Recent memory captures
   - Daily-note "Top 3"
   - Weekly wins and day-by-day activity
4. Can deliver as spoken summary in Jarvis voice

### Technical Path
```
Hermes Agent → HTTP → Obsidian Vault (goldie-obsidian-vault:8200)
                                  │
                                  ▼
                          obsidian-vault-data volume
                          (persistent Docker volume)
```

### Obsidian Vault is Shared Across Agents
- OpenClaw can read/write Obsidian notes
- Hermes reads Obsidian for Jarvis Briefing
- Memory Engine indexes Obsidian content
- This creates a **shared knowledge base** for the entire Agent OS ecosystem

---

## Hermes ↔ n8n Integration

These tools complement each other:

| | Hermes | n8n |
|---|--------|-----|
| **Best for** | Ad-hoc research, learning, creative work | Structured, repeatable workflows |
| **Interface** | Natural language | Visual node editor |
| **Example** | "Research AI trends and create a post" | "When webhook → format data → post → notify" |

### Integration Patterns
1. **Hermes triggers n8n:** Hermes sends webhook to n8n to trigger a structured workflow
2. **n8n triggers Hermes:** n8n workflow sends request to Hermes for AI-powered steps
3. **Hermes monitors n8n:** Hermes checks n8n workflow status and reports to user

---

## Hermes ↔ Memory Engine

Both have memory capabilities but serve different purposes:

| | Hermes Memory | Memory Engine |
|---|--------------|---------------|
| **Type** | Agent conversation memory + skills | File-based persistent memory |
| **Storage** | `memory.md`, `user.md`, `skill.md` in container | Obsidian vault (persistent volume) |
| **Access** | Internal to Hermes | HTTP API (port 8100) |
| **Persistence** | Container-bound (needs volume) | Docker volume (persistent) |

### Relationship
- Hermes' memory files could be stored in the Obsidian vault via the Memory Engine
- This would make Hermes memory persistent across container restarts
- Currently, Hermes memory is container-bound unless volumes are explicitly mounted

---

## Hermes in the Agent OS Dashboard

The Agent OS Dashboard (Next.js on port 3000) has a dedicated **Hermes tab** with 10 sections:

| Section | Purpose |
|---------|---------|
| 💬 **Chat** | Talk to Hermes — can do things (files, web, commands) |
| 🎙️ **Talk** | Real-time voice conversation |
| 🤖 **Hermes-Jarvis** | Iron-Man-style voice assistant (build apps, daily briefings) |
| ✨ **Studio** | Generate videos and media |
| 🕐 **Sessions** | Every past Hermes conversation, saved |
| 📦 **Workspace** | Files Hermes/Jarvis made, organized in folders |
| 🔌 **MCPs** | Plug-ins for extra powers (browsers, databases, tools) |
| ⚙️ **Manage** | Skills, plugins, kanban board, health doctor |
| 🖥️ **Control Room** | Raw terminal view with Status and Insights panels |
| 🎯 **Goal Mode** | Give Hermes a goal, it works toward it in steps |

> These 10 sections are configured in the Agent OS Dashboard codebase, not in Hermes itself. The Dashboard communicates with Hermes via the Connector Router and direct HTTP calls.

---

## Hermes Container Configuration

### Current Setup
- **Container:** `hermes-agent-7llb-hermes-agent-1`
- **Image:** `ghcr.io/hostinger/hvps-hermes-agent:latest`
- **Ports:** 8642 (API), 4860 (web UI) — internal only
- **Network:** `root_default` (Docker bridge)
- **Access:** Via Traefik → `hermes.srv1121935.hstgr.cloud`

### ⚠️ Security Warning
The Hermes compose file has **hardcoded admin credentials** (`ADMIN_PASSWORD=admin123`). **Change these immediately.**

### Environment Variables
- `OPENROUTER_API_KEY` (or other provider key)
- `ADMIN_PASSWORD` — ⚠️ **MUST BE CHANGED**

---

## Adding New Hermes Capabilities

When new Hermes skills or features are discovered:

1. **Document the capability** in the Hermes capability reference files
2. **Check for integration points** with existing Agent OS agents
3. **Update this cross-reference** if new agent connections are established
4. **Test in isolation** before connecting to the production system
5. **Monitor API costs** — new capabilities may increase token usage
6. **Back up custom skills** to the Agent OS GitHub repo

---

## Summary

Hermes Agent is the **self-improving research and automation engine** of the Agent OS system. Its unique learning loop makes it fundamentally different from other agents — it gets smarter over time, building skills from experience.

It works alongside:
- **OpenClaw** (conversational AI + messaging)
- **n8n** (structured workflows)
- **Memory Engine + Obsidian Vault** (persistent knowledge)
- **Connector Router** (agent coordination)
- **Sherlock** (OSINT specialist)
- **Agent OS Dashboard** (management UI)

Together, they form a complete AI agent ecosystem.

For the full capability reference, see:
- `hermes-agent-capabilities-general.md` — General reference (any user)
- `hermes-agent-capabilities-vps-annotated.md` — VPS/Docker annotated version

---

## Metadata

- Tags: `agent-os`, `architecture`, `hermes`, `integration`, `ecosystem`
- VPS: Hostinger 31.220.62.81 (srv1121935)
- Hermes Version: v0.9 (at time of Post #5)
- Last Updated: 2026-06-27

---

## 🆕 Agent Teams (v0.9 — Post #5 Update)

Hermes supports running multiple agents as a team. On the Agent OS VPS:

### Profiles
Run multiple isolated Hermes instances via Docker. Each profile = separate container with own config/model/memory.
```bash
hermes profile create <name>
```

### Telegram Group Chat
Connect multiple Hermes agents to the same Telegram group. No additional Docker config needed.

### Agent Team Frameworks
Open-source frameworks deployable alongside Hermes on the VPS:
- **Paperclipip:** https://github.com/NousResearch/hermes-paperclip-adapter
- **Hermes Workspace:** https://github.com/outsourc-e/hermes-workspace
- **Multica:** https://github.com/multica-ai/multica

> ⚠️ These require additional Docker configuration and Traefik routing for web dashboard access.

## 🆕 Hermes Dashboard (v0.9)

`hermes dashboard` launches a web-based mission control. On the VPS it runs inside the Hermes Docker container and requires SSH tunnel or Traefik route for external access.

Features:
- Scheduled tasks (24/7 autonomous automations)
- Skills manager (saved expert automations on demand)
- Config panel (models, delegation, memory, voice, API keys)
- Token usage analytics and session monitoring

## 🆕 One-Click Setups

- **Ollama:** Add to Docker compose with GPU passthrough for local models. `ollama launch hermes` for one-click Hermes startup.
- **MaxHermes:** Alternative Docker image for quick setup. Less control but easier.

## Related

- For agent teams details: `hermes-agent-teams.md`
- For the dashboard: `hermes-dashboard.md`
- For one-click setups: `hermes-one-click-setups.md`
- For the general capability reference: `hermes-agent-capabilities-general.md`
- For the VPS-annotated reference: `hermes-agent-capabilities-vps-annotated.md`
