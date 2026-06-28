# MEMORY.md - Long-Term Memory

_Last updated: 2026-06-28_

## GitHub - Agent OS 1 (Fresh Install)
- **Repo URL:** https://github.com/arisecrewyes/Agent-OS-1
- **PAT Token:** [SECREDENTIAL — stored in OpenClaw only, not in repo]
- **Token Name:** Agnet OS 1
- **Expires:** 2026-06-29
- **Purpose:** Fresh Agent OS installation (Julian Goldie Skool posts)
- **Deployment style:** Multiple compose files (Version 2) + master compose (Version 1)

## Agent OS System (Original - Being Replaced)
- **Old Repo:** https://github.com/arisecrewyes/agent-os
- **Old VPS Audit:** https://github.com/arisecrewyes/agent-os/blob/main/VPS-FULL-AUDIT.md
- **Status:** Being replaced by fresh install from Skool posts

## Hostinger VPS
- **IP:** 31.220.62.81
- **SSH Key:** /data/.openclaw/.ssh/id_ed25519_vps
- **Domain:** srv1121935.hstgr.cloud
- **Keep:** Traefik + n8n (root Docker project) — infrastructure layer
- **n8n future use:** Connect to Agent OS for workflow automation

## Installation Process
- Step A: VPS audit verified ✅
- Step B: User manually cleaned old projects ✅
- Step C: New repo + PAT ✅
- Step D: Install from Skool posts (D1-D8 loop)
  - Post #1: Original Agent OS (base) — **DEPLOYED ✅**
  - Post #2: Infinite memory — **DEPLOYED ✅** (Goldie Stack: Obsidian Vault + Memory Engine + Hermes Agent)
  - Post #3: OpenClaw capability reference — **DOCUMENTED ✅**
  - Post #4: Hermes Agent capability reference — **DOCUMENTED ✅**
  - Post #5: Hermes Build & Automate Anything (v0.9) — **DOCUMENTED ✅**
  - Post #6: Lead Connector Derivatives + Goldie SEO Framework + Landing Pages — **DOCUMENTED ✅**

## Documentation System (Established 2026-06-27)
- **Master conversion system:** `docs/master-skool-post-conversion-system.md` — unified D1-D8 + tutorial extraction
- **Per-post output:** QuickStart + Launch Plan + Prompt Library + Capability Reference (+ SOP, Framework, Limiting Beliefs, OMI Tool where applicable)
- **Naming convention:** `<topic>-<type>.md` in `docs/` and Obsidian sub-notes
- **Content-only creation:** No empty/placeholder files — saves VPS storage
- **Ecosystem cross-reference:** Always a separate file — never mixed into general reference
- **Quickstart guide:** `docs/tutorial-skool-post-conversion.md` — DIY walkthrough of the conversion process
- **Security flags:** Hermes `ADMIN_PASSWORD=admin123` flagged — change immediately
- **GitHub:** All docs pushed to `Agent-OS-1` repo, fully organized in README.md

## GoStackBase Connection (Established 2026-06-28)
- **Dashboard URL:** https://app.gostackbase.com (NOT gostackbase.com/login — 404s)
- **Location ID:** huqxBD72T6Abd4AJxAni
- **Auth:** LC SSO (email + password + OTP via proton.me)
- **API Base:** services.leadconnectorhq.com (shared LC infrastructure)
- **URL Pattern:** /v2/location/{locationId}/{section}
- **Status:** ✅ Browser login confirmed, full dashboard access
- **Full feature set:** CRM, automations, funnels, calendars, AI agents, client portals, memberships
- **No public funnel share links** (known limitation)
- **API key:** [SECREDENTIAL — stored in OpenClaw only, not in repo]
- **API key name:** OpenClaw Agent
- **API scopes:** contacts, calendars, workflows, pipelines, forms, custom fields, users (read/write)
- **API limitation:** Funnel/site creation NOT supported via API — must use browser builder
- **API docs:** `docs/sop-lc-private-integration-setup.md`
- **Test doc:** `docs/gostackbase-connection-test.md`

## Lead Connector Bridge Skill (Established 2026-06-28)
- **Skill:** `skills/lead-connector-bridge/` — AI agent connection to GHL, GoStackBase, BuildwithOS
- **Purpose:** Let any AI agent (OpenClaw, Hermes, Claude Code) connect to LC platforms and recreate templates, manage contacts, build funnels, trigger automations
- **Workflow:** Connect → Task → Execute → Verify
- **Includes:** 3 connection scripts, 3 reference files, SKILL.md (with 4 connection patterns)
- **Key discovery:** BuildwithOS real domain is `build-os.com` (not `buildwithos.com`)
- **Key discovery:** GoStackBase has NO public docs — uses shared LC infrastructure
- **Connection patterns:** Webhook→n8n→API, Direct API, Hybrid Agent→n8n→API, MCP (BuildwithOS only)

