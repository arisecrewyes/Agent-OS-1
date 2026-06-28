# Lead Connector Platforms — AI Agent Connection Guide

> Step-by-step guide to connect OpenClaw, Hermes Agent, n8n, and Agent OS to GoHighLevel, GoStackBase, BuildwithOS, and Lead Connector.
> Source: Platform support documentation + API research + n8n webhook pattern analysis
> Related: [[lead-connector-derivatives-comparison]] | [[agent-os-lead-connector-integration]] | [[master-skool-post-conversion-system]]

---

## Overview

All four platforms in this guide are **Lead Connector derivatives** — they share the same core architecture, API structure, and authentication patterns. This means:

- ✅ **One connection pattern works for all four**
- ✅ **n8n can connect to all of them** using the same webhook + API approach
- ✅ **AI agents can control all of them** using the same authentication flow
- ✅ **Contacts, funnels, automations, and subaccounts** are manageable programmatically across all platforms

### The Key Insight

The user's purchased course revealed the connection pattern:
1. **Platform webhook** → n8n (receives events from the platform)
2. **n8n workflow** → processes events and triggers actions
3. **Platform API** (called from n8n) → creates/manages resources
4. **Location ID** → identifies which account/subaccount to operate on
5. **API inside n8n only** → no external API calls needed beyond what n8n provides

Since n8n can connect to any Lead Connector platform using this pattern, **AI agents can too**. The AI agent simply replaces or augments the n8n workflow.

---

## Platform Connection Details

### 1. GoHighLevel (GHL)

#### API Connection
| Item | Value |
|------|-------|
| **Base URL** | `https://services.leadconnectorhq.com` |
| **Auth** | Private Integration Token (or OAuth 2.0) |
| **Version Header** | `Version: 2021-07-28` |
| **Rate Limits** | 100 req/10s burst, 200,000/day |
| **API Docs** | https://marketplace.gohighlevel.com/docs/ |
| **Support** | https://help.gohighlevel.com/support/home |
| **Developer Portal** | https://developers.gohighlevel.com/ |

#### Finding Your Location ID
1. Log into GoHighLevel dashboard
2. Go to **Settings → Location Settings**
3. Your Location ID is displayed there
4. It's also in the URL when viewing a location: `.../location/{LOCATION_ID}/...`

#### Finding Your API Key
1. Log into GoHighLevel dashboard
2. Go to **Settings → API Keys**
3. Generate a new Private Integration Token
4. Copy the token (shown only once)

#### Webhook Setup (for n8n)
1. In GHL, go to **Settings → Webhooks**
2. Click **Add Webhook**
3. Enter your n8n webhook URL: `https://your-n8n-instance.com/webhook/ghl-{LOCATION_ID}`
4. Select events to subscribe to (see list below)
5. Save — GHL will now POST events to your n8n webhook

#### Webhook Events (Key Ones)
| Event | Description |
|-------|-------------|
| `contact.created` | New contact created |
| `contact.updated` | Contact record updated |
| `contact.tag_added` | Tag added to contact |
| `opportunity.created` | New pipeline deal |
| `opportunity.stage_changed` | Deal moved between stages |
| `workflow.triggered` | Workflow fired |
| `appointment.booked` | Calendar booking made |
| `form.submitted` | Form submission received |

#### n8n Connection Pattern
```
GHL Webhook (contact.created)
  → n8n Webhook Trigger Node
  → n8n HTTP Request Node (GHL API)
    → Create/update contact, trigger workflow, etc.
  → n8n HTTP Request Node (GoStackBase API)
    → Sync contact to GoStackBase
```

#### Funnel Share Links
GHL uses a unique `funnel_share` parameter system:
- Format: `https://affiliates.gohighlevel.com/?funnel_share={FUNNEL_ID}`
- The funnel ID is extracted from the share link
- When a user clicks the link and has GHL access, the funnel imports into their account
- This is the ONLY LC platform with public funnel share links

---

### 2. GoStackBase

