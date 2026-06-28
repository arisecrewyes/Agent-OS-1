# Agent OS Base — QuickStart Guide

> Part of the [[00 - Index|Agent OS Base]] knowledge base.

## Option A: Use the Zip (Fastest)

1. Download ZIP from Skool Resources section
2. Extract and follow README
3. Run `Start Agent OS.command` (macOS)

## Option B: Build with Claude Code (Recommended)

### Prerequisites
- Claude Code (free at claude.ai/code)
- Node.js 22.16+ (or 24)
- Mac (easiest), Linux, or WSL2

### Step 1: Create the Dashboard
```
Create a beautiful, dopamine-inducing operating system, hosted locally, for
managing Claude through a website connected to my Claude. Make it a mission
control dashboard that also lets me control my other AI agents (OpenClaw,
Hermes, etc.) in separate sections. Use the Claude Code CLI bridge.
Stack: Next.js + Tailwind + Framer Motion. Make it gorgeous.
```

### Step 2: Per-Agent Pages
```
Make it more modern and clean. Add a sidebar with a separate clickable page
for each AI agent, real chat-app feel, and avatars/logos per agent.
```

### Step 3: Voice Input
```
Add a mic button to every chat box. Click to talk and have speech turn into
text using the browser's built-in voice recognition. No API keys.
```

### Step 4: Save to Obsidian
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

## Connecting Real Agents

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon

# Hermes: github.com/NousResearch/hermes-agent
# Obsidian: obsidian.md
```

## First-Run Check
- Dashboard → every agent should show **LIVE** or **BUSY**
- 🟡 DEGRADED → `openclaw doctor` then `openclaw gateway restart`
- 🔴 OFFLINE → `openclaw gateway restart`

## Related

- [[02 - Launch Plan]]
- [[03 - Prompt Library]]

---

## Metadata

- Tags: `agent-os`, `quickstart`, `build`
