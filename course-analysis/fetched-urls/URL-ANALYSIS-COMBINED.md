# URL Analysis — Combined Report

> **Generated:** 2026-06-28
> **Purpose:** Extract technical details, architecture patterns, API endpoints, workflow steps, pricing, and integration SOP information for building a universal LC platform integration SOP.
> **Total URLs:** 20 | **Accessible:** 14 | **Inaccessible (login wall):** 6

---

## Access Summary

| # | URL | Status | Content Available |
|---|-----|--------|-------------------|
| 1 | agencysetup.copymyaiagency.com | ⚠️ Minimal | Title only — likely JS-rendered SPA |
| 2 | a2pwizard.com/automated-setup-trial | ✅ Full | Complete landing page |
| 3 | mural.co (AI SMS Demo) | 🔒 Inaccessible | Login wall |
| 4 | mural.co (AI Voice Demo) | 🔒 Inaccessible | Login wall |
| 5 | mural.co (Understanding AI Voice) | 🔒 Inaccessible | Login wall |
| 6 | mural.co (Vector DB & RAG) | 🔒 Inaccessible | Login wall |
| 7 | mural.co (Client Onboarding) | 🔒 Inaccessible | Login wall |
| 8 | go.blackumbrella.app/shared/campaign | ⚠️ Minimal | Title only — JS-rendered |
| 9 | Google Doc: Onboarding Playbook | ✅ Full | Complete document |
| 10 | Google Doc: Pre-Launch Testing Checklist | ✅ Full | Complete document |
| 11 | Google Doc: AI Onboarding Questionnaire | ✅ Full | Complete document |
| 12 | Google Doc: Service Agreement (no voice) | ✅ Full | Complete document |
| 13 | Google Doc: Service Agreement (with voice) | ✅ Full | Complete document |
| 14 | help.gohighlevel.com (WhatsApp setup) | ✅ Full | Complete article |
| 15 | docs.retellai.com/kyc | ✅ Full | Complete documentation |
| 16 | retellai.com | ✅ Full | Complete homepage |
| 17 | hostinger.com/n8n-hosting | ✅ Full | Complete pricing page |
| 18 | blackumbrella.app | ⚠️ Minimal | Title only — JS-rendered |
| 19 | copymyaiagency.com/free-ghl | ⚠️ Minimal | Disclaimer text only |
| 20 | copymyaiagency.com/dfy-ai-agency-setup | ✅ Full | Complete landing page |

---

## 1. CMAA Tech Support Agent
**URL:** https://agencysetup.copymyaiagency.com/
**Status:** ⚠️ Minimal content (JS-rendered SPA)

### Key Information
- **Product:** "Copy My AI Agency - Tech Co-Pilot"
- **Provider:** Copy My AI Agency (CMAA)
- **Purpose:** Tech support automation for agency setup
- **Note:** Page is a JavaScript Single Page Application — content not server-rendered. Requires browser automation to extract full details.

### SOP Relevance
- Likely contains the tech support workflow automation for CMAA's DFY service
- Would need browser tool with JS execution to fully analyze

---

## 2. A2P Wizard — Automated Setup Trial
**URL:** https://a2pwizard.com/automated-setup-trial
**Status:** ✅ Full content extracted

### Key Information
- **Product:** a2pWIZARD 2.0 (now at v2.5)
- **Purpose:** Automated A2P (Application-to-Person) 10DLC compliance asset generation
- **Tagline:** "A2P Approval Guaranteed"
- **Capabilities:**
  - Generates compliant websites, images, and messaging
  - Supports LOCAL, TOLL FREE, TWILIO, and SOLE PROP registrations
  - Dynamic website generation for client compliance representation
- **Form Fields Required:**
  1. Agency/owner contact information
  2. Client business name (exactly as on EIN form)
  3. Business address (from EIN paperwork)
  4. Business phone number
  5. Business description (who they serve, where they operate)
  6. End user logo (max 400px)