#### API Connection
| Item | Value |
|------|-------|
| **Base URL** | Shared Lead Connector infrastructure (internal) |
| **Auth** | API Key (Premium+ plans only) |
| **API Availability** | Premium ($119/mo) and Elite ($239/mo) plans |
| **Support** | No public support docs — uses shared LC infrastructure |
| **Main Site** | https://gostackbase.com |

#### Finding Your API Key
1. Log into GoStackBase (Premium or Elite plan)
2. Go to **Settings → API** (or **Integrations**)
3. Generate API key
4. Note: API is only available on Premium+ plans

#### Webhook Setup
GoStackBase inherits the Lead Connector webhook system:
1. In GoStackBase, go to **Settings → Webhooks** (or **Integrations → Webhooks**)
2. Add webhook URL for your n8n/AI agent endpoint
3. Select events (same event types as GHL — shared infrastructure)

#### n8n Connection Pattern
```
GoStackBase Webhook (contact.created)
  → n8n Webhook Trigger Node
  → n8n HTTP Request Node (GoStackBase API)
    → Manage contacts, automations, portals
```

#### Key Limitations
- ❌ No public funnel share links
- ❌ No public API documentation
- ❌ API only on Premium+ plans
- ✅ Shares infrastructure with Lead Connector (same webhook events, similar API)
- ✅ Client portal is unique differentiator

---

### 3. BuildwithOS (build-os.com)

#### API Connection
| Item | Value |
|------|-------|
| **Real Domain** | `https://build-os.com` (NOT `buildwithos.com`) |
| **MCP Endpoint** | `https://build-os.com/mcp/buildos` |
| **JSON-RPC Gateway** | `https://build-os.com/api/agent-call/buildos` |
| **Auth** | Agent Key (scoped, per-project) |
| **Protocol** | JSON-RPC 2.0 + MCP |
| **OAuth** | PKCE at `build-os.com/oauth/*` |
| **Docs** | https://build-os.com/docs/connect-agents |
| **Support** | https://build-os.com/help |

#### Finding Your Agent Key
1. Log into BuildOS at https://build-os.com
2. Go to **Profile → Agent Keys**
3. Click **Generate**
4. Choose client profile: **Custom HTTP** (for n8n/AI agent)
5. Choose scope: **read_write**
6. Whitelist write operations needed
7. Copy the env block (shown only once!)

#### Agent Key Environment Variables
```bash
BUILDOS_BASE_URL=https://build-os.com
BUILDOS_AGENT_TOKEN=boca_your_one_time_secret
BUILDOS_CALLEE_HANDLE=buildos:user:YOUR_USER_ID
BUILDOS_CALLER_KEY=your-client-handle
```

#### OAuth 2.0 Scopes
| Scope | Access |
|-------|--------|
| `buildos.read` | Read all projects, tasks, documents |
| `buildos.write` | Create/update tasks, documents, projects |
| `offline_access` | Refresh tokens for long-lived access |

#### Available API Tools
**Reads (all keys):**
- `list_onto_projects`, `search_onto_projects`, `get_onto_project`, `get_onto_project_status`
- `list_onto_tasks`, `search_onto_tasks`, `get_onto_task`
- `list_onto_documents`, `search_onto_documents`, `get_onto_document`
- `search_onto` (cross-entity search)

**Writes (require read_write + whitelist):**
- `create_onto_task`, `update_onto_task`
- `create_onto_document`, `update_onto_document`
- `create_onto_project`, `update_onto_project`
- `create_onto_goal`, `update_onto_goal`
- `create_onto_plan`, `update_onto_plan`
- `create_onto_milestone`, `update_onto_milestone`
- `create_onto_risk`, `update_onto_risk`

**Discovery:**
- `skill_load`, `tool_search`, `tool_schema`

**Session:**
- `call.dial`, `tools/list`, `tools/call`, `call.hangup`

#### n8n Connection Pattern
```
n8n HTTP Request Node (POST)
  → URL: https://build-os.com/api/agent-call/buildos
  → Auth: Header (Authorization: Bearer boca_your_token)
  → Body: JSON-RPC 2.0
  → Method: tools/call
  → Tool: list_onto_projects (or any available tool)
```

