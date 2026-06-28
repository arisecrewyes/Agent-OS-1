# OpenClaw — Advanced Features

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## Schedule Tasks (Cron Jobs)

Set up recurring automations that run on a schedule:

**Prompt Example:**
```
Every Monday at 8am,
analyze my YouTube performance from last week
and send me a report
```

OpenClaw will run this automatically every week without any intervention.

### Common Cron Use Cases
- Daily content reports
- Weekly analytics summaries
- Monthly SEO audits
- Regular competitor monitoring
- Scheduled social media posts
- Periodic backup checks

---

## Sub-Agents

OpenClaw can spawn multiple agents to work in parallel on different tasks:

**Prompt Example:**
```
Create a sub-agent to handle WordPress publishing
while you focus on content creation
```

### How Sub-Agents Work

1. **Main agent (orchestrator)** plans the work and assigns tasks
2. **Sub-agents** execute individual tasks in parallel
3. Results are reported back to the orchestrator
4. Orchestrator combines results and reports to you

### Sub-Agent Strategy (from the video演示)

Use different models for different agent types:
- **Orchestrator:** Claude Opus or ChatGPT CodeX (needs intelligence)
- **Sub-agents:** Cheaper models like Kimmy K2.5 or Ollama (just need to follow instructions)

This saves significant costs while maintaining quality.

---

## Memory & Context

OpenClaw remembers everything you tell it:

- **Your preferences** — how you like things formatted, your tone, your style
- **Your business details** — company info, links, team members
- **Past conversations** — full conversation history
- **Your workflows** — recurring processes you've set up

This means every interaction gets smarter over time. The more you use it, the more personalized and efficient it becomes.

### Memory Tip
Tell OpenClaw important context once, and it remembers:
- "My website is [URL]"
- "My brand voice is [description]"
- "Always link to [internal page] when writing about [topic]"

---

## Real-Time Voice Agent

Create a voice interface for real-time conversation:

**Prompt Example:**
```
Create a voice agent app that I can talk to in real-time
using OpenAI's real-time API
```

This creates a hands-free voice assistant you can speak to directly.

---

## Browser Control + Local Apps

OpenClaw can control more than just your browser:

- **Google Anti-Gravity** — AI coding environment that OpenClaw can operate via Telegram
- **Chrome Extension (Browser Relay)** — Full browser automation
- **Local applications** — OpenClaw can open and interact with apps on your computer
- **Terminal/command line** — Execute commands directly on the host machine

### Anti-Gravity Integration Demo
1. OpenClaw connects to Anti-Gravity
2. Edits HTML/CSS files directly in the editor
3. Can create websites, modify code, run terminal commands
4. All controlled via Telegram chat — no coding knowledge needed

---

## Content Pipeline (Automated)

**Prompt Example:**
```
Watch this folder: /content/drop
When new files appear (PDFs, notes, transcripts),
scan them and group by topic.
Each morning, send me the top 3 content ideas
with titles and hooks based on the scanned content.
```

**Result:** Fully automated content research pipeline — drop files, get ideas daily.

---

## Lead Management System

**Prompt Example:**
```
Scan my inbox every 30 minutes for new leads.
Extract: name, company, need, timeline, budget.
Add to Google Sheet.
Draft a personalized response.
Send me a Telegram message with lead details.
I'll approve the response, and it sends.
```

---

## Metadata

- Tags: `openclaw`, `advanced`, `cron`, `sub-agents`, `memory`, `voice`
- Related: [[08 - Workflow Examples]] | [[09 - Cost Optimization]]
