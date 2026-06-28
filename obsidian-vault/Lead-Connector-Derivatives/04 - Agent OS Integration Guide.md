# 04 — Agent OS Integration Guide

> Connect OpenClaw, Hermes Agent, n8n, and Agent OS with GoHighLevel, GoStackBase, and BuildwithOS.
> Source: Julian Goldie SEO — Skool Post #6
> Parent: [[Lead-Connector-Derivatives/00-index]]

---

## Integration Architecture

```
Agent OS Dashboard (port 3000)
    │
    ├── OpenClaw (agent gateway)
    │   ├── ↔ GoHighLevel (V2 REST API)
    │   ├── ↔ GoStackBase (REST API, Premium+)
    │   └── ↔ BuildwithOS (MCP + REST, connector in progress)
    │
    ├── Hermes Agent (port 8642)
    │   ├── ↔ GHL (via OpenClaw gateway)
    │   ├── ↔ GoStackBase (via OpenClaw gateway)
    │   └── ↔ BuildwithOS (via OpenClaw gateway)
    │
    ├── n8n (workflow automation)
    │   ├── ↔ GHL (webhooks + REST)
    │   ├── ↔ GoStackBase (webhooks)
    │   └── ↔ BuildwithOS (MCP)
    │
    └── Connector Service (port 8888)
        └── Routes all agent ↔ platform calls
```

## GoHighLevel Integration

**API:** V2 REST API
**Base URL:** `https://services.leadconnectorhq.com/`
**Auth:** OAuth 2.0 or Private Integration Token
**Rate Limits:** 100 req/10s burst, 200,000/day
**Docs:** https://marketplace.gohighlevel.com/docs/

**Key Endpoints:**
- Contacts: CRUD, tags, custom fields
- Conversations: SMS, email, calls
- Calendar: Appointments, bookings
- Opportunities: Sales pipeline, deals
- Payments: Transactions, subscriptions
- Workflows: Trigger-based automations
- Webhooks: 50+ event types

## GoStackBase Integration

**API:** REST API (available on Premium+ plan)
**Auth:** API key
**Key Features:**
- Smart CRM & Sales Pipelines
- Smart Forms & Surveys
- Smart Calendar
- Email Marketing & Automation
- Digital Products & Client Portal

## BuildwithOS Integration

**API:** MCP (Model Context Protocol) + REST
**MCP Endpoint:** `/mcp/buildos`
**Auth:** Agent key (local) or OAuth (browser/cloud)
**Client Profiles:**
- OpenClaw: Env/SecretRef/plugin config (connector in progress)
- Claude Code: `claude mcp add` (key header or OAuth)
- Codex: MCP config at `/mcp/buildos`
- ChatGPT: Remote MCP OAuth connector
- Custom HTTP: Env file or secret manager

**BuildOS Direct Tools:**
- `skill_load` — Load a skill playbook
- `tool_search` — Discover candidate tools
- `tool_schema` — Inspect exact arguments
- `list_onto_projects` — List projects
- `list_onto_tasks` — List tasks
- `create_onto_task` — Create task
- `update_onto_task` — Update task

## Cross-Platform Workflows

### Lead Capture → Agent Follow-up
1. Landing page form submission (any platform)
2. Webhook → OpenClaw/Hermes
3. AI agent qualifies lead
4. AI agent sends personalized follow-up
5. Calendar booking for qualified leads

### Content Pipeline
1. Goldie SEO Framework generates content
2. Autoblogging AI creates drafts
3. WordPress (on VPS) publishes content
4. n8n automates social media distribution
5. Platform CRM tracks resulting leads

## Security Best Practices

- 🔴 Never commit API keys to GitHub
- 🔴 Use environment variables for all credentials
- 🔴 Rotate keys regularly
- 🔴 Use per-platform API keys (not master keys)
- 🔴 Enable audit logging where available
- 🔴 Scope API keys to minimum required permissions

---

## Sub-Notes

- [[00-index]] — Back to index
- [[01 - Platform Comparison]] — Full comparison
- [[02 - GHL to GoStackBase Conversion]] — Template conversion
- [[03 - GHL to BuildwithOS Conversion]] — BuildwithOS conversion
