# Course Analysis: Copy My AI Agency — Modules 13-15 (FINAL)

**Analyzed:** 2026-06-28
**Module Range:** 13 (ADRS) + 14 (Voice ADRS) + 15 (Elite)
**Status:** COMPLETE COURSE ANALYSIS

---

## Module 13: ADRS System Setup (AI Delta Response System) - THE CORE

### 13.1: ADRS Installation

- **GHL Snapshot:** AI Delta Response System v10 (separate from AI Agency snapshot, but included in it)
- **n8n Workflow:** `AI Delta Response System v3 - TEMPLATE.json` — THE main workflow
- **API Keys:** Anthropic (primary), Gemini (backup), OpenAI (optional)
- **Bug Fix:** Red variable in "Create Message" node — replace with "User Last Message" webhook

### 13.2: AI Chatbot System Overview (How ADRS Works)

**ADRS = TWO Agents:**
1. **Main Chat Agent** — Live conversation handler (unlimited prompt, dual LLM, tools)
2. **Follow-Up Agent** — Dedicated proactive follow-up (separate prompt, dual LLM, full context)

**Data Flow:**
Contact messages GHL -> GHL webhook to n8n ADRS -> Multi-message intelligence gathers messages -> Loads contact context -> Primary LLM (backup on error) -> AI creates response -> n8n POSTs back to GHL API -> GHL routes reply to correct channel -> Follow-up agent triggered if scheduled

### 13.3: Anatomy of an AI Chatbot Prompt

**The prompt IS the product.** Structure (platform-agnostic):
1. Role/Identity — Who the AI is
2. Context — Business info, services, pricing, hours
3. Instructions — Behaviors, scenarios, escalation rules
4. Knowledge Base — FAQs, objection handling, sales scripts
5. Constraints — What NOT to do, limits, compliance
6. Formatting — Message style, length, tone
7. Tools/Capabilities — Booking, DND, handoff, web search
8. States/Flows — Conversation scenarios and paths

**Base prompt: 3,500+ words. Production prompts 50%+ larger. GHL native: ~2,000 word limit = insufficient.**

### 13.4: Prompt Forge (Prompt Generator Agent)

**META-TOOL: AI that builds AI prompts.**
1. Claude Projects (claude.ai/projects) + Prompt Forge System Instructions
2. Input: Client questionnaire data
3. Output: Complete customized system prompt
4. Paste into n8n ADRS workflow

**This is systematic, reproducible, and scalable.**

### 13.5: Testing and Optimizing Prompts

- **Tool:** Anthropic Workbench (console.anthropic.com/workbench)
- **Process:** Generate -> Test -> Iterate -> Deploy -> Monitor -> Optimize

### 13.6-7: Vector Database and RAG

**RAG = Retrieval-Augmented Generation** — unlimited knowledge without prompt size limits.

**Architecture:**
Client docs -> n8n processes -> Chunks -> Embeddings -> Supabase vector DB
During conversation -> Query embedding -> Search Supabase -> Relevant chunks -> AI context -> Response

**n8n Workflow:** `Supabase Vector Database [RAG] - TEMPLATE.json`
** OPTIONAL layer for businesses that need more knowledge than fits in a prompt.

### 13.8: 10 Proven Chatbot Prompts

Industry-specific templates: AI Agency, Car Dealer, Cosmetic Dentist, HVAC, Life Insurance, Med Spa, Personal Injury Law, Plumber, Roofer, Solar

### 13.9: Sales Script Generation via Gemini Deep Research

1. Gemini: "Find me the best converting message script for [NICHE]"
2. Follow-up: "Give me the full document with only the sales scripts"
3. Feed into Prompt Forge or RAG

### 13.10: Database Reactivation Campaigns

**THE revenue model for AI agencies.**

| Metric | Average (1K sent) | Excellent (1K sent) |
|---|---|---|
| Total Replies | 120 (12%) | 200 (20%) |
| Positive Replies | 20 (2%) | 60 (6%) |
| Booked Appointments | 10 (1%) | 30 (3%) |

