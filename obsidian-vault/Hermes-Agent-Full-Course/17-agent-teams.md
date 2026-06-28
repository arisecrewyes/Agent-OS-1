# Hermes — Agent Teams Deep Dive

> Complete guide to running multi-agent teams with Hermes (Profiles, Telegram, Paperclipip, Hermes Workspace, Multica).
> Source: Julian Goldie SEO — Skool Post #5
> Related: [[14 - QuickStart Guide]] | [[00 - Index]]

---

## 5 Methods for Agent Teams

### 1. Profiles
```bash
hermes profile create INSERTNAME
INSERTNAME setup
coder chat
```
Each profile = isolated agent with own config, model, personality.

### 2. Telegram Group Chat
1. Use `hermes setup` to connect to Telegram
2. Edit Telegram settings → respond to anyone
3. Add multiple agents to a group chat
4. Tag agents to make them chat with each other
> Can also add OpenClaw to the same group.

### 3. Paperclipip
- GitHub: https://github.com/NousResearch/hermes-paperclip-adapter
- Agent framework from Nous Research ecosystem
- Hermes clones repo, runs setup, configures agent team

### 4. Hermes Workspace
- GitHub: https://github.com/outsourc-e/hermes-webspace
- Mission control web dashboard for multi-agent orchestration
- Go to Conductor/Operations to manage agents

### 5. Multica
- GitHub: https://github.com/multica-ai/multica
- Multi-agent task assignment platform
- Runs in Docker containers
- Access dashboard at localhost

> **Tip:** Tell Hermes specifically to connect to Paperclip/Workspace/Multica, or you can't interact with Hermes inside them.