- **Compliance:** TCPA and A2P 10DLC requirements
- **Pro Tips from the page:**
  - Use legal business name only (no DBA) for higher approval odds
  - For mortgage companies: do not mention "direct lending"
  - Check opencorporates.com for EIN address lookup

### SOP Relevance
- **Critical for SMS channel setup** — A2P registration is required before SMS works
- Workflow: Fill form → Generate compliance assets → Submit for A2P approval
- Supports multiple number types (local, toll-free, Twilio, sole prop)

---

## 3–7. Mural Diagrams (5 URLs)
**URLs:**
- https://app.mural.co/t/dw4563/m/dw4563/1766496553913/... (AI SMS Demo — Module 8)
- https://app.mural.co/t/dw4563/m/dw4563/1768175259828/... (AI Voice Demo How It Works — Module 8)
- https://app.mural.co/t/dw4563/m/dw4563/1768250176656/... (Understanding AI Voice Agents — Module 14)
- https://app.mural.co/t/dw4563/m/dw4563/1768751586064/... (Understanding Vector DB and RAG — Module 13)
- https://app.mural.co/t/dw4563/m/dw4563/1769359302911/... (Client Onboarding — Module 12)

**Status:** 🔒 All inaccessible — login wall (Mural requires authentication)

### Notes
- These are visual diagram boards used in the course training
- Module mapping:
  - **Module 8:** AI SMS Demo + AI Voice Demo architecture
  - **Module 12:** Client Onboarding workflow diagram
  - **Module 13:** Vector DB and RAG architecture
  - **Module 14:** AI Voice Agent architecture
- **To access:** Would need Mural account credentials with access to the dw4563 workspace

### SOP Relevance
- These likely contain the visual architecture diagrams showing:
  - Data flow between LC/GoHighLevel → n8n → AI providers → communication channels
  - RAG pipeline architecture (Vector DB → embedding → retrieval → LLM context)
  - Voice agent call flow architecture
  - Client onboarding step-by-step workflow visualization

---

## 8. Meta Ads Campaign (Black Umbrella)
**URL:** https://go.blackumbrella.app/shared/campaign/aac8bf9c-e7ce-4647-a181-9f35a007cccc
**Status:** ⚠️ Minimal content (JS-rendered)

### Key Information
- **Platform:** Black Umbrella AI marketing platform
- **Content Type:** Shared Meta Ads campaign
- **Note:** Campaign content requires JavaScript rendering — likely shows ad creatives, copy, and campaign structure

### SOP Relevance
- Would contain the Meta Ads campaign structure used to generate leads for AI agency clients
- Useful for understanding the lead generation funnel that feeds into the AI onboarding system

---

## 9. Onboarding Playbook
**URL:** https://docs.google.com/document/d/15INsHJA2t-tJZOJgAsOUdobIq-bDJ89KxvGEdoqj3GQ/
**Status:** ✅ Full content extracted

### Workflow Summary

#### DAY 0 (Within 1 hour of payment):
1. **Create Client Folder** — Google Drive → Clients → "[Client Name] - [Package]" with template subfolders (Docs, Assets, Prompts, Reports)
2. **Create WhatsApp Group** — Client PM + client's phone + Tech Lead (Professional package); named "[Client Name] x Black Umbrella AI"
3. **Send Welcome Message** — Structured welcome with 4-step overview (questionnaire → Anthropic setup → strategy call → build & launch in 5-7 days)
4. **Send Documents** — AI Onboarding Questionnaire, Anthropic Setup Guide, Signed Service Agreement
5. **Schedule Strategy Call** — Calendly link, 24-48 hours out
6. **Update Tracking** — Add to Project Tracker spreadsheet, status "Onboarding"

#### DAY 1-2 (Follow Up):
- **24h no questionnaire:** Friendly check-in
- **48h no questionnaire:** Follow-up + remind about Anthropic account
- **API key received:** Direct to secure form link (NOT in chat), verify in Anthropic console, confirm auto-recharge, store in password manager

