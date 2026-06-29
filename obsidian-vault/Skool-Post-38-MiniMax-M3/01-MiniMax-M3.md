---
title: MiniMax M3 + Hermes Agent FREE
source: Skool Post #38 — AI Profit Boardroom
date: 2026-06-01
tags:
  - minimax
  - hermes-agent
  - ai-agent
  - ollama
  - agent-os
  - skool
  - open-weights
  - self-improving
---

# MiniMax M3 + Hermes Agent FREE — The Complete Beginner's Guide

> The complete guide to building your own self-improving AI agent for $0. MiniMax M3 (brain) + Hermes Agent (body) + Agent OS Framework™.

---

## Wait... What Is This Even About?

Imagine a robot helper that lives on the internet. You text it from your phone. It writes, searches, sends emails, teaches itself new skills. And it costs almost nothing to run.

That's what we're building:
- **MiniMax M3** = the thinking engine
- **Hermes Agent** = the body that does things
- Both are free

---

## The Two Tools Explained

### Tool #1: MiniMax M3 (The Brain)

MiniMax M3 is a brand new open-weights AI model — the first to combine three frontier capabilities.

**Benchmarks:**
- 59.0% on SWE-Bench Pro
- 66.0% on Terminal Bench 2.1
- 1 million context via MiniMax Sparse Attention

**Privacy:** Available via Ollama Cloud — US-based with zero data retention. They don't keep your stuff.

### Tool #2: Hermes Agent (The Body)

Built by Nous Research. The key differentiator:

> "It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions."

Most AI tools forget everything when you close them. Hermes remembers. It gets better the more you use it.

**Messaging:** Telegram, Discord, Slack, WhatsApp, Signal, CLI — all from a single gateway process.

**Cost:** Runs on a $5 VPS, GPU cluster, or serverless infrastructure that costs nearly nothing when idle.

---

## Why Putting Them Together Is INSANE

- The brain (MiniMax M3) is free
- The body (Hermes Agent) is free and open-source
- Together they write content, search the web, send emails, run scheduled tasks, and learn your business over time
- Big companies pay thousands for this. You're doing it for free.

---

## The Agent OS Framework™

Three layers that explain every AI agent forever:

### Layer 1: EARS
How your agent hears you. The input. For Hermes: Telegram, Discord, WhatsApp, or terminal.

### Layer 2: BRAIN
The thinking part. The model that decides what to do. Today: MiniMax M3. Swappable anytime.

> "Switch with `hermes model` — no code changes, no lock-in."

### Layer 3: HANDS
How your agent gets things done. The tools. Web search, email, file creation, scheduled tasks.

> "40+ tools, toolset system, terminal backends."

**In one breath:** Ears hear you. Brain decides. Hands do the work.

---

## Breaking Your Limiting Beliefs

| # | Wrong Belief | Right Belief |
|---|--------------|--------------|
| 1 | "I need to know how to code." | Talk in plain English. The installer handles uv, Python 3.11, Node.js, ripgrep, ffmpeg. |
| 2 | "This must cost a fortune." | Free model + free agent + $5 VPS. |
| 3 | "AI tools forget everything." | Hermes has a closed learning loop with agent-curated memory. |
| 4 | "I'm too late." | MiniMax M3 dropped today. You're early. |
| 5 | "I'd figure this out alone." | The AI Profit Boardroom community does it together. |

---

## The Setup (Step By Step)

### Step 1: Install Hermes Agent

