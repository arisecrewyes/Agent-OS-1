# Skool Post #29: Automation Blueprints

> **Source:** https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=6c37ee39c3604e73aa791d74fae3462f
> **Date:** June 11th
> **Author:** AI Profit Lab / Dan B

## Overview

Hermes is a free, open source AI agent by Nous Research. It runs on your computer, a cheap $5 server, or in the cloud. You can talk to it from Telegram, Discord, Slack, WhatsApp or the terminal.

This post covers 5 automation blueprints you can set up today.

**Links:**
- Documentation: https://hermes-agent.nousresearch.com/docs/guides/automation-templates
- GitHub: https://github.com/NousResearch/hermes-agent

---

## Step 0: Install Hermes

**Mac, Linux or WSL2:**
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Then run `hermes setup` to pick your model and add API keys.

Want to skip collecting 5 different API keys? Run `hermes setup --portal` and one Nous Portal subscription covers models, web search, image generation and more.

---

## Blueprint 1: The Daily Report Bot

Hermes has a built-in cron scheduler. You write the schedule in plain English. It runs unattended and delivers to any platform.

**Examples:**
- "Every morning at 7am, check my niche for news and send me a summary on Telegram"
- "Every Friday at 5pm, audit my project folder and send a weekly report"
- "Every night at midnight, back up my notes folder"

Just tell Hermes what you want scheduled. It sets up the cron job for you.

---

## Blueprint 2: The Telegram Assistant

Run Hermes on a server, then message it like a friend.

1. Run `hermes gateway setup` and add your Telegram bot token
2. Run `hermes gateway start`
3. Message your bot from anywhere

It also works with Discord, Slack, WhatsApp and Signal. You can even send voice memos and it transcribes them. Your agent keeps working on the server while you're out.

---

## Blueprint 3: The Agent Team (Profiles)

You can run multiple separate agents on one machine. Each one gets its own memory, personality and settings.

```bash
hermes profile create coder
hermes profile create research
hermes profile create assistant
```

Each profile becomes its own command. So `coder chat` talks to your coding agent. `research chat` talks to your research agent.

Give each one a personality by editing its SOUL.md file:

```bash
echo "You are a focused coding assistant." > ~/.hermes/profiles/coder/SOUL.md
```

Each profile can run its own bot too. So you can have a coding bot on Discord and a personal assistant on Telegram, both running 24/7.

---

## Blueprint 4: The Self-Improving Agent (Skills)

This is the big one. Hermes has a learning loop:
- It creates its own skills after finishing complex tasks
- It improves those skills while using them
- It remembers things about you across sessions
- It can search its own past conversations

So the more you use it, the better it gets at YOUR workflows. You can also browse ready-made skills at the Skills Hub or type `/skills` to see what's installed.

---

## Blueprint 5: The Parallel Worker (Subagents)

For big jobs, Hermes can spawn isolated subagents that work in parallel. Example: one subagent researches, one writes, one reviews. All at the same time.

It can also write Python scripts that call its own tools, collapsing a 10-step process into one step.

---

## Bonus: Run It For Almost Free

Hermes supports serverless backends like Modal and Daytona. Your agent's environment goes to sleep when idle and wakes up when you message it. It costs nearly nothing between sessions.

---

## Quick Command Cheat Sheet

| Command | Description |
|---------|-------------|
| `hermes` | Start chatting |
| `hermes model` | Pick your AI model |
| `hermes gateway` | Start the messaging bot |
| `hermes doctor` | Fix problems |
| `hermes update` | Get the latest version |
| `/new` | Fresh conversation |
| `/skills` | See your skills |

---

## Key Takeaways

1. **One agent, many interfaces** — Talk via Telegram, Discord, Slack, WhatsApp, or terminal
2. **Cron-native scheduling** — Plain English recurring tasks, zero config
3. **Multi-agent via profiles** — Separate personalities, memories, and bots per profile
4. **Self-improving** — Skills auto-create and get better over time
5. **Parallel subagents** — Fan out big jobs across isolated workers
6. **Cheap to run** — Serverless backends (Modal/Daytona) sleep when idle
