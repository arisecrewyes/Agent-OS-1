# Hermes Agent Kanban for AI SEO — Quickstart Guide

> **Source:** Skool Post #20 — "4th May: Hermes Agent Kanban for AI SEO"
> **Author:** Julian (AI Profit Boardroom)
> **Converted:** 2026-06-29
> **Platform references:** GHL → GoStackBase (where applicable)

---

## What Is This?

Hermes Agent + Kanban = an AI assistant that works 24/7 on your SEO tasks.

- You give it a task in plain English.
- It figures out how to do it.
- It actually does it — no hand-holding required.

> "The future of business isn't hiring more people. It's building smarter systems that work without you."

---

## What Is Hermes Agent?

Hermes Agent is an AI tool that lives on your computer. It can:

- Browse the web
- Write code
- Build websites
- Do research
- Use tools like Claude, OpenRouter, and more

You just type what you want in plain English. It figures out the rest.

---

## What Is a Kanban Board?

A to-do list on steroids with columns:

**Triage → Todo → Ready → Running → Done**

- Originated from Toyota's factory system (1940s)
- Used by Spotify, Trello, and thousands of startups
- Simple: you can see exactly what's happening at any time

> "Visibility is the enemy of chaos. When you can see your work, you can control it."

---

## How Hermes + Kanban Work Together

1. You create tasks on the board.
2. The AI agent picks up tasks automatically.
3. It works in the background.
4. When done → moves to **Done**.
5. If it needs help → moves to **Blocked** and asks you a question.
6. You answer → it unblocks → keeps going.

---

## Why Use This for AI SEO?

- Automate the entire SEO content pipeline
- Build content strategies with hundreds of keywords
- Write blog posts, build websites, plan 30-day content calendars
- Focus on growing your community while the AI does the work

---

## Getting Started

### Step 1 — Install Hermes

