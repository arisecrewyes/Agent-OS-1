# Agent OS ↔ Lead Connector Platforms Integration Guide

> Step-by-step guide to connect OpenClaw, Hermes Agent, n8n, and the Agent OS system with GoHighLevel, GoStackBase, and BuildwithOS for full account/subaccount management.
> Source: Julian Goldie SEO — Skool Post #6 + platform API documentation
> Related: [[lead-connector-derivatives-comparison]] | [[hermes-agent-teams]] | [[master-skool-post-conversion-system]]

---

## Overview

This guide covers how to connect your **Agent OS AI agents** (OpenClaw, Hermes Agent, n8n) with **Lead Connector derivative platforms** (GoHighLevel, GoStackBase, BuildwithOS) so your AI systems can:

- ✅ **Access** — Read contacts, pipelines, funnels, automations
- ✅ **Create** — Build funnels, landing pages, email campaigns, contacts
- ✅ **Manage** — Update records, trigger automations, manage subaccounts
- ✅ **Optimize** — Analyze performance, A/B test, report metrics

---

## Architecture Overview

```
                         Agent OS (Hostinger VPS)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐          ┌────▼────┐          ┌────▼────┐
   │ OpenClaw│          │  Hermes │          │   n8n   │
   │  Agent  │          │  Agent  │          │Workflows│
   └────┬────┘          └────┬────┘          └────┬────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼──────┐
        │GoHighLevel│  │GoStackBase│  │BuildwithOS │
        │  (API V2) │  │  (API)    │  │(MCP + REST)│
        └───────────┘  └───────────┘  └────────────┘
```

---

## Part 1: GoHighLevel Integration

### 1A: Connect OpenClaw to GoHighLevel

#### Step 1: Get GoHighLevel API Credentials
1. Log into your GoHighLevel dashboard
2. Go to **Settings → API Keys**
3. Generate a new API key (or use existing)
4. Note your **Location ID** (found in Settings → Location Settings)

#### Step 2: Configure OpenClaw
1. Open your OpenClaw workspace
2. Create a new skill or use the browser tool to access GHL
3. Store your API key securely:
   ```bash
   # In your VPS environment
   export GHL_API_KEY="your_api_key_here"
   export GHL_LOCATION_ID="your_location_id"
   export GHL_BASE_URL="https://services.leadconnectorhq.com"
   ```

#### Step 3: Test the Connection
Use OpenClaw's exec tool to test:
```bash
curl -X GET "https://services.leadconnectorhq.com/contacts/" \
  -H "Authorization: Bearer $GHL_API_KEY" \
  -H "Content-Type: application/json"
```

#### Step 4: Create OpenClaw Skills for GHL
Create skills for common operations:
- **GHL Contact Manager** — Create, update, search contacts
- **GHL Funnel Builder** — Create and manage funnels
- **GHL Automation Trigger** — Trigger workflows programmatically
- **GHL Pipeline Manager** — Move deals through pipelines

### 1B: Connect Hermes Agent to GoHighLevel

#### Step 1: Install Hermes GHL Skill
```bash
hermes skills install ghl-integration
```
(Or create a custom skill)

#### Step 2: Configure GHL in Hermes
```bash
hermes config set ghl.api_key "your_api_key"
hermes config set ghl.location_id "your_location_id"
hermes config set ghl.base_url "https://services.leadconnectorhq.com"
```

#### Step 3: Test with Hermes
```
Inside Hermes chat:
"Connect to GoHighLevel and list my contacts"
"Create a new contact in GHL: John Doe, john@example.com"
"Trigger GHL workflow: Welcome Sequence"
```

### 1C: Connect n8n to GoHighLevel

#### Step 1: Add GHL Credentials in n8n
1. Open n8n dashboard
2. Go to **Settings → Credentials**
3. Add new **HTTP Header Auth** credential:
   - Name: `GHL API`
   - Name: `Authorization`
   - Value: `Bearer YOUR_API_KEY`

#### Step 2: Create n8n Workflows
Example workflows:
- **New GHL Contact → Send Welcome Email**
- **GHL Pipeline Stage Change → Notify Slack**
- **GHL Form Submission → Add to Google Sheets**
- **Daily GHL Report → Send via Telegram**

