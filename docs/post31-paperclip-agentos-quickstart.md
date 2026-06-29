# Skool Post #31: Paperclip + Agent OS — Quickstart

> **Source:** [8th June: Paperclip + Agent OS](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=e86f28fa6cc049778a8b73daac40b75c)
> **Date:** 2026-06-08
> **Topic:** Install Paperclip and connect it to your Agent OS to run an AI company

---

## TL;DR

**Paperclip** is open-source orchestration for teams of AI agents. If OpenClaw/Hermes is an employee, Paperclip is the company. This post shows you how to install Paperclip, connect it to your Agent OS, and hire your first AI agent to run autonomously.

---

## The Core Idea

> Bring your own agents, assign goals, and track work and costs from one dashboard. It looks like a task manager. Under the hood: org charts, budgets, governance, goal alignment, and agent coordination.

Paperclip + Agent OS = a full AI company running on your machine. You define the goal, hire the team, set budgets, and hit go.

---

## How It Works

| Step | What Happens |
|------|-------------|
| **1. Define the goal** | "Build the #1 AI note-taking app to $1M MRR." |
| **2. Hire the team** | CEO, CTO, engineers, designers, marketers — any bot, any provider |
| **3. Approve and run** | Review strategy. Set budgets. Hit go. Monitor from the dashboard |

---

## Two Ways to Install

### 🟢 The Easy Way — Let Claude Code or Hermes Do It

You don't touch the terminal. You hand the whole job to an AI agent and it sets everything up.

1. **Open Claude Code** (or Hermes) in a folder where you want this to live
2. **Drop your Agent OS pack** (the zip from the Boardroom) into that folder
3. **Paste this prompt and let it run:**

```
Set everything up for me, step by step, and show me each step as you go.

1. Install Paperclip from https://github.com/paperclipai/paperclip — or just run "npx paperclipai onboard --yes". It should run on http://localhost:3100.
2. Install my Agent OS from the pack in this folder — run "npm install", then start it on http://localhost:3737.
3. Make sure Hermes is installed ("pip install hermes-agent"). Paperclip already has a built-in Hermes adapter (type: hermes_local).
4. In Paperclip, create a company called "My Company", then add one Hermes agent as the CEO. If Paperclip can't find the hermes command, run "which hermes" and put the full path in the agent's command field.
5. Test that the agent runs, assign it one simple task, and confirm it reports back.
6. Tell me which URLs to open, and confirm Paperclip is connected to my Agent OS.
```

4. **When done:** open http://localhost:3737 and click the Paperclip tab — your AI company is right there ✅

---

### 🔵 The Technical Way — Do It Yourself

Prefer to drive? Manual steps:

| Step | Command / Action | Result |
|------|-----------------|--------|
| 1 | `npm install && npm run dev` (in Agent OS folder) | Agent OS running at http://localhost:3737 |
| 2 | `npx paperclipai onboard --yes` (new terminal) | Paperclip running at http://localhost:3100 |
| 3 | `pip install hermes-agent` | Hermes agent installed |
| 4 | Paperclip UI → New company → Hire → pick Hermes Local → give role + budget → Save | Agent hired |
| 5 | If agent "can't be found": `which hermes` → paste path into agent's command field → re-test | Agent goes green |
| 6 | Agent OS → Paperclip tab → company shows up → assign a task | 🎉 Fully synced |

---

## Tips

- **Set a budget on every agent** so costs never run away
- **Start with one agent + one task**
- **Use a free local model to keep it at $0**
- If you get stuck, go back and forth with your agent — it may take a few tries before it's fully synced

---

## Where to Get the Agent OS Pack

- [Agent OS Download + Setup Guide](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=097eb41a59b74f06a6112351c07216fa)
- Scroll to the bottom of the page — the zip file is in the resources, along with a readme to install it
- Full guide: [github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip)

---

## Key Takeaway

> **Either way, you end up with a full AI company running inside your Agent OS. If you get stuck, go back and forth with your agent. It may take a few tries before it's fully synced and working — but this is exactly how I did it.**

---

## No GHL/GoStackBase Content

This post does not contain GoHighLevel (GHL) references. No conversion needed.
