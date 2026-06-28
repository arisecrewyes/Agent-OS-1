# SOP: Create a Private Integration API Key on Lead Connector Platforms

**Purpose:** Generate an API key (JWT) for programmatic access to any Lead Connector derivative platform (GoHighLevel, GoStackBase, BuildwithOS, LeadConnector) so AI agents (OpenClaw, Hermes, etc.) can automate tasks 10-100x faster than browser automation.

**Trigger:** "Connect AI agent to [LC platform]" / "Get API key for [platform]" / "Set up Private Integration"

**Applies to:** All LC derivatives — they share the same `services.leadconnectorhq.com` API infrastructure.

---

## Overview

A Private Integration creates a JWT (JSON Web Token) that allows AI agents to make REST API calls directly to the platform. This is dramatically faster and more reliable than browser automation for:
- Bulk operations (contacts, messages, pipelines)
- Workflow triggers
- Webhook registration
- Data extraction and reporting

---

## Step-by-Step Process (User + Agent Together)

### Step 1: Open Settings → API / Integrations

**Agent action:** Navigate browser to the API settings page:
```
https://app.gostackbase.com/v2/location/{locationId}/settings/api
```
Or manually: Settings (gear icon) → API / Integrations

### Step 2: Click "Private Integrations" tab

The page has two tabs:
- **Marketplace** — public integrations built by others
- **Private Integrations** — custom integrations you create

Click **Private Integrations**.

### Step 3: Click "Generate New Token" (or "Create Private Integration")

This opens a form where you:
1. **Name the integration** — e.g., "OpenClaw Agent" or "Hermes Agent"
2. **Select permissions/scopes** — choose what the agent can do:
   - ✅ Contacts (read/write)
   - ✅ Conversations (read/write)
   - ✅ Opportunities (read/write)
   - ✅ Calendars (read/write)
   - ✅ Workflows (trigger)
   - ✅ Funnels (read)
   - ✅ Forms (read/write)
   - ✅ Surveys (read/write)
   - ❌ Payments (optional — sensitive)
   - ❌ Account settings (skip — least privilege)

### Step 4: Generate the Token

Click **Generate** or **Create**. The platform will display the **JWT token** once.

⚠️ **CRITICAL:** The token is shown ONLY ONCE. You must copy it immediately.

### Step 5: Securely Store the Token

**The user copies the token and provides it to the agent.** The agent stores it in:
- **OpenClaw secredentials** (encrypted, never in plain text or git)
- **Environment variable** for runtime access
- **NOT** in any file that goes to GitHub

### Step 6: Test the Token

**Agent action:** Verify the token works:
```bash
curl -s "https://services.leadconnectorhq.com/contacts/?locationId={locationId}&limit=1" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Version: 2021-07-28" \
  -H "Content-Type: application/json"
```

Expected result: `200 OK` with JSON contact data.

### Step 7: Document the Connection

Save to `MEMORY.md`:
```
## {Platform} API Access (Established YYYY-MM-DD)
- **Platform:** GoStackBase / GHL / BuildwithOS
- **Location ID:** {locationId}
- **Integration Name:** OpenClaw Agent
- **Token:** [SECREDENTIAL — stored in OpenClaw only]
- **Scopes:** contacts, conversations, opportunities, calendars, workflows, funnels, forms
- **API Base:** services.leadconnectorhq.com
- **Status:** ✅ Active
```

---

## Security Best Practices

| Practice | Why |
|---|---|
| **Least privilege** | Only grant scopes the agent needs |
| **One token per agent** | Don't share tokens between agents |
| **Never in git** | Token goes in secredentials only |
| **Rotate on compromise** | Regenerate immediately if leaked |
| **Revoke unused** | Delete integrations you no longer use |
| **Audit logs** | Check API usage in platform logs |

---

## What the Agent Can Do with the API Key

| Capability | API Endpoint | Example |
|---|---|---|
| Get contacts | `GET /contacts/` | List all leads |
| Create contact | `POST /contacts/` | Add new lead from chat |
| Update contact | `PUT /contacts/{id}` | Add tags, update fields |
| Search contacts | `POST /contacts/search` | Find by email/phone |
| Send SMS | `POST /conversations/messages` | Follow-up messages |
| Send email | `POST /conversations/messages` | Email campaigns |
| Create opportunity | `POST /opportunities/` | New deal in pipeline |
| Update pipeline | `PUT /opportunities/{id}` | Move deal stage |
| Get calendars | `GET /calendars/` | Check availability |
| Create appointment | `POST /appointments/` | Book a call |
| Trigger workflow | `POST /workflows/{id}/trigger` | Start automation |
| List funnels | `GET /funnels/` | Get funnel data |
| Get forms | `GET /forms/` | Form submissions |
| Create webhook | `POST /webhooks/` | Real-time event routing |

---

## Workflow: Agent → API → Platform

```
OpenClaw Agent
     │
     ▼
REST API calls (Bearer JWT)
     │
     ▼
services.leadconnectorhq.com
     │
     ▼
GoStackBase / GHL / BuildwithOS
     │
     ├── Contacts (CRUD)
     ├── Conversations (SMS/email)
     ├── Opportunities (pipeline)
     ├── Calendars (booking)
     ├── Workflows (trigger)
     ├── Webhooks (real-time events)
     └── Funnels/Forms (read)
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| 401 Invalid JWT | Token expired or revoked — regenerate |
| 403 Forbidden | Scope not granted — add permission in integration settings |
| 429 Too Many Requests | Rate limit hit — add delays between calls |
| Token not showing | Can only be viewed once at creation — must regenerate |

---

## Cross-Platform Note

All LC derivatives share the same API infrastructure. A Private Integration created on GoStackBase uses the exact same endpoints and authentication as GHL. The only differences are:
- **Dashboard URL** (app.gostackbase.com vs app.gohighlevel.com)
- **Location ID** (unique per platform)
- **Feature availability** (some platforms may disable certain features)

The token, scopes, and API base are identical.
