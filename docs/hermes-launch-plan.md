# Hermes Agent — Launch Plan

> Structured 30-day timeline for mastering Hermes Agent.
> Source: Julian Goldie SEO — Skool Post #4
> Related: [[hermes-agent-capabilities-general]] | [[hermes-quickstart]]

---

## Phase 1: Installation & Setup (Days 1-7)

### Day 1-3: Learning Period
- [ ] Install Hermes Agent
- [ ] Run setup wizard and configure model
- [ ] Verify with `hermes doctor`
- [ ] Connect Telegram (or preferred platform)
- [ ] **Give it real tasks** — not toy examples
- [ ] Hermes builds `memory.md` (your projects, preferences)
- [ ] Hermes builds `user.md` (communication style, priorities)
- [ ] These files are injected into every session automatically

### Day 4-7: Applied Learning
- [ ] Hermes now knows your projects and preferences
- [ ] Give it complex tasks (5+ tool calls = auto-skill creation)
- [ ] Install Wonderly Skills: `hermes skills install wonderly-skills`
- [ ] Set up first scheduled task (cron job)
- [ ] **Give feedback on every task** — this is how it improves
- [ ] By Day 7: Dramatically better than Day 1

## Phase 2: Training & Tuning (Days 8-14)

### Focus Areas
- [ ] Start connecting external tools:
  - Firecrawl (web browsing)
  - Browser Base (visual browsing)
  - Nana Banana 2 (image generation)
  - X/Twitter Developer API
- [ ] Create your first custom skill (let Hermes auto-create one)
- [ ] Set up fallback model chain (primary + backup)
- [ ] Set up spending limits on your API account
- [ ] Test social media posting (X, TikTok, Instagram)

### First Custom Skill
Ask Hermes to create a skill:
```
"Create a skill for [your specific workflow]"
```

Then give feedback every time it runs:
- Tell it what worked
- Tell it what didn't
- It updates `skill.md` files and improves

## Phase 3: Automation & Scaling (Days 15-21)

### Scheduled Tasks
- [ ] Set up daily news scanning
- [ ] Set up social media analytics reporting
- [ ] Set up competitor monitoring
- [ ] Set up automated content pipeline

### Multi-Agent Profiles
- [ ] Create isolated profiles for different tasks:
  ```bash
  hermes profile create twitter-agent
  hermes profile create research-agent
  hermes profile create content-writer
  ```
- [ ] Each profile has its own model, memory, and skills

### MCP Setup
- [ ] Explore MCP integrations
- [ ] Run `hermes mcp serve` to use Hermes as backend for Claude/Cursor
- [ ] Connect external tools via MCP

## Phase 4: Mastery (Days 22-30)

### Review & Optimize
- [ ] Review all custom skills — refine and improve
- [ ] Back up all `skill.md` files outside Hermes
- [ ] Optimize model selection (cheaper models for simple tasks)
- [ ] Set up `hermes claw migrate` if coming from OpenClaw
- [ ] Explore the Awesome Hermes Agent extension for more skills

### Advanced
- [ ] Set up PaperclipIP for multi-agent hierarchy
- [ ] Configure Jarvis Voice for daily briefings
- [ ] Set up Goal Mode for long-term projects
- [ ] Export/import profiles for backup

## Ongoing

- [ ] Give feedback on every task (compounding improvement)
- [ ] Back up skill.md files weekly
- [ ] Monitor API usage and costs weekly
- [ ] Review and update skills monthly
- [ ] Test new community skills
- [ ] Always approve social media posts manually for first 10 posts

## Key Mindset

> **The more you use it, the better it gets.** This is a compounding effect.
> **Always give feedback on every task.** This is how it improves.
> **Be prepared for the first 7 days.** It will not be perfect but it gets dramatically better by day 7.

---

## Related

- For the full capability reference: `hermes-agent-capabilities-general.md`
- For implementation steps: `hermes-quickstart.md`
- For prompts: `hermes-prompts.md`
