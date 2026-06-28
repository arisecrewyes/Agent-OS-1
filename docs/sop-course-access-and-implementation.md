# SOP: Course Access & Implementation — DFY / DWY / Automation

**Created:** 2026-06-28
**Version:** 2.0
**Trigger:** User mentions a "course" and wants it implemented (DFY or DWY)
**Applies to:** OpenClaw, Hermes Agent, Agent OS, Claude Code, or any AI agent

---

## Overview

This SOP governs how an AI agent accesses any online course, extracts all content, and implements it for the user in one of three modes:

1. **DFY (Done For You)** — Agent does everything. User only handles what AI physically cannot (signing contracts, 2FA, phone calls, payments).
2. **DWY (Done With You / Hybrid)** — Agent + User work together. Agent adapts course material to user's existing tools/budget and guides user through implementation.
3. **Post-Implementation Automation** — After DFY or DWY, the agent automates everything that can be automated, leaving only human-only tasks.

---

## Phase 1: Access

### Step 1.1 — Determine Access Method

| Method | When to Use |
|--------|-------------|
| **Browser Login** (preferred) | User has credentials for the course platform |
| **File Provision** | User provides downloaded course files (PDFs, videos, ZIP) |
| **URL + web_fetch** | Course content is publicly accessible |
| **Hybrid** | Some content behind login, some public |

### Step 1.2 — Browser Login Procedure

1. Open browser (OpenClaw browser tool)
2. Navigate to the course platform URL
3. Log in with user-provided credentials
4. Verify access — confirm all modules/lessons are visible
5. Document the platform type (Skool, Teachable, Kajabi, Black Umbrella, Thinkific, Podia, custom, etc.)

### Step 1.3 — Credential Security

- **NEVER** store credentials in plain text in code, commits, or memory files
- **NEVER** log credentials in chat output
- **Use browser session only** — credentials live in the browser, not in files
- **If credentials must be referenced:** Store only in MEMORY.md with flag: `[CREDENTIAL — do not expose in repo]`
- **After course work is complete:** Log out of the course platform via browser
- **Remind the user** to change their password after temporary credential sharing

### Step 1.4 — Platform-Specific Access Notes

| Platform | Access Method | Content Type | Notes |
|----------|--------------|--------------|-------|
| Skool | Browser login | Video + text + community | Transcripts available, community posts may have bonus content |
| Teachable | Browser login | Video + text + downloads | Structured modules, downloadable PDFs |
| Kajabi | Browser login | Video + text + community | All-in-one, course + community + blog |
| Black Umbrella | Browser login | Video + text + files | JS-rendered, needs browser tool |
| Thinkific | Browser login | Video + text + downloads | SCORM packages possible |
| Podia | Browser login | Video + text + downloads | Simple structure |
| Udemy | Browser login | Video + captions | Video captions available for extraction |
| Coursera | Browser login | Video + text | Some content paywalled per-course |
| Custom/Django | Browser login | Varies | Inspect page structure |
| Google Drive | Direct download | Files only | No video, but all documents accessible |
| YouTube | web_fetch | Video + auto-captions | Public content only, transcripts available |

---

## Phase 2: Extraction

### Step 2.1 — Iterate Every Module

For each module/lesson in the course:

1. **Open the module** in the browser
2. **Capture ALL content:**
   - Video transcripts (auto-generated or manual)
   - Text/lesson content
   - Attached files (PDFs, JSON, images, ZIP, code)
   - Embedded links and resources
   - Code snippets and configurations
   - Screenshots and diagrams
   - Community posts/comments (if applicable)
3. **Save** to organized directory: `course-analysis/<course-name>/`
4. **Extract all URLs** from each module
5. **Note module order and dependencies** (some modules require prior modules)

### Step 2.2 — File Organization

```
course-analysis/
  <course-name>/
    Module-01-<title>.md
    Module-02-<title>.md
    ...
    attachments/
    urls/
    ANALYSIS-Complete.md
```

### Step 2.3 — URL Extraction & Fetching