1. Go to [hermesagent.ai](https://hermesagent.ai) and follow the install guide.
2. Run `hermes setup` in your terminal.
3. Connect to your AI provider (OpenRouter or Anthropic).
4. **Critical:** Make sure your API key is valid and has credits.
   - Check OpenRouter credits at: [openrouter.ai/settings/credits](https://openrouter.ai/settings/credits)

### Step 2 — Set Up Your Kanban Board

```bash
hermes kanban init        # Creates the Kanban database
hermes gateway start      # Starts the task processor
hermes dashboard          # Opens the visual board in your browser
```

### Step 3 — Create Your First AI SEO Task

```bash
hermes kanban create "build an ai seo content strategy for a community trying to rank and get traffic in the ai niche to teach people how to use AI" --assignee julian
```

The agent picks it up within 60 seconds. Watch it live:

```bash
hermes kanban watch
```

---

## Task Lifecycle

| Stage    | Description                                          |
|----------|------------------------------------------------------|
| Triage   | Raw idea, not yet ready                              |
| Todo     | Waiting on something before it can start             |
| Ready    | Assigned and waiting for the AI to pick it up        |
| Running  | The AI agent is actively working on it right now     |
| Blocked  | The AI needs your input before it can continue       |
| Done     | Finished! ✅                                          |

---

## Communicating With Your Agent

The AI communicates through **comments** on tasks:

1. When stuck → leaves a comment → moves to **Blocked**
2. You read the message → reply in the comment box → click **Unblock**
3. Agent reads your reply → continues working

**Via CLI (faster):**

```bash
hermes kanban comment t_TASKID "Your answer here"
hermes kanban unblock t_TASKID
```

---

## Common Problems & Fixes

### Task keeps crashing (401 error)
- API key is broken or expired
- Fix: Update `OPENROUTER_API_KEY=` in `~/.hermes/profiles/YOUR_PROFILE/.env`
- Clear auth cache and restart the gateway

### Task stuck in "Running"
- Claim TTL (time lock) might still be active
- Reset from SQLite database, or wait for it to expire (~10 min)
- Nudge with: `hermes kanban dispatch`

### Task is "Done" but you want changes
- You **CANNOT** comment on a Done task and expect the agent to see it
- Create a new task that builds on the previous one instead

---

## What the AI Actually Built (Real Results)

### Task 1: AI SEO Content Strategy

Output: `~/.hermes/kanban/workspaces/t_60d3509f/ai-seo-content-strategy.md`

Included:
- **3 keyword pillars:** Tool tutorials, use-case/outcome pages, beginner onboarding
- **5 topic clusters** for topical authority
- **GEO optimisation** targeting AI search engines (Perplexity, ChatGPT, Claude)
- **200+ long-tail keywords** ready to target
- **30-day content calendar** ready to execute
- **Target:** 200K+ monthly visitors by month 12

> "Don't compete on broad 'AI' terms. Own the 'how to use AI for [specific outcome]' space where competition is lower and conversion intent is higher."

### Task 2: Building the AI SEO Website

Built a full **Next.js website** from scratch:
- Homepage with SEO-optimised copy
- Blog section with MDX support
- Topic cluster pages
- About and Guides sections
- Tools directory
- Internal linking structure
- Tailwind CSS styling
- Mobile-responsive layout

Running locally at `http://localhost:3001` — ready to deploy.

---

## Standard Operating Procedure (SOP)

### Phase 1: Setup (One-Time)

1. Install Hermes Agent
2. Run `hermes setup` and enter your API key
3. Run `hermes kanban init`
4. Run `hermes gateway start`
5. Run `hermes dashboard` and bookmark the URL
6. Verify API key has credits at openrouter.ai/settings/credits

### Phase 2: Strategy Creation (Weekly)

1. Create a strategy task:
   ```bash
   hermes kanban create "Build AI SEO content strategy for [YOUR NICHE] targeting [YOUR AUDIENCE]" --assignee julian
   ```
2. Wait 5–15 minutes for completion
3. Read the output file in the workspace folder
4. Copy the keyword list and content calendar to your content team

### Phase 3: Website/Content Build (Per Project)

1. Create a build task referencing the strategy:
   ```bash
   hermes kanban create "Build [CONTENT TYPE] based on SEO strategy in [STRATEGY FILE PATH]" --assignee julian
   ```
2. Monitor in the dashboard
3. If Blocked → read comment → reply → Unblock
4. When Done → review output files → deploy

### Phase 4: Monitoring (Daily)

1. `hermes kanban list` — see all task statuses
2. Check for Blocked tasks needing input
3. Nudge stuck-in-Ready tasks: `hermes kanban dispatch`
4. Archive completed tasks

### Emergency SOP: Task Keeps Failing

1. Check the error: `hermes kanban log t_TASKID --tail 100`
2. If "401 User not found" → API key issue
3. Open `~/.hermes/profiles/julian/.env` in a text editor
4. Update the `OPENROUTER_API_KEY=` line
5. Delete `credential_pool` section in `~/.hermes/profiles/julian/auth.json`
6. Restart gateway:
   ```bash
   hermes gateway stop
   hermes gateway start
   ```
7. Reset and dispatch:
   ```bash
   hermes kanban unblock t_TASKID
   hermes kanban dispatch
   ```

---

## 30-Day Roadmap

### Week 1: Foundation (Days 1–7)

| Day | Action |
|-----|--------|
| 1 | Install Hermes Agent and connect API key |
| 2 | Run first test task: "Create a list of 50 AI tool keywords with low competition" |
| 3 | Review output, get comfortable with workflow |
| 4 | Create first real content strategy task for your niche |
| 5 | Review strategy — highlight top 20 keywords |
| 6 | Create task to write first 3 SEO blog posts |
| 7 | Review blog posts and publish the best one |

### Week 2: Building Momentum (Days 8–14)

| Day | Action |
|-----|--------|
| 8 | Create task for full site content architecture |
| 9 | Set up 5 topic cluster tasks (one per keyword pillar) |
| 10 | Review outputs, give feedback via task comments |
| 11 | Start task to build/optimise website SEO structure |
| 12 | Publish 3 more blog posts from content calendar |
| 13 | Create task for internal linking maps |
| 14 | Review all published content — track keyword positions |

### Week 3: Scale Up (Days 15–21)

| Day | Action |
|-----|--------|
| 15 | Create a swarm of tasks: one per topic cluster (5 total) |
| 16 | Let agents run overnight — check results in morning |
| 17 | Review and publish best 5 pieces of content |
| 18 | Create task to build tools directory for your niche |
| 19 | Set up GEO optimisation task (Perplexity, ChatGPT) |
| 20 | Create task for 10 comparison articles ("X vs Y") |
| 21 | Publish first batch of comparison articles |

### Week 4: Optimise and Automate (Days 22–30)

| Day | Action |
|-----|--------|
| 22 | Run audit task: "Audit my published content and identify gaps vs competitors" |
| 23 | Create update tasks for thin/weak content flagged |
| 24 | Set up recurring weekly content task using Hermes Cron |
| 25 | Build automated brief-to-publish pipeline using Kanban chains |
| 26 | Create task for email capture / lead magnet page |
| 27 | Run task to create 30 social media posts |
| 28 | Review all metrics: traffic, rankings, engagement |
| 29 | Double down on what worked — create 10 more posts |
| 30 | Create Month 2 strategy task and hand off to agents |

> "By Day 30, your AI agents should be running most of your SEO content machine. Your job shifts from doing the work to reviewing and directing it."

---

## Key Things to Remember

- **Always have valid API credits** — the #1 cause of failures is an expired key
- **Comments don't trigger done tasks** — always create a new task for new work
- **Blocked = the AI needs YOU** — check your board daily for blocked tasks
- **The workspace folder is your output** — everything the AI builds lives in `~/.hermes/kanban/workspaces/`
- **One task, one goal** — keep tasks focused with a clear, specific title
- **More specific = better results** — tell the AI your niche, audience, and goals

---

## Recap

- **Hermes Agent:** AI assistant that lives on your computer and works autonomously
- **Kanban:** Structured to-do list with clear statuses so nothing gets lost
- **Why it's powerful for SEO:** Automate keyword research, content strategy, blog writing, and full website builds — all in plain English
- **Communication:** Through comments on tasks — it reads, acts, and asks questions when stuck
- **Biggest mistake to avoid:** Don't comment on a Done task — create a new one instead
- **What's possible in 30 days:** Full AI SEO website, 200+ keywords, content calendar, automated publishing pipeline

> "You don't need to work harder. You need better systems. Hermes Kanban is the system."

---

## References

- [Hermes Agent Docs — Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Hermes Agent GitHub](https://github.com/NousResearch/hermes-agent)
- [OpenRouter Credits](https://openrouter.ai/settings/credits)
