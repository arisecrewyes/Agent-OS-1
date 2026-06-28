---
name: lead-connector-bridge
description: "Connect AI agents to Lead Connector platforms (GoHighLevel, GoStackBase, BuildwithOS) for template recreation, contact management, funnel building, and automation control."
user-invocable: true
allowed-tools: ["exec", "web_fetch", "browser"]
---

# Lead Connector Bridge

Connect AI agents to GoHighLevel, GoStackBase, and BuildwithOS platforms. For the full integration SOP, see `docs/sop-universal-lc-integration.md`.

## Trigger Phrases

- "connect to gohighlevel" / "connect to stackbase" / "connect to buildwithos"
- "recreate template" / "convert funnel" / "import template"
- "build funnel in stackbase" / "create landing page in buildwithos"
- "sync contacts" / "manage pipeline"

## Supported Platforms

| Platform | Auth | API Base | Template Sharing |
|----------|------|----------|-----------------|
| GoHighLevel | API Key + Location ID | `https://services.leadconnectorhq.com` | ✅ `funnel_share` links |
| GoStackBase | API Key (Premium+) | Internal (dashboard) | ❌ No public share links |
| BuildwithOS | Agent Key (scoped) | `https://build-os.com` | ✅ Pre-built business kits |

## Workflow

### Phase 1: Connect

1. **Ask user which platform** they want to connect (GHL, GoStackBase, BuildwithOS, or Lead Connector)
2. **Gather credentials** — see `references/api-cheatsheet.md` for what's needed per platform
3. **Run the connection script** for that platform:
   ```bash
   bash <skill_dir>/scripts/connect-ghl.sh
   bash <skill_dir>/scripts/connect-stackbase.sh
   bash <skill_dir>/scripts/connect-buildos.sh
   ```
4. **Verify connection** by fetching account info or listing contacts
5. **Store credentials** in environment (never in workspace files)

### Phase 2: Task

Ask user what they want the agent to do. Common tasks:

- **Recreate template** — User provides GHL funnel share link → Agent recreates in target platform
- **Build funnel** — Agent creates a new funnel from scratch
- **Manage contacts** — Create, update, search contacts
- **Trigger automation** — Fire workflows programmatically
- **Sync data** — Cross-platform contact/pipeline sync

### Phase 3: Execute

For **template recreation** (the primary use case):

1. **Get the source template** — User provides GHL funnel share link
2. **Fetch template details** — Use `web_fetch` on the GHL affiliate link to identify template type
3. **Load the template reference** — See `references/ghl-templates.md` for the 5 standard templates
4. **Map to target platform** — See `references/template-mapping.md` for equivalent structures
5. **Execute creation** — Use platform API to create equivalent funnel/pages/forms
6. **Verify & report** — Confirm creation, provide links to user

For **platform operations** (contacts, funnels, automations):

1. **Identify the operation** — What to do, on which platform
2. **Check API cheatsheet** — `references/api-cheatsheet.md` for endpoints
3. **Execute via curl or n8n** — Direct API call or n8n HTTP Request node
4. **Verify result** — Confirm the operation succeeded

### Phase 4: Verify

- Confirm the recreated template is accessible
- Test form submissions if applicable
- Report status to user with direct links

## Connection Patterns

### Pattern 1: Webhook → n8n → API (Recommended)
All LC platforms support webhooks (except BuildwithOS). The n8n pattern:
1. Platform webhook → n8n Webhook Trigger
2. n8n workflow processes the event
3. n8n HTTP Request node calls platform API
4. Location ID ensures correct account/subaccount

### Pattern 2: AI Agent → Direct API
For simple operations without n8n:
1. Agent calls platform API directly
2. Uses bearer <REDACTED> or API key
3. Parses response and acts on it

### Pattern 3: Agent → n8n → API (Hybrid)
For complex operations:
1. Agent triggers n8n workflow via HTTP
2. n8n handles multi-step logic
3. n8n calls platform API

### Pattern 4: MCP (BuildwithOS Only)
For AI-native bidirectional communication:
1. Agent connects to `https://build-os.com/mcp/buildos`
2. Discovers tools via `tools/list`
3. Executes operations via `tools/call`

## Template Recreation Details

### GoHighLevel → GoStackBase

GoHighLevel has 5 standard funnel templates accessible via `funnel_share` links. GoStackBase does NOT have public share links — templates must be recreated via the dashboard or API.

**The 5 GHL templates and their GoStackBase equivalents:**

| GHL Template | GHL Link Pattern | GoStackBase Equivalent |
|-------------|-----------------|----------------------|
| Book a Call | `funnel_share=65914bbf...` | Smart Form → Smart Calendar → Thank You |
| ChatGPT Opt-In | `funnel_share=656e6e2d...` | Lead Capture → Email Delivery → Thank You |
| Mastermind | `funnel_share=659cb7e8...` | Application Form → Calendar → Checkout → Welcome |
| Course Tripwire | `funnel_share=659d112e...` | Sales Page → Checkout → Upsell → Thank You |
| Free Book | `funnel_share=659d112e...` | Lead Capture → Email Delivery → Thank You |

See `references/template-mapping.md` for detailed page-by-page mapping.

### GoHighLevel → BuildwithOS

BuildwithOS uses a project-based ontology instead of traditional funnels. Map GHL funnels to BuildOS projects with tasks.

See `references/template-mapping.md` for BuildOS mapping.

## API Quick Reference

### GoHighLevel V2 REST API
```
Base: https://services.leadconnectorhq.com
Auth: Bearer {API_KEY}
Key endpoints:
  GET  /contacts/          — List contacts
  POST /contacts/          — Create contact
  GET  /funnels/           — List funnels
  POST /funnels/           — Create funnel
  GET  /funnels/{id}/pages — List funnel pages
  POST /workflows/         — Trigger workflow
  GET  /opportunities/      — List pipeline deals
```

### BuildwithOS JSON-RPC API
```
Base: https://build-os.com/api/agent-call/buildos
Auth: Bearer {AGENT_TOKEN}
Method: tools/call
Key tools:
  list_onto_projects    — List all projects
  list_onto_tasks       — List tasks in project
  create_onto_task      — Create new task
  update_onto_task      — Update task status
```

### GoStackBase API
```
Base: Internal (dashboard only on Premium+)
Auth: Bearer {API_KEY}
Note: GoStackBase has no public funnel share links.
      Templates must be recreated via dashboard UI or API.
```

## Security Rules

- 🔴 **Never store API keys in workspace files** — use environment variables
- 🔴 **Never log API keys** in chat or logs
- 🟡 **Use least-privilege scopes** — read-only when possible
- 🟡 **Confirm before write operations** — creating funnels, sending emails
- 🟢 **Verify after creation** — always confirm resources were created

## Reference Files

- `references/ghl-templates.md` — Detailed specs for all 5 GHL funnel templates
- `references/template-mapping.md` — Cross-platform template equivalence map
- `references/api-cheatsheet.md` — API endpoint quick reference for all 3 platforms
- `scripts/connect-ghl.sh` — GoHighLevel connection & verification
- `scripts/connect-stackbase.sh` — GoStackBase connection & verification
- `scripts/connect-buildos.sh` — BuildwithOS connection & verification
