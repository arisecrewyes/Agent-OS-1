# OpenClaw — Complete Capability Reference (General Version)

> Source: Julian Goldie SEO — Skool Post #3: "OpenClaw: FULL 6 Hour Course"
> Original Video: https://www.youtube.com/watch?v=hRwjoU4RlMY
> Date: 2026-06-27
> Purpose: Comprehensive capability reference for any OpenClaw user

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

### Setup Wizard Steps
1. Choose your AI provider (Claude Opus, ChatGPT CodeX, or Ollama)
2. Enter your API key
3. Select messaging channels (Telegram, WhatsApp, Discord, etc.)
4. Install skills (optional plugins)

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

---

## Messaging App Integration

### Telegram (Recommended)
1. Open Telegram → search for @BotFather
2. Create new bot with `/newbot`
3. Get your bot token
4. Enter token in OpenClaw setup
5. Start chatting

### WhatsApp
- Scan QR code during setup
- ⚠️ Caution: may flag bot accounts as spam

### Discord / Slack
- Follow OAuth flow during setup
- Grant necessary permissions

---

## Skills (Plugins)

### Installing
```bash
claudebot skills install <skill-name>
```

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

---

## Security Best Practices

### ⚠️ 5 Critical Rules

1. **Don't Use VPS Without Proper Security** — People actively scan for exposed instances. Use Cloudflare Workers for sandboxed setup.
2. **Don't Connect Personal Email** — Risk of prompt injection. Create a separate account for OpenClaw only.
3. **Protect Your API Keys** — Never share screenshots with keys visible. Store in environment variables.
4. **Start Small** — Begin with test accounts. Don't give full system access immediately.
5. **Set Spending Limits** — All AI APIs have spending limits. Set them. Monitor usage regularly.

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

---

## Advanced Features

### Cron Jobs (Scheduled Tasks)
```
Every Monday at 8am, analyze my YouTube performance from last week
and send me a report
```

### Sub-Agents
```
Create a sub-agent to handle WordPress publishing
while you focus on content creation
```

### Memory & Context
OpenClaw remembers everything: preferences, business details, past conversations, workflows.

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

**Security Checklist:**
- ✅ Running locally (not exposed VPS)
- ✅ API keys in environment variables
- ✅ Spending limits set
- ✅ Test accounts for initial setup
- ✅ No personal email connected
- ✅ Separate WordPress account for OpenClaw
- ✅ Browser extension properly sandboxed

---

> **Remember:** OpenClaw is powerful but experimental. Don't do anything you're not comfortable with. Start small, test thoroughly, and scale gradually. The goal is to automate the boring stuff so you can focus on what matters.
