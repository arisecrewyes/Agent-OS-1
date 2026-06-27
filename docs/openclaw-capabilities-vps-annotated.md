# OpenClaw — Complete Capability Reference (VPS-Annotated Version)

> Source: Julian Goldie SEO — Skool Post #3: "OpenClaw: FULL 6 Hour Course"
> Original Video: https://www.youtube.com/watch?v=hRwjoU4RlMY
> Date: 2026-06-27
> Purpose: Capability reference with annotations for VPS/Docker deployment
>
> 📝 **Note:** This version includes deployment-specific annotations marked with `[VPS]` tags. For the general reference without annotations, see `openclaw-capabilities-general.md`.

---

## What is OpenClaw?

OpenClaw is an open-source AI assistant that runs 24/7 on your computer and connects to your messaging apps (WhatsApp, Telegram, Discord, Slack). Unlike traditional AI chatbots, OpenClaw can actually **do things** — control your browser, manage files, publish content, and automate workflows.

### Key Differences from Regular AI

- **Lives in your messaging apps** (not a website you visit)
- **Remembers everything** across conversations
- **Takes actions** on your computer
- **Works 24/7** if you want it to
- **Self-hosted** (you control your data)

---

## Installation

### Requirements
- Node.js version 22 or higher
- A computer (Mac/Windows/Linux) or VPS
- API key for your chosen AI provider

### Quick Install
```bash
npm install -g claudebot@latest
claudebot onboard-install-daemon
claudebot doctor
```

> **[VPS] Docker Deployment Note:** In a Docker/VPS environment, OpenClaw runs inside a container. The `claudebot onboard-install-daemon` step is typically handled by the container's entrypoint or Dockerfile. See the Agent OS compose files for the current Docker setup. The gateway runs as a persistent service inside the container, not as a system daemon.

### Setup Wizard Steps
1. Choose your AI provider (Claude Opus, ChatGPT CodeX, or Ollama)
2. Enter your API key
3. Select messaging channels (Telegram, WhatsApp, Discord, etc.)
4. Install skills (optional plugins)

> **[VPS] API Key Management:** In the Agent OS Docker setup, API keys are passed via environment variables in the `.env` file and injected into the container. Never hardcode API keys in Dockerfiles or compose files. Use the `.env.example` template as your starting point.

---

## AI Provider Selection

### Ranked Options

| Provider | Intelligence | Cost | Best For |
|----------|-------------|------|----------|
| Claude Opus 4.5 | ⭐⭐⭐⭐⭐ | $$$ | Complex orchestration, browser control |
| ChatGPT CodeX CLI | ⭐⭐⭐⭐ | $$ | Daily driver, best value |
| Kimmy K2.5 | ⭐⭐⭐⭐ | $ | Sub-agents, routine work |
| Ollama (Local) | ⭐⭐⭐ | Free | Simple tasks, high volume |

### Recommended Hybrid Setup
- **Main agent:** ChatGPT CodeX CLI or Claude Opus
- **Sub-agents:** Kimmy K2.5 or Ollama for smaller tasks
- This saves money while maintaining quality

> **[VPS] Current Agent OS Setup:** The Agent OS project currently uses OpenRouter as the primary API provider, with the model set to `openrouter/owl-alpha`. OpenRouter provides access to multiple models (Claude, GPT, Gemini, etc.) with automatic fallback. The API key is configured in the `agent-connector/docker-compose.yml` and `agentos/.env` files. See `openclaw-agentos-ecosystem.md` for how OpenClaw fits into the broader Agent OS architecture.

> **[VPS] Ollama on VPS:** Running Ollama locally inside a VPS container is possible but requires significant RAM (8GB+ for usable models). On a VPS with limited resources, it's more practical to use OpenRouter's cheaper models (like Google Gemini Flash or dedicated budget models) as your "cheap" tier rather than running Ollama locally.

---

## Messaging App Integration

### Telegram (Recommended)
1. Open Telegram → search for @BotFather
2. Create new bot with `/newbot`
3. Get your bot token
4. Enter token in OpenClaw setup
5. Start chatting

> **[VPS] Telegram in Docker:** The Telegram bot connection works the same way in Docker as it does locally. The bot token is passed via environment variable. The gateway inside the container maintains the Telegram connection. No special Docker configuration needed.

### WhatsApp
- Scan QR code during setup
- ⚠️ Caution: may flag bot accounts as spam

> **[VPS] WhatsApp in Docker:** WhatsApp requires a QR code scan which is problematic in headless Docker environments. For VPS setups, **Telegram is strongly recommended** as it only requires a bot token (no QR scan).

### Discord / Slack
- Follow OAuth flow during setup
- Grant necessary permissions

---

## Skills (Plugins)

### Installing
```bash
claudebot skills install <skill-name>
```

> **[VPS] Skills in Docker:** Skills are stored inside the container. If the container is rebuilt, skills may need to be reinstalled. For persistent skill storage, mount a volume for the skills directory or rebuild with a Dockerfile that includes `RUN` commands for each skill.

### Recommended Skills

