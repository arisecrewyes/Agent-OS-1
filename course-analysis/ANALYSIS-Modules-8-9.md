# Course Analysis: Copy My AI Agency — Modules 8-9

**Analyzed:** 2026-06-28
**Module Range:** 8 (AI Agency Setup - FULL TECHNICAL SETUP) + 9 (Sales/Getting First Client)
**Course Creator:** Zalo Kabche

---

## Module 8: AI Agency Setup — THE CORE TECHNICAL MODULE

This is the most technically dense module. Complete setup sequence from zero to working AI agency.

---

### 8.1: Important Information (Setup Order)

**Setup sequence MUST be followed in order:**
1. Pre-requisites
2. GHL Setup
3. n8n Setup
4. A2P Approval

**Not optional.** Each step depends on the previous.

---

### 8.2: Pre-requisites

**Required Accounts/APIs:**

| Requirement | URL | Purpose | Cost |
|---|---|---|---|
| GHL Account ($297/mo OR 90-day free) | copymyaiagency.com/free-ghl | LC Platform - must support Private Integrations | $297/mo or free 90 days |
| Gemini API Key | aistudio.google.com/app/apikey | Backup LLM for ADRS | Free tier available |
| Anthropic API Key | console.anthropic.com/settings/keys | Primary LLM for ADRS | Pay-per-use |
| OpenAI API Key (Optional) | platform.openai.com/api-keys | Additional LLM option | Pay-per-use |
| n8n (Private Hostinger VPS) | (link in course) | Workflow engine - SELF-HOSTED | VPS cost |
| Claude AI Account | (link) | Prompt development/copywriting | $20/mo |
| Stripe Account | (link) | Accept payments/deposits | Free + transaction fees |

**CRITICAL DISCOVERIES:**
- GHL $97/mo accounts **NO LONGER ALLOW Private Integrations** - must have $297/mo OR use CMAA 90-day free account
- **Private Integrations = Custom API connections** (this is how n8n connects to GHL)
- n8n is **SELF-HOSTED on a Hostinger VPS** (not n8n Cloud)
- User controls infrastructure, no vendor lock-in on workflow engine side

**Architecture Implication for Universal SOP:**
- Any LC platform that supports custom webhooks/API connections can replace GHL
- "Private Integration" maps to: API keys, OAuth, webhook integrations on any LC platform
- Self-hosted n8n is the bridge - it can connect to anything with an API

---

### 8.3: GHL Setup

**Step-by-step setup process:**

1. **Create GHL sub-location and push snapshot**
   - Snapshot v46 (latest at time of course)
   - Snapshot contains: ALL workflows, forms, funnels, tags, custom values, custom fields
   - **Pattern: Snapshot = Full System Deployment** - not just templates

2. **Activate GHL Calendars** (Settings > Calendars > 3 dots > Activate)

3. **Setup "Success Session" calendar** (team member, availability, Zoom link)

4. **Integrate FB Messenger and Instagram** (Settings > Integrations)
   - **Pattern: Channel integrations configured in LC platform, not n8n**

5. **Add domain to AI Agency funnel** (Settings > Domain, DNS config required)

6. **Upload company logo -> update `agency_logo` custom value**
   - **Pattern: Custom Values = System-wide configuration variables (like env vars)**

7. **Update custom values (3 required):**
   - `privacy policy url`
   - `tos url`
   - `legal company name`

8. **Update Business Profile**
   - Email domain MUST match funnel domain (critical for A2P)

**Key Custom Values Identified:**
- `agency_logo` - company logo URL
- `privacy policy url` - legal compliance
- `tos url` - legal compliance
- `legal company name` - A2P compliance
- `ai_demo_webhook` - **n8n webhook URL for AI Demo**
- `magic link` - custom FIELD (not value) for per-contact magic demo links

**Pattern: GHL Custom Values = Environment Variables for the system**
They store: API endpoints, legal URLs, branding, compliance info - all referenced by workflows dynamically.

---

### 8.4: n8n Setup + SMS AI Demo

**THE n8n-to-GHL CONNECTION SETUP - CRITICAL FOR UNIVERSAL SOP**

**Known GHL Bug:** Private Integration may glitch - delete browser cookies, log out, log back in.

