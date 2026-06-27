# Hermes Agent — Commands Reference

> Complete CLI command reference for Hermes Agent.
> Source: Julian Goldie SEO — Skool Post #5 (NEW — expanded from Post #4)
> Related: [[hermes-quickstart]] | [[hermes-agent-capabilities-general]]

---

## Core Commands

| Command | What It Does |
|---------|-------------|
| `hermes` | Interactive CLI — start a conversation |
| `hermes model` | Choose your LLM provider and model |
| `hermes tools` | Configure which tools are enabled |
| `hermes config set` | Set individual config values |
| `hermes gateway` | Start the messaging gateway (Telegram, Discord, etc.) |
| `hermes setup` | Run the full setup wizard (configures everything at once) |
| `hermes update` | Update to the latest version |
| `hermes doctor` | Diagnose any issues |

## Migration & Troubleshooting Commands

| Command | What It Does |
|---------|-------------|
| `hermes claw migrate` | Migrate from OpenClaw (if coming from OpenClaw) |

## Agent Teams Commands

| Command | What It Does |
|---------|-------------|
| `hermes profile create <name>` | Create a new agent profile |
| `hermes dashboard` | Launch the Hermes Dashboard (v0.9+) |

## Non-Technical Setup

If you're not comfortable with the terminal:
1. Use **Claude Code** (or any AI coding tool)
2. Paste in the GitHub documentation URL
3. Say: "Set this up for me"
4. The AI tool will run all the commands for you

---

## Installation Command

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

---

## Version History

| Version | Key Features |
|---------|-------------|
| v0.9 | Dashboard, scheduled tasks, skills, multi-agent |
| v0.6 | Custom skills, scheduled tasks, external tools |

> Hermes is still pre-1.0. Julian notes: "This is the worst it's going to be — and it's already really good."

---

## Related

- For the main quickstart: `hermes-quickstart.md`
- For the Hermes Dashboard: `hermes-dashboard.md`
- For Agent Teams: `hermes-agent-teams.md`
- For One-Click Setups: `hermes-one-click-setups.md`
