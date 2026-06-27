# Goldie Stack — Launch Plan

> Structured timeline for deploying the Goldie Stack (Infinite Memory).
> Source: Julian Goldie SEO — Skool Post #2
> Related: [[goldie-stack-capabilities-general]] | [[goldie-stack-quickstart]]

---

## Prerequisites

- [ ] Agent OS Dashboard deployed (Post #1)
- [ ] OpenClaw running (for agent integration)
- [ ] Docker and Docker Compose installed
- [ ] OpenRouter API key configured
- [ ] Traefik configured for SSL

## Day 1: Deploy the Stack

- [ ] Create Obsidian vault directory: `mkdir -p /data/obsidian-vault`
- [ ] Navigate to `compose/goldie-stack/`
- [ ] Copy `.env.example` to `.env` and add API key
- [ ] Run `docker compose up -d`
- [ ] Verify both containers are running
- [ ] Test Obsidian Vault web UI (port 8200)
- [ ] Test Memory Engine API (port 8100)

## Day 2: Configure Integration

- [ ] Verify Docker volume `obsidian-vault-data` is created
- [ ] Connect OpenClaw agents to vault
- [ ] Connect Hermes Agent to vault
- [ ] Test Memory Engine can index vault content
- [ ] Verify Traefik routing for `obsidian.yourdomain.com`
- [ ] Verify Traefik routing for `memory.yourdomain.com`

## Day 3: Test Memory Persistence

- [ ] Create notes in Obsidian via web UI
- [ ] Wait for Memory Engine to index them
- [ ] Ask OpenClaw agent to find information from vault
- [ ] Ask Hermes Agent to generate a briefing from vault
- [ ] Verify notes persist after container restart
- [ ] Test vault access from multiple agents simultaneously

## Week 1: Populate & Organize

- [ ] Create organized folder structure in Obsidian
- [ ] Set up daily notes template
- [ ] Set up memory capture workflow
- [ ] Import existing knowledge into vault
- [ ] Test Jarvis Briefing feature (reads vault contents)

## Week 2: Automate

- [ ] Set up automated daily briefings
- [ ] Configure Memory Engine to index new notes automatically
- [ ] Set up knowledge base workflows
- [ ] Create custom templates in Obsidian

## Month 1: Scale

- [ ] Full knowledge base populated
- [ ] All agents connected to vault
- [ ] Daily briefings running
- [ ] Memory persistence verified across restarts
- [ ] Backups configured for vault data

## Ongoing

- [ ] Back up vault data weekly
- [ ] Monitor Memory Engine health
- [ ] Add new knowledge to vault regularly
- [ ] Review and organize vault contents monthly
