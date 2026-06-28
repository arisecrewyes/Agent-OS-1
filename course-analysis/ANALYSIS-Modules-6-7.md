# Course Analysis: Copy My AI Agency — Modules 6-7

**Analyzed:** 2026-06-28
**Module Range:** 6-7
**Status:** Module 6 attachment missing; Module 7 fully analyzed from transcript

---

## Module 6: 7-Day Quickstart Blueprint

**Status:** ❌ ATTACHMENT NOT RECEIVED
- The lesson references "⚠️ Please download the full doc in the attached files ⚠️"
- No file was received in the inbound media directory
- **Action needed:** Re-upload the 7-Day Blueprint document

**Expected content based on course outline:**
- "Go from 0 to $5k in 7 days" — the rapid deployment guide
- Likely covers: Day-by-day setup sequence, pre-requisites checklist, GHL account creation, n8n setup, domain/A2P, first demo, first sale
- This is probably the most operationally critical module for the SOP

---

## Module 7: Chatbot System Overview

**Status:** ✅ FULLY ANALYZED (two video transcripts)

### Video 1: System Architecture Overview

**Complete data flow:**

```
CONTACT (SMS / WhatsApp / Instagram DM / Facebook Messenger / GHL Widget)
    │
    ▼
GoHighLevel (receives message via native channel integration)
    │
    ▼ Webhook / API call
n8n (AI Agent processes message)
    │
    ├── Creates chat conversations
    ├── Manages memory (conversation history + contact context)
    │
    ▼回复 via GHL API
GoHighLevel (routes reply to correct channel)
    │
    ▼
CONTACT (receives AI reply on same channel they used)
```

**Core Features Documented:**

1. **Multi-Message Intelligence**
   - Gathers multiple messages within a time window (e.g., "hi" + "how are you" = one combined message)
   - Prevents multiple AI replies to rapid separate messages
   - Time window: configurable (default appears to be every 12 sessions/checks)

2. **Auto-Recover / Error Handling**
   - Detects API errors
   - Has fallback mechanisms when LLM APIs fail

3. **Proactive Follow-Ups**
   - GHL-based follow-up triggers
   - Default: daily if contact didn't book appointment
   - Configurable: can set specific follow-up dates based on conversation
   - **Separate follow-up AGENT** (not just a timer)

4. **3rd Party API Integration**
   - Agent lives in n8n → can connect to ANY external API
   - Web search capabilities
   - Custom tools/workflows callable from the agent
   - **Key quote:** "Literally anything you can connect to it"

5. **Auto Human Handoff**
   - AI detects when it can't help (missing info, escalation instructions)
   - Adds a TAG in GHL to signal human takeover
   - Sends internal notification

6. **Dual LLM with Fallback**
   - Primary LLM + Backup LLM running simultaneously
   - If primary fails → backup takes over
   - If both fail → error handling path
   - Uses Claude 4.5 Sonnet (primary) + Gemini 3 Pro (backup)
   - **Critical insight:** This is NOT just API failover — it's a designed redundancy pattern

7. **Native Booking**
   - Connected to GHL calendars
   - Agent can check availability and book appointments
   - Supports multiple calendars

8. **Self-Service DND (Do Not Disturb)**
   - Contact tells AI they don't want to be contacted
   - AI automatically triggers DND in GHL
   - No manual intervention needed

9. **Full Prompt Control**
   - Editable system prompts in both GHL and n8n
   - Variable injection in prompts
   - No black-box limitations

10. **Omni-Channel**
    - All channels: SMS, WhatsApp, IG DM, FB Messenger, Live Chat
    - Single agent handles all channels

11. **Time Zone Awareness**
    - Agent understands and operates in correct time zones

12. **Full Contact Journey Awareness**
    - AI has access to ALL contact data: forms filled, surveys, previous interactions
    - Context-aware responses based on full contact history
    - Follow-up agent has full chat memory and knows what context to use

---

### Video 2: Native GHL AI Chatbot vs ADRS (AI Delta Response System) Comparison

**This is the SALES pitch for why n8n is superior to GHL's built-in AI. Critical for understanding the architecture decisions.**

