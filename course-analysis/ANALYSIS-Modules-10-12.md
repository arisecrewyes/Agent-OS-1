# Course Analysis: Copy My AI Agency — Modules 10-12

**Analyzed:** 2026-06-28
**Module Range:** 10 (Free Client Acquisition) + 11 (Meta Ads) + 12 (Client Onboarding)
**Course Creator:** Zalo Kabche

---

## Module 10: Getting Clients for Free (Organic Acquisition)

**Core Strategy: Warm outreach first.**
- "If you already have clients for other services, they are going to be the easiest to sell to."

**Two Outreach Methods:**
1. **WARM Private Beta Outreach** — Target existing clients/contacts
2. **Cold Outreach Strategy** — Reach new prospects

**Referenced Assets (not received):**
- Cold Message Outreach Example.png
- [NEW] WARM Private Beta Outreach.pdf
- The Private Beta Cold Outreach Strategy.pdf

**Insight for Universal SOP:** The sales process is separate from the technical integration. The universal SOP should include a "Business Launch" section covering: sales scripts, pricing, outreach templates, and client acquisition strategies — but these are platform-agnostic (not specific to any LC platform).

---

## Module 11: Meta Ads (Paid Client Acquisition)

**Full Campaign Link:** https://go.blackumbrella.app/shared/campaign/aac8bf9c-e7ce-4647-a181-9f35a007cccc

**AI Marketing Platform:** https://blackumbrella.app/

**16 Ad Creative Examples** (ad1.png through ad16.png)
**Meta Ads Copy.pdf** — Ad copy templates

**New Platform Discovered: Black Umbrella**
- URL: blackumbrella.app
- Purpose: AI-powered marketing/ad management platform
- Used for: Creating and managing Meta (Facebook/Instagram) ad campaigns
- Has campaign sharing functionality

**Insight for Universal SOP:** Paid acquisition is another business-layer component. The Black Umbrella platform could be integrated into n8n workflows for automated ad management, but this is an extension beyond the core LC↔n8n bridge.

---

## Module 12: Full Client Onboarding Walkthrough — ⭐ CRITICAL OPERATIONAL MODULE

This is the operational playbook that bridges sale → live system. Contains complete SOPs, legal, and QA.

### 12.1: Visual Workflow (Mural)
- https://app.mural.co/t/dw4563/m/dw4563/1769359302911/
- Visual representation of the entire onboarding flow

### 12.2: New Client Onboarding Playbook
- **Google Doc:** https://docs.google.com/document/d/15INsHJA2t-tJZOJgAsOUdobIq-bDJ89KxvGEdoqj3GQ/edit
- **Purpose:** Step-by-step guide from signed contract to live AI system
- **Covers:**
  - Creating client's WhatsApp group
  - Sending welcome messages
  - Running strategy call
  - Launching bot
  - All steps include copy/paste scripts

### 12.3: AI Onboarding Questionnaire
- **Google Doc:** https://docs.google.com/document/d/1O40S2aA3kIFkZSug3qOXDff6hNHSCUuE/edit
- **Purpose:** Intake form sent to every new client
- **Collects:**
  - Business info
  - Pricing details
  - Operating hours
  - Tone preferences
  - FAQs
  - Objection handling
  - More...
- **Key Insight:** Quality of bot = quality of questionnaire responses. The questionnaire IS the prompt engineering data.
- Send immediately after sale closes
- Required vs optional sections clearly marked

### 12.4: Internal AI System Pre-Launch Testing Checklist
- **Google Doc:** https://docs.google.com/document/d/1eKrnRAVLSAml5WCnvagotXhbQkTjErOHmEBzIpvTVYY/edit
- **Purpose:** QA checklist before going live
- **Covers:**
  - Setup verification
  - Channel connectivity
  - Conversation testing
  - Quality checks
  - Go-live readiness
- 🔴 Items = blockers (bot CANNOT launch until those pass)
- **Critical for Universal SOP:** This testing checklist pattern applies to ANY LC platform integration

### 12.5: AI Service Agreements (Legal)

**Two versions:**
1. **WITHOUT Voice AI:** https://docs.google.com/document/d/1j7T1e1oNL2aVzw5M4YYstW4nUFI3LDkGVxAf-MrrOJA/edit
2. **WITH Voice AI:** https://docs.google.com/document/d/1SVtD3KVJDQR-3FVvyj3T9_GwvUocrf7RXEChMlenZ7o/edit

**Covers:**
- Payment terms
- Client responsibilities
- Late deliverable penalties
- IP ownership
- Liability limits
- Termination clauses
- Part A: Legal terms (rarely changes)
- Part B: Statement of Work (package details, timelines)

**Get signed BEFORE starting any work.**

### 12.6: GHL Bot Control Tutorial

**Video walkthrough for CLIENTS** explaining how to manage their AI in GHL.

**Key Operational Details:**

1. **Conversations Tab:**
   - Shows all pro client conversations
   - Filter by: recent, unread, channel (Instagram, FB, SMS)
   - Contacts with `AI opt in` tag = actively engaging with bot
   - Channel tags visible: Instagram tag, Facebook tag, SMS tag

2. **Bot Control Tag:**
   - To stop bot from talking to a lead: Add tag `dndgpt` (exact spelling required)
   - This is the manual override / kill switch
   - **Pattern: Single tag controls bot engagement per-contact**

