# OpenClaw — Installation & Setup

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## Requirements

- **Node.js** version 22 or higher
- A computer (Mac/Windows/Linux) or VPS
- API key for your chosen AI provider (Claude, ChatGPT, or local models)
- Basic command-line familiarity

## Installation

### Step 1: Install OpenClaw

```bash
npm install -g claudebot@latest
```

> **Note:** The package name is `claudebot` on npm. The project is called "OpenClaw" on GitHub.

### Step 2: Run Onboarding

```bash
claudebot onboard-install-daemon
```

This launches the setup wizard which will guide you through:
- Choosing your AI provider
- Entering your API key
- Selecting messaging channels
- Installing skills (optional plugins)

### Step 3: Follow the Setup Wizard

During onboarding, you will:

1. **Choose your AI provider** — Claude Opus, ChatGPT CodeX, Ollama, or others
2. **Enter your API key** — stored securely for gateway use
3. **Select messaging channels** — Telegram, WhatsApp, Discord, Slack, etc.
4. **Install skills** — optional plugins for extended functionality

### Step 4: Verify Installation

```bash
claudebot doctor
```

This checks that everything is configured correctly and the gateway is running.

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm install -g claudebot@latest` | Install/update OpenClaw |
| `claudebot onboard-install-daemon` | Run setup wizard |
| `claudebot doctor` | Verify installation & health |
| `claudebot gateway restart` | Restart the gateway service |
| `claudebot skills install <name>` | Install a skill/plugin |

## Gateway Management

The gateway is the core service that connects your messaging apps to the AI provider. Key operations:

- **Start:** Handled by the daemon installed during onboarding
- **Restart:** `claudebot gateway restart` (useful after config changes or skill installs)
- **Status:** `claudebot doctor` includes gateway health check

## Post-Installation Checklist

- [ ] `claudebot doctor` reports healthy
- [ ] Gateway is running and accessible
- [ ] Messaging app (Telegram/WhatsApp/etc.) is connected
- [ ] API key is configured and working
- [ ] Test message sends and receives successfully
- [ ] Skills installed (if needed)

---

## Metadata

- Tags: `openclaw`, `installation`, `setup`, `gateway`
- Related: [[02 - AI Provider Selection]] | [[03 - Messaging Integration]] | [[05 - Security Best Practices]]
