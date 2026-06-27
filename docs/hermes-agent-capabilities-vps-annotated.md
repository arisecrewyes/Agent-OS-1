# Hermes Agent — Complete Capability Reference (VPS-Annotated Version)

> Source: Julian Goldie SEO — Skool Post #4: "Hermes: Full 2 Hour Course!"
> Original Video: https://www.youtube.com/watch?v=8avW0D2sEn8
> GitHub: https://github.com/NousResearch/hermes-agent
> Date: 2026-06-27
> Purpose: Capability reference with annotations for VPS/Docker deployment
>
> 📝 **Note:** This version includes deployment-specific annotations marked with `[VPS]` tags. For the general reference without annotations, see `hermes-agent-capabilities-general.md`.

---

## What is Hermes Agent?

Hermes Agent is a free, open-source AI agent built by **Nous Research**. Unlike regular chatbots, it:
- **Remembers everything** across sessions
- **Creates its own skills** from experience
- **Improves those skills** every time it uses them
- **Runs 24/7** even when your computer is off
- Connects to **Telegram, Discord, Slack, WhatsApp, Signal**, and your terminal

> **[VPS] Already Deployed:** Hermes Agent is already running in the Agent OS Docker stack. Container: `hermes-agent-7llb-hermes-agent-1`. See `openclaw-agentos-ecosystem.md` for how it fits into the broader Agent OS architecture.

