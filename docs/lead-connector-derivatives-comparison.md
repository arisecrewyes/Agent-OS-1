# Lead Connector Derivatives — Platform Comparison Guide

> Comprehensive comparison of GoHighLevel, LeadConnector, GoStackBase, and BuildwithOS — all derived from the Lead Connector platform.
> Source: Julian Goldie SEO — Skool Post #6 + platform documentation research
> Related: [[landing-pages-websites-sop]] | [[highlevel-funnels-reference]] | [[hermes-agent-teams]]

---

## What Are Lead Connector Derivatives?

All four platforms in this guide are **derivatives of the original Lead Connector (LC) platform**. They share the same core architecture (CRM, funnels, automations, email/SMS marketing) but each has customized the platform for different audiences and use cases.

### Platform Lineage

```
Lead Connector (Original Platform)
├── GoHighLevel (GHL) — The most popular fork, full-featured SaaS for agencies
├── LeadConnector (LC) — The original platform, now a separate entity
├── GoStackBase — Fork optimized for digital product businesses
└── BuildwithOS — Fork with AI-first approach, highest affiliate payouts
```

---

## Platform Comparison Matrix

| Feature | GoHighLevel (GHL) | LeadConnector (LC) | GoStackBase | BuildwithOS |
|---------|-------------------|--------------------|-----------|-------------|
| **Best For** | Agencies, marketers | Agencies, local businesses | Digital product businesses | AI-first entrepreneurs |
| **CRM** | ✅ Full | ✅ Full | ✅ Smart CRM + Pipelines | ✅ Full |
| **Funnels/Websites** | ✅ Full builder | ✅ Full builder | ✅ Landing pages + sites | ✅ Full builder |
| **Email Marketing** | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| **SMS Marketing** | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| **Automations** | ✅ Workflow builder | ✅ Workflow builder | ✅ Revenue-generating automations | ✅ AI-powered automations |
| **AI Agents** | ✅ AI Employee | ✅ AI features | ❌ Limited | ✅ AI voice & chat agents |
| **AI Phone Calls** | ✅ | ✅ | ❌ | ✅ (Platinum plan) |
| **White-Label** | ✅ (higher plans) | ✅ | ❌ | ✅ (Partner plan) |
| **API Access** | ✅ V2 REST API | ✅ REST API | ✅ API access (Premium+) | ✅ MCP + REST API |
| **Webhooks** | ✅ 50+ events | ✅ | ✅ | ✅ |
| **Calendar** | ✅ | ✅ | ✅ | ✅ + Google Calendar sync |
| **Payments** | ✅ | ✅ | ❌ | ✅ |
| **Course/LMS** | ✅ | ✅ | ✅ (digital products) | ✅ |
| **Client Portal** | ❌ | ❌ | ✅ All-in-one portal | ❌ |
| **Project Management** | ❌ | ❌ | ❌ | ✅ (BuildOS Ontology) |
| **Daily Briefs** | ❌ | ❌ | ❌ | ✅ AI-generated |
| **Affiliate Payout** | Standard | Standard | Standard | **Highest** (up to 50% tier 1) |
| **Free Trial** | ✅ 14 days | ✅ | ❌ (paid plans only) | ✅ 14 days (Pro) |
| **Starting Price** | $97/mo | $97/mo | $79/mo | $97/mo |

---

## GoHighLevel (GHL) — Deep Dive

### Overview
The most popular Lead Connector derivative. Built for **marketing agencies** who need to manage multiple client accounts from one platform.

### Key Features
- **Full CRM** with custom fields, tags, pipelines
- **Funnel & Website Builder** (drag-and-drop)
- **Email & SMS Marketing** with templates
- **Workflow Automations** (trigger-based)
- **AI Employee** (AI agent for customer interactions)
- **Phone System** (LC Phone)
- **Payments & Invoicing**
- **Course/LMS** module
- **White-label** (on higher plans)
- **Marketplace** for apps and integrations

### API
- **V2 REST API** (V1 deprecated Dec 2025)
- **Base URL:** `https://services.leadconnectorhq.com/`
- **Auth:** OAuth 2.0 or Private Integration Token
- **Rate Limits:** 100 req/10s burst, 200,000/day
- **Webhooks:** 50+ event types
- **Docs:** https://marketplace.gohighlevel.com/docs/

### Pricing Tiers
| Plan | Price | Key Features |
|------|-------|-------------|
| Starter | $97/mo | Basic API, core features |
| Unlimited | $297/mo | More contacts, locations |
| Agency Pro | $497/mo | Advanced API, OAuth, agency keys |
| SaaS | $497/mo | White-label, rebranding |

### API Endpoints (V2)
| Category | Endpoints |
|----------|-----------|
| **Contacts** | CRUD, tags, custom fields |
| **Conversations** | SMS, email, calls |
| **Calendar** | Appointments, bookings |
| **Opportunities** | Sales pipeline, deals |
| **Payments** | Transactions, subscriptions |
| **Workflows** | Trigger-based automations |
| **Webhooks** | 50+ event types |

---

## LeadConnector (LC) — Deep Dive

### Overview
The **original platform** that GoHighLevel forked from. Still actively maintained with its own feature set. Popular with local businesses and agencies.

### Key Features
- Nearly identical feature set to GoHighLevel
- **Phone System** (LC Phone — the original)
- **Funnels, CRM, Email, SMS, Automations**
- **API V2** with OAuth 2.0
- **Developer community** (Slack, GitHub)

