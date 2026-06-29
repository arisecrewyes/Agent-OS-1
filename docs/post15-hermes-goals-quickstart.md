# QuickStart: Hermes /goal — Autonomous AI Agent Goals

> Converted from Julian Goldie Skool Post #15 — "2nd May: Hermes Goals"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=86ee7476378d493f85e1bc35bd999ddd

---

## What You're Building

The **Hermes /goal system** — a persistent AI goal engine that:
1. Takes ONE command from you
2. Works autonomously through multiple steps
3. Self-evaluates progress (built-in judge AI)
4. Stops only when the goal is achieved (or runs out of turns)

No babysitting. No "keep going" every 30 minutes. Set it and walk away.

---

## Core Concept: /goal

Think of it like setting a destination in Google Maps:

| Action | What Happens |
|--------|-------------|
| `/goal [your task]` | Starts a new goal — Hermes begins immediately |
| `/goal status` | Check progress — see turns used and current state |
| `/goal pause` | Pause without losing progress |
| `/goal resume` | Pick up where it left off (resets turn counter) |
| `/goal clear` | Cancel the goal entirely |

---

## Under the Hood: How It Works

1. **You set the goal** → `/goal [your task]`
2. **Hermes works** → writes code, searches web, creates files
3. **The Judge checks** → separate AI evaluates: "Is the goal complete?"
4. **Loop or Stop** → NO = keep going automatically / YES = ✅ Goal achieved
5. **Safety net** → 20-turn budget prevents runaway costs

---

## Quick Setup

### Step 1: Install Hermes Agent
```bash
# On Mac or PC (Linux/WSL2)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Reload shell
source ~/.bashrc

# Launch Hermes
hermes
```

### Step 2: Configure the Judge Model (Optional — Saves Costs)
```yaml
# In config.yaml:
auxiliary:
  goal_judge:
    provider: openrouter
    model: google/gemini-3-flash-preview
```

### Step 3: Adjust Turn Budget (Optional)
```yaml
# In config.yaml:
goals:
  max_turns: 20
```

### Step 4: Run Your First Goal
```
/goal Write 3 short blog post outlines about AI automation
```

---

## Goal Writing Rules

| Bad Goal | Good Goal |
|----------|-----------|
| `/goal write some blog posts` | `/goal Write 3 SEO blog posts about AI automation, each 1000 words, targeting keywords "AI agent tools 2026", "best AI automation software", and "how to automate with AI". Save each as a separate .md file.` |

**Rules for great goals:**
- Be specific about the OUTPUT (file, report, deployed site)
- Mention the FORMAT if it matters
- Include constraints (word count, keyword, style)
- The more detail, the better the judge can verify completion

---

## Real Example (From Docs)

**Command:** `/goal Create four files /tmp/note_1.txt through /tmp/note_4.txt, one per turn`

| Turn | Action | Judge Response |
|------|--------|---------------|
| 1 | Hermes creates note_1.txt | "3 files remaining, continue" |
| 2 | Hermes creates note_2.txt | "2 files remaining, continue" |
| 3 | Hermes creates note_3.txt | "1 file remaining, continue" |
| 4 | Hermes creates note_4.txt | "✅ All four files created — goal achieved" |

**Result:** 4 turns, 1 command, zero effort from you.

---

## Safety Features

- **Interrupt anytime** — just type any message, Hermes prioritises you
- **20-turn budget** — won't run forever
- **Fail-open judging** — if judge crashes, Hermes continues (never stuck)
- **Mid-run controls** — pause or check status without disrupting current turn
- **One goal at a time** — must `/stop` before setting a new one
- **Persistent storage** — goals saved to SessionDB, survive restarts

---

## When to Use /goal

### ✅ USE /goal when:
- Task takes multiple steps
- You'd normally say "keep going" more than twice
- You want to set it and walk away
- Task involves building, writing, researching, or fixing

### ❌ SKIP /goal when:
- One-shot question ("What's the capital of France?")
- Single simple task ("Rename this file")
- You need to review each step before next one happens

---

## 30-Day Implementation Plan

### Week 1: Foundation

| Day | Task |
|-----|------|
| 1 | Install Hermes, spend 30 min exploring |
| 2 | Run first `/goal` — simple task (3 blog post outlines) |
| 3 | Research goal: top 5 AI agent tools comparison |
| 4 | Experiment with `/goal pause` and `/goal resume` |
| 5 | Content goal relevant to YOUR business |
| 6 | Review outputs — note what worked |
| 7 | Rest |
