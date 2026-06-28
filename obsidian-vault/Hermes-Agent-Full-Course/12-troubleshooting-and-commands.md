# Hermes Agent — Troubleshooting & Commands Reference

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Troubleshooting

### Problem: Hermes stops responding or gets stuck
**Cause:** Context window grew too big.

**Fix in terminal:**
1. Press `Ctrl+C` to stop
2. Type `hermes` to restart

**Fix in Telegram:**
- Type `/new` to start a new conversation
- Or type `/restart`

### Problem: Something breaks in the Telegram gateway
**Fix:** Open a second Hermes instance in terminal and troubleshoot from there. The terminal instance can diagnose and fix issues with the Telegram instance.

### Problem: Context getting too large during long sessions
**Fix:**
- Use `/compress` to compress the context
- Or `/new` to start fresh
- **Memory persists across sessions** so you do not lose anything

## Essential Commands Reference

### Core Commands
| Command | Purpose |
|---------|---------|
| `hermes` | Start chatting in terminal |
| `hermes setup` | Run the full setup wizard |
| `hermes model` | Switch your AI model |
| `hermes tools` | Configure which tools are enabled |
| `hermes doctor` | Diagnose issues |
| `hermes --version` | Check version |
| `hermes update` | Update to latest version |

### Gateway Commands
| Command | Purpose |
|---------|---------|
| `hermes gateway setup` | Set up messaging platforms |
| `hermes gateway start` | Start the messaging gateway |

### Skills Commands
| Command | Purpose |
|---------|---------|
| `hermes skills browse` | Browse available skills |
| `hermes skills install [name]` | Install a skill library |

### Profile Commands
| Command | Purpose |
|---------|---------|
| `hermes profile create [name]` | Create a new agent profile |
| `hermes profile list` | List all profiles |

### Migration Commands
| Command | Purpose |
|---------|---------|
| `hermes claw migrate` | Migrate from OpenClaw |
| `hermes claw migrate --dry-run` | Preview migration |

### MCP Commands
| Command | Purpose |
|---------|---------|
| `hermes mcp serve` | Run Hermes as MCP server |

### In-Chat Commands
| Command | Purpose |
|---------|---------|
| `/new` or `/reset` | Start a fresh conversation |
| `/compress` | Compress context to save tokens |
| `/usage` | Check token usage |
| `/skills` | Browse installed skills |
| `/stop` | Kill the current agent run |
| `/retry` | Retry the last turn |
| `/undo` | Undo the last turn |

---

## Metadata

- Tags: `hermes`, `troubleshooting`, `commands`, `reference`
- Related: [[01 - Installation & Setup]] | [[03 - Messaging Platforms]]
