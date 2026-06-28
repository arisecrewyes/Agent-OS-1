# ADRS v3 Internal Architecture — Deep Analysis

**Source:** AI Delta Response System v3 - TEMPLATE.json (from Google Drive)
**Date:** 2026-06-28

---

## ADRS v3 Workflow: 60 Nodes

### AGENT NODES (3)

1. **AI Agent Bench** — Testing/benchmarking agent (not production)
2. **AI Agent** — **MAIN PRODUCTION AGENT** (conversation handler)
3. **Follow Up Agent** — **FOLLOW-UP PRODUCTION AGENT** (proactive outreach)

### AI TOOLS (6 tools available to agents)

Each tool is an `httpRequestTool` node that the AI agent can call during conversations:

1. **dnd_contact tool**
   - **API:** `PUT https://services.leadconnectorhq.com/contacts/{contact_id}`
   - **Headers:** Accept, Version (2021-07-28), Authorization (Bearer + Private Integration)
   - **Body:** `{"tags": ["dnd gpt"]}`
   - **Trigger:** User says they don't want messages two times
   - **Response:** "No worries, we will remove you from our list, thank you"

2. **book_appointment tool**
   - **API:** `POST https://services.leadconnectorhq.com/calendars/events/appointments`
   - **Headers:** Accept, Authorization, Version (2021-04-15), Content-Type
   - **Params:** startTime (ISO 8601), calendarId (from Edit Fields)
   - **Rules:** Must use get_calendar_slots first. Cannot cancel/reschedule (escalate to human).

3. **get_calendar_slots tool**
   - **API:** `GET https://services.leadconnectorhq.com/calendars/{calendar_id}/free-slots`
   - **Params:** startDate (millis epoch), endDate (millis epoch)
   - **Headers:** Accept, Version (2021-07-28), Authorization
   - **Rules:** Always use before booking. If only traceId returned = no slots available.

4. **future_follow_up tool**
   - **API:** `POST https://services.leadconnectorhq.com/calendars/events/appointments`
   - **Headers:** Accept, Version (2021-07-28), Authorization, Content-Type
   - **Params:** startTime (AI-generated datetime), calendarId
   - **Rules:** Default 10am unless user prefers different time. Always confirm date first.

5. **human_escalation tool**
   - **API:** `POST https://services.leadconnectorhq.com/contacts/{contact_id}/tags`
   - **Headers:** Accept, Version (2021-07-28), Authorization
   - **Body:** `{"tags": ["human"]}`
   - **Trigger:** AI can't resolve or user requests escalation

6. **knowledge_database tool** (vectorStoreInMemory)
   - **Mode:** retrieve-as-tool
   - **Tool Name:** knowledge_base
   - **Description:** "Retrieve information about X"
   - **Purpose:** RAG — AI queries vector store during conversation

### LLM MODELS (4)

1. **Anthropic Chat Model** — Primary LLM for Main Agent
2. **Anthropic Chat Model1** — Backup/fallback for Main Agent
3. **Anthropic Chat Model2** — For Follow-Up Agent
4. **Google Gemini Chat Model** — Primary Gemini for Main Agent
5. **Google Gemini Chat Model1** — Backup Gemini for Main Agent

### INFRASTRUCTURE NODES

- **Webhook** — Entry point (receives messages from GHL)
- **Message Key?** (Switch) — Routes based on message type
- **Status / Status2** (Switch) — State machine switches
- **Wait 1 minute / Wait 12 Seconds** (Wait) — Multi-message intelligence delay
- **Edit Fields** (Set) — Prepares data (timezone, private_integration key, calendar_id, etc.)
- **Create Message / Get full message / Update message** (dataTable) — Message buffer for multi-message gathering
- **Chat History** (memoryBufferWindow) — Conversation memory (buffer window)
- **Get Custom Fields** (httpRequest) — Fetches contact custom fields from GHL API
- **Retry Count / If / Stop and Error** — Error handling with retry limits
- **Scrape ID** (Code) — Extracts data from webhook payload
- **Update Assistant Chat Last Message** (httpRequest) — Writes AI reply back to GHL

### COMPLETE API ENDPOINTS USED

| Endpoint | Method | Purpose |
|---|---|---|
| `services.leadconnectorhq.com/contacts/{id}` | PUT | Add DND tag |
| `services.leadconnectorhq.com/contacts/{id}/tags` | POST | Add tags (human escalation) |
| `services.leadconnectorhq.com/calendars/{id}/free-slots` | GET | Check availability |
| `services.leadconnectorhq.com/calendars/events/appointments` | POST | Book appointment |
| `services.leadconnectorhq.com/contacts/{id}` | GET | Get custom fields |

### AUTH PATTERN (Confirmed)

All API calls use:
```
Authorization: Bearer {{ $('Edit Fields').item.json.private_integration }}
Version: 2021-07-28  (or 2021-04-15 for calendar events)
Accept: application/json
```

The `private_integration` value is pulled from the `Edit Fields` node which processes webhook data. This confirms:
- **Private Integration Key is stored as a variable in the n8n workflow**
- **Location/contact ID comes from the webhook payload sent by GHL**
- **All API calls go to `services.leadconnectorhq.com`** — shared across all LC derivatives

### MULTI-MESSAGE INTELLIGENCE MECHANISM

1. GHL sends webhook to n8n
2. Message stored in dataTable buffer
3. **Wait 12 seconds** — gives user time to send multiple messages
4. All buffered messages combined into single input
5. AI processes combined message as one
6. Single response sent back

### FOLLOW-UP AGENT

- Separate agent node with its own LLM models
- Input: "follow up" text
- Has access to same tools as Main Agent
- Triggered by GHL workflow (scheduled follow-up)
- Has full chat history context via Chat History memory

### HUMAN ESCALATION TAG

- Tag added: `human` (NOT "human handoff" — specifically `human`)
- This adds the tag to the contact in GHL
- GHL workflow then triggers notification to human