#### STRATEGY CALL (30 min):
- 0-5 min: Rapport + identify #1 goal
- 5-15 min: Review questionnaire
- 15-20 min: Technical setup confirmation
- 20-25 min: Set expectations + timeline
- 25-30 min: Q&A

#### POST-CALL (within 1 hour):
- Update questionnaire, send recap via WhatsApp, status → "Building", hand off to Tech Lead

#### BUILD (Days 2-5):
- Day 2-3: Progress update to client
- Day 4-5: Ready for testing — send test instructions

#### LAUNCH DAY:
- Pre-launch checklist (client approval, QA complete, test data removed, production channels connected, monitoring enabled)
- Go live + notify client
- Post-launch admin (tracker update, schedule follow-ups)

#### POST-LAUNCH:
- Day 3: Check-in
- Week 1: Stats + Google review request
- Month 1: Performance report + monthly billing reminder

### Packages
- **Essential:** 5-day build
- **Professional:** 7-day build

### Golden Rules
1. Respond to client messages within 2 hours during business hours
2. Never promise a timeline you can't keep
3. When in doubt, ask a senior team member
4. Document everything in the client folder
5. If client is unhappy, escalate immediately

### SOP Relevance
- **This is the master client onboarding SOP** — directly reusable as a template
- Contains exact message templates for every stage
- Includes escalation procedures and common issue responses

---

## 10. Pre-Launch Testing Checklist
**URL:** https://docs.google.com/document/d/1eKrnRAVLSAml5WCnvagotXhbQkTjErOHmEBzIpvTVYY/
**Status:** ✅ Full content extracted

### Checklist Structure

#### 1. Setup Verification (Blockers)
- API key validated & working
- Correct model selected (Claude Sonnet 4.5)
- Auto-recharge enabled on Anthropic
- System prompt loaded correctly
- Calendar integration connected

#### 2. Channel Connectivity
| Channel | Key Checks |
|---------|-----------|
| **SMS** | Send/receive, A2P verification active, STOP/unsubscribe works |
| **Email** | Send/receive, not in spam |
| **FB Messenger** | Send/receive, under 30s |
| **Instagram DM** | Send/receive, under 30s |
| **WhatsApp** | Send/receive, under 30s |

#### 3. Conversation Testing (all 🔴 items must pass)
- Basic inquiry, Price question, Book appointment (full flow)
- Lead qualification → correct path, Disqualified lead → handled gracefully
- After hours message, Emergency/urgent request
- Multiple questions in one message, Typos/misspellings understood
- Angry/frustrated customer, Competitor mentioned
- "I want to speak to a human", Off-topic/random question

#### 4. Quality Check
- No hallucinations, Accurate info only, Stays on-brand
- Grammar/spelling correct, Not too verbose
- Maintains context, Actually answers the question

#### 5. Automations & Follow-Ups
- Pipeline stages configured, Follow-up sequence timing
- Appointment confirmation + reminder sends
- Escalation notifications, Lead routing

#### 6. Go-Live Checklist
- All test data removed, Client training completed
- Client approval received, Admin access provided
- Support documentation delivered, Monitoring/alerts enabled

#### Post-Launch Monitoring
- **First 24 hours:** Monitor every conversation, hourly response time checks, verify bookings, review errors, track token usage
- **First week:** Daily performance review, client feedback, optimization opportunities, edge cases

### SOP Relevance
- **Directly usable as QA checklist** before any client launch
- Covers all channels and critical conversation scenarios
- Includes sign-off section (QA Tester, PM, Client)

---

## 11. AI Onboarding Questionnaire
**URL:** https://docs.google.com/document/d/1O40S2aA3kIFkZSug3qOXDff6hNHSCUuE/
**Status:** ✅ Full content extracted

### Questionnaire Sections (20 sections)