#### Step 3: Use GHL Webhooks with n8n
1. In GHL, go to **Settings → Webhooks**
2. Add webhook URL: `https://your-n8n-url/webhook/ghl`
3. Select events: Contact Created, Pipeline Stage Changed, etc.
4. In n8n, create a webhook trigger node

### 1D: Agent OS Dashboard Integration

#### Step 1: Add GHL Status to Dashboard
Create a custom widget showing:
- GHL connection status
- Contact count
- Active funnels count
- Recent pipeline changes

#### Step 2: Add GHL Quick Actions
- Sync contacts between Agent OS and GHL
- Trigger GHL automations from Agent OS dashboard
- View GHL analytics in Agent OS

---

## Part 2: GoStackBase Integration

### 2A: Connect OpenClaw to GoStackBase

#### Step 1: Get GoStackBase API Credentials
1. Log into GoStackBase (Premium or Elite plan required for API)
2. Go to **Settings → API** (or **Integrations**)
3. Generate API key

#### Step 2: Configure OpenClaw
```bash
export STACKBASE_API_KEY="your_api_key"
export STACKBASE_BASE_URL="https://gostackbase.com/api"
```

#### Step 3: Test Connection
```bash
curl -X GET "https://gostackbase.com/api/contacts" \
  -H "Authorization: Bearer $STACKBASE_API_KEY"
```

### 2B: Connect Hermes Agent to GoStackBase

#### Step 1: Configure in Hermes
```bash
hermes config set stackbase.api_key "your_api_key"
hermes config set stackbase.base_url "https://gostackbase.com/api"
```

#### Step 2: Test
```
Inside Hermes:
"Connect to GoStackBase and show my client portal"
"List all contacts in GoStackBase"
```

### 2C: Connect n8n to GoStackBase

Same pattern as GHL:
1. Add HTTP Header Auth credential in n8n
2. Create workflows for GoStackBase events
3. Use webhooks if available

---

## Part 3: BuildwithOS Integration

### 3A: Connect OpenClaw to BuildwithOS

BuildwithOS has the most advanced API with MCP support.

#### Step 1: Generate Agent Key
1. Log into BuildwithOS
2. Go to **Profile → Agent Keys**
3. Click **Generate**
4. Choose **OpenClaw** as client profile
5. Select scope: **read_write**
6. Whitelist all write ops
7. Copy the env block

#### Step 2: Configure OpenClaw
Add the BuildOS env block to your OpenClaw config:
```bash
# Add to OpenClaw environment
export BUILDOS_BASE_URL="https://build-os.com"
export BUILDOS_AGENT_TOKEN="boca_your_one_time_secret"
export BUILDOS_CALLEE_HANDLE="buildos:user:YOUR_USER_ID"
export BUILDOS_CALLER_KEY="openclaw:local:your-handle"
```

#### Step 3: Test Connection
```bash
curl -X POST "https://build-os.com/api/agent-call/buildos" \
  -H "Authorization: Bearer $BUILDOS_AGENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "call.dial",
    "params": {},
    "id": 1
  }'
```

#### Step 4: List Projects
```bash
curl -X POST "https://build-os.com/api/agent-call/buildos" \
  -H "Authorization: Bearer $BUILDOS_AGENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "call_id": "test-1",
      "name": "list_onto_projects",
      "arguments": {}
    },
    "id": 2
  }'
```

### 3B: Connect Hermes Agent to BuildwithOS

#### Step 1: Generate Agent Key for Hermes
1. In BuildwithOS → Profile → Agent Keys
2. Generate new key for **Custom HTTP** client
3. Copy the env block

#### Step 2: Configure Hermes
```bash
hermes config set buildos.agent_token "boca_your_secret"
hermes config set buildos.base_url "https://build-os.com"
```

#### Step 3: Test
```
Inside Hermes:
"Connect to BuildwithOS and list my projects"
"Create a new task in BuildOS project: Research competitors"
```

### 3C: Connect n8n to BuildwithOS

#### Step 1: Add BuildOS Credentials
1. In n8n, add **HTTP Header Auth** credential
2. Use the BuildOS agent token

