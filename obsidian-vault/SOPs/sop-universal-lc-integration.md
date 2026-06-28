# SOP: Universal LC Platform Integration — n8n, OpenClaw, Hermes, Agent OS

**Created:** 2026-06-28
**Version:** 1.0
**Trigger:** User wants to connect n8n, OpenClaw, Hermes, or Agent OS to any Lead Connector platform
**Purpose:** Universal process for connecting any AI agent or workflow engine to any LC-type platform

---

## Overview

This SOP provides a **universal integration process** that allows any user to connect n8n, OpenClaw, Hermes Agent, Agent OS, etc. with any Lead Connector-type platform. The result: n8n workflows and AI agents can control, optimize, automate, create, and manage every function inside the user's chosen LC platform.

### What This Enables
- **n8n workflows** → trigger actions inside LC platforms (create contacts, send SMS, book appointments, update pipelines)
- **AI agents** (OpenClaw, Hermes, Claude Code) → read/write LC platform data, manage automations, build funnels
- **Agent OS** → orchestrate multi-platform operations across LC derivatives
- **Any combination** → chain agents, workflows, and platforms together

### The Core Discovery

**ALL LC derivatives share the same API infrastructure:**
- API Base URL: `https://services.leadconnectorhq.com`
- Same Private Integration system
- Same API v2.0
- Same OAuth2 framework
- Same webhook system

**This means:** An n8n workflow built for GHL works identically on GoStackBase, BuildwithOS, and any other LC derivative. Only the UI changes, not the API.

---

## Architecture

### The Universal Bridge

```
USER/LEAD → LC Platform (GHL/StackBase/BuildwithOS) ↔ n8n ↔ AI Agents
                ↑                                       ↑
                └── Webhook OUT → n8n ── API IN ───────┘
```

### Connection Methods

| Connection | Method | Direction | Auth |
|---|---|---|---|
| LC → n8n | LC Workflow Webhook Action → n8n Webhook Trigger | Outbound | n8n Webhook Production URL |
| n8n → LC | n8n HTTP Request node → LC REST API | Inbound | Private Integration Key + Location ID |
| LC → Retell | Phone number routing | Voice calls | Retell phone number |
| Retell → n8n | Outbound webhook | Call events | n8n Webhook Production URL |
| n8n → Retell | Inbound webhook on Retell | Call control | Retell Agent IDs |

---

## Phase 1: Platform Setup

### Step 1.1 — Choose the LC Platform

| Platform | Best For | Private Integration | Pricing |
|----------|----------|-------------------|---------|
| **GoHighLevel** | Full-featured agency CRM | ✅ ($297/mo or free 90 days) | $97-$297/mo |
| **LeadConnector** | Simplified GHL | ✅ | Similar to GHL |
| **GoStackBase** | Budget-friendly | ✅ (Premium+) | Lower than GHL |
| **BuildwithOS** | AI-native, MCP support | ✅ (Agent Key) | Higher affiliate payouts |

### Step 1.2 — Create Private Integration

**All LC platforms share the same process:**

1. Go to: Settings → Other Settings → Private Integrations
   - (If not visible: enable in Labs first)
2. Click "Create new Integration"
3. Name it (e.g., "n8n Integration" or "OpenClaw Bridge")
4. Select scopes/permissions (minimum needed):
   - Contacts: Read/Write
   - Conversations: Read/Write
   - Calendars: Read/Write
   - Workflows: Read/Write
   - Tags: Read/Write
   - Custom Fields: Read/Write
5. **COPY THE TOKEN** (shown only once)
6. Note your **Location ID** (Settings → Business Profile)

### Step 1.3 — Known GHL Bug

If Private Integration glitches or doesn't generate:
1. Delete browser cookies
2. Log out of GHL
3. Log back in
4. Try again

---

## Phase 2: n8n Setup

### Step 2.1 — n8n Hosting

n8n must be **self-hosted** (not n8n Cloud) for full webhook + API access.

**Recommended:** Hostinger VPS with Docker
- URL: https://www.hostinger.com/pricing/n8n-hosting
- Or self-install on any VPS with Docker

