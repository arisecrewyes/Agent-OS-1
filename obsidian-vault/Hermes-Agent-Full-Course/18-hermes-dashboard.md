# Hermes — Dashboard (v0.9)

> Mission control web interface built into Hermes Agent.
> Source: Julian Goldie SEO — Skool Post #5
> Related: [[14 - QuickStart Guide]] | [[00 - Index]]

---

## Launch

```bash
hermes dashboard
```

Opens a localhost URL with full mission control.

## Sections

### Overview
- Recent sessions
- Live session monitoring
- Token usage analytics
- Activity logs

### ⏰ Scheduled Tasks (Cron Jobs)
- Daily automations running 24/7 autonomously
- Researching news, posting content, messaging team
- Manage from dashboard

### 🧩 Skills Manager
- Individual experts you can call upon anytime
- Saved automations on demand
- Toggle on/off, delete, reactivate

### ⚙️ Config
- Change models (LLM provider switching)
- Manage agents
- Terminal settings
- Delegation (route different tasks to different models)
- Memory settings, compression
- Voice (text-to-speech, speech-to-text)

### 🔑 API Keys
- Manage all API keys in one place
- See configured models

## Scheduled Tasks vs Skills
| | Scheduled Tasks | Skills |
|---|---|---|
| **When** | 24/7 automatically | On-demand |
| **Use case** | Recurring automations | One-off expert tasks |
| **Example** | Daily news + post | Publish article |

## For VPS Users
- Runs inside Hermes Docker container
- Need SSH tunnel or Traefik route for external access
- Not exposed by default in existing compose