**Mac / Linux / WSL:**
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
```

### Step 2: Reload And Start
```bash
source ~/.bashrc
hermes
```

### Step 3: Set MiniMax M3 As Your Brain
```bash
hermes model
```
Pick MiniMax M3 from the list.

**Test M3 directly:**
```bash
ollama run minimax-m3:cloud
```

### Step 4: Give It Hands (Tools)
```bash
hermes tools
```
Turn on web search, file creation, etc.

### Step 5: Let It Live On Your Phone
```bash
hermes gateway
```
Connect Telegram or your favorite app.

---

## Standard Operating Procedure (SOP)

### Daily SOP
1. Open your messaging app
2. Send your agent your top task for the day
3. Be specific — tell it the goal, not the steps
4. Let it work, then review the output
5. Correct it once if needed (it learns from this)
6. Save any winning result as a skill

### Weekly SOP
1. Run `hermes update` to get the newest version
2. Check `/insights` to see what your agent learned
3. Review your scheduled cron tasks
4. Add one new automation you do by hand
5. Back up your memory files

### Monthly SOP
1. Review every skill your agent created
2. Delete skills you don't use
3. Try swapping in a new brain model and compare
4. Document your best 3 workflows
5. Teach one to a team member

> "A weak system used daily beats a perfect system used never."

---

## 30-Day Roadmap

### Week 1: Foundation (Days 1–7)
| Day | Task |
|-----|------|
| 1 | Install Hermes Agent |
| 2 | Connect MiniMax M3 as your brain |
| 3 | Turn on web search and file tools |
| 4 | Have one full conversation, learn the commands |
| 5 | Connect it to Telegram |
| 6 | Give it your first real task |
| 7 | Review the week, note what worked |

### Week 2: Real Tasks (Days 8–14)
| Day | Task |
|-----|------|
| 8 | Use it to write one piece of content |
| 9 | Have it research a competitor |
| 10 | Let it draft 3 emails |
| 11 | Save your first custom skill |
| 12 | Set up your first scheduled task (cron) |
| 13 | Test it on a task you usually hate doing |
| 14 | Review — what saved you the most time? |

### Week 3: Automation (Days 15–21)
| Day | Task |
|-----|------|
| 15 | Build a daily report automation |
| 16 | Build a nightly backup automation |
| 17 | Connect a second platform (Discord or Slack) |
| 18 | Spawn a subagent for a parallel task |
| 19 | Refine your top 3 skills |
| 20 | Document your workflows |
| 21 | Review — what can run without you now? |

### Week 4: Scale (Days 22–30)
| Day | Task |
|-----|------|
| 22 | Automate one full business process end-to-end |
| 23 | Teach a team member to use it |
| 24 | Test a different brain model |
| 25 | Build a weekly audit automation |
| 26 | Clean up unused skills |
| 27 | Map out your next 5 automations |
| 28 | Calculate hours saved this month |
| 29 | Share a win in the community |
| 30 | Plan month two |

---

## 100+ Prompts To Use With Your Agent

### Content Creation
- Write a YouTube title for a video about [topic] in my voice.
- Draft a 60-second script hook about [topic].
- Turn this transcript into a blog post: [paste].
- Write 10 tweet ideas about [topic].
- Rewrite this paragraph at a 3rd-grade reading level: [paste].
- Create a LinkedIn post from this idea: [idea].
- Write an email subject line for [offer].
- Give me 5 hooks for a short-form video on [topic].
- Summarize this article in 5 bullet points: [link].
- Write a product description for [product].
- Create an outline for a guide about [topic].
- Write a call-to-action for joining a community.
- Turn these notes into a clean newsletter: [notes].
- Write 3 versions of this headline: [headline].
- Draft a thread about [topic] with 7 tweets.

### Research
- Search the web for the latest news on [topic].
- Find 5 competitors in the [niche] space.
- Summarize what people are saying about [tool].
- Find the top 3 articles about [topic] this week.
- Compare [tool A] and [tool B] for me.
- Find statistics about [topic] from 2026.
- Research my audience's biggest pain points around [topic].
- Find trending topics in [niche] right now.
- Look up pricing for [product/service].
- Find quotes from experts on [topic].
- Research the best practices for [task].
- Find case studies about [result].
- Summarize this long PDF for me: [file].
- Find the most asked questions about [topic].
- Check if [claim] is actually true.

### Email & Outreach
- Draft a cold outreach email to [type of person].
- Write a follow-up email after no reply.
- Reply to this email politely declining: [paste].
- Write a thank-you email to a new customer.
- Draft an email announcing [news].
- Write a re-engagement email to old leads.
- Make this email shorter and friendlier: [paste].
- Write 3 subject lines and pick the best.
- Draft an apology email for [situation].
- Write a welcome email for new members.

### Automation & Scheduling
- Send me a daily news summary every morning at 8am.
- Back up my files every night.
- Send me a weekly report every Friday.
- Remind me to review my goals every Monday.
- Check this website daily and tell me if it changes.
- Run a monthly audit of my tasks.
- Alert me when [condition] happens.
- Schedule a daily motivation message.
- Summarize my week every Sunday night.
- Track my progress on [goal] weekly.

### Skill & Memory
- Save this process as a skill I can reuse.
- What have you learned about my business?
- Remember that my brand voice is [description].
- Create a skill for writing my video titles.
- What skills do you have right now?
- Improve the skill you used last time.
- Search our past conversations about [topic].
- Remember my top 3 goals this month.
- Build a skill for my weekly reporting.
- Forget the old instructions about [thing].

### Business & Strategy
- Help me plan my content for next week.
- Brainstorm 10 offers I could create.
- Analyze my biggest time-wasters and suggest fixes.
- Build me a simple 90-day plan for [goal].
- What's one task I should automate first?
- Help me write a job description for [role].
- Create an onboarding checklist for new hires.
- Suggest 5 ways to improve customer retention.
- Draft a simple sales script for [offer].
- Help me prioritize this to-do list: [list].

### Agent Management
- What tools do you currently have enabled?
- Switch your brain to a different model.
- Show me my recent scheduled tasks.
- Compress this conversation to save space.
- Show me my usage this week.
- Spawn a subagent to research [topic] separately.
- What can you do that I'm not using yet?
- Walk me through your available commands.
- Set a personality that's direct and friendly.
- Start a fresh conversation.

### YouTube & Creator
- Give me 10 video title ideas for [topic].
- Write a hook for the first 5 seconds of my video.
- Turn this video into 3 short clips with captions.
- Write a description for my video on [topic].
- Suggest thumbnail text for [video idea].
- Find trending AI tools to make a video about.
- Write a script outline for a tool review.
- Give me 5 video ideas based on [trending topic].
- Write community post ideas for my channel.
- Summarize the comments on this video: [link].

### Problem-Solving
- I'm stuck on [problem], walk me through it step by step.
- Explain [concept] like I'm in 3rd grade.
- What am I missing about [situation]?
- Give me 3 ways to solve [problem].
- Debug this error message for me: [paste].
- What's the simplest version of [complex task]?
- Help me make a decision between [A] and [B].
- What questions should I be asking about [topic]?
- Break this big goal into tiny steps: [goal].
- What's the 80/20 of [task]?

### Bonus Power Prompts
- Act as my chief of staff and plan my day.
- Review everything I did today and suggest improvements.
- Build me a custom workflow for [recurring task].
- Be brutally honest — what's holding my business back?
- Teach me one new thing about AI agents today.

---

## Recap (The Whole Thing In 60 Seconds)

1. **MiniMax M3** = the Brain. Free, open-weights, 1M context.
2. **Hermes Agent** = the Body. Free, open-source, self-improving.
3. **Agent OS Framework™** = Ears hear you, Brain decides, Hands do the work.
4. Broke the 5 beliefs that stop most people.
5. Install with one line.
6. SOP for daily, weekly, monthly use.
7. 30-day roadmap from zero to automated.
8. 100+ prompts to start today.

> "Tools change. Frameworks don't."

---

## Related
- [[Agent-OS-Base|Agent OS Framework]]
- [[Skool-Post-34-Hermes-Hyperframes]]
- [[Skool-Post-24-Hermes-V017]]