### Step 2.2 — Import Workflow Templates

Import the n8n workflow JSON templates into your n8n instance:

| # | Workflow | Purpose | File |
|---|----------|---------|------|
| 1 | Magic Link Generator | Creates unique demo links | `Magic Link Generator v2 - TEMPLATE.json` |
| 2 | AI Demo (SMS) | SMS-based AI chatbot demo | `AI Demo v4 - TEMPLATE.json` |
| 3 | Live Chat AI Demo | Live chat channel demo | `Live Chat AI Demo [TEMPLATE].json` |
| 4 | AI Voice Demo | Voice AI demo | `AI Voice Demo [TEMPLATE].json` |
| 5 | **ADRS v3** | **Main production chatbot** | `AI Delta Response System v3 - TEMPLATE.json` |
| 6 | Supabase Vector DB | RAG knowledge base | `Supabase Vector Database [RAG] - TEMPLATE.json` |
| 7 | Voice ADRS Inbound | Production voice agent | `AI Voice Delta Response System - Inbound [TEMPLATE].json` |
| 8 | Voice ADRS Outbound | Outbound voice calls | `AI Voice Delta Response System - outbound [TEMPLATE].json` |
| 9 | Voice ADRS Client | Client voice config | `AI Voice Agent - CLIENT [TEMPLATE].json` |

### Step 2.3 — Configure Credentials in Each Workflow

For each imported workflow:

1. **Open the workflow** in n8n
2. **Find the "Edit Fields" node** (or similar first node)
3. **Set these values:**
   - `private_integration` → Your Private Integration Key
   - `location_id` → Your Location ID
   - `calendar_id` → Your LC Calendar ID
   - `timezone` → Your timezone
4. **For voice workflows:** Add Retell AI agent IDs and phone number
5. **Save and activate** the workflow
6. **Copy the Webhook Production URL** from the Webhook trigger node

### Step 2.4 — Connect n8n to LC Platform

1. Take the **Webhook Production URL** from the n8n workflow
2. Go to your LC platform → Workflows → Webhook Action step
3. Paste the n8n Webhook URL
4. For API calls back to LC: n8n HTTP Request nodes use:
   ```
   Authorization: Bearer {{ private_integration_key }}
   Version: 2021-07-28
   Accept: application/json
   ```

---

## Phase 3: LC Platform Configuration

### Step 3.1 — Setup Steps

1. **Create sub-location** and push snapshot (if using a course snapshot)
2. **Activate Calendars:** Settings → Calendars → Activate
3. **Setup "Success Session" calendar:** Add team member, availability, Zoom link
4. **Integrate channels:** Settings → Integrations (FB Messenger, Instagram, WhatsApp)
5. **Add domain:** Settings → Domain (DNS: CNAME or A record)
6. **Upload logo:** Media Storage → copy URL → update `agency_logo` custom value
7. **Update custom values:**
   - `privacy policy url`
   - `tos url`
   - `legal company name` (must match tax returns for A2P)
   - `ai_demo_webhook` (n8n webhook URL)
8. **Update Business Profile:** Address, phone, email (email domain MUST match funnel domain)

### Step 3.2 — Custom Values Reference

| Custom Value | Purpose | Set In |
|---|---|---|
| `agency_logo` | Company logo URL | LC Settings |
| `privacy policy url` | Legal compliance | LC Settings |
| `tos url` | Terms of service | LC Settings |
| `legal company name` | A2P compliance | LC Settings |
| `ai_demo_webhook` | n8n AI Demo webhook URL | n8n → LC Settings |
| `magic link` (custom FIELD) | Per-contact demo link | n8n (auto-populated) |

### Step 3.3 — Tag Taxonomy

