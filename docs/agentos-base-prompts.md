# Agent OS Base — AI Prompt Library

> Ready-to-use prompts for building and using Agent OS.
> Source: Julian Goldie SEO — Skool Post #1
> Related: [[agentos-base-capabilities-general]] | [[agentos-base-quickstart]]

---

## Build Prompts (Paste into Claude Code)

### Prompt 1: Create the Dashboard
```
Create a beautiful, dopamine-inducing operating system, hosted locally, for
managing Claude through a website connected to my Claude. Make it a mission
control dashboard that also lets me control my other AI agents (OpenClaw,
Hermes, etc.) in separate sections. Use the Claude Code CLI bridge.
Stack: Next.js + Tailwind + Framer Motion. Make it gorgeous.
```

### Prompt 2: Make it Beautiful + Per-Agent Pages
```
Make it more modern and clean. Add a sidebar with a separate clickable page
for each AI agent, real chat-app feel, and avatars/logos per agent.
```

### Prompt 3: Voice Input
```
Add a mic button to every chat box. Click to talk and have speech turn into
text using the browser's built-in voice recognition. No API keys.
```

### Prompt 4: Save Everything to Obsidian
```
My Obsidian vault is at [YOUR_VAULT_PATH]. Auto-save
every chat, goal, and journal entry into an "Agentic OS" folder there, as
markdown, one file per day.
```

### Prompt 5: Goals + Journal
```
Add a Goals page (checkbox tasks) and a Journal page (one file per day).
Both save to my Obsidian vault and support voice input.
```

### Optional Prompts
- **Prompt 6:** Fix bugs by describing them to Claude
- **Prompt 7:** Make it portable with a config file + setup wizard
- **Prompt 8:** Generate a shareable guide

---

## Setup Prompts

### First-Run Check
```
Check that all agents show LIVE or BUSY in the dashboard.
If DEGRADED: run openclaw doctor then openclaw gateway restart
If OFFLINE: run openclaw gateway restart, then openclaw doctor --fix
```

### Agent Connection Test
```
Open each agent in the dashboard and verify:
1. Claude tab → can send and receive messages
2. OpenClaw tab → shows agent status
3. Hermes tab → shows agent status
4. Voice input → mic button works in browser
```

### Obsidian Vault Connection
```
My Obsidian vault is at [YOUR_VAULT_PATH].
Connect Agent OS to my vault and verify:
1. Chats auto-save to vault
2. Goals save to vault
3. Journal saves to vault
4. Memory persists across sessions
```

---

## Usage Prompts

### General Agent Task
```
Draft a content plan from my goals for this week.
```

### Research Task
```
Research the latest trends in [niche] and give me
a summary with actionable insights.
```

### Social Media Task
```
Create a social media post about [topic] that aligns
with my brand voice and goals.
```

### Daily Briefing
```
Look at my Goals, Journal, and recent memory files.
Generate a daily briefing with:
1. Today's priorities
2. Open to-dos
3. Recent progress
4. Suggested focus areas
```

---

## Tips for Better Prompts

1. **Paste prompts one at a time** — let Claude complete each before moving on
2. **Describe errors clearly** — if something breaks, tell Claude exactly what you saw
3. **Be specific with paths** — use your actual Obsidian vault path
4. **Iterate** — each prompt builds on the previous one
5. **Don't write code** — Claude writes the code for you

---

## Related

- For implementation steps: `agentos-base-quickstart.md`
- For the timeline: `agentos-base-launch-plan.md`
- For technical build guide: `version2/DEPLOYMENT.md`