| Skill | Purpose |
|-------|---------|
| WordPress | Publish blog posts directly |
| Browser Control | Automate web tasks |
| Notion | Create and update notes |
| Email | Manage inbox (use carefully) |
| Bird | Post to Twitter/X |
| Remotion | Create videos |
| Netlify | Deploy websites |

> **[VPS] WordPress Skill in Docker:** The WordPress skill works from a VPS container as long as the container can reach your WordPress site via HTTP/HTTPS. You'll need to create a WordPress Application Password (not your admin password) and provide it to OpenClaw. This works the same in Docker as locally.

---

## Security Best Practices

### ⚠️ 5 Critical Rules

1. **Don't Use VPS Without Proper Security** — People actively scan for exposed instances. Use Cloudflare Workers for sandboxed setup.
2. **Don't Connect Personal Email** — Risk of prompt injection. Create a separate account for OpenClaw only.
3. **Protect Your API Keys** — Never share screenshots with keys visible. Store in environment variables.
4. **Start Small** — Begin with test accounts. Don't give full system access immediately.
5. **Set Spending Limits** — All AI APIs have spending limits. Set them. Monitor usage regularly.

> **[VPS] Agent OS Security Implementation:**
> - OpenClaw containers are on the `root_default` Docker bridge network (internal only)
> - Traefik reverse proxy handles SSL termination and routes external traffic
> - OpenClaw's internal port (51461) is NOT exposed directly — only through Traefik if configured
> - API keys stored in `.env` files (not in Dockerfiles or compose files)
> - Spending limits should be set on your OpenRouter/Anthropic/OpenAI dashboard
> - The `root_default` network isolates containers from each other and the host

> **[VPS] Additional Docker-Specific Security:**
> - Use `read-only` root filesystem where possible
> - Run containers as non-root user
> - Limit container memory and CPU
> - Use Docker secrets for sensitive data (or at minimum, `.env` files excluded from git)
> - Regularly update base images
> - Monitor container logs for unusual activity

---

## Practical Use Cases

### 1. SEO Content Creation
```
Create an SEO-optimized blog post about [topic],
include keyword [keyword] 5-7 times naturally,
add internal links to [your site],
and publish to WordPress
```
**Result:** Ranked on Google's first page within 12 hours (proven case study).

> **[VPS] From Docker:** This works from the container as long as WordPress is reachable and credentials are configured. The content is generated inside the container and pushed to WordPress via API.

### 2. YouTube Research & Monitoring
```
Monitor these competitor YouTube channels: [URLs].
Alert me when they publish a video that performs 2x better
than their average. Check every 60 minutes.
```

### 3. AI Avatar Videos
```
Create an AI avatar video about [topic] using HeyGen
```

### 4. Thumbnail Generation
```
Create a YouTube thumbnail about [topic]
```

### 5. Voice Notes
```
Create a voice note in my voice about [topic]
```

### 6. Landing Page Creation
```
Create a landing page for [business],
make it conversion-optimized,
deploy to Netlify at [domain]
```

### 7. Notion Management
```
Create a Notion page about [topic] with step-by-step instructions
```

### 8. Browser Automation
```
Using Chrome extension, go to Google and search for [query]
```

> **[VPS] Browser Automation in Docker:** The Chrome extension (Browser Relay) requires a browser on the host or a Chrome instance accessible from the container. In a pure VPS environment, this requires running headless Chrome in a separate container and connecting it to OpenClaw. The Agent OS project includes a `browser-use-webui` container (currently stopped) that could serve this purpose.

---

## Advanced Features

### Cron Jobs (Scheduled Tasks)
```
Every Monday at 8am, analyze my YouTube performance from last week
and send me a report
```

> **[VPS] Cron in Docker:** OpenClaw's cron system works inside the container. Jobs persist as long as the container is running. For persistence across container restarts, store cron job definitions in a mounted volume or recreate them via the entrypoint script.

### Sub-Agents
```
Create a sub-agent to handle WordPress publishing
while you focus on content creation
```

### Memory & Context
OpenClaw remembers everything: preferences, business details, past conversations, workflows.

> **[VPS] Memory in Docker:** OpenClaw's memory is stored in its internal state. In Docker, this is ephemeral unless you mount a volume for the OpenClaw data directory. For persistent memory across container restarts, ensure the OpenClaw data directory is on a persistent volume.

### Real-Time Voice Agent
```
Create a voice agent app that I can talk to in real-time
using OpenAI's real-time API
```

---

## Workflow Examples

### Complete SEO Workflow (~5 minutes active work)
1. Research keyword → 2. Generate outline → 3. Write 1500-word post → 4. Optimize for SEO → 5. Add internal links → 6. Publish to WordPress → 7. Create social posts → 8. Share on Twitter/X

### Content Creation Pipeline
- Drop files (PDFs, notes, transcripts) in a folder
- OpenClaw scans daily, groups by topic
- Sends top 3 content ideas each morning
- You pick one → OpenClaw creates it

> **[VPS] File Watching in Docker:** For folder-watching workflows, the folder must be mounted into the container. Use Docker volumes to mount host directories into the OpenClaw container.