**Setup Steps:**

1. **Load n8n workflows** (JSON files imported into n8n)
   - AI Demo v4 - TEMPLATE.json
   - Magic Link Generator v2 - TEMPLATE.json

2. **Setup "Magic Link Generator" n8n workflow**
   - Follow notes INSIDE the workflow (embedded documentation)
   - **Output: Webhook Production URL** - this URL is the bridge

3. **Connect n8n to GHL: Magic Link**
   - Take Webhook Production URL from "Magic Link Generator" n8n workflow
   - Paste into "Generate Magic Link" GHL workflow Webhook step
   - **Pattern: n8n Webhook URL + GHL Workflow Webhook Action = Connection established**

4. **Update landing page URL in "Send Magic Link" GHL workflow**
   - Change `www.website.com` to your actual domain

5. **Setup AI Demo n8n workflow**
   - Follow notes inside the workflow
   - Dual LLM configuration: Primary (Claude/Gemini) + Backup
   - System prompt from AI Demo System Prompt.md

6. **Connect n8n to GHL: AI Demo**
   - Take Webhook Production URL from AI Demo n8n workflow
   - Paste into GHL Custom Value `ai_demo_webhook`

**THE UNIVERSAL BRIDGE PATTERN:**

```
GHL WORKFLOW                          n8n WORKFLOW
                                      
Trigger (FormSubmitted)               Webhook Trigger (Production URL)
         |                                     |
         v                                     v
Webhook Action -------[URL]--------->  Receive payload
(POST to n8n URL)                              |
                                               v
                                       Process (LLM/API/etc)
                                               |
                                               v
<--------[GHL API]-------------------  GHL API Call
Update contact/tag/etc                  (POST back to GHL)
```

**TWO connection methods:**
1. **GHL -> n8n:** GHL Webhook Action (POST to n8n Production URL)
2. **n8n -> GHL:** n8n HTTP Request node using GHL Private Integration API

**n8n Workflow Files:**
| Workflow | File | Purpose |
|---|---|---|
| Magic Link Generator | Magic Link Generator v2 TEMPLATE.json | Creates unique demo URLs |
| AI Demo (SMS) | AI Demo v4 TEMPLATE.json | SMS-based AI chatbot demo |
| AI Demo System Prompt | AI Demo System Prompt.md | Prompt for AI demo agent |
| Live Chat AI Demo | Live Chat AI Demo TEMPLATE.json | Live chat channel demo |
| AI Voice Demo | AI Voice Demo TEMPLATE.json | Voice AI demo (Retell AI) |
| AI Voice (ENG) | AI Voice Demo Bot (ENG).json | English voice agent (Retell) |
| AI Voice (ESP) | AI Voice Demo Bot (ESP).json | Spanish voice agent (Retell) |
| Orchestrator | Orchestrator AI Demo Multi-lingual.json | Routes voice to language agent |

---

### 8.5: LIVE Chat AI Demo Setup

- Requires base n8n setup first (uses Magic Link Generator)
- Same connection pattern: n8n Webhook URL -> GHL custom value

---

### 8.6: AI Voice Demo Setup

**NEW PLATFORM: Retell AI** (retellai.com)
- AI Voice agent platform - separate from GHL and n8n
- **THIRD platform in the stack** - handles voice AI specifically

**Retell AI Setup:**
1. Create account, import 3 demo agents
2. Select ESP and ENG agents inside orchestrator's transfer nodes + individual agents' transfer functions
3. Add billing card, buy phone number
4. Add phone number to Orchestrator agent
5. Publish all agents

**GHL Setup for Voice:**
1. Update URL in "Send Magic Link" with correct domain
2. Add n8n Magic Link Generator Webhook URL -> GHL workflow "[AI Voice] Generate Magic Link"
3. Add Retell AI phone number to landing page button (text + target)

**n8n Setup for Voice:**
1. Get GHL Private Integration Key + Location ID -> Add to "Get Custom Field ID V2" node
2. Run "Execute Workflow" from Manual -> Get custom field IDs for "Company Type" and "Demo Context"
3. Add custom field IDs to "Edit Fields" / "Edit Fields1" + Private Integration Key + Location ID
4. Add inbound Webhook URL -> Retell phone number
5. Add outbound Webhook URL -> All demo agents
6. Add Orchestrator agent ID -> "Dynamic Info" node
7. Add timezone in workflow settings
8. Save and Publish

