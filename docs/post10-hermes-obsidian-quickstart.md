# QuickStart: Hermes + Obsidian — The Goldie Second Brain Stack

> Converted from Julian Goldie Skool Post #10 — "30th May: Hermes + Obsidian"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=990e985eb129463eac48e77b69752175
> Google Doc: https://docs.google.com/document/d/1i4AzstLHF7W3IhhE8uNtybEi4-uBCDbtL2epZNxnnus

---

## What You're Building

A **permanent memory system** for your AI agents using Obsidian vault + Agent OS.

The Goldie Second Brain Stack:
- 🧠 AI agents that **never forget** who you are
- 📓 One shared vault that **all agents** read from
- ✍️ AI that **writes its own notes** while you sleep
- 🔄 A system that **gets sharper every day**

**Cost:** $0 (all free tools)
**Time to build:** 30 days (progressive setup)
**Difficulty:** Beginner-friendly

---

## The 5 Layers of the Goldie Second Brain Stack

| Layer | What It Does | Tool |
|-------|-------------|------|
| 1. The Vault �️ | Stores all notes, goals, client info | Obsidian |
| 2. The Bridge � | Agent reads the vault | Agent OS |
| 3. Shared Brain 🧠 | All agents read the SAME vault | Obsidian + Agent OS |
| 4. Auto-Notes �️ | AI writes notes automatically | Hermes/Claude + Obsidian |
| 5. The Loop 🔄 | Every note makes the system smarter | All combined |

---

## Your 30-Day Plan

### Week 1: Foundation (Days 1-7)

| Day | Action | Prompt |
|-----|--------|--------|
| 1 | Download Obsidian → Create "My Second Brain" vault | — |
| 2 | Make "About Me" note | "Ask me 10 questions about my business, then write a clean summary" |
| 3 | Add goals | "Help me write my top 5 goals for the next 90 days" |
| 4 | Map ideal customer | "Create a profile of my ideal customer — who they are, what they want" |
| 5 | Connect agent to vault | "My notes are in this Obsidian folder. Use them for memory from now on." |
| 6 | Test memory | "Based on my notes, what do I do and who do I help?" |
| 7 | Reflect | Write one note about what surprised you |

### Week 2: Automate (Days 8-14)

| Day | Action | Prompt |
|-----|--------|--------|
| 8 | Enable auto-notes | AI automatically saves notes to vault |
| 9 | Build content engine | "Read my vault. Write me a week of short posts that sound like me." |
| 10 | Make dashboard | "Build a colorful single-page dashboard of goals, tasks, and notes." |
| 11 | Auto-summarize | "Read everything I added this week and give me a 5-bullet summary." |
| 12 | Train on voice | "Study how I write. Save a note describing my tone and style." |
| 13 | Build FAQ brain | "Based on my notes, write answers to the 10 questions customers ask most." |
| 14 | Review | "What did you learn about me this week?" |

### Week 3: Scale (Days 15-21)

| Day | Action | Prompt |
|-----|--------|--------|
| 15 | Connect second agent | Point a different AI tool at the SAME vault |
| 16 | Test handoff | One agent writes, another reads the next day |
| 17 | Research notes | Upload best content → "Pull out my key ideas and save them." |
| 18 | Idea generator | "Based on everything in my vault, give me 10 new content ideas." |
| 19 | Visual timeline | "Make a colorful timeline showing everything I built this month." |
| 20 | Audit edge | "Based on my notes, what makes my business different?" |
| 21 | Tidy vault | "Clean and color-code my vault." |

### Week 4: Systematise (Days 22-30)

| Day | Action | Prompt |
|-----|--------|--------|
| 22 | Daily start priority | "Every morning, read my vault and give me 3 priorities for today." |
| 23 | Weekly review | "Each week, summarize what I did and suggest one thing to improve." |
| 24 | Automation audit | "Based on my recent work, what could I automate to save time?" |
| 25 | Welcome guide | "Write a simple guide explaining my business to a new helper." |
| 26 | Make it pretty | "Turn my mission control into something visually stunning." |
| 27 | Full loop test | Run a real task end-to-end |
| 28 | Find gaps | "Look at my vault. What's missing that would make you smarter?" |
| 29 | Document system | "Write one note explaining my whole setup." |
| 30 | Look back | "Read my Day 7 reflection. See how far the brain has come." |

---

## Setup Commands (VPS + Agent OS)

### Step 1: Install Obsidian Vault
```bash
# On VPS, create vault directory
mkdir -p /root/obsidian-vault/My-Second-Brain
cd /root/obsidian-vault/My-Second-Brain
```

### Step 2: Connect Agent OS
Tell your agent:
```
My notes live in /root/obsidian-vault/My-Second-Brain.
Use this vault for memory and context from now on.
```

### Step 3: Configure Auto-Notes
- Hermes Agent: Set vault path in Memory Engine config
- OpenClaw: Vault is already connected at `/data/.openclaw/workspace/obsidian-vault/`
- Claude: Paste vault path into project instructions

---

## Example Prompts

### Brand Voice
```
Read my Obsidian vault. Based on my goals, my voice, and what I worked on this month, write me 5 short posts that sound exactly like me — not generic AI.
```

### Mission Control Dashboard
```
Build me a clean, colorful mission control dashboard that shows all my agent tasks, my goals, and my recent notes in one single view. Make it visual and easy to read at a glance.
```

### Vault Organizer
```
Read all my notes in Obsidian. Reorganize them, tag them, color code them, and link related ideas together so it becomes a clean second brain.
```

---

## VPS Configuration

```yaml
# docker-compose snippet for Obsidian + Agent OS
services:
  obsidian:
    image: ghcr.io/pxobsidian/obsidian-remote
    volumes:
      - ./obsidian-vault:/vaults
    ports:
      - "8080:8080"
```

---

## Agent OS Ecosystem Map

```
Obsidian Vault (notes)
    ├── OpenClaw Agent (reads/writes)
    ├── Hermes Agent (reads/writes)
    ├── Claude Code (reads/writes)
    ├── Memory Engine (indexes)
    └── All agents speak in ONE voice
```

---

## Related

- [[Agent-OS-Ecosystem|Ecosystem: Second Brain Stack]]
- [[Goldie-SEO-Framework|Goldie SEO Framework]]
- [[SOP - Infinite Memory Setup]]
- Full Google Doc: https://docs.google.com/document/d/1i4AzstLHF7W3IhhE8uNtybEi4-uBCDbtL2epZNxnnus/edit