#### Step 2: Create Workflows
- **BuildOS Task Created → Send Notification**
- **BuildOS Project Status Change → Update Agent OS Dashboard**
- **BuildOS Document Published → Share to Social Media**

### 3D: MCP Integration (Advanced)

BuildwithOS supports **Model Context Protocol (MCP)** at `/mcp/buildos`. This is the most powerful integration method.

#### For Claude Code:
```bash
claude mcp add --transport http buildos https://build-os.com/mcp/buildos \
  --header "Authorization: Bearer boca_your_one_time_secret"
```

#### For OpenClaw:
Configure as MCP server in OpenClaw settings (when OpenClaw connector ships).

---

## Part 4: Cross-Platform Workflows

### 4A: Sync Contacts Across Platforms

**Use Case:** Keep contacts in sync between GHL, GoStackBase, and Agent OS.

**n8n Workflow:**
```
GHL Webhook (Contact Created)
  → Filter (check if email exists in GoStackBase)
  → GoStackBase API (Create Contact)
  → Agent OS Memory Engine (Log new contact)
  → OpenClaw (Send notification)
```

### 4B: AI Agent Manages All Platforms

**Use Case:** Hermes Agent manages funnels, contacts, and automations across all platforms.

**Hermes Setup:**
```
"Connect to GoHighLevel and list contacts"
"Create a landing page in GoStackBase using template X"
"Check BuildwithOS for project status"
"Trigger GHL automation: Welcome Sequence for new contact"
```

### 4C: Unified Reporting

**Use Case:** Pull analytics from all platforms into Agent OS dashboard.

**n8n Workflow:**
```
Schedule (Daily at 8am)
  → GHL API (Get contact count, funnel stats)
  → GoStackBase API (Get portal stats, revenue)
  → BuildwithOS API (Get project status, task completion)
  → Google Sheets (Compile report)
  → Telegram (Send daily report)
```

---

## Part 5: Security Best Practices

### API Key Management
1. **Never hardcode API keys** in scripts — use environment variables
2. **Rotate keys** every 90 days
3. **Use least-privilege** — only grant needed permissions
4. **Monitor usage** — check rate limits and access logs
5. **Store secrets** in a secrets manager (not plain text)

### Platform-Specific Security
| Platform | Security Notes |
|----------|----------------|
| **GoHighLevel** | Use Private Integration Tokens for internal tools; OAuth for public apps |
| **GoStackBase** | API only available on Premium+ plans; use HTTPS only |
| **BuildwithOS** | Agent keys are scoped per-project; use read_only when possible |

### Agent OS Security
1. Store all API keys in `/data/.openclaw/.env` (not in workspace)
2. Use Docker secrets for container-level credentials
3. Restrict API key access to specific agents
4. Log all API access for audit trails

---

## Part 6: Quick Reference — API Endpoints

### GoHighLevel V2 API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/contacts/` | GET | List contacts |
| `/contacts/` | POST | Create contact |
| `/contacts/{id}` | PUT | Update contact |
| `/conversations/` | GET | List conversations |
| `/conversations/` | POST | Send message |
| `/opportunities/` | GET | List opportunities |
| `/opportunities/` | POST | Create opportunity |
| `/calendars/` | GET | List calendar events |
| `/calendars/` | POST | Create appointment |
| `/funnels/` | GET | List funnels |
| `/funnels/` | POST | Create funnel |
| `/workflows/` | GET | List workflows |
| `/webhooks/` | POST | Register webhook |

### BuildwithOS API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/agent-call/buildos` | POST | JSON-RPC gateway |
| `/mcp/buildos` | MCP | Model Context Protocol |
| `/api/agent-call/bootstrap/{token}` | GET | Bootstrap config |

### GoStackBase API
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/contacts` | GET/POST | Contact management |
| `/api/automations` | GET/POST | Automation management |
| `/api/portals` | GET | Client portal data |

---

## Related

- For the platform comparison: `lead-connector-derivatives-comparison.md`
- For GHL → GoStackBase conversion: `ghl-to-stackbase-conversion.md`
- For GHL → BuildwithOS conversion: `ghl-to-buildwithos-conversion.md`
- For the SOP: `landing-pages-websites-sop.md`
- For Hermes Agent Teams: `hermes-agent-teams.md`