| Feature | GHL Native AI Chatbot | ADRS (n8n-based) |
|---------|----------------------|-------------------|
| **LLM Selection** | OpenAI only (4.1, 4.1 mini) — limited | Any LLM (Claude 4.5 Sonnet, Gemini 3 Pro, etc.) — unlimited |
| **Dual LLM / Redundancy** | ❌ No | ✅ Primary + Backup + Error handling |
| **Prompt Size** | ~2,000 words + unknown base prompt (1,351-2,351 tokens) — BLACK BOX | **Unlimited** — full control, any size |
| **Prompt Control** | ❌ Can't see or change base prompt | ✅ Full system prompt control |
| **Follow-up Agent** | ❌ No prompt control on follow-ups | ✅ **Separate dedicated follow-up agent** with full prompt control + Dual LLM |
| **Multi-Message Intelligence** | ❌ Replies to every individual message | ✅ Gathers multiple messages → single natural reply |
| **3rd Party API Access** | ❌ None | ✅ Unlimited — web search, custom tools, external APIs, sub-workflows |
| **Custom Workflows** | ❌ Black box | ✅ Can call separate n8n workflows (e.g., quote calculator) and return results |
| **Error Handling** | ❌ Limited/None | ✅ Auto-recover with fallback LLMs |

**Key Architecture Insight:**
The ADRS is essentially TWO agents:
1. **Main Chat Agent** — handles live conversations (unlimited prompt, dual LLM, 3rd party tools)
2. **Follow-Up Agent** — dedicated agent for proactive follow-ups (separate prompt, dual LLM, full context awareness)

Both operate through n8n, both have GHL API access, both share contact memory.

**Why n8n over native GHL AI:**
- GHL's native AI is a constrained black box — limited to OpenAI, limited prompt, no tools
- n8n gives unlimited extensibility: any LLM, any tool, any API, any workflow
- The conversation quality directly correlates with prompt quality and size → GHL's 2K word limit is insufficient
- The CMAA base prompt alone is 3,500+ words, and production prompts are typically 50%+ larger

---

## Updated System Architecture (After Modules 6-7)

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTACT / LEAD                             │
│   SMS │ WhatsApp │ Instagram DM │ FB Messenger │ Live Chat   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                 GoHighLevel (LC Platform)                     │
│                                                               │
│  ┌─────────────┐  ┌──────────┐  ┌─────────────────────────┐ │
│  │   Funnels   │  │  Forms   │  │     Workflows           │ │
│  │   & Sites   │  │          │  │  (Triggers + Actions)   │ │
│  └──────┬──────┘  └────┬─────┘  └───────────┬─────────────┘ │
│         │              │                    │                 │
│  ┌──────┴──────────────┴────────────────────┴──────────────┐ │
│  │              Tags (State Management)                     │ │
│  │  Channel demo tags │ ai demo optin │ human handoff │     │ │
│  │  magic link (custom field) │ DND │ follow-up dates       │ │
│  └─────────────────────────────────┬───────────────────────┘ │
│                                    │                          │
│  ┌─────────────────────────────────┴───────────────────────┐ │
│  │              Calendars & Booking                         │ │
│  │  Multi-calendar │ Availability check │ Auto-book         │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  Webhook OUT ──────────────────────────────────────────────► │
│  API IN ◄──────────────────────────────────────────────────  │
└──────────────────────────────────────────────────────────────┘
                           │
              Webhook / API (bidirectional)
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    n8n (Workflow Engine)                       │
│                                                               │
│  ┌─────────────────────┐    ┌──────────────────────────────┐ │
│  │  MAIN CHAT AGENT    │    │   FOLLOW-UP AGENT            │ │
│  │  ┌───────────────┐  │    │   ┌──────────────────────┐   │ │
│  │  │ Primary LLM   │  │    │   │ Primary LLM          │   │ │
│  │  │ (Claude 4.5   │  │    │   │ (Claude 4.5 Sonnet)  │   │ │
│  │  │  Sonnet)      │  │    │   └──────────┬───────────┘   │ │
│  │  └───────┬───────┘  │    │   ┌──────────▼───────────┐   │ │
│  │  ┌───────▼───────┐  │    │   │ Backup LLM           │   │ │
│  │  │ Backup LLM    │  │    │   │ (Gemini 3 Pro)       │   │ │
│  │  │ (Gemini 3     │  │    │   └──────────────────────┘   │ │
│  │  │  Pro)         │  │    │   Full prompt control        │ │
│  │  └───────┬───────┘  │    │   Full contact context       │ │
│  │  ┌───────▼───────┐  │    │   Chat memory access         │ │
│  │  │ Error Handler │  │    │   Dual LLM + fallback        │ │
│  │  └───────────────┘  │    └──────────────────────────────┘ │
│  │                     │                                     │
│  │  Unlimited prompt   │    ┌──────────────────────────────┐ │
│  │  3rd party APIs     │    │   MAGIC LINK GENERATOR       │ │
│  │  Custom tools       │    │   (Demo link creation)       │ │
│  │  Web search         │    └──────────────────────────────┘ │
│  │  Sub-workflows      │                                     │
│  └─────────────────────┘    ┌──────────────────────────────┐ │
│                              │   DEMO BOT WORKFLOWS         │ │
│                              │   Per-channel trigger bots   │ │
│                              │   SMS | Voice | WA | Chat    │ │
│                              └──────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## Key Patterns for Universal SOP (Updated):