#### Webhooks
BuildwithOS does NOT have a public webhook system. Workaround:
- Use n8n's HTTP Request node to poll the JSON-RPC API
- Or use n8n's Schedule trigger to check for changes periodically
- Or use BuildOS's internal notification system (email/push) as a trigger

#### Key Advantages for AI Agents
- ✅ MCP support (native AI agent protocol)
- ✅ OAuth 2.0 (no key paste needed for cloud clients)
- ✅ Per-project scoped keys (least privilege)
- ✅ Full CRUD on projects, tasks, documents, goals, plans, milestones, risks
- ✅ Idempotency keys (prevent duplicate writes)
- ✅ Audit trail (all API calls logged)

---

### 4. Lead Connector (Original Platform)

#### API Connection
| Item | Value |
|------|-------|
| **Base URL** | `https://services.leadconnectorhq.com` |
| **Auth** | OAuth 2.0 or Private Integration Token |
| **Support** | https://help.leadconnectorhq.com/support/home |
| **Developer Docs** | https://developers.gohighlevel.com/ (shared) |

#### Finding Your API Key
1. Log into Lead Connector
2. Go to **Settings → API Keys**
3. Generate Private Integration Token

#### Webhook Setup
Same pattern as GHL:
1. Go to **Settings → Webhooks**
2. Add webhook URL
3. Select events

#### Why This Matters
Lead Connector is the **original platform**. All three other platforms (GHL, GoStackBase, BuildwithOS) forked from it. Understanding LC means understanding the shared infrastructure:
- Same base URL (`services.leadconnectorhq.com`)
- Same authentication flow
- Same webhook event types
- Same Location ID system
- Similar API endpoints (contacts, conversations, opportunities, calendars, funnels)

---

## Cross-Platform Connection Patterns

### Pattern 1: Webhook → n8n → API (Recommended)

This is the pattern from the user's purchased course:

```
Lead Connector Platform
    │
    ├── Webhook (contact.created, form.submitted, etc.)
    │       │
    │       ▼
    │   n8n Webhook Trigger
    │       │
    │       ▼
    │   n8n Workflow (filter, transform, route)
    │       │
    │       ├──→ Platform API (create/update resources)
    │       ├──→ Another Platform API (cross-platform sync)
    │       ├──→ OpenClaw/Hermes (AI agent actions)
    │       └──→ Database/Sheet (logging, reporting)
```

**Why this works:**
- Webhooks are event-driven (no polling needed)
- n8n handles the logic (if this, then that)
- API calls from n8n use the platform's native REST API
- Location ID ensures the right account/subaccount is targeted
- All platforms support webhooks (except BuildwithOS — use polling)

### Pattern 2: AI Agent → Direct API (No n8n)

```
OpenClaw/Hermes Agent
    │
    ├──→ GHL API (REST, Bearer <REDACTED>)
    ├──→ GoStackBase API (REST, Bearer <REDACTED>)
    ├──→ BuildwithOS API (JSON-RPC, Bearer <REDACTED>)
    └──→ Lead Connector API (REST, Bearer <REDACTED>)
```

**When to use:**
- Simple operations (create contact, list funnels)
- Real-time responses (chat agent needs to look up contact)
- When n8n is not available

### Pattern 3: AI Agent → n8n → API (Hybrid)

```
OpenClaw/Hermes Agent
    │
    ├──→ n8n (HTTP Request node triggers n8n workflow)
    │       │
    │       └──→ Platform API (n8n handles the actual platform interaction)
    │
    └──→ Direct API (for simple reads that don't need n8n logic)
```

**When to use:**
- Agent needs n8n's logic capabilities (filtering, routing, multi-step)
- Agent wants to leverage existing n8n workflows
- Complex operations that benefit from n8n's visual workflow builder

### Pattern 4: MCP (BuildwithOS Only)

