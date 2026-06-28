# Hermes Agent — Multi-Agent Profiles

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## What Are Profiles?

Profiles let you run **multiple fully isolated Hermes instances** from one installation (v0.6+).

Each profile has its own:
- Config
- API keys
- Memory
- Sessions
- Skills
- Gateway

They **do not bleed into each other**.

## Managing Profiles

### Create a Profile
```bash
hermes profile create [name]
```

### Examples
```bash
hermes profile create twitter-agent
hermes profile create research-agent
hermes profile create content-writer
```

### Clone a Profile
```bash
hermes profile create research-agent --clone
```

### List Profiles
```bash
hermes profile list
```

## Per-Profile Commands

Once created, each profile becomes its own command:

```bash
twitter-agent chat
twitter-agent setup
twitter-agent gateway start
research-agent chat
research-agent setup
```

## Export and Import

You can **export and import profiles**:
- Share agent setups with others
- Move profiles to another machine
- Backup configurations

## Use Case Examples

| Profile | Purpose | Model |
|---------|---------|-------|
| **twitter-agent** | Social media management | Qwen 3.6 (free) |
| **research-agent** | Web research & monitoring | Claude Opus (paid) |
| **content-writer** | Blog & SEO content | ChatGPT CodeX |

Each runs independently with its own memory and skills, but shares the same installation.

---

## Metadata

- Tags: `hermes`, `profiles`, `multi-agent`, `isolated-instances`
- Related: [[01 - Installation & Setup]] | [[10 - OpenClaw Migration]]