### API
- **Base URL:** `https://services.leadconnectorhq.com/`
- **Auth:** OAuth 2.0 or Private Integration Token
- **Docs:** https://help.leadconnectorhq.com/support/home
- **Developer Portal:** https://developers.gohighlevel.com/

### Key Differences from GHL
- LC Phone system is the original (GHL licensed it)
- Slightly different UI/EX
- Same API base URL (shared infrastructure)
- Independent development roadmap

---

## GoStackBase — Deep Dive

### Overview
A Lead Connector derivative **optimized for digital product businesses** (courses, memberships, SaaS). Focuses on **client portals** and **revenue-generating automations**.

### Key Features
- **All-in-One Client Portal** — each client gets their own branded hub
- **Smart CRM & Sales Pipelines** — track leads, deals, conversations
- **Lead Capture & Conversion Engine** — forms, surveys, landing pages, chat widgets
- **Revenue-Generating Automations** — email, SMS, voice, chat nurturing
- **15-Minute Setup Kits** — pre-built templates and workflows
- **Unified Dashboard** — marketing, sales, service metrics in one view
- **Team Collaboration** — team roles and permissions

### Pricing
| Plan | Price | Key Features |
|------|-------|-------------|
| Starter | $79/mo (yr) | 5K contacts, 5 team members, 10 templates |
| Premium | $119/mo (yr) | Unlimited contacts, API access, 50+ templates |
| Elite | $239/mo (yr) | White-label, dedicated manager, custom integrations |

### API
- Available on **Premium and Elite plans**
- REST API for contacts, automations, CRM
- Webhooks support

### Key Differences from GHL
- **Client Portal** is the killer feature (GHL doesn't have this)
- **15-minute setup kits** for fast deployment
- **No AI agents** or phone system
- **Lower starting price** ($79 vs $97)
- **No marketplace** ecosystem

---

## BuildwithOS — Deep Dive

### Overview
The most **AI-forward** Lead Connector derivative. Positions itself as an "AI-powered business operating system" with the **highest affiliate payouts** in the ecosystem.

### Key Features
- **AI Voice & Chat Agents** — human-like voices, 24/7 inbound/outbound
- **Pre-Built Business Kit** — done-for-you funnels, campaigns, templates
- **AI Phone Calls** (Platinum plan) — automated outbound/inbound
- **White-Label Brand Partner** — rebrand the entire platform
- **Custom ChatGPT ("Rocky")** — your own branded AI assistant
- **Project Management Boards** — built-in PM
- **Team Chat** — internal team communication
- **Full Academy** — training and game plans
- **AI Group Chat** — community of entrepreneurs

### Pricing
| Plan | Price | Key Features |
|------|-------|-------------|
| Pro | $97/mo | All features, click-by-click training, 40% tier 1 affiliate |
| Partner | $297/mo | Pre-built kit, AI chat, white-label, 45% tier 1 + 5% tier 2 |
| Platinum | $497/mo | AI phone calls, 3-tier payouts (50/30/10%), custom kit |
| Done For You | $1,997/mo | Full done-for-you setup by their team |

### API & Integrations
- **MCP (Model Context Protocol)** support at `/mcp/buildos`
- **REST API** at `https://build-os.com/api/agent-call/buildos`
- **Agent Key system** with per-project scope and per-op write whitelist
- **Works with:** Claude Code, OpenClaw, ChatGPT, Codex, Cursor, Claude Desktop
- **Google Calendar** integration
- **OAuth 2.0** for cloud clients
- **JSON-RPC gateway** for custom integrations

### BuildOS Ontology (How It Structures Work)
| Entity | What It Is |
|--------|-----------|
| **Project** | Root work unit (contains everything) |
| **Task** | Actionable item with clear outcome |
| **Plan** | Grouping of tasks with timeline |
| **Document** | Project knowledge (specs, research, decisions) |
| **Goal** | Strategic objective |
| **Milestone** | Time-based progress marker |
| **Risk** | Known issue with mitigation |
| **Event** | Calendar item linked to work |
| **Member** | Person on the project with role |
| **Asset** | File, image, or diagram (OCR'd) |

### Key Differences from GHL
- **AI-first** (voice agents, chat agents, phone calls)
- **Project management** built-in (GHL doesn't have this)
- **Daily briefs** (AI-generated morning summaries)
- **Highest affiliate payouts** (up to 50% tier 1)
- **MCP support** for external agent connections
- **No CRM** in the traditional sense (uses project ontology instead)
- **Different philosophy:** BuildOS is a "thinking environment," GHL is a "marketing platform"

---

## Choosing the Right Platform

| If You Need... | Choose |
|----------------|--------|
| Full marketing suite for agencies | **GoHighLevel** |
| Client portals for digital products | **GoStackBase** |
| AI agents + phone calls + project management | **BuildwithPlatform** |
| Original platform with phone system | **LeadConnector** |
| Highest affiliate income | **BuildwithOS** |
| Lowest entry price | **GoStackBase** ($79/mo) |
| Best ecosystem/marketplace | **GoHighLevel** |
| AI voice/chat agents | **BuildwithOS** |

---

## Related

- For the SOP: `landing-pages-websites-sop.md`
- For funnel templates: `highlevel-funnels-reference.md`
- For AI prompts: `landing-pages-prompts.md`
- For Hermes integration: `hermes-agent-teams.md`