```
AI Agent (Claude Code, Codex, OpenClaw)
    │
    └──→ BuildwithOS MCP (https://build-os.com/mcp/buildos)
            │
            ├──→ tools/list (discover available tools)
            ├──→ tools/call (execute operations)
            └──→ skill_load (load skill playbooks)
```

**When to use:**
- AI agent needs real-time, bidirectional communication
- Agent wants to discover capabilities dynamically
- Agent needs to work within BuildwithOS's project ontology

---

## Step-by-Step: Connecting OpenClaw to Any Lead Connector Platform

### Step 1: Gather Credentials

**For GoHighLevel:**
```
GHL_API_KEY=your_private_integration_token
GHL_LOCATION_ID=your_location_id
GHL_BASE_URL=https://services.leadconnectorhq.com
```

**For GoStackBase:**
```
STACKBASE_API_KEY=your_api_key
STACKBASE_BASE_URL=https://gostackbase.com/api
```

**For BuildwithOS:**
```
BUILDOS_AGENT_TOKEN=boca_your_one_time_secret
BUILDOS_BASE_URL=https://build-os.com
BUILDOS_CALLEE_HANDLE=buildos:user:YOUR_USER_ID
```

**For Lead Connector:**
```
LC_API_KEY=your_private_integration_token
LC_LOCATION_ID=your_location_id
LC_BASE_URL=https://services.leadconnectorhq.com
```

### Step 2: Test Connection

Use the connection scripts in the lead-connector-bridge skill:
```bash
# GoHighLevel
bash skills/lead-connector-bridge/scripts/connect-ghl.sh

# GoStackBase
bash skills/lead-connector-bridge/scripts/connect-stackbase.sh

# BuildwithOS
bash skills/lead-connector-bridge/scripts/connect-buildos.sh
```

### Step 3: Set Up Webhook Listener (n8n or OpenClaw)

**In n8n:**
1. Create new workflow
2. Add **Webhook** trigger node
3. Set path: `/webhook/{platform}-{location_id}`
4. Copy the webhook URL
5. Paste into platform's webhook settings

**In OpenClaw:**
OpenClaw can receive webhooks via its built-in HTTP capabilities or through n8n.

### Step 4: Configure Platform Webhook

Go to your platform's webhook settings and add the URL:
- **GHL:** Settings → Webhooks → Add
- **GoStackBase:** Settings → Webhooks → Add
- **Lead Connector:** Settings → Webhooks → Add
- **BuildwithOS:** No webhook system — use polling or n8n workaround

### Step 5: Test End-to-End

1. Trigger an event on the platform (e.g., submit a test form)
2. Verify the webhook fires (check n8n/OpenClaw logs)
3. Verify the AI agent can call the platform API (create a test contact)
4. Verify cross-platform sync works (create in GHL → verify in GoStackBase)

---

## Security Best Practices

1. **Never commit API keys to GitHub** — use environment variables
2. **Use least-privilege scopes** — read-only when possible
3. **Scope keys per-project** (BuildwithOS supports this natively)
4. **Rotate keys regularly** — every 90 days
5. **Use webhook signatures** — verify webhook payloads come from the platform
6. **Log all API access** — audit trail for compliance
7. **Use HTTPS only** — never HTTP for API calls
8. **Store secrets in a secrets manager** — not plain text files

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid/expired API key | Regenerate key |
| 403 Forbidden | Insufficient permissions | Check key scopes |
| 429 Too Many Requests | Rate limit hit | Wait and retry with backoff |
| Webhook not firing | Wrong URL or events not selected | Double-check webhook config |
| Missing data in webhook | Wrong event type subscribed | Add the correct event types |
| Cross-platform sync fails | Different field mappings | Map fields explicitly in n8n |

---

## Related

- For the platform comparison: `lead-connector-derivatives-comparison.md`
- For the original integration guide: `agent-os-lead-connector-integration.md`
- For the skill: `skills/lead-connector-bridge/SKILL.md`
- For the template conversion: `stackbase-template-conversion.md`
