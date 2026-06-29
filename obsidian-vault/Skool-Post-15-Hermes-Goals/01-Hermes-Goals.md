# Hermes /goal — Autonomous AI Agent Goals (Post #15)

> Converted from Julian Goldie Skool Post #15 — 2nd May
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=86ee7476378d493f85e1bc35bd999ddd

## The Core Problem

AI agents do one step, then stop. You say "continue" over and over. Exhausting.

## The Solution: /goal

> "The best AI isn't the one that waits for you to keep pushing it. It's the one that keeps going on its own."

The `/goal` feature gives Hermes a **standing objective** — a goal it keeps chasing no matter what. After every action, a "judge" AI checks if the goal is done. If NO → keeps working. If YES → stops.

## Key Insight

Think of `/goal` like setting a destination in Google Maps. You type where you want to go. The app figures out every turn. You just sit back.

## Commands Reference

| Command | Action |
|---------|--------|
| `/goal [your task]` | Start a new goal (Hermes begins immediately) |
| `/goal status` | Check progress (turns used, current status) |
| `/goal pause` | Pause without losing progress |
| `/goal resume` | Pick up where it left off (resets turn counter) |
| `/goal clear` | Cancel the goal entirely |

## How It Works (5 Steps)

1. **You Set The Goal** → `/goal [your task]` — Hermes starts on Turn 1
2. **Hermes Works** → writes code, searches web, creates files
3. **The Judge Checks** → separate AI asks: "Is the goal complete?"
4. **Loop Or Stop** → NO = continue automatically / YES = ✅ Goal achieved
5. **Budget Safety Net** → 20 turns default, then auto-pause

## The Judge Model

- Separate AI model watches every turn
- Only says "done" when result **explicitly confirms** goal completion
- Deliberately conservative — false positives are rare
- If it stops too soon → re-set with clearer description
- If it goes too long → 20-turn budget catches it

### Configuring the Judge (Cost Savings)

```yaml
# In config.yaml:
auxiliary:
  goal_judge:
    provider: openrouter
    model: google/gemini-3-flash-preview
```

## Goal Writing Framework

### Bad vs. Good

| ❌ Bad | ✅ Good |
|--------|--------|
| `/goal write some blog posts` | `/goal Write 3 SEO blog posts about AI automation, each 1000 words, targeting keywords "AI agent tools 2026", "best AI automation software", and "how to automate with AI". Save each as a separate .md file.` |

### Rules for Great Goals

1. Be specific about the OUTPUT (file, report, deployed site)
2. Mention the FORMAT if it matters
3. Include constraints (word count, keyword, style)
4. The more detail, the better the judge can verify completion

## Real Examples You Can Steal

```
📝 /goal Write 5 SEO blog posts about AI automation and save them as files
� /goal Fix every error in my code and make sure all tests pass
📊 /goal Research the top 10 AI agent tools in 2026 and write a comparison report
🌐 /goal Build a landing page for my product and deploy it to Netlify
� /goal Draft 7 days of email sequences for my new course launch
```

## Safety Features

- **Interrupt anytime** — type any message, Hermes prioritises you immediately
- **20-turn budget** — won't run forever without checking in
- **Fail-open judging** — if judge crashes, Hermes continues (never stuck)
- **Mid-run controls** — pause or check status without disrupting current turn
- **One goal at a time** — must `/stop` before setting a new one
- **Persistent storage** — goals saved to SessionDB, survive restarts

## When to Use /goal

### ✅ USE when:
- Task takes multiple steps
- You'd normally say "keep going" more than twice
- You want to set it and walk away
- Task involves building, writing, researching, or fixing something complex

### ❌ SKIP when:
- One-shot question ("What's the capital of France?")
- Single simple task ("Rename this file")
- You need to review each step before the next one happens

## SOP: Using /goal In Your Business

### Phase 1: Setup (One Time Only)
1. Install Hermes Agent on Mac or PC
2. Open terminal → type `hermes` to launch
3. Choose your AI model (kimi-k2.6 recommended)
4. Optionally set cheaper judge model in config
5. Optionally change turn budget in config.yaml

### Phase 2: Writing a Good Goal (Every Time)
- Bad goal = vague results
- Good goal = specific, measurable output
- Include: output type, format, constraints

### Phase 3: Running Your Goal
1. Type `/goal [your detailed task]`
2. Watch Hermes confirm: ⊙ Goal set (20-turn budget)
3. Step away — let it work
4. Check back with `/goal status`
5. If paused at 20 turns → `/goal resume`
6. When ✅ Goal achieved — check the output

### Phase 4: Saving Your Best Goals
- Keep a document of top-performing goal prompts
- Label each by use case
- Reuse as templates
- Build a library over time → this is your **AI automation playbook**

## 30-Day Roadmap

### Week 1: Foundation (Days 1–7)

| Day | Task |
|-----|------|
| 1 | Install Hermes, spend 30 min exploring |
| 2 | Run first `/goal` — simple task (3 blog post outlines) |
| 3 | Research goal: top 5 AI agent tools comparison |
| 4 | Experiment with `/goal pause` and `/goal resume` |
| 5 | Content goal relevant to YOUR business |
| 6 | Review outputs — note what worked |
| 7 | Rest |

### Week 2: Automation (Days 8–14)

| Day | Task |
|-----|------|
| 8 | Run a code-fix goal on a real project |
| 9 | Set up a research goal that runs daily via cron |
| 10 | Try a multi-file content generation goal |
| 11 | Test the judge with an intentionally vague goal (learn its limits) |
| 12 | Build a business-specific goal relevant to your SOPs |
| 13 | Review and refine your goal prompts library |
| 14 | Measure time saved vs. manual prompting |

### Week 3: Systems (Days 15–21)

| Day | Task |
|-----|------|
| 15 | Combine /goal with Obsidian vault for auto-saving outputs |
| 16 | Set up sub-agents that each run their own /goal |
| 17 | Build a competitor research goal with weekly schedule |
| 18 | Create a content pipeline goal (research → write → format → save) |
| 19 | Test /goal resume after a full restart |
| 20 | Document your top 5 reusable goal templates |
| 21 | Track week-over-week improvement in output quality |

### Week 4: Scale (Days 22–30)

| Day | Task |
|-----|------|
| 22 | Deploy Hermes on a VPS for 24/7 goal running |
| 23 | Set up Telegram notifications for goal completion |
| 24 | Build a team goal template library |
| 25 | Create a client delivery goal (automate a service you sell) |
| 26 | Set up nightly goals that run while you sleep |
| 27 | Review your goal library — prune what doesn't work |
| 28 | Calculate ROI: hours saved through /goal automation |
| 29 | Share your best goal templates with the community |
| 30 | Plan next month's automation expansion |

## Related

- [[Skool-Post-10-Hermes-Obsidian/01-Second-Brain-Stack|Post #10: Hermes + Obsidian]]
- [[Skool-Post-12-Claude-Obsidian/01-Claude-Obsidian|Post #12: Claude + Obsidian]]
- [[SOPs/SOP - Hermes Agent Setup]]
- [[Agent-OS-Base/Agent-OS-Ecosystem|Ecosystem: Hermes Agent]]
- [[docs/post15-hermes-goals-quickstart|QuickStart: Hermes /goal]]
