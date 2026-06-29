# QuickStart: Ruflo Agent Swarms

> Converted from Julian Goldie Skool Post #17 — "9th May: Ruflo Agent Swarms"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=af384934b1d14c1db4538434a2c34864

---

## What You're Building

**Ruflo Agent Swarms** — orchestrate 100+ AI workers that all run at once, talk to each other, and learn from every task they complete. One agent is useful. A hundred working together is unstoppable.

> "The future of work isn't humans doing more. It's humans directing smarter machines to do it for them."

---

## What Is Ruflo?

Ruflo is a platform that lets you control an army of AI agents — specialized robots that each do one thing brilliantly — all coordinated together. It runs on top of **Claude Code** (Anthropic's coding AI) and turns it into something far more powerful than one AI chatting with you.

### The Restaurant Kitchen Analogy

| Component | Role |
|-----------|------|
| **Router** (Head Chef) | Decides what kind of task it is and which agents handle it |
| **Agents** (Specialist Cooks) | Each one brilliant at their specific job |
| **Learning Loop** (Recipe Book) | Updated every night with new winning techniques |
| **Vector Memory** (Memory System) | Never forgets a customer's order |

---

## 🤖 The 100+ Agents

Ruflo comes with 100+ specialized agents out of the box:

- 🔐 **Security agents** — check systems for vulnerabilities
- ✍️ **Content agents** — write, edit, and structure written material
- 🧪 **Testing agents** — test code automatically
- 📖 **Documentation agents** — write user guides and technical docs
- 🏗️ **Architecture agents** — plan how systems should be built
- 🔍 **Research agents** — dig up information fast

---

## 🐝 What's a Swarm?

A swarm is a team of agents that organizes itself. You give the swarm a goal — it figures out who does what.

### Three Swarm Structures

| Structure | How It Works |
|-----------|-------------|
| 🌲 **Hierarchical** | One lead agent manages the others (like a manager and team) |
| 🕸️ **Mesh** | Every agent talks directly to every other agent |
| 🔄 **Adaptive** | The swarm changes its own structure based on the task |

---

## 💾 Vector Memory

Ruflo doesn't forget. Its vector memory system uses **HNSW indexing** — up to 12,500x faster than normal memory search. Every preference, result, and lesson learned is stored and pulled up for future tasks.

> "Like hiring an employee who reads every note from every meeting and never forgets a single thing."

---

## 🛡️ Security Features

- 🔒 **AIDefence system** — blocks bad inputs
- 🧹 **PII stripping** — removes private data (emails, phone numbers, SSNs) before anything leaves your system
- ✍️ **Digital signatures** — every message between agents is signed
- 📋 **Full audit trail** — everything that happened is logged
- 🚫 **Attack blocking** — path traversal and CVE vulnerabilities blocked automatically

---

## 🔌 Integrations & Plugins

**AI Providers:**
- 🤖 Claude (Anthropic)
- 🧠 GPT (OpenAI)
- 💎 Gemini (Google)
- 🌐 Cohere
- 🏠 Ollama (local AI on your own machine)

**Plugins:** 32 native plugins + 21 npm plugins available in the marketplace.

---

## 🌐 Web UI — No Install Needed

- **flo.ruv.io** — Multi-model chat with 210+ tools, persistent memory, parallel tool calling. No account, no API key, no installation.
- **goal.ruv.io** — Type a plain English goal, watch Ruflo break it into steps and execute with live agents.

---

## 📋 SOP: Getting Ruflo Running

### Step 1: Try Before You Install
🖥️ Go to [flo.ruv.io](https://flo.ruv.io), pick a model, type a task you'd normally spend 30+ minutes on.

### Step 2: Install Ruflo
```bash
npx ruflo@latest init
```

### Step 3: Add to Claude Code as MCP Server
```bash
claude mcp add ruflo -- npx ruflo@latest mcp start
```

### Step 4: Choose Your First Use Case
Pick ONE: Content creation, Research, Code review, Security scanning, or Documentation.

### Step 5: Set Up Memory
Tell Ruflo key facts about your business — who you are, what you do, your audience, your voice.

### Step 6: Install Core Plugins
```
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
/plugin install ruflo-autopilot@ruflo
```

### Step 7: Run Your First Swarm Task
Go to [goal.ruv.io](https://goal.ruv.io), type a plain English goal, watch it decompose and execute.

### Step 8: Document What Works
Build a log of tasks, outputs, and refinements — this becomes your AI workflow playbook.

---

## 📅 30-Day Roadmap

### Week 1 — Explore and Understand (Days 1–7)
| Day | Action |
|-----|--------|
| 1 | Visit flo.ruv.io — run 3 different tasks in the web UI |
| 2 | Watch a task run in parallel — notice multiple tools firing at once |
| 3 | Visit goal.ruv.io — type a real business goal, see how it breaks it down |
| 4 | Install Ruflo locally: `npx ruflo@latest init` |
| 5 | Add Ruflo to Claude Code as an MCP server |
| 6 | Identify your top 3 most time-consuming business tasks |
| 7 | Map each task to an agent type (research, content, security, documentation, code) |

### Week 2 — First Real Workflows (Days 8–14)
| Day | Action |
|-----|--------|
| 8 | Install ruflo-core, ruflo-swarm, and ruflo-autopilot plugins |
| 9 | Feed Ruflo your business context — who you are, what you do, your audience |
| 10 | Run your first REAL business task through Ruflo |
| 11 | Review the output critically — what was great, what needs tweaking? |
| 12 | Refine your prompt/goal and run again — notice the improvement |
| 13 | Run two tasks in parallel using the swarm |
| 14 | Write down the first workflow Ruflo has officially taken off your plate |

### Week 3 — Build Your AI Workforce (Days 15–21)
| Day | Action |
|-----|--------|
| 15 | Identify 5 recurring tasks that happen weekly or daily |
| 16 | Map each one to a Ruflo goal or agent combination |
| 17 | Set up memory prompts so Ruflo knows your business deeply |
| 18 | Test federation — let agents collaborate across machines |
| 19 | Connect a second AI provider (Gemini or local Ollama) for redundancy |
| 20 | Install 2 additional plugins relevant to your business vertical |
| 21 | Review time saved — calculate value in hours and money |

### Week 4 — Systemise and Scale (Days 22–30)
| Day | Action |
|-----|--------|
| 22 | Document your top 3 working Ruflo workflows as internal SOPs |
| 23 | Train a team member to use the web UI for simple tasks |
| 24 | Explore the 30 skills — find 3 you haven't used yet |
| 25 | Run a security scan using AIDefence agents |
| 26 | Set up 12 background auto-triggered workers |
| 27 | Review agent memory — what has Ruflo learned about your business? |
| 28 | Identify the next 5 tasks to automate in month 2 |
| 29 | Explore self-hosting options if data privacy is critical |
| 30 | Calculate total hours saved, output produced, and revenue impact |

---

## 🚫 Breaking Limiting Beliefs

| ❌ Wrong Belief | ✅ Right Belief |
|----------------|----------------|
| "I need to be a developer to use this" | Use the web UI at flo.ruv.io with zero coding |
| "AI agents make mistakes — can't trust them" | Built-in validation, security scanning, audit trails, self-correction |
| "Too expensive for my business" | CLI install is free and open source — only pay for API calls |
| "It'll take months to set up" | One command: `npx ruflo@latest init` — running in minutes |
| "AI forgets everything" | Vector memory remembers across every session — gets smarter over time |
| "I'll need to micromanage every agent" | Give a goal — the swarm figures out who does what |
| "Only for big tech companies" | Open source, self-hostable, built for solo operators and small teams |
| "My data will be sent to third parties" | Run entirely on your own machine with local models via Ollama |

---

## 🔁 Recap — Everything to Remember

- 🌊 **Ruflo** = AI agent orchestration platform running on top of Claude Code
- 🤖 **100+ specialized agents** — each built for a specific type of work
- 🐝 **Swarms** — self-organizing teams that handle tasks in parallel
- 🧠 **Persistent vector memory** — remembers everything across sessions
- 🔒 **Enterprise-grade security** — PII stripping, signed messages, audit trails
- 🌐 **Try it now** at [flo.ruv.io](https://flo.ruv.io) — no install, no account, no cost
- 🎯 **goal.ruv.io** — type a plain English goal, watch agents execute it live
- 📡 **Federation** — agents talk across different machines and organisations securely
- 🔌 **Connects to** Claude, GPT, Gemini, Cohere, and local Ollama models
- 💰 **Free and open source** — you only pay for API calls
- ⚡ **One command** — `npx ruflo@latest init` — up and running in minutes

> "You don't need more hours in your day. You need better systems running while you sleep."

---
*Built on Cognitum.One architecture. Powered by Claude Code. Supercharged by Ruflo.*