3. **Client Empowerment:**
   - Clients can monitor AI conversations
   - Clients can pause bot on any conversation
   - Send this tutorial to clients after launch

**NEW TAG DISCOVERED:**
- `dndgpt` — Do Not Disturb GPT. Manual bot kill switch per contact
- `AI opt in` — Contact actively opted into AI conversation
- Channel tags: Instagram, Facebook, SMS (identifies source channel)

---

## CRITICAL ARCHITECTURE DISCOVERY: The Complete Tag System

After analyzing all modules, here's the complete tag taxonomy:

### State Management Tags
| Tag | Purpose | Set By | Removed By |
|---|---|---|---|
| `AI opt in` | Contact opted into AI conversation | GHL Workflow (form submit) | Human handoff or DND |
| `dndgpt` | Manual bot kill switch per contact | Human (client/agent) | Manual removal only |
| `ai demo optin` | Contact opted into AI Demo | GHL Demo workflow | AI Demo completion or ADRS opt-in |

### Channel Demo Tags
| Tag | Purpose |
|---|---|
| `ai voice demo` | Currently in AI Voice demo |
| `ai voice demo completed` | Completed AI Voice demo |
| `live chat demo` | Currently in Live Chat demo |
| `sms demo` / `SMSDemo` | Currently in SMS demo |
| `whatsapp` | Currently in WhatsApp demo |

### Channel Source Tags
| Tag | Purpose |
|---|---|
| `Instagram` | Contact came from Instagram |
| `Facebook` | Contact came from Facebook |
| `SMS` | Contact came from SMS |

### Tag Management Rules:
1. **Always remove previous demo tags before setting new ones** (prevents crossover)
2. **Demo tags are ACTIONS, not triggers** (triggers use FormSubmitted + FormIs)
3. `dndgpt` overrides all other tags (highest priority kill switch)
4. Cross-system coordination: ADRS and Demo system share/compete for tags

---

## ONBOARDING FLOW (Complete)

```
SALE CLOSED
    │
    ▼
1. Send AI Service Agreement (get signed)
    │
    ▼
2. Collect Payment
    │
    ▼
3. Send AI Onboarding Questionnaire
    │  (Collects: business info, pricing, hours, tone, FAQs, objections)
    │
    ▼
4. Create Client WhatsApp Group
    │  (Welcome messages via copy/paste scripts)
    │
    ▼
5. Run Strategy Call
    │  (Review questionnaire, align expectations)
    │
    ▼
6. Build AI System
    │  - Create GHL sub-account (push snapshot)
    │  - Configure n8n workflows (ADRS + Demo)
    │  - Input questionnaire data into system prompt
    │  - Configure channels (SMS, WhatsApp, IG, FB, Live Chat)
    │  - Set up calendar/booking
    │  - Configure A2P compliance
    │
    ▼
7. Pre-Launch Testing (QA Checklist)
    │  - Setup verification
    │  - Channel connectivity
    │  - Conversation testing
    │  - Quality checks
    │  - 🔴 Blockers must pass
    │
    ▼
8. Go Live
    │  - Remove test tags
    │  - Activate workflows
    │  - Send GHL Bot Control Tutorial to client
    │
    ▼
9. Monitor & Iterate
    - Client monitors via Conversations tab
    - `dndgpt` tag for manual override
    - Prompt tuning based on real conversations
```

---

## COMPLETE CUSTOM VALUES REFERENCE (GHL)

| Custom Value | Purpose | Set In |
|---|---|---|
| `agency_logo` | Company logo URL | GHL Setup |
| `privacy policy url` | Legal compliance link | GHL Setup |
| `tos url` | Terms of service link | GHL Setup |
| `legal company name` | A2P compliance | GHL Setup |
| `ai_demo_webhook` | n8n AI Demo webhook URL | n8n Setup |
| `magic link` (custom FIELD) | Per-contact demo link | n8n (auto-populated) |

---

## GAP ANALYSIS (Cumulative, Updated)

### Filled by Modules 10-12:
- [x] Onboarding process end-to-end
- [x] Legal framework (service agreements)
- [x] QA/testing checklist pattern
- [x] `dndgpt` tag for bot control
- [x] `AI opt in` tag for engagement tracking
- [x] Questionnaire = prompt engineering data source
- [x] Client handoff process (GHL Bot Control Tutorial)

### Still Missing (Critical for Full System):
- [ ] **ADRS (AI Delta Response System) - the MAIN production chatbot workflow** (not just demo)
- [ ] **AI Voice Delta Response System** (production voice, not just demo)
- [ ] n8n workflow JSON internals (we know the 8 files but haven't analyzed their contents)
- [ ] How contact memory works in n8n
- [ ] Follow-up agent trigger mechanism
- [ ] Database Reactivation Campaign details
- [ ] How questionnaire data maps to system prompt
- [ ] How to create ADRS for a NEW client (customization process)
- [ ] Sub-workflow/tool connection to main agent
- [ ] OpenClaw / Hermes / Agent OS integration points

### Still Expected (Based on Course Outline):
- Module on ADRS (AI Delta Response System - AI Chatbot) — should contain the MAIN agent workflow
- Module on AI Voice Delta Response System — production voice agent
- Elite/upgrade content (referenced but not provided)