## Lead Connector Derivatives (Established 2026-06-27)
- **Platforms:** GoHighLevel, LeadConnector, GoStackBase, BuildwithOS (all LC derivatives)
- **User's stack:** GoStackBase (current) → BuildwithOS (future, higher affiliate payouts)
- **Comparison doc:** `docs/lead-connector-derivatives-comparison.md`
- **Conversion systems:** GHL→GoStackBase + GHL→BuildwithOS template conversion guides
- **Integration guide:** `docs/agent-os-lead-connector-integration.md` — OpenClaw + Hermes + n8n ↔ all platforms
- **API refs:** GHL V2 REST, BuildwithOS MCP + REST, GoStackBase REST
- **Obsidian:** `Lead-Connector-Derivatives/` vault with 8 sub-notes + index (includes Goldie SEO Framework)
- **Goldie SEO Framework:** `docs/goldie-seo-framework.md` — 5-phase AI SEO framework with 6 case studies
- **StackBase conversion:** `docs/stackbase-template-conversion.md` — honest guide (GoStackBase has no public funnel share links)
- GitHub commit: `62c4c2f` — Post #6 D3-D8 complete
- Agent OS Dashboard: https://agentos.srv1121935.hstgr.cloud
- OpenRouter API key: [SECREDENTIAL — stored in OpenClaw only, not in repo]
- **Dashboard live at: https://agentos.srv1121935.hstgr.cloud**

## Copy My AI Agency Course (Analyzed 2026-06-28)
- **Course Creator:** Zalo Kabche (Black Umbrella)
- **Platform:** learn.blackumbrella.app (behind login)
- **Google Drive (all files):** https://drive.google.com/drive/folders/1b7shAaiiJFKNiP2IpflCzEg9ouH5YQBF
- **Total modules:** 15 | **Total files:** 111 | **URLs analyzed:** 30+
- **Core system:** LC Platform (GHL/StackBase/BuildwithOS) ↔ n8n ↔ AI Agents
- **Critical discovery:** ALL LC derivatives share `services.leadconnectorhq.com` API — same Private Integration system, same endpoints, same auth. n8n workflows work identically across all platforms.
- **ADRS v3:** 60-node n8n workflow with dual-agent (Main Chat + Follow-Up), 6 AI tools (DND, booking, calendar, escalation, RAG, follow-up), dual LLM (Claude 4.5 Sonnet + Gemini 3 Pro)
- **Voice platform:** Retell AI (separate from n8n/GHL) — orchestrator routes to EN/ESP agents
- **12 universal integration patterns** extracted — documented in course-analysis/
- **Prompt Forge:** Meta-AI in Claude Projects generates client-specific chatbot prompts from questionnaire data
- **Pricing:** Essential Chat $3K+$99/mo, Professional Chat $5K+$99/mo, Voice $4-7K+$149-199/mo
- **Onboarding SOP:** Day 0 (create folder/WhatsApp/agreements) → Day 1-2 (follow-ups) → Strategy Call → Build → QA → Launch
- **A2P compliance:** Must wait 15 days for new LLCs, or register as Sole Proprietor first. Root domain must be compliant.
- **GitHub:** All analysis pushed to Agent-OS-1 repo (secrets sanitized from n8n JSON templates)

## Course Access SOP (Established 2026-06-28, Updated 2026-06-28)
- **SOP A:** `docs/sop-course-access-and-implementation.md` — DFY/DWY course implementation
  - Trigger: User mentions a "course" and wants it implemented
  - DFY: Agent does everything, user only does human-only tasks
  - DWY: Agent adapts course to user's tools/budget, works together
  - Post-implementation: Automate everything automatable, leave human-only tasks
- **SOP B:** `docs/sop-universal-lc-integration.md` — Universal LC integration
  - Trigger: User wants to connect n8n/OpenClaw/Hermes to any LC platform
  - All LC derivatives share `services.leadconnectorhq.com` API
  - 12 universal integration patterns extracted from CMAA course
  - Complete setup: Private Integration → n8n → AI agents → Voice → A2P
- **SOP C:** `docs/sop-lc-private-integration-setup.md` — API key creation for AI agents
  - Trigger: User wants programmatic API access to LC platform
  - Step-by-step: Settings → API → Private Integrations → Generate Token
  - Token shown ONCE — store as secredential only
- **Preferred access method:** Browser login to course platform
- **Credential security:** Never store in plain text, use browser session only

## Video Transcription Skill (Established 2026-06-28)
- **Skill:** `skills/video-transcription/` — Extract text from any online video
- **SOP:** `docs/sop-video-transcription.md` — Full platform-agnostic video transcription
- **Trigger:** "Transcribe this video" / "Extract text from course videos" / "Get captions from [URL]"
- **4 methods in cascade:** Platform transcript API → DOM caption scraping → yt-dlp + Whisper → Screen recording fallback
- **Tools:** yt-dlp (installed), whisper, ffmpeg, tesseract, youtube-transcript-api
- **Scripts:** `transcribe.sh` (single video), `batch_transcribe.py` (course-wide batch)
- **Platform notes:** YouTube (transcript API), ClientClub/GHL (blob URLs — needs screen recording), Vimeo/Wistia (yt-dlp), Teachable/Kajabi (DOM scrape)
- **Saved to:** GitHub + Obsidian vault + OpenClaw skills
