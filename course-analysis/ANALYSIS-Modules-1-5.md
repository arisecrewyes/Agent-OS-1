# Course Analysis: Copy My AI Agency — Modules 1-5 (Intro Modules)

**Analyzed:** 2026-06-28
**Module Range:** Intro / Overview modules (1-5)
**Course Creator:** Zalo Kabche
**Platform:** Skool (behind login wall)

---

## Module 1: Tech Support Setup Agent

**Content:** Introduction to an AI support agent trained on the full CMAA system.
- URL: `https://agencysetup.copymyaiagency.com/`
- Purpose: Help users get unstuck during setup (Pre-requisites, GHL, n8n, A2P)
- Free to use
- **Key insight:** This is a GPT-style chatbot trained specifically on the CMAA course content — an AI agent for AI agent setup. Worth noting as a pattern.

---

## Module 2: White-Glove DFY Services

**Content:** Done-For-You setup service offering.
- Full GHL Setup + n8n workflow setup + domain setup + A2P submission
- Price: $199 (or $99 for Elite members)
- URL: `https://www.copymyaiagency.com/dfy-ai-agency-setup`
- **Key insight:** The DFY service covers the ENTIRE technical stack: GHL + n8n + domain + A2P compliance. This confirms the full integration path.

---

## Module 3: Troubleshooting

**Content:** AI Demo Bot not firing — fix for old workflow versions.
- **Problem:** Demo bot trigger was using a TAG instead of FORM SUBMISSION
- **Fix:** Change trigger from tag-based to `FormSubmitted` → `FormIs` → `AI DemoStarter`
- Add filter in the correct place
- Add tag `AI DemoOptin` as an ACTION (not a trigger)
- **Key architecture insight:** GHL workflows use `FormSubmitted` + `FormIs` as triggers, NOT tags. Tags are ACTIONS within the workflow, not triggers. This is an important pattern for the universal SOP.

---

## Module 4: System Updates / Change Log

**HEAVIEST MODULE — 25,504 chars, 304 paragraphs**

This is the complete changelog from 12/24/25 to 1/19/26. Critical technical documentation.

### Architecture Revealed (in reverse chronological order):

#### Hotfix 1/19/26 — Multi-Demo Isolation
- **Problem:** Leads testing different AI demo types (Live Chat, AI Voice, SMS, WhatsApp) experienced interference between demos
- **Solution:** Add `SMSDemo` branch to `SendMagicLink` automation with tag-based filtering
- **Pattern:** Remove all demo tags before adding a new one → prevents demo crossover
- **Steps:**
  1. New branch in `SendMagicLink`: `SMSDemo` → Tags → Includes → `sms demo`
  2. Move SMS step to new branch
  3. Add "add tag SMSDemo" in Generate Magic Link step
  4. **For each demo opt-in workflow:** Remove ALL demo tags first (`ai voice demo`, `live chat demo`, `sms demo`, `whatsapp`) THEN add relevant demo tag
  5. Clear magic link custom field after each demo

#### Live Chat AI Demo (1/15/26)
- Requires base AI Agency n8n setup completed first (uses Magic Link Generator n8n workflow)
- Snapshot version: v41
- **GHL Assets Added:**
  - Funnel steps: `[LIVE Chat] AI Demo Magic Link`, `[LIVE CHAT] AI Live Chat`
  - Form: `[LIVE Chat] AI Demo Magic Link Generator`
  - Tag: `live chat demo`
  - Updated: `Send magic link v3` GHL workflow
- **Pattern:** Each demo type gets its own: funnel step + form + tag + workflow

#### Hotfix 1/14/26 — AI Voice/Chat Separation
- **Problem:** Users trying AI Voice then AI Chat demo had conflicts
- **Fix:** Add `Remove Tag AI Voice Demo` before new demo starts
- **Pattern:** Always clean up previous demo state before starting new demo