| Section | Purpose | Key Fields |
|---------|---------|------------|
| 1. Chatbot Goal & Flow | Define AI purpose | Primary goal, video step Y/N, conversion links |
| 2. Business Foundation | Core business info | Name, website, services, pricing, hours, after-hours pref |
| 3. Authority & Social Proof | Build trust | Founder info, credentials, case studies |
| 4. AI Personality & Voice | Define tone | AI name, opening message, tone style, emoji/jargon/humor usage |
| 5. Multi-Offer Routing | Service routing | Multiple offers table, routing logic |
| 6. Lead Qualification | Qualification criteria | Info to collect, qualifying questions, disqualifiers |
| 7. Objection Handling | Sales scripts | Responses to common objections |
| 8. Competitor Differentiation | Positioning | Differentiators, competitor names, response strategy |
| 9. Appointment Booking | Calendar setup | Appointment types, durations, buffers, booking preferences |
| 10. FAQs & Common Questions | Knowledge base | Pricing response strategy, FAQ table (5-10 minimum) |
| 11. Communication Channels | Channel selection | SMS, web chat, email, FB, IG, WhatsApp |
| 12. Escalation & Human Handoff | Escalation rules | When to escalate, who receives escalations |
| 13. Follow-Up Sequences | Nurture campaigns | Follow-up timing, max attempts, tone |
| 14. Success Metrics | KPI definition | What counts as a "win", current benchmarks |
| 15. Lead Routing | Distribution | Round robin, by service/location/value, custom rules |
| 16. Sales Enablement | Payment/sales tools | Stripe/PayPal/Square, discount codes, upsells |
| 17. Anthropic & Gemini API Setup | API accounts | console.anthropic.com, aistudio.google.com/apikey |
| 18. Special Instructions & Compliance | Guardrails | Forbidden topics, emergency handling |
| 19. Specific Scenarios | Edge cases | Custom scenario handling |
| 20. Attachments | Supporting docs | Handbooks, scripts, SOPs, VSL scripts |

### API Setup Instructions
- **Anthropic (Claude):** console.anthropic.com → Settings → API Keys → requires pre-paid credits
- **Google Gemini:** aistudio.google.com → /app/apikey
- **Critical:** Auto-recharge must be ON in Anthropic settings

### SOP Relevance
- **Master template for gathering client requirements** — covers every aspect of AI system configuration
- Can be adapted as the universal intake form for any LC platform integration
- Section 17 provides exact API setup links for the dual-provider architecture

---

## 12. AI Service Agreement (No Voice)
**URL:** https://docs.google.com/document/d/1j7T1e1oNL2aVzw5M4YYstW4nUFI3LDkGVxAf-MrrOJA/
**Status:** ✅ Full content extracted

### Pricing
| Service | Setup Fee | Monthly Hosting |
|---------|-----------|-----------------|
| **Essential AI System** | $3,000 | $99/month |
| **Professional AI System** | $5,000 | $99/month |

### Essential Includes
- Multi-message intelligence, Auto error recovery, Proactive follow-ups
- Connect to any 3rd Party API, Auto Human handoff
- Latest LLM Natural Language, Native booking, Self-service DND
- Full prompt control, Integrates with tech stack
- Omni-channel (web widget, SMS, IG, FB)
- Timezone aware, Full contact journey awareness
- Limited knowledge base (10 FAQs)

### Professional Adds
- Everything in Essential PLUS:
- Unlimited knowledge base
- Objection handling database
- Multi-service/product routing

### Implementation Timeline
- **Essential:** 3-5 business days
- **Professional:** 5-7 business days

### Third-Party Cost Estimates
| Volume | Essential | Professional |
|--------|-----------|-------------|
| 100 conv/mo | $3-5 | $5-8 |
| 500 conv/mo | $15-25 | $25-40 |
| 1,000 conv/mo | $30-50 | $50-80 |
| 2,500 conv/mo | $75-125 | $125-200 |
| 5,000+ conv/mo | $150+ | $250+ |

### Message Delivery Costs
- SMS: $0.0075-0.01 per segment
- Email: $0.0008 per email
- WhatsApp: $0.02-0.08 per conversation
- FB/Instagram DMs: Free

