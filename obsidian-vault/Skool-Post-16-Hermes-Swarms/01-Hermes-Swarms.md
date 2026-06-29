# Hermes AI Agent Swarms (Post #16)

> Converted from Julian Goldie Skool Post #16 — 2nd May
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=2db85a47e1b94bf3b8d03617f6caa77e

## The Core Idea

> "What if you could hire 14 AI workers, each with their own job, all running at the same time — for free?"

That's Hermes Agent Swarms. Instead of one AI doing one thing, you run multiple agents in parallel — each with a specific role, its own memory, and its own mission.

## The Two Pieces

### 🐍 Hermes Agent (The Brain)
- Built by [Nous Research](https://github.com/NousResearch/hermes-agent)
- Uses tools, remembers things, browses the web, writes files, runs code
- A smart robot assistant that lives on your computer

### 🖥️ Hermes Workspace (The Control Panel)
- Website running at `localhost:3000`
- See all agents, talk to them, watch them work in real time
- Like NASA mission control for AI workers
- GitHub: [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace)

## Swarm Mode

Each agent gets:
- Its own **role**
- Its own **job**
- Its own **memory**

They all work in parallel — like a real team.

### Real Example: SEO Content Team

| Agent | Role | Output |
|-------|------|--------|
| Swarm5 (Builder) | Content Writer | 5 full blog posts + meta tags |
| Swarm2 (Foundation) | Keyword Research | 50+ keywords, topic clusters, competitor gaps |
| Swarm4 (Sage) | Technical SEO | JSON-LD schema, Open Graph templates, site architecture |
| Swarm12 (Triage) | Link Building | 30+ link opportunities, outreach templates, 20 social posts |
| Swarm11 (QA) | Content Strategy | 90-day calendar, content brief template, SEO style guide |

All 5 agents ran simultaneously → 22 files delivered automatically → zero humans needed.

## How It Works (4 Steps)

1. **Orchestrator Receives Mission** → You type a goal. Aurora (boss agent) receives it.
2. **Orchestrator Decomposes** → Aurora breaks the job into smaller tasks and dispatches to specialists.
3. **Workers Execute** → Each agent spins up in its own tmux session. Works independently with assigned AI model.
4. **Results Delivered** → Each agent writes output to a shared folder. Workspace UI shows live status.

## The Workspace UI

Open `localhost:3000/swarm2`:

- **📊 Control Board** — Agent statuses: 🟢 Running | 🟡 Ready | 🔴 Blocked | 🔵 Reviewing
- **📥 Inbox** — Checkpoints and reports from agents
- **🔄 Router** — Orchestrator decides task assignment
- **📺 TUI View** — Watch any agent's terminal in real time

## Common Problems & Fixes

| Problem | Meaning | Fix |
|---------|---------|-----|
| "Can't find pane: swarm-swarm2" | No chat history to start from | **Seed** the agent — give it one message first |
| "401 Error: User not found" | API key wrong or expired | Update `.env` and restart |
| Page slow/won't load | Leaked background processes | `pkill -f "pty-helper.py"` |
| Agents don't show up | Server started without `.env` | Restart with env file loaded |

## SOP: Launch Sequence

### Pre-Flight Checklist
- [ ] Hermes Agent installed and updated
- [ ] Hermes Workspace installed and running
- [ ] `.env` has valid API keys
- [ ] `HERMES_DASHBOARD_TOKEN` set in `.env`
- [ ] Gateway on port 8642
- [ ] Dashboard on port 9119

### Launch Commands
```bash
# Terminal 1 — Gateway
hermes gateway run

# Terminal 2 — Dashboard
hermes dashboard

# Terminal 3 — Workspace (in workspace folder)
pnpm dev
```

Then open `http://localhost:3000/swarm2` (hard refresh: Cmd/Ctrl + Shift + R).

### Post-Mission
- Review all output files for quality
- Archive output folder with today's date
- Reset agent states to "idle"
- Kill lingering tmux sessions
- Commit improvements to swarm config

## Quick Tips

1. **Be Specific** — "Write 3 SEO blog posts about X, 1200+ words, with CTA to [URL]" beats "write some content"
2. **Always Assign a Reviewer** — One agent checks the work of others before publishing
3. **Different Models for Different Jobs** — Fast/cheap for research, smart/expensive for editing
4. **Kill Leaked Processes** — `pkill -f "pty-helper.py"` fixes 90% of performance issues
5. **Keep .env Updated** — Monthly reminder to rotate API keys

## 30-Day Roadmap

### Week 1: Setup & First Test
| Day | Task |
|-----|------|
| 1 | Install Hermes Agent, verify with `hermes` |
| 2 | Install Hermes Workspace, run at `localhost:3000` |
| 3 | Configure `.env` with API keys (OpenRouter easiest) |
| 4 | Run first single-agent task |
| 5 | Explore Workspace UI |
| 6 | Run first 2-agent swarm |
| 7 | Review outputs, fix problems |

### Week 2: Build Core Team
| Day | Task |
|-----|------|
| 8 | Define 5 core roles for your business |
| 9 | Create agent profiles in `swarm.yaml` |
| 10 | Run 5-agent mission on low-stakes task |
| 11 | Review outputs, note improvements |
| 12 | Improve prompts, re-run, compare |
| 13 | Add Reviewer agent |
| 14 | Run first full reviewed mission end-to-end |

### Week 3: Scale Up
| Day | Task |
|-----|------|
| 15 | Identify highest-ROI content type, build dedicated swarm |
| 16 | Set up SEO swarm (keyword research, writer, technical SEO, link building) |
| 17 | Run SEO swarm on real topic |
| 18 | Publish first AI-swarm-produced content |
| 19 | Build social media swarm |
| 20 | Set up YouTube script swarm |
| 21 | Run all three swarms simultaneously |

### Week 4: Automate
| Day | Task |
|-----|------|
| 22 | Set up cron jobs for automatic swarm runs |
| 23 | Create master prompt templates |
| 24 | Set up quality gate (reviewer must approve) |
| 25 | Connect output to content calendar |
| 26 | Train reviewer, create 10-point checklist |
| 27 | Build reporting swarm for weekly analytics |
| 28 | Full retrospective |
| 29 | Document workflow in SOP |
| 30 | Measure results — content, time saved, ROI |

## Resources

- **Hermes Agent:** [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Hermes Workspace:** [github.com/outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace)
- **Official Docs:** [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)
- **Workspace Docs:** [hermes-workspace.com](https://hermes-workspace.com)
- **Discord:** Invite on Hermes Agent GitHub page

## Related

- [[01-Hermes-Goals|Post #15: Hermes /goal System]]
- [[01-Hermes-Use-Cases|Post #13: 237+ Hermes Agent Use Cases]]
- [[01-Hermes-Owl-Alpha|Post #14: Hermes + Owl Alpha]]
- [[01-Second-Brain-Stack|Post #10: Hermes + Obsidian]]
- [[SOP - Hermes Agent Setup]]
- [[Agent-OS-Ecosystem|Ecosystem: Hermes Agent]]