**CRITICAL - GHL Private Integration:**
- Uses **Private Integration Key** (not OAuth, not standard API key)
- Requires **Location ID** (sub-account specific)
- n8n uses HTTP Request nodes with these credentials to call GHL API
- Custom Fields accessed by their IDs (fetched dynamically)

**Voice Architecture:**
```
CONTACT (Phone Call) -> Retell AI (Voice Platform)
  -> Orchestrator (Multi-lingual router)
    -> English Agent / Spanish Agent
  -> Inbound Webhook <- n8n
  -> Outbound Webhook -> n8n
-> n8n (AI Voice Demo workflow)
  -> GHL API calls (custom fields, tags, contacts)
-> GHL (Contact management, CRM, follow-up)
```

---

### 8.7: A2P Approval

**A2P = Application-to-Person (10DLC SMS compliance - US requirement)**

**2026 Updates:**
- Dynamic form checkboxes matching website content
- Marketing + Non-Marketing consent with opt-out language
- Privacy Policy now needs: Cookie disclosure, Message Frequency
- Terms need: Age Restriction (18+)

**A2P Wizard Tool:** https://a2pwizard.com/?ref=copymyaiagency
- Generates compliant website + compliance kit + all messaging
- Register for **Low Volume Standard** (not High Volume)

**A2P Steps:**
1. Verify business info matches legal paperwork
2. Generate compliance kit at a2pwizard.com
3. GHL Trust Center -> Start brand registration
4. EIN, area of operation, authorized representative
5. Register for Low Volume Standard
6. Copy/paste use case, sample messages from wizard
7. Optin method: Website form -> paste wizard URL
8. Business website: same wizard URL
9. Copy/paste opt-in description and message
10. Submit and confirm

**Must purchase phone number BEFORE submitting A2P**

**For Universal SOP: A2P is US-specific. Different countries = different compliance. The PATTERN (legal name, compliant website, opt-in) is universal.**

---

### 8.8: WhatsApp AI Demo Setup

**Requires base n8n setup first**

**Steps:**
1. Create WA message template (opt-in confirmation with "START" reply)
2. Update GHL Workflow: [WhatsApp] AI Demo Bot - Base Triggers - (AI Reply) - add WA message step
3. Update GHL Workflow: Send Magic Link - add WA template ai_demo_start
4. Update GHL Workflow: [WhatsApp] Generate Magic Link - add Magic Link Generator Webhook URL

**Pattern: Each channel demo follows identical structure:**
Channel template -> GHL workflow trigger -> n8n Magic Link -> AI Demo workflow -> Channel reply

---

## Module 9: Getting Your First Client + Sales

**Database Reactivation:** Use ADRS to reactivate old leads for clients

**Sales Assets (not received, listed for reference):**
- Top Biz to sell AI chatbots to.pdf
- Sales Flow.png
- AI Chatbot Sales Process.pdf
- AI Chatbot VSL Example.pdf
- ai delta response infographic.png
- AI VSL CMAA.mp4
- MIT Study on LeadGen.pdf
- Pricing Models - AI Chatbots.pdf
- Pricing Tiers.png
- AI Chatbots - Pricing Tiers.pdf

**Not critical for technical SOP but useful for business model documentation.**

---

## COMPLETE SYSTEM ARCHITECTURE (After Modules 8-9)

```
CONTACT / LEAD
SMS | WhatsApp | Instagram DM | FB Messenger | Live Chat | Phone Call
     |              |                |              |           |        |
     +--------------+----------------+--------------+-----------+--------+
                                   |
                                   v
                     GoHighLevel (LC Platform)
                     - Receives messages via native channels
                     - Routes to workflows based on triggers
                     - Manages contacts, tags, custom fields
                     - Handles calendar/booking
                     - Manages SMS compliance (A2P)
                                   |
                    +--------------+--------------+
                    |                             |
             Webhook OUT                    Webhook OUT
             (GHL -> n8n)               (GHL -> Retell AI)
                    |                             |
                    v                             v
              n8n (Self-Hosted)           Retell AI
              - AI Demo Agent             - Voice AI Agents
              - Magic Link Generator      - Orchestrator + EN + ES
              - Main Chat Agent (ADRS)    - Phone number mgmt
              - Follow-Up Agent (ADRS)              |
              - Sub-workflows/tools                  |
                    |                    Webhook IN/OUT
                    |                         |
                    +------------+------------+
                                 |
                          n8n Voice Demo
                          - GHL API integration
                          - Custom field read/write
                          - Contact context
                                 |
                          API Call Back
                                 |
                                 v
                     GoHighLevel (Update)
                     - Tags, custom fields
                     - Contact properties
                     - Calendar bookings
                     - DND status
                     - Internal notifications
```