| Tag | Purpose | Set By |
|-----|---------|--------|
| `AI opt in` | Contact opted into AI conversation | LC Workflow |
| `dndgpt` | Manual bot kill switch (exact spelling) | Human |
| `ai demo optin` | Demo system opt-in | LC Demo workflow |
| `ai voice demo` | Currently in AI Voice demo | LC Demo workflow |
| `live chat demo` | Currently in Live Chat demo | LC Demo workflow |
| `SMSDemo` | Currently in SMS demo | LC Demo workflow |
| `whatsapp` | Currently in WhatsApp demo | LC Demo workflow |
| `Instagram` | Contact came from Instagram | LC (auto) |
| `Facebook` | Contact came from Facebook | LC (auto) |
| `SMS` | Contact came from SMS | LC (auto) |
| `human` | Escalation to human agent | n8n AI tool |

**Tag Rules:**
1. Tags are **state flags**, NOT triggers (triggers use FormSubmitted + FormIs)
2. Always **remove previous demo tags** before setting new ones
3. `dndgpt` overrides all other tags (highest priority kill switch)
4. Cross-system coordination: AI agents and LC workflows share tags

---

## Phase 4: AI Agent Setup

### Step 4.1 — LLM API Keys Required

| Service | Purpose | URL | Cost |
|---------|---------|-----|------|
| Anthropic (Claude) | Primary LLM | console.anthropic.com/settings/keys | Pay-per-use |
| Gemini (Google) | Backup LLM | aistudio.google.com/app/apikey | Free tier available |
| OpenAI (optional) | Additional LLM | platform.openai.com/api-keys | Pay-per-use |

### Step 4.2 — Dual LLM Configuration

In n8n, configure **Primary + Backup** LLM for each agent:

1. **Primary:** Claude 4.5 Sonnet (best reasoning, instruction following)
2. **Backup:** Gemini 3 Pro (if primary API errors or is rate-limited)
3. **Error handling:** If both fail → graceful error message to user

### Step 4.3 — AI Agent Tools

The AI agent has 6 tools it can use during conversations:

| Tool | API Endpoint | What It Does |
|------|-------------|-------------|
| `dnd_contact` | `PUT /contacts/{id}` | Adds `dndgpt` tag — contact opts out |
| `book_appointment` | `POST /calendars/events/appointments` | Books on LC calendar |
| `get_calendar_slots` | `GET /calendars/{id}/free-slots` | Checks availability |
| `future_follow_up` | `POST /calendars/events/appointments` | Schedules follow-up |
| `human_escalation` | `POST /contacts/{id}/tags` | Adds `human` tag — triggers handoff |
| `knowledge_database` | Vector store query | RAG knowledge retrieval |

### Step 4.4 — Multi-Message Intelligence

n8n gathers multiple messages within a time window before processing:

1. Contact sends message → LC webhook → n8n
2. Message stored in buffer
3. **Wait 12 seconds** (configurable)
4. All buffered messages combined into single input
5. AI processes combined message → single response
6. Response sent back to LC → routed to correct channel

---

## Phase 5: Voice AI Setup (Optional)

### Step 5.1 — Retell AI Platform

Retell AI is a **separate platform** for voice AI (not built into LC or n8n).

1. Create account: https://www.retellai.com/
2. **KYC verification required** for outbound calling: docs.retellai.com/accounts/kyc
3. Buy a phone number
4. Import agent configurations (JSON templates)
5. Add phone number to orchestrator agent
6. Publish agents

### Step 5.2 — Voice Architecture

```
Contact calls business phone number
    → Retell AI answers
    → Orchestrator Agent (multi-lingual router)
        → English Agent / Spanish Agent
    → Inbound Webhook → n8n
    → n8n processes (LC API calls, AI reasoning)
    → Outbound Webhook → Retell AI
    → AI speaks response to caller
    → Post-call: LC creates conversation record, tags, follow-up triggers
```

### Step 5.3 — Voice Prompt Engineering

