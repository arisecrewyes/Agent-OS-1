# OpenClaw — Skills & Plugins

> Part of the [[00 - Index|OpenClaw 6 Hour Course]] knowledge base.

## What Are Skills?

Skills are plugins that extend OpenClaw's functionality. Each skill adds new capabilities — think of them like apps for your phone. You only install what you need.

## Installing Skills

```bash
claudebot skills install <skill-name>
```

If a skill doesn't install via CLI, try:
- Restart gateway first: `claudebot gateway restart`
- Install manually from ClawHub marketplace

## Recommended Skills

### Content & Publishing
| Skill | Purpose | Use Case |
|-------|---------|----------|
| **WordPress** | Publish blog posts directly | SEO content, automated publishing |
| **Notion** | Create and update notes | Knowledge base, project management |
| **Bird** | Post to Twitter/X | Social media automation |
| **GitHub** | Manage repos, issues, PRs | Code management, CI/CD |

### Communication
| Skill | Purpose | Use Case |
|-------|---------|----------|
| **Email** | Manage inbox | Automated email handling (use with caution) |
| **SMS** | Send text messages | Alerts, notifications |

### Development & Deployment
| Skill | Purpose | Use Case |
|-------|---------|----------|
| **Netlify** | Deploy websites | Landing pages, static sites |
| **Remotion** | Create videos | Automated video generation |
| **Browser Control** | Automate web tasks | Scraping, form filling, navigation |

### Media & AI Generation
| Skill | Purpose | Use Case |
|-------|---------|----------|
| **11 Labs** | Voice generation | Voice notes, audio content |
| **HeyGen** | Avatar videos | AI spokesperson videos |
| **Nano Banana / AI Studio** | Image generation | Thumbnails, featured images |

### Infrastructure
| Skill | Purpose | Use Case |
|-------|---------|----------|
| **Sub-Agents** | Spawn parallel workers | Parallel task execution |
| **Cron Jobs** | Schedule automations | Recurring tasks, reports |

## Important Notes on Skills

- **Start with 3-5 essential skills** — don't install everything at once
- **Test skills with non-critical tasks first** before using them in production
- **Some skills require additional setup** — API keys, account credentials, OAuth flows
- **Skills can interact** — e.g., WordPress skill + 11 Labs = audio blog posts published automatically

## Finding More Skills

- **ClawHub:** Marketplace for OpenClaw skills
- **GitHub:** Community-contributed skills
- **Community Discord:** Users share custom skills

---

## Metadata

- Tags: `openclaw`, `skills`, `plugins`, `extensions`
- Related: [[06 - Practical Use Cases]] | [[07 - Advanced Features]]
