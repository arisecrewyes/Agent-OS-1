# Skool Post #32: Setup Free Claude Code + Agent OS

> **Source:** [7th June: Setup Free Claude Code + Agent OS](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=9a37b3f5d2b944638fd61f66c4673874)
> **Date:** 7 June 2025
> **Category:** Agent OS / Claude Code / Free AI Tooling

---

## What This Post Covers

How to set up and link **Free Claude Code** with **Agent OS** — a free alternative to paid Claude Code usage that routes through free AI models via a local proxy.

---

## What AgentOS Actually Is (10-Second Version)

AgentOS is your own private AI dashboard that runs on your computer at `http://localhost:3000`. It puts all your AI agents — Claude, Hermes, Gemini, Codex, Free Claude Code, OpenClaw — on one screen, plus:

- Studio (image/video/voice)
- SEO tools
- NotebookLM
- Goals/Memory
- Obsidian knowledge graph
- Phone agent

You don't "operate" it with commands. You talk to it and let the agents do the work.

---

## What "Free Claude Code" Means

Normally Claude Code costs money per use. **Free Claude Code** runs the exact same Claude Code, but routes it through a tiny local helper (called `fcc-server`) that sends the work to **free AI models** (OpenRouter, NVIDIA, Gemini, etc.) instead of charging you.

AgentOS already has a Free Claude Code panel built in — it lights up automatically once the helper is running.

---

## Setup in 3 Simple Steps

### ✅ Step 1 — Let Your Agent Install It for You

Open the `agent-os-pack` folder in Claude Code (or open Hermes) and paste this:

> "Read the README and the file `source/src/lib/fcc.ts` in this folder. Then install the Free Claude Code proxy from `github.com/Alishahryar1/free-claude-code`, start it with `fcc-server` so it's listening on port 8082, and keep it running. Tell me when it's live and walk me through getting a free API key. Don't make me run anything myself unless you're stuck."

That's it for the technical part — your agent installs it, starts it, and keeps it alive.

### ✅ Step 2 — Get ONE Free Key (~60 seconds, the only "human" step)

The proxy needs a free model to use.

**OPTION 1: OpenRouter**
- Go to [openrouter.ai/keys](https://openrouter.ai/keys)
- Gemma 4 or Owl Alpha are free and work the same way
- Just paste the key in the matching box

**OPTION 2: NVIDIA**
- Go to [build.nvidia.com](https://build.nvidia.com) → sign in → API Keys → create one → copy it
- Your agent will have opened the proxy's settings page at `http://127.0.0.1:8082/admin`
- Paste the key into the `NVIDIA_NIM_API_KEY` box and click **Validate**, then **Apply**

### ✅ Step 3 — Use It Inside AgentOS

1. Open `http://localhost:3000`
2. Click the **Free Claude Code** panel — it now shows green with your model name (e.g. "nemotron · NVIDIA NIM")
3. Start chatting / building
4. Anything it creates lands in `~/freeclaude-scratch/` and you can preview it live in the Workspace tab

**Done.** You're now running Claude Code for free, right inside AgentOS.

---

## How to Know It Worked

- The Free Claude Code panel is **green** (not "fcc-server isn't running")
- It shows your model + provider as a little pill
- You type a request and it replies — for free

---

## If Anything Breaks — Ask Your Agent

Paste this to Claude Code or Hermes:

> "The Free Claude Code panel in Agent OS says the proxy isn't running / shows an error. Check if fcc-server is listening on port 8082, restart it if needed, confirm my API key is set in the admin page, and get the panel green again."

---

## Two Things Worth Knowing

1. **It's completely optional.** If you're on a Claude Max plan, you can just use the normal Claude agent in AgentOS and skip all of this — Free Claude Code only exists to save you money by using free models.

2. **Keep it on the same machine.** AgentOS launches the agents locally, so run the dashboard and the proxy on the same computer (view it remotely with Tailscale/SSH if needed).

---

## Key Links

| Resource | URL |
|----------|-----|
| Agent OS Zip File | [Skool link](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=097eb41a59b74f06a6112351c07216fa) |
| Free Claude Code Proxy (GitHub) | `github.com/Alishahryar1/free-claude-code` |
| OpenRouter API Keys | [openrouter.ai/keys](https://openrouter.ai/keys) |
| NVIDIA API Keys | [build.nvidia.com](https://build.nvidia.com) |
| AgentOS Dashboard | `http://localhost:3000` |
| FCC Proxy Admin | `http://127.0.0.1:8082/admin` |

---

## Related Posts

- [[Skool-Post-31-Paperclip-AgentOS|Post #31: Paperclip + Agent OS]]
- [[Skool-Post-30-Idea-Factory|Post #30: Hermes Idea Factory]]
- [[Skool-Post-21-OpenClaw-Aion|Post #21: OpenClaw + Aion UI]]