---

## AUTH & CONNECTION REFERENCE (Complete)

| Connection | Method | Credentials Needed | Direction |
|---|---|---|---|
| GHL -> n8n | Webhook Action in GHL Workflow | n8n Webhook Production URL | Outbound |
| n8n -> GHL | GHL Private Integration API | Private Integration Key + Location ID | Inbound |
| Retell AI -> n8n | Outbound Webhook | n8n Webhook Production URL | Inbound to n8n |
| n8n -> Retell AI | Inbound Webhook on Retell | Retell Agent IDs | Outbound to Retell |
| GHL -> Retell | Phone number routing | Retell phone number | Voice calls |

---

## UNIVERSAL SOP PATTERNS EXTRACTED

### Pattern 1: Environment Variables via Custom Values
- LC platform stores system config as "custom values" / "custom fields"
- Workflows reference these dynamically (not hardcoded)
- **Universal:** Any LC platform with custom fields can do this

### Pattern 2: Webhook Bridge (LC -> n8n)
- LC workflow sends POST to n8n Webhook Production URL
- n8n processes, calls LC API back with result
- **Universal:** Any LC platform with webhook actions + REST API

### Pattern 3: Per-Channel Demo Architecture
- Each demo channel gets: Form + Funnel Step + Tag + Workflow + n8n workflow
- Channel template triggers LC workflow -> calls n8n -> AI processes -> LC routes reply
- **Universal:** Any LC platform with multi-channel support

### Pattern 4: Snapshot/Template Deployment
- Entire system deployable as a snapshot/template
- Version-controlled, push to client sub-accounts
- **Universal:** LC platforms with sub-account + snapshot features

### Pattern 5: State Management via Tags
- Tags = state flags (not triggers)
- Always clean previous state before setting new state
- Cross-system coordination via shared tags
- **Universal:** All LC platforms support tags/labels

### Pattern 6: Dual LLM Fallback
- Primary LLM + Backup LLM in n8n
- If primary errors -> backup takes over
- If both error -> error handling path
- **Universal:** n8n supports this regardless of LC platform

### Pattern 7: A2P/SMS Compliance Pipeline
- Legal entity verification -> compliant website -> carrier registration -> approval
- **Universal:** US-specific 10DLC pattern, adapt per country

---

## Gap Analysis (Cumulative, Updated)

### Filled by Module 8:
- [x] GHL API authentication -> Private Integration Key + Location ID
- [x] n8n credential setup for GHL -> HTTP Request node with Private Integration
- [x] Webhook connection pattern -> GHL Webhook Action + n8n Webhook Production URL
- [x] n8n workflow files identified -> 8 JSON templates + system prompt
- [x] A2P compliance process -> A2P Wizard + GHL Trust Center

### Still Missing:
- [ ] **ADRS (AI Delta Response System) internals** - the MAIN chatbot agent workflow (not just demo)
- [ ] n8n workflow JSON content analysis (we know the files but haven't seen inside them)
- [ ] How contact memory works in n8n (stored where? format?)
- [ ] Follow-up agent trigger mechanism (GHL scheduled? n8n cron?)
- [ ] Sub-workflow/tool connection to main agent
- [ ] Human handoff notification details
- [ ] Database Reactivation Campaign details
- [ ] AI Voice Delta Response System (separate from demo)
- [ ] How prompts use GHL custom field data as context
- [ ] OpenClaw / Hermes integration points (not in this course - we'll need to research)

These should be filled by Modules on: ADRS, AI Voice Delta Response System, and client onboarding.
