# Agent OS Base — Launch Plan

> Structured timeline for building and deploying Agent OS.
> Source: Julian Goldie SEO — Skool Post #1
> Related: [[agentos-base-capabilities-general]] | [[agentos-base-quickstart]]

---

## Day 1: Build the Dashboard

- [ ] Install Claude Code (free at claude.ai/code)
- [ ] Install Node.js 22.16+ (or 24)
- [ ] Paste Prompt 1 into Claude Code → Dashboard created
- [ ] Paste Prompt 2 → Per-agent pages added
- [ ] Paste Prompt 3 → Voice input added
- [ ] Access dashboard at `http://localhost:3000`
- [ ] Verify it looks good and is functional

## Day 2: Add Persistence

- [ ] Install Obsidian and create a vault
- [ ] Paste Prompt 4 → Auto-save to Obsidian
- [ ] Paste Prompt 5 → Goals + Journal pages
- [ ] Test that chats save to Obsidian vault

## Day 3: Connect Agents

- [ ] Install OpenClaw (`npm install -g openclaw@latest`)
- [ ] Run `openclaw onboard --install-daemon`
- [ ] Connect Claude API key
- [ ] Install Hermes Agent
- [ ] Verify all agents show LIVE in the dashboard

## Week 1: Customize & Stabilize

- [ ] Fix any bugs by describing them to Claude (Prompt 6)
- [ ] Make it portable with config file (Prompt 7)
- [ ] Set up on your VPS with Docker (see Version 2 compose files)
- [ ] Configure Traefik for SSL
- [ ] Test voice input in the browser

## Week 2: Automate

- [ ] Set up first scheduled task in OpenClaw
- [ ] Connect Telegram to OpenClaw
- [ ] Test agent communication via Connector Router
- [ ] Set up Obsidian vault on persistent Docker volume

## Week 3: Scale

- [ ] Add more agents (Hermes, Content Creator, etc.)
- [ ] Set up Memory Engine
- [ ] Configure Jarvis Voice (ElevenLabs)
- [ ] Set up PaperclipIP for multi-agent hierarchy

## Month 1: Mastery

- [ ] All agents connected and showing LIVE
- [ ] Daily briefings working
- [ ] Goals and Journal syncing to Obsidian
- [ ] Voice input functional
- [ ] SSL configured and accessible from domain
- [ ] Backups running

## Ongoing

- [ ] Check for Agent OS updates (use `Update Agent OS.command`)
- [ ] Add new agents as needed
- [ ] Review and optimize agent performance
- [ ] Back up Obsidian vault regularly