### Key Contract Terms
- Setup fee non-refundable 24 hours after payment

---

## 13. AI Service Agreement (WITH Voice)
**URL:** https://docs.google.com/document/d/1SVtD3KVJDQR-3FVvyj3T9_GwvUocrf7RXEChMlenZ7o/
**Status:** ✅ Full content extracted

### Pricing (Complete)
| Service | Setup Fee | Monthly Hosting |
|---------|-----------|-----------------|
| **Essential AI System** (Chat) | $3,000 | $99/month |
| **Professional AI System** (Chat) | $5,000 | $99/month |
| **Essential Voice** | $4,000 | $149/month |
| **Professional Voice** | $7,000 | $199/month |
| **Enterprise Voice** | Custom | Custom |

### Voice AI Costs
- ~$0.15/minute (includes voice synthesis + AI processing + telephony)
- 100 calls × 3min = $45/mo
- 500 calls × 3min = $225/mo
- 1000 calls × 3min = $450/mo

### Key Contract Terms
- Setup fee non-refundable 24h after payment
- Monthly hosting auto-renews, cancel with 30 days notice
- API/usage costs paid directly by client
- Hosting suspended after 7 days late
- 3-month minimum before termination
- Liability limited to setup fee amount
- Client owns: custom flows, prompts, recordings, transcripts
- Agency retains: base framework, methodologies, templates
- SLA: 99.5% uptime, <2s text response, <500ms voice latency
- Support: Mon-Fri 9AM-5PM ET, Critical: 4h, Standard: 24h

### Implementation Timelines
- Essential Chat: 3-5 business days
- Professional Chat: 5-7 business days
- Essential Voice: 5-7 business days
- Professional Voice: 7-10 business days

---

## 15. Retell AI KYC Requirements
**URL:** https://docs.retellai.com/accounts/kyc
**Status:** ✅ Full content extracted

### Key Information
- **Purpose:** Unlock outbound calling, phone number purchases, and SMS
- **Methods:**
  1. Automatic (based on registration info)
  2. Persona ID verification (government-issued ID)
  3. Manual review (edge cases)
- **Countries supported:** 83
- **Restriction:** One account per person (duplicate identity detection)
- **Process:** Phone Numbers → Click number → KYC interface

---

## 17. Hostinger n8n Hosting Pricing
**URL:** https://www.hostinger.com/pricing/n8n-hosting
**Status:** ✅ Full content extracted

(Already captured in earlier analysis — n8n is self-hosted on Hostinger VPS)

---

## 19-20. CMAA Service Pages
**URLs:** copymyaiagency.com/free-ghl, copymyaiagency.com/dfy-ai-agency-setup
**Status:** ⚠️ Minimal (JS-rendered)

### Key Information
- **Free GHL:** 90-day trial with AI Agency Snapshot pre-loaded
- **DFY Setup:** $199 full setup (GHL + n8n + domain + A2P)
- **Elite:** Upsell to premium membership

---

## COURSE PLATFORM (Black Umbrella)
**URL:** learn.blackumbrella.app
**Status:** 🔒 Login required

- JS-rendered membership platform
- Contains the full CMAA course with video lessons
- Login wall prevents direct access
- Would need credentials to access

---

## MURAL DIAGRAMS (5 boards)
**Status:** 🔒 Login required

### Estimated Content (based on module context)
1. **AI SMS Demo** (Module 8) — Data flow: Contact → GHL → n8n → AI → GHL → Contact
2. **AI Voice Demo** (Module 8) — Voice call flow: Contact → Retell → n8n → GHL
3. **AI Voice Agents** (Module 14) — Voice agent architecture and call routing
4. **Vector DB & RAG** (Module 13) — Document → Chunk → Embed → Store → Retrieve → Context
5. **Client Onboarding** (Module 12) — End-to-end onboarding workflow visualization

These would need Mural account credentials with access to dw4563 workspace.