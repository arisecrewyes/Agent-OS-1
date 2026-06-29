# QuickStart: Hermes AI Agent Swarms

> Converted from Julian Goldie Skool Post #16 — "2nd May: Hermes AI Agent Swarms"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=2db85a47e1b94bf3b8d03617f6caa77e

---

## What You're Building

**Hermes Agent Swarms** — run multiple AI agents in parallel, each with its own role, job, and memory. One agent is helpful. Fourteen agents working in parallel is a superpower.

> "What if you could hire 14 AI workers, each with their own job, all running at the same time — for free?"

---

## The Two Pieces of Software

### Piece #1 — 🐍 Hermes Agent (The Brain)
- AI agent built by [Nous Research](https://github.com/NousResearch/hermes-agent)
- Can use tools, remember things, browse the web, write files, run code
- Think of it as a very smart robot assistant that lives on your computer

### Piece #2 — 🖥️ Hermes Workspace (The Control Panel)
- Beautiful website that runs at `localhost:3000`
- See all your agents, talk to them, watch them work in real time
- Like NASA mission control — but for AI workers
- GitHub: [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace)

---

## 🐝 Swarm Mode — The Magic Sauce

Swarm Mode lets you run multiple agents at the same time. Each agent gets:
- Its own **role**
- Its own **job**
- Its own **memory**

They all work in parallel — like a real team.

### Real Example: An SEO Content Team

| Agent | Role | What It Produced |
|-------|------|-----------------|
| Swarm5 (Builder) | Content Writer | 5 full blog posts + meta tags |
| Swarm2 (Foundation) | Keyword Research | 50+ keywords, topic clusters, competitor gap analysis |
| Swarm4 (Sage) | Technical SEO | JSON-LD schema, Open Graph templates, site architecture |
| Swarm12 (Triage) | Link Building | 30+ link opportunities, outreach templates, 20 social posts |
| Swarm11 (QA) | Content Strategy | 90-day calendar, content brief template, SEO style guide |

**Result:** All 5 agents ran simultaneously. 22 files delivered automatically. Zero humans needed.

---

## 🔧 How It Works — 4 Steps

### Step 1 — The Orchestrator Receives a Mission
You type: *"Build an SEO team to create blog content about Hermes AI Agent."*
The main agent (**Aurora**) receives this. She is the orchestrator — the boss agent.

### Step 2 — The Orchestrator Decomposes the Mission
Aurora breaks the big job into smaller jobs and dispatches tasks to specialist agents.

### Step 3 — Workers Execute Their Tasks
Each worker agent spins up in its own tmux session (background terminal). They work independently using whatever AI model you've assigned.

### Step 4 — Results Are Delivered
Each agent writes output to a shared folder. The Workspace UI shows live status of every agent.

---

## 🖥️ The Workspace UI

When you open `localhost:3000/swarm2`:

- **📊 The Control Board** — Every agent and their status:
  - 🟢 Running — currently working
  - 🟡 Ready — waiting for a task
  - 🔴 Blocked — hit a problem, needs help
  - 🔵 Reviewing — human needs to check something

- **📥 The Inbox** — Checkpoints and reports from agents
- **🔄 The Router** — Orchestrator decides which agent gets which task
- **📺 The TUI View** — Watch any agent's terminal in real time

---

## ⚠️ Common Problems & Fixes

| Problem | What It Means | The Fix |
|---------|--------------|---------|
| "Can't find pane: swarm-swarm2" | Agent has no chat history to start from | **Seed** the agent — give it one message first |
| "401 Error: User not found" | API key is wrong or expired | Update API key in `.env` and restart |
| Page won't load / is slow | Leaked background processes eating resources | Run `pkill -f "pty-helper.py"` |
| Server loads but agents don't show up | Server started without `.env` file loaded | Restart server with env file properly loaded |

---

## 📋 SOP — Standard Operating Procedure

### ✅ Pre-Flight Checklist
- [ ] Hermes Agent is installed and updated
- [ ] Hermes Workspace is installed and running
- [ ] `.env` file has valid API keys
- [ ] `HERMES_DASHBOARD_TOKEN` is set in `.env`
- [ ] Gateway is running on port 8642
- [ ] Dashboard is running on port 9119

### 🚀 Launch Sequence

```bash
# Step 1 — Start the Gateway
hermes gateway run

# Step 2 — Start the Dashboard (second terminal)
hermes dashboard

# Step 3 — Start the Workspace (third terminal, in workspace folder)
pnpm dev
```

Then open `http://localhost:3000/swarm2` in your browser (hard refresh: Cmd/Ctrl + Shift + R).

### Step 4 — Check All Agents Are Healthy
Every agent should show as "Ready" or "Idle". If blocked, check logs and clear.

### Step 5 — Write Your Mission
Example: *"Create a full SEO content strategy for [topic] with keyword research, 5 blog posts, and a link-building plan. Send traffic to [your URL]."*

### Step 6 — Watch It Run
The orchestrator routes tasks to specialist agents. Watch the status board update in real time.

### Step 7 — Review Results
Once all agents show "Done", review every file for quality before publishing.

### 🛑 If Something Breaks
- **Blocked agent** → Click in, read the reason, clear the block, re-dispatch
- **Page freeze** → `pkill -f "pty-helper.py"` then refresh
- **401 error** → Check API key in `.env`, restart server

### 🔁 Post-Mission Cleanup
- Review all output files for quality
- Archive the output folder with today's date
- Reset all agent states to "idle"
- Kill any lingering tmux sessions
- Commit any improvements to your swarm config

---

## 🗓️ 30-Day Roadmap

### Week 1 — Setup & First Test (Days 1–7)

| Day | Task |
|-----|------|
| 1 | Install Hermes Agent using the one-line installer. Verify with `hermes` in terminal. |
| 2 | Install Hermes Workspace. Get it running at `localhost:3000`. |
| 3 | Configure `.env` with API keys. Set up at least one AI model provider (OpenRouter is easiest). |
| 4 | Run your first single-agent task — ask one agent to write something simple. |
| 5 | Explore the Workspace UI — learn Control Board, Inbox, and Router. |
| 6 | Run your first 2-agent swarm (research + writing). |
| 7 | Review outputs. Fix any problems. |

### Week 2 — Build Your Core Team (Days 8–14)

| Day | Task |
|-----|------|
| 8 | Define the 5 core roles your business needs most (Researcher, Writer, Editor, Social Media, Analytics). |
| 9 | Create profiles for each agent in `swarm.yaml` — assign role, model, specialty. |
| 10 | Run a full 5-agent mission on a low-stakes task (e.g., 3 blog posts about your niche). |
| 11 | Review all outputs. Note which agents performed well and which need better prompts. |
| 12 | Improve agent prompts and role descriptions. Re-run and compare quality. |
| 13 | Add a Reviewer agent to check all work before it leaves the swarm. |
| 14 | Run your first full reviewed mission end-to-end. No human intervention needed. |

### Week 3 — Scale Up & Specialise (Days 15–21)

| Day | Task |
|-----|------|
| 15 | Identify your highest-ROI content type. Build a dedicated swarm just for that. |
| 16 | Set up an SEO swarm: keyword research, content writer, technical SEO, link building. |
| 17 | Run the SEO swarm on a real business topic. |
| 18 | Review outputs and publish your first AI-swarm-produced content. |
| 19 | Build a social media swarm that repurposes blog content. |
| 20 | Set up a YouTube script swarm that turns blog posts into video scripts. |
| 21 | Run all three swarms on the same topic simultaneously. |

### Week 4 — Automate & Systemise (Days 22–30)

| Day | Task |
|-----|------|
| 22 | Set up cron jobs to run swarms automatically at set times. |
| 23 | Create a master prompt template for each swarm type (30-second mission launch). |
| 24 | Set up a quality gate — reviewer agent must approve content before saving. |
| 25 | Connect swarm output folder to a content calendar tool or spreadsheet. |
| 26 | Train someone to review swarm outputs daily. Create a 10-point quality checklist. |
| 27 | Build a reporting swarm that creates weekly analytics summaries. |
| | 28 | Run a full retrospective — what worked, what didn't, what to change. |
| 29 | Document your entire workflow in a simple SOP. |
| 30 | Measure results — content produced, time saved, ROI. |

---

## 💡 Quick Tips for Best Results

1. **Be Specific With Missions** — Bad: "Write some SEO content." Good: "Write 3 SEO blog posts targeting 'best AI agent tools for small businesses', each 1200+ words, with a CTA linking to [URL]."
2. **Always Assign a Reviewer Agent** — Don't let raw output go straight to publish.
3. **Use Different Models for Different Jobs** — Fast/cheap for research and drafting. Smarter/more expensive for final editing.
4. **Check for Leaked Processes** — If workspace gets slow, run `pkill -f "pty-helper.py"` first. Fixes 90% of performance issues.
5. **Keep Your .env File Updated** — Set a monthly reminder to check and rotate API keys.

---

## 📚 Useful Resources

- **Hermes Agent (the brain):** [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Hermes Workspace (the control panel):** [github.com/outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace)
- **Official Docs:** [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)
- **Hermes Workspace Docs:** [hermes-workspace.com](https://hermes-workspace.com)
- **Discord Community:** Find the invite on the Hermes Agent GitHub page

---

## 🔁 Recap — Everything in 60 Seconds

- 🤖 **Hermes Agent** is a self-improving AI agent built by Nous Research
- 🖥️ **Hermes Workspace** is the control panel at `localhost:3000`
- 🐝 **Swarm Mode** lets you run 14 agents at once, each with a different job
- 📋 Each agent gets a role, a model, a mission, and a memory
- 🎯 The orchestrator receives your mission and routes it to specialist agents
- 📁 All outputs land in a shared folder on your computer automatically
- ⚠️ Common problems: blocked agents (seed them), 401 errors (fix API keys), slow pages (kill leaked processes)
- 🗓️ 30 days is all you need to go from zero to a fully automated AI content team
- 💰 The ROI is massive — one session can produce what a human team takes weeks to do

> *"The future of work isn't humans vs AI. It's humans directing AI teams to do the work humans shouldn't have to do themselves."*