**Benchmarks:** 50% of positive replies should book. Opt-out: 1-3% (4%+ = problem). A2P required.

### 13.11: Bonus Sales Scripts (9 industries, PDFs)

---

## Module 14: AI Voice Delta Response System

### Voice ADRS Architecture

```
Contact calls business
  -> Retell AI answers (STT -> LLM -> TTS)
  -> n8n actions (lookup contact, book, update GHL)
  -> Post-call: GHL creates conversation record, tags, follow-up triggers
```

### Key Components
- **Inbound:** `AI Voice Delta Response System - Inbound [TEMPLATE].json`
- **Client Config:** `AI Voice Agent- CLIENT [TEMPLATE].json`
- **Outbound:** `AI Voice Delta Response System - outbound [TEMPLATE].json`

### Voice Prompt Forge
Same concept as chat, optimized for voice: shorter responses, natural speech, turn-taking, pronunciation, tone.

### Outbound Voice
- **KYC required** in Retell AI (docs.retellai.com/accounts/kyc)
- n8n triggers (scheduled or GHL webhook) -> Retell AI API creates call -> Agent handles -> GHL updated
- Use cases: follow-ups, reactivation, reminders, confirmations, outreach

---

## Module 15: Elite Invitation

Upsell only, no technical content.

---

## COMPLETE INVENTORIES

### n8n Workflows (12 total)

| # | File | Purpose | Type |
|---|---|---|---|
| 1 | Magic Link Generator v2 TEMPLATE.json | Demo link creation | Infrastructure |
| 2 | AI Demo v4 TEMPLATE.json | SMS demo chatbot | Demo |
| 3 | Live Chat AI Demo TEMPLATE.json | Live chat demo | Demo |
| 4 | AI Voice Demo TEMPLATE.json | Voice demo | Demo |
| 5 | AI Voice Demo Bot (ENG).json | English voice agent | Demo |
| 6 | AI Voice Demo Bot (ESP).json | Spanish voice agent | Demo |
| 7 | Orchestrator AI Demo Multi-lingual.json | Voice language router | Demo |
| 8 | **AI Delta Response System v3 TEMPLATE.json** | **MAIN production chatbot** | **Production** |
| 9 | Supabase Vector Database RAG TEMPLATE.json | Knowledge base | Infrastructure |
| 10 | **AI Voice Delta Response System Inbound TEMPLATE.json** | **Production voice** | **Production** |
| 11 | AI Voice Agent CLIENT TEMPLATE.json | Client voice config | Production Config |
| 12 | **AI Voice Delta Response System outbound TEMPLATE.json** | **Outbound voice** | **Production** |

### GHL Snapshots (3 total)

| Snapshot | Version | Purpose |
|---|---|---|
| AI Agency Snapshot - CMAA | v46 | Full agency (includes ADRS) |
| AI Delta Response System | v10 | ADRS only |
| AI Voice Delta Response System | - | Voice ADRS |

### Prompts (6 categories)

| Category | Files |
|---|---|
| Base System Prompt | Base AI Agent System Prompt.md |
| Demo Prompt | AI Demo System Prompt.md |
| Prompt Forge (Chat) | Chatbot Prompt Forge System Instructions v3.md |
| Prompt Forge (Voice) | AI Voice Agent Prompt Forge.md |
| Industry Prompts (10) | AI Agency, Car Dealer, Dentist, HVAC, Insurance, Med Spa, Law, Plumber, Roofer, Solar |
| Sales Scripts (9) | Same industries (PDFs) |

### Platforms/APIs