Voice prompts differ from text prompts:
- **Shorter responses** (people don't want to listen to long AI speeches)
- **Natural speech patterns** (avoid robotic phrasing)
- **Turn-taking awareness** (know when to pause for user response)
- **Pronunciation guidance** for business-specific terms
- **Tone of voice** instructions (warm, professional, etc.)
- **Emergency escalation** patterns (when to transfer to human immediately)

---

## Phase 6: A2P / SMS Compliance (US)

### Step 6.1 — Pre-Registration Checklist

- [ ] Menu link says "pricing" not "investing" (old snapshot issue)
- [ ] Phone number NOT required on forms
- [ ] T&C format updated on forms
- [ ] Website works on both `www` and non-`www`
- [ ] Root domain is compliant (not broken, parked, or mismatched)
- [ ] Footer has legal company name + brand name (if DBA)
- [ ] Calendar is active with team member added

### Step 6.2 — The Root Domain Trap

Reviewers check the **root domain**, not the subdomain.
- `app.client.com` → they check `client.com`
- If root is broken → **REJECTED**

**Workarounds:**
1. **301 redirect** root → compliant funnel (free)
2. **Buy new domain** (~$12) with funnel on root

### Step 6.3 — Brand Registration

**New LLCs:** Wait 15 days for third-party databases to update, OR register as Sole Proprietor first.

**LLC Rules:**
- Legal Business Name must match IRS/SS-4/Tax docs CHARACTER FOR CHARACTER
- EIN/Tax ID: single wrong digit = rejection
- Business Address must match EIN registration address

**Sole Proprietor Rules:**
- Legal Business Name = Full Legal Name (unless DBA filed)
- Mobile number: personal only (NO VoIP)
- Physical address: valid location, not P.O. Box

### Step 6.4 — Campaign Registration

**Use Case Template:**
> This messaging campaign is used by [LEGAL COMPANY NAME] to send text messages to individuals who have voluntarily opted in to receive updates, service information, scheduling communications, and relevant announcements.

**Sample Message 1:**
> Hello, this is a team member from [LEGAL COMPANY NAME] reaching out regarding your recent inquiry. Let us know if you'd like to continue the conversation. Reply STOP to opt out.

**Sample Message 2:**
> Hi from [LEGAL COMPANY NAME]. This message is to confirm your upcoming scheduled session. If you need assistance, reply directly. Reply STOP to unsubscribe.

**Opt-in Method:** Website form
**Register for:** Low Volume Standard

### Step 6.5 — A2P Wizard

Tool: https://a2pwizard.com/?ref=copymyaiagency
- Generates compliant website + compliance kit + all messaging
- Supports: LOCAL, TOLL FREE, TWILIO, SOLE PROP registrations
- Provides: use case, sample messages, opt-in description, privacy policy, T&C

---

## Phase 7: Testing & Verification

### Step 7.1 — Connection Test

1. **Webhook test:** Trigger a test event in LC → verify n8n receives it
2. **API test:** n8n creates a test contact in LC → verify it appears
3. **Round-trip test:** LC → n8n → LC → verify data integrity

### Step 7.2 — Channel Test

For each communication channel:
1. **SMS:** Send test message → verify receipt → test STOP opt-out
2. **WhatsApp:** Send template message → verify delivery
3. **Live Chat:** Send test message → verify bot response
4. **Voice:** Make test call → verify agent answers and responds correctly

### Step 7.3 — AI Agent Test

Test all 6 AI tools:
1. **DND:** Tell bot "stop messaging me" → verify `dndgpt` tag added
2. **Booking:** Ask to book appointment → verify calendar event created
3. **Calendar slots:** Ask for availability → verify correct slots returned
4. **Follow-up:** Request future follow-up → verify scheduled
5. **Escalation:** Say "I want to speak to a human" → verify `human` tag added
6. **Knowledge:** Ask a question from RAG → verify accurate response

### Step 7.4 — Pre-Launch QA Checklist

- [ ] API key validated & working
- [ ] Correct model (Claude Sonnet 4.5)
- [ ] Auto-recharge enabled
- [ ] System prompt loaded correctly
- [ ] Calendar integration connected
- [ ] SMS: send/receive, A2P active, STOP works
- [ ] All conversation scenarios tested
- [ ] No hallucinations in AI responses
- [ ] Test data removed
- [ ] Client approval received

---

## API Quick Reference

### LC Platform V2 REST API
```
Base: https://services.leadconnectorhq.com
Auth: Bearer {PRIVATE_INTEGRATION_KEY}
Headers: Version: 2021-07-28, Accept: application/json