### Lead Management System
- Scans inbox every 30 minutes
- Extracts: name, company, need, timeline, budget
- Adds to Google Sheet
- Drafts personalized response
- Sends Telegram summary for your approval

---

## Cost Optimization

### Hybrid Approach (Recommended)
| Role | Provider | Cost |
|------|----------|------|
| Main orchestrator | ChatGPT CodeX CLI | ~$20/month |
| Sub-agents | Kimmy K2.5 or Ollama | Cheap/Free |
| Simple tasks | Ollama (local) | Free |

> **[VPS] Current Cost Setup:** The Agent OS project uses OpenRouter which aggregates many models at competitive prices. OpenRouter's pricing is per-token and generally cheaper than direct Anthropic/OpenAI pricing. The `owl-alpha` model used in the current setup is a high-capability model on OpenRouter.

### Token Saving Tips
- Use streaming responses when possible
- Clear context for simple queries
- Use specific skills instead of general LLM calls
- Set up local models for routine tasks

---

## Comparisons

### OpenClaw vs ChatGPT
ChatGPT: Browser-only, no memory between sessions, no actions.
OpenClaw: Lives in your apps, remembers everything, takes actions.

### OpenClaw vs Make.com/Zapier
Make/Zapier: Pre-built workflows, visual interface, limited flexibility.
OpenClaw: Natural language control, infinite flexibility, coding ability.

### OpenClaw vs N8N
N8N: Node-based workflow builder, requires setup per workflow.
OpenClaw: Describe what you want in plain English, it figures out the workflow.

> **[VPS] OpenClaw + N8N Combo:** These tools complement each other. N8N excels at structured, repeatable workflows with clear inputs/outputs. OpenClaw excels at ad-hoc tasks, creative work, and situations where you don't know the exact workflow in advance. In the Agent OS project, N8N handles structured automation workflows while OpenClaw handles conversational AI and ad-hoc tasks. They run as separate containers on the same Docker network.

### OpenClaw vs Claude Desktop/MCP
MCP: Access tools from Claude interface.
OpenClaw: AI comes to you in messaging apps, 24/7 operation.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Wrong language | Add "Respond only in English" to system instructions |
| AWS install fails | Install locally first; use Mac Mini or secured VPS for 24/7 |
| Chrome extension broken | `mbot browser extension install` → Developer Mode → Load unpacked |
| API costs too high | Switch to cheaper models, use Ollama, set spending limits |
| Skills won't install | Check Node.js 22+, restart gateway, install manually from ClawHub |

> **[VPS] Docker-Specific Troubleshooting:**
> - **Container can't reach API:** Check that the container has network access and DNS resolution works. Verify the API key environment variable is set correctly.
> - **Gateway not starting:** Check container logs with `docker logs <container>`. Common issues: missing API key, Node.js version mismatch, port conflicts.
> - **Telegram not connecting:** Verify the bot token is correct. Check that the container can reach Telegram's servers (api.telegram.org). Some VPS providers may block or rate-limit Telegram API access.
> - **Memory/data lost on restart:** Ensure persistent volumes are mounted for OpenClaw's data directory.
> - **Container OOM killed:** OpenClaw can be memory-intensive. Set appropriate memory limits in docker-compose and monitor usage.

---

## When NOT to Use OpenClaw

❌ Skip if: enterprise security compliance needed, zero technical setup required, uncomfortable with CLI, need guaranteed SLA, handling extremely sensitive data.

✅ Use if: want a personal AI assistant that does things, comfortable with some technical setup, want to automate tasks, content creator/founder/builder, want control over your data.

---

## Resources

- Official Docs: https://docs.openclaw.ai
- Community Discord: 8,000+ active users
- GitHub: 140,000+ stars
- Skill Marketplace: ClawHub

---

## Final Recommendations

**Best Setup for Most People:**
1. Install locally on Mac Mini or personal computer
2. Use ChatGPT CodeX CLI as main AI
3. Connect to Telegram (easiest)
4. Start with 3-5 essential skills
5. Don't connect email initially
6. Test with non-critical tasks first
7. Expand as you learn

> **[VPS] Agent OS VPS Recommendations:**
> - Use Docker Compose for deployment (see `version2/` directory)
> - Use Traefik for SSL termination
> - Use OpenRouter for API access (aggregates multiple providers)
> - Use Telegram as the primary messaging channel (most reliable in Docker)
> - Mount persistent volumes for OpenClaw data and memory
> - Set up monitoring for container health and API usage
> - See `openclaw-agentos-ecosystem.md` for how OpenClaw integrates with the full Agent OS stack

**Security Checklist:**
- ✅ Running locally or on properly secured VPS
- ✅ API keys in environment variables
- ✅ Spending limits set
- ✅ Test accounts for initial setup
- ✅ No personal email connected
- ✅ Separate WordPress account for OpenClaw
- ✅ Browser extension properly sandboxed

---

> **Remember:** OpenClaw is powerful but experimental. Don't do anything you're not comfortable with. Start small, test thoroughly, and scale gradually. The goal is to automate the boring stuff so you can focus on what matters.
