# Goldie Stack — QuickStart Guide

> Step-by-step walkthrough to deploy the Goldie Stack (Infinite Memory).
> Source: Julian Goldie SEO — Skool Post #2
> Related: [[goldie-stack-capabilities-general]] | [[00 - Index]]

---

## What You're Building

The Goldie Stack adds **infinite memory** to your Agent OS:
1. **Obsidian Vault** — Persistent knowledge storage
2. **Memory Engine** — Indexes and serves vault content via API
3. **Hermes Agent** — Self-improving AI agent that reads the vault

## Step 1: Create the Obsidian Vault Directory

```bash
mkdir -p /data/obsidian-vault
```

This will be mounted into multiple containers via Docker volume.

## Step 2: Deploy the Goldie Stack Compose

```bash
cd compose/goldie-stack
cp .env.example .env
# Edit .env with your OpenRouter API key
docker compose up -d
```

This deploys:
- **Obsidian Vault** (port 8200) — Web-based Obsidian access
- **Memory Engine** (port 8100) — Python service that indexes the vault

## Step 3: Verify the Stack

```bash
# Check containers are running
docker ps | grep goldie

# Test Obsidian Vault
curl http://localhost:8200

# Test Memory Engine
curl http://localhost:8100
```

## Step 4: Connect Agents to the Vault

The Obsidian vault is shared across the Agent OS network:
- **OpenClaw** agents can read/write Obsidian notes
- **Hermes Agent** reads the vault for Jarvis Briefing
- **Memory Engine** indexes vault content for semantic search

## Step 5: Test Memory Persistence

1. Create a note in Obsidian via the web UI
2. Ask an AI agent about the note's content
3. The agent should be able to find and reference it

## Environment Variables

```bash
OPENROUTER_API_KEY=your_key_here
LLM_MODEL=openrouter/owl-alpha
```

## Troubleshooting

- **Vault not accessible:** Check Docker volume is mounted correctly
- **Memory Engine errors:** Verify API key in `.env`
- **Obsidian UI not loading:** Check Traefik routing and SSL config

---

## Related

- For the full capability reference: `goldie-stack-capabilities-general.md`
- For the timeline: `goldie-stack-launch-plan.md`
- For prompts: `goldie-stack-prompts.md`
