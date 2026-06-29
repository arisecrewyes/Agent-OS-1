---
tags:
  - paperclip
  - agent-os
  - skool
  - orchestration
  - ai-agents
  - hermes
  - claude
  - automation
  - company-management
source: "Skool Post #31 — AI Profit Boardroom"
author: Julian
date: 2026-06-08
converted: 2026-06-29
platform: paperclip
---

# Paperclip + Agent OS

> [!info] Metadata
> - **Source:** [Skool Post #31](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=e86f28fa6cc049778a8b73daac40b75c)
> - **Author:** Julian (AI Profit Boardroom)
> - **Date:** 8th June (original post)
> - **Topics:** Paperclip, Agent OS, AI Agent Orchestration, Company Management, Budgets, Hermes Agent
> - **Related:** [[Agent-OS]], [[Hermes-Agent]], [[Claude-Code]], [[OpenClaw]]

---

## Overview

**Paperclip** is open-source orchestration for teams of AI agents. If OpenClaw (or Hermes) is an employee, Paperclip is the company.

Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Bring your own agents, assign goals, and track work and costs from one dashboard.

> "It looks like a task manager. Under the hood: org charts, budgets, governance, goal alignment, and agent coordination."

**Manage business goals, not pull requests.**

---

## Why Paperclip Exists

### The Problem It Solves

| Without Paperclip | With Paperclip |
|-------------------|----------------|
| ❌ 20 Claude Code tabs open — can't track which does what. On reboot you lose everything | ✅ Tasks are ticket-based, conversations threaded, sessions persist across reboots |
| ❌ Manually gather context from several places to remind your bot what you're doing | ✅ Context flows from task → project → company goals — agent always knows what to do and why |
| ❌ Folders of disorganized agent configs — re-inventing task management and coordination | ✅ Paperclip gives you org charts, ticketing, delegation, and governance out of the box |
| ❌ Runaway loops waste hundreds of dollars before you know what happened | ✅ Cost tracking surfaces token budgets and throttles agents when they're out |
| ❌ Recurring jobs require manually kicking them off | ✅ Heartbeats handle regular work on a schedule |
| ❌ Fire up Claude Code, keep a tab open, babysit it | ✅ Add a task in Paperclip — agent works until done, management reviews |

### Who It's For

- ✅ You want to build autonomous AI companies
- ✅ You coordinate many different agents (OpenClaw, Codex, Claude, Cursor) toward a common goal
- ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing
- ✅ You want agents running autonomously 24/7, but still want to audit work and chime in
- ✅ You want to monitor costs and enforce budgets
- ✅ You want a process for managing agents that feels like using a task manager
- ✅ You want to manage your autonomous businesses from your phone

---

## How It Works

| Step | What Happens |
|------|-------------|
| **1. Define the goal** | "Build the #1 AI note-taking app to $1M MRR." |
| **2. Hire the team** | CEO, CTO, engineers, designers, marketers — any bot, any provider |
| **3. Approve and run** | Review strategy. Set budgets. Hit go. Monitor from the dashboard |

> "If it can receive a heartbeat, it's hired."

---

## Installation — Two Paths

### 🟢 The Easy Way — Let Claude Code or Hermes Do It

You don't touch the terminal. Hand the job to an AI agent and it sets everything up.

**Steps:**

1. Open Claude Code (or Hermes) in a folder where you want this to live
2. Drop your Agent OS pack (the zip from the Boardroom) into that folder
3. Paste this prompt:

```
Set everything up for me, step by step, and show me each step as you go.

1. Install Paperclip from https://github.com/paperclipai/paperclip — or just run "npx paperclipai onboard --yes". It should run on http://localhost:3100.
2. Install my Agent OS from the pack in this folder — run "npm install", then start it on http://localhost:3737.
3. Make sure Hermes is installed ("pip install hermes-agent"). Paperclip already has a built-in Hermes adapter (type: hermes_local).
4. In Paperclip, create a company called "My Company", then add one Hermes agent as the CEO. If Paperclip can't find the hermes command, run "which hermes" and put the full path in the agent's command field.
5. Test that the agent runs, assign it one simple task, and confirm it reports back.
6. Tell me which URLs to open, and confirm Paperclip is connected to my Agent OS.
```

4. When done: open http://localhost:3737 → click the Paperclip tab → your AI company is there ✅

### 🔵 The Technical Way — Do It Yourself

You'll need: Node 20+, a terminal, your Agent OS pack, and one agent (Hermes, Claude, etc.).

| Step | Command / Action | Result |
|------|-----------------|--------|
| 1 | `npm install && npm run dev` (in Agent OS folder) | Agent OS at http://localhost:3737 |
| 2 | `npx paperclipai onboard --yes` (new terminal) | Paperclip at http://localhost:3100 |
| 3 | `pip install hermes-agent` | Hermes installed |
| 4 | Paperclip UI → New company → Hire → pick Hermes Local → role + budget → Save | Agent hired |
| 5 | `which hermes` → paste path into agent's command field → re-test | Agent goes green |
| 6 | Agent OS → Paperclip tab → company appears → assign task | 🎉 Fully synced |

---

## Core Features

### Any Agent, Any Runtime

Every task traces back to the company mission. Agents know what to do and why. Agents wake on a schedule, check work, and act. Delegation flows up and down the org chart.

### Budget Enforcement

Monthly budgets per agent. When they hit the limit, they stop. **No runaway costs.**

### Multi-Company Isolation

One deployment, many companies. Complete data isolation. One control plane for your portfolio.

### Full Audit Trail

Every conversation traced. Every decision explained. Full tool-call tracing and immutable audit log.

### Governance

Approve hires, override strategy, pause or terminate any agent — at any time.

### Org Charts

Hierarchies, roles, reporting lines. Your agents have a boss, a title, and a job description.

### Mobile Management

Monitor and manage your autonomous businesses from anywhere.

---

## Key Technical Details

- **Atomic execution:** Task checkout and budget enforcement are atomic — no double-work, no runaway spend
- **Persistent agent state:** Agents resume the same task context across heartbeats instead of restarting from scratch
- **Runtime skill injection:** Agents can learn Paperclip workflows and project context at runtime

---

## Tips

- **Set a budget on every agent** so costs never run away
- **Start with one agent + one task**
- **Use a free local model to keep it at $0**
- If you get stuck, go back and forth with your agent — it may take a few tries before it's fully synced

---

## Where to Get It

- **Paperclip GitHub:** [github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip)
- **Paperclip Docs:** [paperclip.ing/docs](https://paperclip.ing/docs)
- **Agent OS Download + Setup Guide:** [Skool Resource](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=097eb41a59b74f06a6112351c07216fa)
- Scroll to the bottom of the page — the zip file is in the resources, along with a readme to install it

---

## Key Takeaways

- ✅ **Paperclip is the company, OpenClaw/Hermes are the employees** — orchestration layer on top of agents
- ✅ **Two install paths** — easy (let Claude Code do it) or manual (terminal commands provided)
- ✅ **Budget enforcement** — monthly caps per agent, no runaway costs
- ✅ **Any agent, any runtime** — Hermes, OpenClaw, Codex, Claude, Cursor all work
- ✅ **One deployment, many companies** — complete data isolation
- ✅ **Full audit trail** — every conversation traced, every decision explained
- ✅ **Start simple** — one agent, one task, free local model

> "Either way, you end up with a full AI company running inside your Agent OS. If you get stuck, go back and forth with your agent. It may take a few tries before it's fully synced and working — but this is exactly how I did it."

---

## Linked Concepts

- [[Agent-OS]] — The agent operating system that Paperclip orchestrates
- [[Hermes-Agent]] — One of the agent types compatible with Paperclip
- [[Claude-Code]] — Can be used for the easy install method
- [[OpenClaw]] — Another agent that fits into the Paperclip model
- [[OpenHue]] — Smart home control from agents
- [[AI-Orchestration]] — Broader category of multi-agent coordination

---

## References

- [Paperclip GitHub](https://github.com/paperclipai/paperclip)
- [Paperclip Docs](https://paperclip.ing/docs)
- [Agent OS Download + Setup Guide](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=097eb41a59b74f06a6112351c07216fa)
- [Paperclip Discord](https://discord.gg/m4HZY7xNG3)
- [Paperclip Website](https://paperclip.ing)
