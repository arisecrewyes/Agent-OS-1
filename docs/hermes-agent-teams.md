# Hermes Agent — Agent Teams Deep Dive

> Complete guide to running multi-agent teams with Hermes (Profiles, Telegram, Paperclipip, Hermes Workspace, Multica).
> Source: Julian Goldie SEO — Skool Post #5 (NEW section — not in Post #4)
> Related: [[hermes-quickstart]] | [[hermes-agent-capabilities-general]] | [[hermes-dashboard]]

---

## Overview

Hermes supports running **multiple agents working together** as a team. There are 5 distinct approaches, each suited to different needs:

| Method | Best For | Complexity |
|--------|----------|------------|
| **Profiles** | Multiple isolated agent personalities on one machine | Low |
| **Telegram Group Chat** | Collaborative agent conversations in a group | Low |
| **Paperclipip** | Running Paperclipip agent framework with Hermes | Medium |
| **Hermes Workspace** | Mission control dashboard for agent teams | Medium |
| **Multica** | Full multi-agent task assignment and orchestration | Medium-High |

> **Julian's recommendation:** For most people, you don't need agent teams. Set up Hermes normally, give it good memory, then explore teams if you need more power or want to experiment.

---

## Method 1: Profiles

Profiles let you run multiple isolated instances of Hermes on the same machine, each with its own configuration, model, and personality.

### Create a Profile
```bash
hermes profile create INSERTNAME
INSERTNAME setup
coder chat
```

Each profile is independent — different models, different memory, different use cases.

---

## Method 2: Telegram Group Chat

Connect two or more Hermes agents to the same Telegram group chat so they can collaborate.

### Setup Steps
1. During onboarding, use `hermes setup` to connect to Telegram
2. Edit Telegram settings to allow the bot to respond to anyone
3. Add both agents to a group chat together
4. Get them to chat with each other by tagging them

> **Tip:** You can also add an OpenClaw agent to the same group chat alongside Hermes agents.

---

## Method 3: Paperclipip

Paperclipip is an open-source agent framework from the Nous Research ecosystem, designed to orchestrate multiple AI agents working together.

- **GitHub:** https://github.com/NousResearch/hermes-paperclip-adapter

### Setup Steps
1. Get the Paperclipip GitHub URL
2. Inside your main Hermes agent, tell it to set up Paperclipip locally
3. Hermes will clone the repository, run the setup, and configure the agent team

### How It Works
- Paperclipip manages agent communication and task distribution
- Hermes acts as one of the agents in the Paperclipip network
- You get multiple agents working side-by-side, each handling different tasks

---

## Method 4: Hermes Workspace

Hermes Workspace provides a **mission control** interface for managing agent teams. It's a separate open-source project that adds a web-based dashboard for multi-agent orchestration.

- **GitHub:** https://github.com/outsourc-e/hermes-workspace

### Setup Steps
1. Start a new Hermes session
2. Tell Hermes to set up Hermes Workspace locally
3. Hermes will install and configure it (you may need to grant Docker permissions)

### Key Features
- Web-based mission control dashboard
- Multiple agents working alongside each other
- View agent status, logs, and progress in real-time
- Assign tasks to specific agents

### Post-Setup Navigation
Once running, go to the **Conductor** or **Operations** section to:
- View active agents
- Manage agent tasks
- Monitor agent communication

---

## Method 5: Multica

Multica is a dedicated multi-agent management platform that lets you assign tasks to agents and get them working together.

- **GitHub:** https://github.com/multica-ai/multica

### Setup Steps
1. Inside Hermes, ask Multica to set up locally
2. Multica will start Docker containers for its services
3. Access the Multica dashboard at `localhost` (specific port shown during setup)
4. Connect Hermes to Multica so you can interact with your Hermes agent through the Multica interface

### Key Features
- Full agent task assignment
- Multiple agent types (not just Hermes)
- Web-based management console
- Works alongside Paperclipip and Hermes Workspace

### Troubleshooting
- If any service isn't setting up correctly, paste the error into Multica and ask it to fix it
- Some services (like Multica) take a few minutes to fully start up — be patient during initial setup

---

## Running Multiple Methods Simultaneously

All five methods can run at the same time. Julian demonstrates this in the video:

```
Terminal Tab 1: Paperclipip (running + setting up)
Terminal Tab 2: Hermes Workspace (setting up Docker)
Terminal Tab 3: Multica (installing + Docker containers)
```

Then connect to Hermes through any of these:
- Direct terminal chat
- Hermes Workspace dashboard
- Multica dashboard at localhost
- Telegram group chat

---

## Important Configuration Note

> **When setting up agent teams, make sure you tell Hermes specifically to connect to Paperclip/Hermes Workspace/Multica.** Otherwise you won't be able to interact with Hermes inside those platforms.

---

## For VPS / Docker Users

The agent team tools (Paperclipip, Hermes Workspace, Multica) are designed for local development. On a VPS:
- **Profiles** work natively (just create multiple Hermes instances)
- **Telegram Group Chat** works well (connect via Hermes gateway)
- **Paperclipip / Hermes Workspace / Multica** can be deployed via Docker but require additional port configuration and Traefik routing
- The existing `docker-compose.yml` in the Hermes project uses a single agent profile — multi-agent setup would require additional configuration

---

## Related

- For the main Hermes capability reference: `hermes-agent-capabilities-general.md`
- For the Hermes Dashboard (v0.9): `hermes-dashboard.md`
- For the quickstart: `hermes-quickstart.md`
