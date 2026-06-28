# API Cheatsheet — Lead Connector Platforms

> Quick reference for API endpoints across all 3 platforms.
> Source: Julian Goldie SEO — Skool Post #6 + platform documentation

---

## GoHighLevel V2 REST API

**Base URL:** `https://services.leadconnectorhq.com`
**Auth:** `Authorization: Bearer {API_KEY}`
**Version Header:** `Version: 2021-07-28`
**Rate Limits:** 100 req/10s burst, 200,000/day

### Contacts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/contacts/` | List contacts (limit, page, query params) |
| POST | `/contacts/` | Create contact |
| GET | `/contacts/{id}` | Get contact by ID |
| PUT | `/contacts/{id}` | Update contact |
| DELETE | `/contacts/{id}` | Delete contact |
| POST | `/contacts/{id}/tags` | Add tags to contact |

### Conversations
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/conversations/` | List conversations |
| POST | `/conversations/` | Create/send message |
| GET | `/conversations/{id}` | Get conversation |
| POST | `/conversations/{id}/messages` | Send message in conversation |

### Opportunities (Pipeline)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/opportunities/` | List opportunities |
| POST | `/opportunities/` | Create opportunity |
| GET | `/opportunities/{id}` | Get opportunity |
| PUT | `/opportunities/{id}` | Update opportunity (stage, value) |

### Calendars
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/calendars/` | List calendars |
| GET | `/calendars/{id}/slots` | Get available time slots |
| POST | `/calendars/` | Create calendar event (booking) |

### Funnels
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/funnels/` | List funnels |
| GET | `/funnels/{id}` | Get funnel details |
| GET | `/funnels/{id}/pages` | List funnel pages |

### Workflows
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workflows/` | List workflows |
| POST | `/workflows/{id}/trigger` | Trigger a workflow |

### Webhooks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/webhooks/` | List webhooks |
| POST | `/webhooks/` | Register webhook |
| DELETE | `/webhooks/{id}` | Delete webhook |

### Location
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/locations/{id}` | Get location details |

---

## BuildwithOS JSON-RPC API

**Base URL:** `https://build-os.com/api/agent-call/buildos`
**Auth:** `Authorization: Bearer {AGENT_TOKEN}`
**MCP Endpoint:** `https://build-os.com/mcp/buildos`
**Protocol:** JSON-RPC 2.0

### Connection
```json
{
  "jsonrpc": "2.0",
  "method": "call.dial",
  "params": {},
  "id": 1
}
```

### List Projects
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "call_id": "list-projects",
    "name": "list_onto_projects",
    "arguments": {}
  },
  "id": 2
}
```

### List Tasks in Project
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "call_id": "list-tasks",
    "name": "list_onto_tasks",
    "arguments": {
      "project_id": "YOUR_PROJECT_ID"
    }
  },
  "id": 3
}
```

### Create Task
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "call_id": "create-task",
    "name": "create_onto_task",
    "arguments": {
      "project_id": "YOUR_PROJECT_ID",
      "title": "Task title",
      "description": "Task description",
      "status": "todo"
    }
  },
  "id": 4
}
```

### Update Task
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "call_id": "update-task",
    "name": "update_onto_task",
    "arguments": {
      "task_id": "TASK_ID",
      "status": "done"
    }
  },
  "id": 5
}
```

### Agent Key Scopes
| Scope | Access |
|-------|--------|
| `read_only` | List projects, tasks, documents |
| `read_write` | Create/update tasks, create documents |
| `admin` | Full project management |

### Client Profiles
| Client | Auth Method |
|--------|-------------|
| Claude Code | `claude mcp add` with key header |
| OpenClaw | Env/SecretRef (connector in progress) |
| Codex | MCP config at `/mcp/buildos` |
| ChatGPT | Remote MCP OAuth connector |
| Custom HTTP | Env file or secret manager |

---

## GoStackBase API

**Note:** GoStackBase API is only available on Premium ($119/mo) and Elite ($239/mo) plans. Endpoints are not publicly documented. The following is based on the Lead Connector shared infrastructure.

**Base URL:** Internal (dashboard API)
**Auth:** `Authorization: Bearer {API_KEY}`

### Known Endpoints (from LC shared infrastructure)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/contacts` | List contacts |
| POST | `/api/contacts` | Create contact |
| GET | `/api/automations` | List automations |
| GET | `/api/portals` | List client portals |

### Limitations
- ❌ No public funnel share links
- ❌ No documented template API
- ❌ API only on Premium+ plans
- ✅ Dashboard UI for template creation
- ✅ Client portal is key differentiator

---

## Cross-Platform Comparison

| Capability | GHL | GoStackBase | BuildwithOS |
|------------|-----|-------------|-------------|
| **Auth** | API Key + Location | API Key (Premium+) | Agent Key (scoped) |
| **Protocol** | REST | REST | JSON-RPC + MCP |
| **Contacts** | ✅ Full CRUD | ✅ Full CRUD | ❌ (Project members) |
| **Funnels** | ✅ Full CRUD | ✅ Dashboard only | ❌ (Projects instead) |
| **Automations** | ✅ Full CRUD | ✅ Full CRUD | ✅ Task automations |
| **Templates** | ✅ Share links | ❌ In-dashboard | ✅ Business kits |
| **Webhooks** | ✅ 50+ events | ✅ | ✅ |
| **Rate Limit** | 100/10s | Unknown | Unknown |
| **Docs Quality** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
