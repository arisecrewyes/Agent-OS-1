# Goldie Stack — QuickStart Guide

> Part of the [[00 - Index|Goldie Stack]] knowledge base.

## What You're Building

Three components that give your Agent OS **infinite memory**:
1. **Obsidian Vault** — Web-based knowledge storage
2. **Memory Engine** — Python service that indexes vault content
3. **Hermes Agent** — Self-improving AI that reads the vault

## Step 1: Create Vault Directory

```bash
mkdir -p /data/obsidian-vault
```

## Step 2: Deploy the Stack

```bash
cd compose/goldie-stack
cp .env.example .env
# Edit .env with your OpenRouter API key
docker compose up -d
```

This deploys:
- **Obsidian Vault** (port 8200)
- **Memory Engine** (port 8100)

## Step 3: Verify

```bash
# Check containers
docker ps | grep goldie

# Test Obsidian Vault
curl http://localhost:8200

# Test Memory Engine
curl http://localhost:8100
```

## Step 4: Connect Agents

The vault is shared across the Agent OS network:
- **OpenClaw** agents can read/write notes
- **Hermes Agent** reads for Jarvis Briefing
- **Memory Engine** indexes for semantic search

## Step 5: Test Persistence

1. Create a note in Obsidian via web UI
2. Ask an agent about the note
3. Notes persist after container restart

## Environment Variables

```bash
OPENROUTER_API_KEY=your_key
LLM_MODEL=openrouter/owl-alpha
```

## Troubleshooting

- **Vault not accessible:** Check Docker volume
- **Memory Engine errors:** Verify API key in `.env`
- **Obsidian UI not loading:** Check Traefik routing

## Related

- [[02 - Launch Plan]]
- [[03 - Prompt Library]]

---

## Metadata

- Tags: `goldie-stack`, `quickstart`, `obsidian`, `memory-engine`, `hermes`
