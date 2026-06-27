# Hermes Agent — Dashboard (v0.9)

> Complete guide to the Hermes Dashboard: mission control, scheduled tasks, skills, config, and API key management.
> Source: Julian Goldie SEO — Skool Post #5 (NEW section — not in Post #4)
> Related: [[hermes-agent-capabilities-general]] | [[hermes-agent-teams]] | [[hermes-quickstart]]

---

## Overview

As of **Hermes v0.9**, there is a built-in **web dashboard** that provides a full mission control interface for managing your Hermes agents. This is separate from Hermes Workspace (which is a third-party project) — the dashboard is built directly into Hermes.

> **Note:** Hermes is still pre-1.0 (currently v0.9). The dashboard is already powerful, and will only get better with the v1.0 release.

---

## Launch The Dashboard

```bash
hermes dashboard
```

This gives you a **localhost URL** that you can open in your browser.

---

## Dashboard Sections

### 📊 Overview / Home
- Recent sessions
- Live session monitoring
- Token usage analytics
- Activity logs

### ⏰ Scheduled Tasks (Cron Jobs)
Daily automations that run **24/7 autonomously without you**.

Examples:
- Researching and posting content
- Messaging your team with updates
- Checking analytics and sending reports
- Any recurring task you want running on autopilot

### 🧩 Skills Manager
Skills are **individual experts** that you can call upon anytime. They are:
- Saved automations you can invoke when needed
- Like having a specialist on speed dial
- Can be toggled on/off from the dashboard
- Can be deleted or reactivated anytime

**Example:** An SEO skill that creates content, publishes it, and indexes it — you call it when you need it.

### ⚙️ Config
From the dashboard config panel you can:
- **Change models** — switch between LLM providers
- **Manage agents** — view all agent instances
- **Terminal settings** — configure display and behavior
- **Delegation** — set up model delegation (route different tasks to different models)
- **Memory settings** — compression, browser setup
- **Voice** — enable text-to-speech and speech-to-text

### 🔑 API Keys
- Manage all your API keys in one place
- See which models are configured
- Add or remove providers

---

## Scheduled Tasks vs Skills

| Feature | Scheduled Tasks | Skills |
|---------|----------------|--------|
| **When it runs** | 24/7 automatically | On-demand when you call it |
| **Use case** | Recurring automations | One-off expert tasks |
| **Example** | Daily news research + post | Publish a new article |
| **Analogy** | An employee on a schedule | A specialist you call when needed |

---

## Dashboard Technical Details

- **Access:** `localhost` URL (shown when you run `hermes dashboard`)
- **Version:** Available from Hermes v0.9+
- **Protocol:** Local web server (HTTP)
- **No cloud dependency:** Everything runs locally

---

## For VPS / Docker Users

The Hermes Dashboard is designed for **local access**. On a VPS:
- Running `hermes dashboard` inside a Docker container exposes a port
- You would need to either:
  1. Access it via SSH tunnel: `ssh -L 3000:localhost:3000 user@vps`
  2. Expose the port via Traefik (add a route in your `docker-compose.yml`)
- The existing Hermes compose project does NOT expose the dashboard port by default

---

## Related

- For agent teams: `hermes-agent-teams.md`
- For the main capability reference: `hermes-agent-capabilities-general.md`
- For the quickstart: `hermes-quickstart.md`
