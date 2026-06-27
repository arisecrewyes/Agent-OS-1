# Agent OS Base — QuickStart Guide

> Step-by-step walkthrough to build the Agent OS Dashboard with Claude Code.
> Source: Julian Goldie SEO — Skool Post #1
> Related: [[agentos-base-capabilities-general]] | [[00 - Index]]

---

## Option A: Use the Zip (Fastest)

1. Download the ZIP from the Skool post Resources section
2. Extract and follow the README inside
3. Run `Start Agent OS.command` (macOS) or equivalent

## Option B: Build with Claude Code (Recommended)

### Prerequisites
- **Claude Code** — free at claude.ai/code (or Hermes, Codex, etc.)
- **Laptop** — Mac easiest, Linux works, Windows via WSL2
- **Node.js** 22.16+ (or 24)

### Step 1: Create the Dashboard

Paste this prompt into Claude Code:
```
Create a beautiful, dopamine-inducing operating system, hosted locally, for
managing Claude through a website connected to my Claude. Make it a mission
control dashboard that also lets me control my other AI agents (OpenClaw,
Hermes, etc.) in separate sections. Use the Claude Code CLI bridge.
Stack: Next.js + Tailwind + Framer Motion. Make it gorgeous.
```

Claude will:
- Ask ~3 questions
- Install tools
- Write files
- Start a server
- Give you `http://localhost:3000`

### Step 2: Make it Beautiful + Per-Agent Pages

```
Make it more modern and clean. Add a sidebar with a separate clickable page
for each AI agent, real chat-app feel, and avatars/logos per agent.
```

### Step 3: Add Voice Input

```
Add a mic button to every chat box. Click to talk and have speech turn into
text using the browser's built-in voice recognition. No API keys.
```

### Step 4: Save Everything to Obsidian

```
My Obsidian vault is at /Users/yourname/Documents/ObsidianVault. Auto-save
every chat, goal, and journal entry into an "Agentic OS" folder there, as
markdown, one file per day.
```

### Step 5: Goals + Journal

```
Add a Goals page (checkbox tasks) and a Journal page (one file per day).
Both save to my Obsidian vault and support voice input.
```

### Optional Prompts

- **Prompt 6:** Fix bugs by describing them to Claude
- **Prompt 7:** Make it portable with a config file + setup wizard
- **Prompt 8:** Generate a shareable guide

---

## Connecting Real Agents

```bash
# 1. Node.js 22.16+ (or 24) — from nodejs.org

# 2. OpenClaw (the agent gateway/router)
npm install -g openclaw@latest
openclaw onboard --install-daemon

# 3. Connect Claude — paste your Anthropic API key when the wizard asks

# Hermes — github.com/NousResearch/hermes-agent
# Install, connect to your OpenClaw gateway; it appears in Mission Control.

# Obsidian — obsidian.md — install, create a vault, point Agent OS at its path.
```

---

## First-Run Check

- Open dashboard → every agent should show **LIVE** or **BUSY** (also fine)
- 🟡 DEGRADED → `openclaw doctor` then `openclaw gateway restart`
- 🔴 OFFLINE → `openclaw gateway restart` (still stuck? `openclaw doctor --fix`)

---

## Then

Open an agent → give it a real task (e.g. "draft a content plan from my goals") → watch it work.

---

## Resources & Updates

- **ZIP file** — available in the Resources section of the Skool post (contains full Agent OS project + README)
- **UPDATE.md / UPDATE-WITH-AI.md** — included in the zip file for updating old versions
- **Last updated:** 27th June 2026 (check the Skool post for the latest version)

## Notes

- ZIP file available in Resources section of the Skool post
- If you have old version, use `UPDATE.md` or `UPDATE-WITH-AI.md` from the new zip
- **~60 minutes** to build with Claude Code
- Don't write code — paste prompts into Claude; Claude builds it
