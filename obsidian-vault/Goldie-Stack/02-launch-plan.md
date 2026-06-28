# Goldie Stack — Launch Plan

> Part of the [[00 - Index|Goldie Stack]] knowledge base.

## Prerequisites

- [ ] Agent OS Dashboard deployed (Post #1)
- [ ] OpenClaw running
- [ ] Docker and Docker Compose installed
- [ ] OpenRouter API key
- [ ] Traefik configured

## Day 1: Deploy

- [ ] Create vault: `mkdir -p /data/obsidian-vault`
- [ ] Navigate to `compose/goldie-stack/`
- [ ] Copy `.env.example` to `.env`, add API key
- [ ] `docker compose up -d`
- [ ] Verify both containers running
- [ ] Test Obsidian UI (port 8200)
- [ ] Test Memory Engine API (port 8100)

## Day 2: Configure Integration

- [ ] Verify Docker volume `obsidian-vault-data`
- [ ] Connect OpenClaw to vault
- [ ] Connect Hermes to vault
- [ ] Test Memory Engine indexing
- [ ] Verify Traefik routing

## Day 3: Test Persistence

- [ ] Create notes in Obsidian
- [ ] Wait for Memory Engine indexing
- [ ] Ask agent to find info from vault
- [ ] Test Jarvis Briefing
- [ ] Verify persistence after restart

## Week 1: Populate

- [ ] Create folder structure in Obsidian
- [ ] Set up daily notes template
- [ ] Set up memory capture workflow
- [ ] Import existing knowledge

## Week 2: Automate

- [ ] Daily briefings
- [ ] Auto-indexing
- [ ] Knowledge base workflows
- [ ] Custom templates

## Month 1: Scale

- [ ] Full knowledge base
- [ ] All agents connected
- [ ] Daily briefings running
- [ ] Backups configured

## Ongoing

- [ ] Back up vault weekly
- [ ] Monitor Memory Engine
- [ ] Add knowledge regularly
- [ ] Review and organize monthly

## Related

- [[01 - QuickStart Guide]]
- [[03 - Prompt Library]]

---

## Metadata

- Tags: `goldie-stack`, `launch-plan`, `timeline`