| Platform | Purpose | Auth Method |
|---|---|---|
| GoHighLevel | LC Platform | Private Integration Key + Location ID |
| n8n (Self-hosted) | Workflow engine | Webhook Production URLs |
| Anthropic (Claude) | Primary LLM | API Key |
| Gemini | Backup LLM | API Key |
| OpenAI | Optional LLM | API Key |
| Retell AI | Voice AI | API Key + Webhooks |
| Supabase | Vector DB (RAG) | API Key + Connection String |
| Stripe | Payments | API Key |
| Black Umbrella | Ad management | Web login |
| Claude (Projects) | Prompt Forge | Web login |

---

## UNIVERSAL LC INTEGRATION PATTERNS (COMPLETE SET)

### Pattern 1: Webhook Bridge (LC <-> n8n)
- LC Webhook Action POSTs to n8n Production URL
- n8n HTTP Request POSTs back to LC REST API
- **Works with any LC platform that has webhooks + REST API**

### Pattern 2: Environment Variables via Custom Values
- LC platform stores config as custom fields/values
- Workflows reference dynamically (not hardcoded)
- **Works with any LC platform with custom fields**

### Pattern 3: State Management via Tags
- Tags = state flags, not triggers
- Always clean previous state before new
- Cross-system coordination via shared tags
- **Works with any LC platform with tags/labels**

### Pattern 4: Per-Channel Architecture
- Each channel: Form + Funnel + Tag + Workflow + n8n workflow
- Channel routing handled by LC platform natively
- **Works with any LC platform with multi-channel support**

### Pattern 5: Snapshot/Template Deployment
- Full system deployable as snapshot
- Version-controlled, push to sub-accounts
- **Works with LC platforms with sub-account + snapshot features**

### Pattern 6: Dual LLM Fallback
- Primary + Backup LLM in n8n
- Error handling chain
- **Platform-agnostic — n8n handles this regardless of LC**

### Pattern 7: Prompt Forge Systematic Generation
- Client questionnaire -> Prompt Forge -> System prompt -> n8n workflow
- Prompt is LC-platform-agnostic
- **Only the API integration layer changes per LC platform**

### Pattern 8: RAG Knowledge Expansion
- Vector DB + n8n = unlimited knowledge
- Optional layer for complex businesses
- **Platform-agnostic infrastructure component**

### Pattern 9: Voice AI Bridge (n8n <-> Retell AI <-> LC)
- n8n bridges voice platform and LC platform
- Voice platform handles STT/LLM/TTS
- n8n handles CRM writes and workflow triggers
- **Works with any LC platform that n8n can write to**

### Pattern 10: A2P/SMS Compliance Pipeline
- Legal verification -> Compliant website -> Carrier registration
- **Pattern is universal, specifics vary by country/carrier**

### Pattern 11: Onboarding QA Checklist
- Pre-launch testing with blocker items
- Systematic verification before go-live
- **Platform-agnostic operational pattern**

### Pattern 12: Database Reactivation Revenue Model
- Use ADRS on client's existing contacts
- AI converts dormant leads to appointments
- **Business model, not technical — but repeatable across LC platforms**

---

## COMPLETE TAG TAXONOMY

**State Tags:**
- `AI opt in` — Contact opted into AI conversation
- `dndgpt` — Manual bot kill switch (exact spelling)
- `ai demo optin` — Demo system opt-in

**Channel Demo Tags:**
- `ai voice demo` / `ai voice demo completed`
- `live chat demo`
- `SMSDemo` / `sms demo`
- `whatsapp` (demo)

**Channel Source Tags:**
- `Instagram` / `Facebook` / `SMS`

---

## COMPLETE CUSTOM VALUES REFERENCE

| Custom Value | Purpose |
|---|---|
| `agency_logo` | Company logo URL |
| `privacy policy url` | Legal compliance |
| `tos url` | Terms of service |
| `legal company name` | A2P compliance |
| `ai_demo_webhook` | n8n AI Demo webhook URL |
| `magic link` (custom FIELD) | Per-contact demo link (auto-populated) |

---

## COURSE ANALYSIS COMPLETE

**All 15 modules analyzed. Full technical architecture extracted. Ready to build Universal SOP + OpenClaw Skill.**