#### AI Voice Agent Demo (1/11/26)
- Snapshot import process: Select location → Skip All → selectively import
- **Import order:** Forms → Funnels → Workflows → Tags
- Only import what's new (avoid overwriting existing customizations)
- **GHL Assets:**
  - Form: `[AI Voice] AI Demo Magic Link Generator`
  - Funnel Steps: `[AI Voice] AI Demo Magic Link`, `[AI Voice] Magic Demo Landing`
  - Workflows: `[Voice AI] Send feedback SMS`, `[AI Voice] Generate Magic Link`
  - Tags: `ai voice demo`, `ai voice demo completed`
  - Modified: `Send Magic Link` — added branch `If Tags includes "ai voice demo" THEN send SMS with magic demo link`

#### A2P Update (1/9/26)
- **A2P = Application-to-Person** (10DLC SMS compliance in the US)
- Critical compliance requirements:
  - Account name = Brand name
  - Business email = domain used for A2P
  - Legal Business Name = exact match
  - Forms must NOT require phone number unnecessarily
  - T&C format required on forms
  - Website must work with AND without `www`
  - Root domain must be compliant (not broken, not parked, not mismatched)
  - Footer must have legal company name + brand name (if DBA)
  - Calendar must be active with at least one team member
- **ROOT DOMAIN TRAP:** Reviewers check the root domain, not just the subdomain. If root is broken, you get rejected.
- **Two workarounds for non-compliant root domains:**
  1. 301 redirect root → compliant funnel (free)
  2. Buy new dedicated domain (~$12) with funnel on root
- **Key insight:** A2P compliance is a major gatekeeper. This is one of the blockers you mentioned (KYC requirements). Different LC platforms may have different compliance requirements.

#### WhatsApp Demo Add-On (12/31/25)
- **Full snapshot update process documented:**
  1. Delete existing snapshot in agency
  2. Re-add snapshot from CMAA lesson
  3. Push to sub-location — selectively add only new assets
  4. Update funnel: duplicate `AI Demo Magic Link` step → change form to WhatsApp form → rename path → publish
  5. Add WhatsApp trigger exclusion tag: `AI DEMO OPTIN` in `AI Bot - Opt-in` workflow
- **Assets Added:**
  - Workflow folder: `[NEW] WhatsApp AI Demo`
  - Workflows: `Send Magic Link`, `[WhatsApp] Generate Magic Link`, `[WhatsApp] AI Demo START`, `[WhatsApp] AI Demo Bot - Base Triggers (AI Reply)`, `[WhatsApp] AI Demo Bot - Base Triggers (Lead Reply)`
  - Form: `[WhatsApp] AI Demo Magic Link Generator`
- **Pattern confirmed:** Each channel (SMS, Live Chat, AI Voice, WhatsApp) gets identical structure: form + funnel step + tag + trigger workflow + bot workflow

#### Double Message Fix (12/29/25)
- **Problem:** If user opts in from bot AND AI demo, they get double messages
- **Fix:** Add IF condition in AI Demo Bot AI Reply: `Tags Includes Ai demo optin` → only then send SMS
- Also remove `Ai demo optin` tag in AI Delta Response System opt-in
- **Pattern:** Cross-system tag management prevents message duplication

#### Older Phone Support Fix (12/24/25)
- Custom HTML code added to Magic Demo Landing page
- CSS fix to hide phone field on demo starter form: `#form-phone { display: none !important; }`
- n8n Magic Link URL encoding fix: Add `%2B` after `UID=` for proper phone number encoding
- **Pattern:** URL encoding matters for phone numbers in magic links (`+` must be encoded as `%2B`)

---

## Module 5: 90 Days FREE GHL Account

**Content:** GHL account provisioning.
- 90-day free trial, then $47/month (50% off regular)
- Pre-loaded with AI Agency Snapshot
- Single GHL account (not agency) — enough to get started
- Client account link also $47/mo with AI Delta Response System Snapshot pre-loaded
- **Key insight:** The business model relies on GHL sub-accounts. Each client gets their own GHL sub-account with the AI Agency snapshot.

---

## Cross-Module Architecture Summary

### System Components Identified:

```
┌─────────────────────────────────────────────────────┐
│                  USER / LEAD                         │
│    (Interacts via SMS, WhatsApp, Live Chat, Voice)   │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────┐
│            GoHighLevel (LC Platform)                  │
│  ┌────────────┐  ┌──────────┐  ┌──────────────────┐ │
│  │  Funnels   │  │  Forms   │  │   Workflows      │ │
│  │  & Sites   │  │          │  │   (Triggers +    │ │
│  │            │  │          │  │    Actions)       │ │
│  └─────┬──────┘  └────┬─────┘  └────────┬─────────┘ │
│        │              │                 │            │
│        │    FormSubmitted              Webhook /     │
│        │    + FormIs                   API Call      │
│        ▼              ▼                 ▼            │
│  ┌──────────────────────────────────────────────────┐│
│  │           Tags (State Management)                 ││
│  │  ai voice demo | live chat demo | sms demo |     ││
│  │  whatsapp | ai demo optin | magic link           ││
│  └────────────────────────┬─────────────────────────┘│
└───────────────────────────┼──────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────┐
│              n8n (Workflow Engine)                     │
│  ┌────────────────┐  ┌────────────────────────────┐  │
│  │ Magic Link     │  │ AI Delta Response System    │  │
│  │ Generator      │  │ (AI Chatbot Engine)        │  │
│  └────────────────┘  └────────────────────────────┘  │
│  ┌────────────────┐  ┌────────────────────────────┐  │
│  │ Demo Bot       │  │ [Per-Channel Workflows]    │  │
│  │ Triggers       │  │ SMS | WhatsApp | Voice |   │  │
│  │                │  │ LiveChat                   │  │
│  └────────────────┘  └────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

### Key Patterns for Universal SOP:

1. **Trigger Pattern:** GHL `FormSubmitted` + `FormIs <form_name>` (not tags as triggers)
2. **State Management:** Tags act as state flags, not triggers — always clean up previous state before setting new state
3. **Per-Channel Architecture:** Each communication channel (SMS, WhatsApp, Voice, Live Chat) gets identical components: Form → Funnel Step → Tag → Workflow
4. **Snapshot-Based Deployment:** Entire system deployed as GHL snapshots — versioned (v28, v41, etc.)
5. **n8n ↔ GHL Communication:** Via webhooks + GHL API (custom fields, tags, contacts)
6. **A2P Compliance:** Major gatekeeper — requires compliant root domain, business verification, proper form configuration
7. **Magic Link System:** n8n generates unique demo links → stored in GHL custom field → delivered via SMS/email
8. **Cross-System Coordination:** Tags bridge GHL workflows and n8n workflows (both systems read/write tags)

### GAP Analysis (What's Missing From Modules 1-5):

- [ ] Exact n8n workflow JSON/configuration details (only high-level described)
- [ ] GHL API authentication details (OAuth? API key? Location-based?)
- [ ] n8n credential setup for GHL connection
- [ ] AI Delta Response System internals (how it actually works)
- [ ] OpenRouter / LLM API key configuration
- [ ] Specific webhook URLs and payload formats
- [ ] How to set up new demo types from scratch (not just update existing)
- [ ] Domain/DNS configuration details
- [ ] n8n hosting (self-hosted or cloud?)

**These gaps should be filled by Modules 6+ (Chatbot System Overview, AI Agency Setup, etc.)**

---

## Version History Extracted:

| Date | Version | Change |
|------|---------|--------|
| 12/24/25 | - | Older phone support fix, URL encoding fix |
| 12/29/25 | - | Double message fix (demo + ADRS conflict) |
| 12/31/25 | v28 | WhatsApp AI Demo add-on |
| 01/09/26 | - | A2P compliance update |
| 01/11/26 | - | AI Voice Agent Demo |
| 01/13/26 | - | AI Agency Funnel Update [Voice AI] |
| 01/14/26 | - | AI Voice/Chat separation hotfix |
| 01/15/26 | v41 | Live Chat AI Demo |
| 01/19/26 | - | Multi-demo isolation hotfix |