### Pattern: Dual-Agent Architecture
- **Main Agent:** Live conversation handler (unlimited prompt, dual LLM, tools)
- **Follow-Up Agent:** Dedicated proactive follow-up (separate prompt, full context, dual LLM)
- Both share GHL API access and contact memory
- **Universal application:** Any LC platform needs both agents

### Pattern: Multi-Message Intelligence
- Gather messages within time window → process as single input → single response
- Prevents bot spam / awkward rapid-fire replies
- **Universal application:** Essential for any chatbot on any LC platform

### Pattern: Human Handoff via Tags
- AI detects limitation → adds tag in LC platform → triggers internal notification
- **Universal application:** All LC platforms support tags → this pattern transfers directly

### Pattern: Channel Routing via LC Platform
- GHL handles channel routing natively (SMS, WhatsApp, IG, FB, Live Chat)
- n8n doesn't need to know which channel — GHL routes replies correctly
- **Universal application:** LC platforms handle channel routing; AI agent just sends/receives via LC API

### Pattern: Self-Service DND
- Contact requests no contact → AI triggers DND in LC platform
- **Universal application:** Most LC platforms have DND features

### Pattern: Calendar Integration
- AI reads calendar availability → books appointments → confirms with contact
- **Universal application:** All LC platforms have calendar/scheduling features

### Pattern: Dynamic Prompt with Variables
- System prompt includes GHL variables (contact data, form responses, etc.)
- **Universal application:** Any LC platform's custom fields can be injected into prompts

---

## Gap Analysis (Cumulative):

From Modules 1-5:
- [ ] Exact n8n workflow JSON/configuration
- [ ] GHL API authentication setup
- [ ] n8n credential configuration for GHL
- [ ] AI Delta Response System internals
- [ ] OpenRouter / LLM API key setup
- [ ] Webhook URLs and payloads
- [ ] Domain/DNS configuration
- [ ] n8n hosting specifics

From Module 6:
- [ ] **7-Day Blueprint document** (attachment missing — needs re-upload)

From Module 7:
- [ ] Multi-message intelligence time window configuration
- [ ] How exactly the webhook from GHL to n8n is configured
- [ ] How n8n routes replies back to GHL (which API endpoints)
- [ ] How contact memory is stored and retrieved
- [ ] How follow-up agent is triggered (GHL workflow → n8n? or n8n scheduled?)
- [ ] How custom tools/sub-workflows are connected to the main agent
- [ ] Calendar API integration details
- [ ] Human handoff notification details (email? SMS? GHL notification?)

**These gaps should be filled by the remaining modules (AI Agency Setup, AI Delta Response System, Sales Process, etc.)**