---

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes setup
hermes doctor
```

> **[VPS] Docker Installation:** In the Agent OS, Hermes is deployed via Docker Compose (container image: `ghcr.io/hostinger/hvps-hermes-agent:latest`). The install script is NOT used in Docker — the container image handles setup. Configuration is via environment variables in the compose file.

> **[VPS] Admin Credentials:** ⚠️ **SECURITY WARNING:** The Hermes compose file has hardcoded admin credentials (`ADMIN_PASSWORD=admin123`). **Change these immediately** if you haven't already. Use strong, unique passwords.

---

## AI Model Selection

### Free Option
Use **Alibaba's Qwen 3.6 Plus Preview** on OpenRouter (1M token context, free).

> **[VPS] Current Agent OS Setup:** The Hermes container is configured with OpenRouter API key via environment variable. The model can be changed in the Hermes web UI or config without rebuilding the container.

### Switching Models
```bash
hermes model
```

> **[VPS] Docker Model Switch:** In Docker, models are configured via the Hermes web UI (port 4860) or by editing the config file. No container rebuild needed for model changes.

### Fallback Chains
Set up backup models so your agent never stops if one API goes down.

> **[VPS] Docker Fallback:** Configure fallback chains in the Hermes config file mounted into the container, or via environment variables in the compose file.

---

## Messaging Platforms

```bash
hermes gateway setup
hermes gateway start
```

**Supported:** Telegram, Discord, Slack, WhatsApp, Signal, CLI

> **[VPS] Docker Networking:** The Hermes container is on the `root_default` Docker bridge network. Ports 8642 (API) and 4860 (web UI) are internal. External access is via Traefik reverse proxy. The gateway setup is done through the web UI, not CLI.

> **[VPS] Telegram in Docker:** Works the same as local — bot token is configured via environment variable or web UI. The gateway runs inside the container and maintains the Telegram connection.

---

## First 7 Days (Training Period)

**Critical:** Do NOT treat Hermes like a regular chatbot.

- **Day 1-3:** Hermes builds `memory.md` and `user.md` — injected into every session.
- **Day 4-7:** Knows your projects and preferences. Creates skills automatically.
- **Key mindset:** Not perfect at first. Give feedback. It improves.

> **[VPS] Memory Persistence in Docker:** Hermes memory files (`memory.md`, `user.md`, `skill.md`) are stored inside the container. **Ensure these are on a persistent Docker volume** or they'll be lost on container rebuild. The Agent OS compose should mount a volume for Hermes data.

---

## Community Skills

```bash
hermes skills install wonderly-skills
```

- **40+ skills** out of the box
- **Wonderly Skills** library: 250+ stars
- Skills load efficiently (only when needed)
- Security scanner checks every skill

> **[VPS] Skills in Docker:** Skills are stored inside the container. For persistence, mount a volume for the skills directory. Alternatively, rebuild the container with a Dockerfile that includes skill installation.

---

## Creating Custom Skills

Three ways:
1. **Automatic:** Hermes creates skills after complex tasks
2. **Ask:** "Create a skill for..."
3. **Manual:** Write markdown in `~/.hermes/skills/`

**Back up skill.md files weekly.**

> **[VPS] Custom Skills in Docker:** Store custom skills on a mounted volume to persist across container restarts. Consider version-controlling your custom skills in the Agent OS GitHub repo.

---

## Scheduled Tasks (Cron Jobs)

Tell Hermes in plain language what you want and when. Handles scheduling natively.

> **[VPS] Cron in Docker:** Hermes' built-in scheduler works inside the container. For persistence across restarts, store scheduled task definitions in a mounted volume or recreate them via the entrypoint.

> **[VPS] Alternative — System Cron:** For critical scheduled tasks, consider using the host system's cron to trigger Hermes via API call, as a backup if the container restarts.

---

## External Tools

| Tool | Purpose | Setup |
|------|---------|-------|
| **Firecrawl** | Web browsing | API key from firecrawl.dev/app |
| **Browser Base** | Visual browsing | Browser instance |
| **Nana Banana 2** | Image generation | API key |
| **X/Twitter API** | Direct posting | developer.x.com |
| **MCP** | External tools | `hermes mcp serve` |

> **[VPS] Firecrawl in Docker:** Works from the container as long as the API key is configured. The container can reach Firecrawl's API via the internet.

> **[VPS] Browser Base in Docker:** Requires a browser instance accessible from the container. The Agent OS project includes a `browser-use-webui` container (currently stopped) that could serve this purpose.

> **[VPS] MCP in Docker:** `hermes mcp serve` can be exposed on a dedicated port, allowing other containers (OpenClaw, Claude Code, etc.) to connect to Hermes as an MCP server.

---

## Multi-Agent Profiles

```bash
hermes profile create twitter-agent
hermes profile create research-agent
```

Each profile = fully isolated (own config, API keys, memory, sessions, skills, gateway).

> **[VPS] Profiles in Docker:** Profiles can be created via the web UI (port 4860) or CLI if you exec into the container. Each profile's data should be on a persistent volume.

---

## Migrating from OpenClaw

```bash
hermes claw migrate
hermes claw migrate --dry-run
```

Migrates: SOUL.md, memories, skills, command allowlist, messaging settings, API keys, TTS assets, workspace instructions.

> **[VPS] Migration in Docker:** Run `hermes claw migrate` via `docker exec` inside the container, or use the web UI if it offers migration. Ensure both OpenClaw and Hermes containers are running during migration.

---

## Hermes vs OpenClaw

| Category | OpenClaw | Hermes |
|----------|----------|--------|
| Community | ✅ Larger | Growing fast |
| Self-Improving Loop | ❌ Limited | ✅ Core feature |
| Security | ⚠️ Had issues | ✅ Docker isolation |
| Speed | Slower | ✅ Faster |
| MCP Server Mode | ❌ | ✅ |
| Research Lab | ❌ Solo dev | ✅ Nous Research |

**Best answer:** Use both. They complement each other.

> **[VPS] Coexistence in Agent OS:** Both OpenClaw and Hermes run as separate containers on the same Docker network. They can communicate via the `root_default` bridge network. OpenClaw handles conversational AI and messaging; Hermes handles research, self-improving skills, and complex multi-step tasks. See `openclaw-agentos-ecosystem.md` for the full architecture.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Stuck/not responding | `Ctrl+C` → `hermes` (terminal) or `/new` (Telegram) |
| Telegram gateway broken | Use terminal Hermes to diagnose and fix |
| Context too large | `/compress` or `/new` (memory persists) |

> **[VPS] Docker-Specific Troubleshooting:**
> - **Container can't reach API:** Check network access and DNS. Verify API key environment variable.
> - **Web UI not accessible:** Check Traefik routing. Verify port 4860 is routed correctly.
> - **Memory/data lost on restart:** Ensure persistent volumes are mounted for Hermes data directory.
> - **Container OOM killed:** Hermes can be memory-intensive. Set appropriate memory limits in docker-compose.
> - **Gateway not starting:** Check container logs with `docker logs <container>`. Common issues: missing API key, port conflicts.

---

## Essential Commands

| Command | Purpose |
|---------|---------|
| `hermes` | Start chatting |
| `hermes setup` | Setup wizard |
| `hermes model` | Switch model |
| `hermes doctor` | Diagnose issues |
| `hermes gateway setup` | Set up messaging |
| `hermes gateway start` | Start gateway |
| `hermes skills install [name]` | Install skill |
| `hermes profile create [name]` | Create profile |
| `hermes claw migrate` | Migrate from OpenClaw |
| `/new` or `/reset` | Fresh conversation |
| `/compress` | Compress context |
| `/usage` | Check token usage |

> **[VPS] Docker CLI Access:** To run Hermes CLI commands in Docker:
> ```bash
> docker exec -it hermes-agent-7llb-hermes-agent-1 hermes [command]
> ```

---

## The 3-Step Automation Blueprint

1. **Where do you spend your time?** Identify the repetitive task.
2. **What's one thing you can automate this week?** Pick one.
3. **Ask Hermes how to automate it.** Then define trigger, give data sources, test once, schedule it.

---

> **Remember:** Hermes Agent is powerful but still maturing (v0.6). It gets better every day. Start simple, give feedback, and let the compounding effect work for you.