For every URL found in course content:

1. **Categorize:** API docs, tool signup, video, diagram, reference, payment, affiliate
2. **Fetch accessible URLs** via `web_fetch`
3. **Flag inaccessible URLs** (login walls, JS-rendered SPAs)
4. **Try browser** for JS-rendered content
5. **Analyze content** for technical details, architecture patterns, API endpoints

---

## Phase 3: Analysis

For each module, extract:

### Technical Architecture
- System components and their relationships
- Data flow diagrams
- API endpoints and authentication methods
- Integration patterns (webhooks, API calls, etc.)
- Error handling and fallback mechanisms

### Tools & Services Required
- List every tool, service, platform, and API mentioned
- Note pricing for each (free tier, paid, enterprise)
- Note access requirements (KYC, approval, invitation)
- Identify which tools are essential vs. optional

### Configuration Details
- Required accounts/APIs and their signup URLs
- Credential types and setup steps
- Environment variables and configuration values
- Per-channel or per-feature configurations

### Operational Processes
- Setup sequences (must follow order)
- Troubleshooting steps
- Testing/verification procedures
- Onboarding workflows

### Business Model
- Pricing structures
- Service tiers
- Legal agreements
- Revenue models

### Identified Gaps
- What's NOT covered by the course
- What requires external research
- What's platform-specific vs. universal
- What needs custom development

---

## Phase 4: Implementation Mode Selection

After analysis, present the user with the findings and ask which mode:

### Mode A: DFY (Done For You)

**Agent does everything.** The user only handles what AI physically cannot:
- Signing legal contracts
- 2FA / phone verification
- Calling banks or service providers
- Making payments (if no payment method on file)
- Physical actions (buying hardware, etc.)
- KYC/identity verification that requires the user's face/ID

**Agent handles:**
- Creating all accounts (where possible)
- Configuring all tools and integrations
- Implementing all course steps
- Testing and verification
- Automating everything automatable
- Reporting what needs human action

### Mode B: DWY (Done With You / Hybrid)

**Agent + User work together.** The agent adapts the course to the user's circumstances:

1. **Tool Substitution Analysis:**
   - For each tool the course requires, check:
     - Can the user afford it? (if not → find alternative)
     - Does the user have access? (if not → find alternative)
     - Does the user already have a tool that does the same thing? (if yes → use it)
   - Document all substitutions in a mapping table

2. **Adaptation Plan:**
   - Original tool → User's alternative tool
   - Step-by-step adaptation for each substitution
   - What changes in the workflow
   - What additional configuration is needed

3. **Guided Implementation:**
   - Agent does what it can
   - Agent instructs user on what they need to do
   - Agent verifies each step before moving on
   - Agent adapts in real-time based on user's results

### Mode C: Analysis Only

User just wants the course analyzed and documented (no implementation). Produce the full analysis and save to GitHub + Obsidian.

---

## Phase 5: Implementation (DFY or DWY)

### Step 5.1 — Pre-Implementation

1. **Present the implementation plan** to the user for approval
2. **List all required accounts/tools** and their signup URLs
3. **Identify blockers** (things the user must do first)
4. **Set up tracking** (spreadsheet or checklist of all steps)

### Step 5.2 — Account & Tool Setup

For each required tool/service:

1. **Check if user already has access** → use existing
2. **If not, attempt to create account** via browser
3. **If payment required** → ask user to provide payment or choose free tier
4. **If KYC/verification required** → flag for user action
5. **Configure the tool** per course instructions
6. **Verify the tool is working** before moving on

### Step 5.3 — Course Step Implementation

For each course step:

1. **Read the step** and understand what it accomplishes
2. **Check for prerequisites** (previous steps, accounts, configurations)
3. **Implement the step** using the appropriate tool (original or DWY substitute)
4. **Verify the step** worked correctly
5. **Document what was done** (screenshots, configs, notes)
6. **Move to next step**

### Step 5.4 — Handling Blockers

When the agent encounters something it can't do:

1. **Stop and notify the user** immediately
2. **Explain what's needed** (be specific)
3. **Provide exact steps** the user needs to take
4. **Wait for user to complete** the action
5. **Verify the action** was completed correctly
6. **Continue implementation**

**Common blockers:**
- Payment required → User must pay or choose free alternative
- 2FA / phone verification → User must provide code
- KYC / ID verification → User must submit documents
- Email confirmation → User must click link
- CAPTCHA → User must solve
- Phone call required → User must make the call
- Contract signing → User must sign

---

## Phase 6: Post-Implementation Automation

After all course steps are implemented:

### Step 6.1 — Identify Automatable Tasks

Review everything that was set up and identify:
- **Recurring tasks** that can be scheduled (cron jobs, n8n workflows)
- **Monitoring tasks** that can be automated (alerts, health checks)
- **Data flows** that can be automated (syncs, imports, exports)
- **Communication tasks** that can be automated (follow-ups, notifications)
- **Reporting tasks** that can be automated (dashboards, summaries)

### Step 6.2 — Build Automations

For each automatable task:
1. **Create n8n workflow** or **cron job** or **script**
2. **Test the automation** to verify it works
3. **Document the automation** (what it does, when to check it)
4. **Set up monitoring** (alert if automation fails)

### Step 6.3 — Human-Only Task List

Create a clear list of what the user must still do manually:
- **Daily/Weekly tasks** the user should monitor
- **Monthly tasks** the user should review
- **Exception handling** — what to do if something breaks
- **Contact information** for support/services

### Step 6.4 — Handoff Document

Produce a final document containing:
1. **What was implemented** (summary of everything set up)
2. **What was automated** (list of all automations)
3. **What the user must do** (human-only tasks with schedule)
4. **How to monitor** (what to check, how often)
5. **How to troubleshoot** (common issues and fixes)
6. **Credentials reference** (where everything is stored — securely)

---

## Phase 7: Save & Distribute

### GitHub Repository
- SOPs → `docs/`
- Course analysis → `docs/course-analysis/`
- Implementation configs → `configs/` (secrets redacted)
- Updated README.md

### Obsidian Vault
- Course summary note with backlinks
- Implementation notes
- Automation documentation

### OpenClaw Skill (if applicable)
If the course enables a new capability:
- Create/update skill in `skills/` directory
- Include SKILL.md with connection patterns
- Include scripts and reference files

### Memory Update
- Course analyzed (name, date, mode: DFY/DWY)
- Tools/services implemented
- Automations created
- Human-only tasks for user
- Cross-references to documentation

---

## Trigger Phrases

**This SOP activates when the user says:**
- "I have a course for you to implement"
- "Let me give you access to this course"
- "I want you to do this course for me" (DFY)
- "Help me work through this course" (DWY)
- "I want you to take this course"
- "Go through this course and set everything up"
- "Do this course for me"

---

## Examples

### Example: DFY Mode
**User:** "Here's the login to my CMAA course. Set everything up for me."
**Agent:** Logs in → Extracts all 15 modules → Analyzes → Creates all accounts → Configures n8n + GHL + Retell → Implements ADRS → Sets up automations → Reports: "Everything is done. You just need to: 1) Pay the Retell bill, 2) Verify your A2P phone number, 3) Sign the GHL terms."

### Example: DWY Mode
**User:** "I want to do this course but I can't afford Retell AI. What are my options?"
**Agent:** Analyzes → Identifies Retell AI as voice platform → Researches alternatives (VAPI, Bland, Voiceflow) → Presents comparison → User chooses VAPI → Agent adapts all voice workflows to VAPI → Continues implementation with substituted tool.

### Example: Analysis Only
**User:** "Just analyze this course and tell me what I'd need."
**Agent:** Logs in → Extracts → Analyzes → Produces report: "You'd need: GHL ($297/mo), n8n (self-hosted), Retell AI ($0.15/min), Anthropic API, Gemini API. Total minimum: ~$500/mo + setup time of 5-7 days."
