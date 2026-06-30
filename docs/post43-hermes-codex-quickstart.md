# QuickStart: How To Use Hermes Agent With Codex

> Converted from Julian Goldie Skool Post #43 — "14th May: How To Use Hermes Agent With Codex"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=463acf1c2d4c4aee90c0b4f8ff1c3c08
> Duration: 14:50 video

---

## What You're Building

The **Goldie Stack Framework™** — a 4-layer system connecting Hermes Agent + MCP + Codex into a fully automated business engine.

---

## The 4 Layers

| Layer | Component | Role |
|-------|-----------|------|
| 🧱 1 | **The Brain** — Hermes Agent | Smart AI that talks to tools, reads files, writes code, sends messages |
| 🧱 2 | **The Hands** — MCP (Model Context Protocol) | Bridge between AI brain and real world (GitHub, Stripe, databases, etc.) |
| 🧱 3 | **The Builder** — Codex (OpenAI) | Coding agent that reads, writes, fixes code automatically |
| 🧱 4 | **The Output** — Business Automation | SEO, content, outreach, code — all automated |

---

## The 5 Principles

| Principle | Old Way | Goldie Stack Way |
|-----------|---------|-----------------|
| 1. **Connect Everything** | One tool at a time, manual copy-paste | All tools talk to each other automatically |
| 2. **Automate Boring First** | 80% time on non-growth tasks | Automate 80% in week one, focus on growth |
| 3. **Agents Compound** | One human = one task = one result | One agent triggers another → full workflow, zero manual input |
| 4. **Build Once, Profit Forever** | Do work manually every day | Set up MCP config once (30 min), runs forever |
| 5. **Stay In Loop, Get Out of Way** | Micromanage everything | Set guardrails, let agents work, review outputs |

---

## 4 Limiting Beliefs Busted

| ❌ Wrong Belief | ✅ Right Belief |
|---|---|
| "I'm not a coder, too technical" | If you can copy-paste text, you can set this up. One config file. No coding. |
| "AI agents are for big companies" | Smallest businesses benefit MOST — can't afford big teams. |
| "I'll set up later" | Every day you wait, competitors pull further ahead. 6 months in AI = 5 years in other industries. |
| "Hermes is just a chatbot" | Hermes sends messages, reads files, writes code, queries databases, calls APIs. That's not a chatbot. |

---

## Setup Guide

### Step 1: Install Hermes Agent
```bash
git clone https://github.com/crawlab-team/hermes
cd hermes
# Follow README install instructions
```

### Step 2: Install Codex (OpenAI)
```bash
# Install OpenAI Codex CLI
npm install -g @openai/codex
```

### Step 3: Connect via MCP (Model Context Protocol)
Create/edit the MCP config file:
```json
{
  "mcpServers": {
    "codex": {
      "command": "npx",
      "args": ["-y", "@openai/codex"]
    }
  }
}
```

### Step 4: Verify Connection
```
Ask Hermes: "Can you connect to Codex and write a simple Python script?"
```

### Step 5: Automate
- Connect GitHub MCP → Codex can push code
- Connect Stripe MCP → Codex can query payments
- Connect Database MCP → Codex can run queries
- Connect Slack MCP → Codex can send messages

---

## Key Tools

| Tool | Purpose | URL |
|------|---------|-----|
| Hermes Agent | AI brain + automation | https://github.com/crawlab-team/hermes |
| Codex | OpenAI coding agent | https://github.com/openai/codex |
| MCP | Tool connection protocol | https://modelcontextprotocol.io |
| GitHub MCP | Code management | GitHub MCP Server |
| Stripe MCP | Payment processing | Stripe MCP Server |

---

## Related

- [[post42-hermes-marketing-team-quickstart|Post #42: Hermes Marketing Team]]
- [[post41-hermes-agent-seo-quickstart|Post #41: Hermes Agent SEO]]
- [[post14-hermes-owl-alpha-quickstart|Post #14: Hermes + Owl Alpha]]
- [[Agent-OS-Ecosystem|Ecosystem: Hermes + Codex Stack]]
