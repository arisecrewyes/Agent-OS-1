# 🔄 Master Skool Post Conversion System

> The complete, unified process for converting any Julian Goldie Skool post into Agent OS documentation.
> Source: Derived from Skool Posts #1–#4 conversion experience.
> Related: [[tutorial-skool-post-conversion]] | [[agentos-base-quickstart]] | [[goldie-stack-sop]]

---

## Overview

This document is the **single source of truth** for how to convert any Skool post from Julian Goldie into a complete Agent OS documentation package. It merges the original D1-D8 conversion loop with the tutorial extraction workflow discovered during Posts #3 and #4.

**Who this is for:** Anyone (human or AI) who needs to process a Skool post into the Agent OS system.

---

## The Combined Workflow At A Glance

```
D1: Analyze YouTube video (if provided)
D2: Analyze Skool post text + links
D3: Analyze attachments one by one
D4: Produce step-by-step installation plan for Hostinger VPS
D5: Ask clarifying questions until 98% mutual understanding
D6: Execute continuously — produce ALL documentation files
D7: Audit VPS post-install and push to GitHub
D8: Repeat for next Skool post
```

---

## Pre-Setup (Before D1)

Before starting the loop, ensure these prerequisites are in place:

### Step A: VPS Audit Live
- The VPS audit must be live at the GitHub repo URL
- If not, generate one using the current Docker container state

### Step B: Manual Cleanup Complete
- Old projects cleaned from VPS
- Only infrastructure (Traefik + n8n) remains unless otherwise specified

### Step C: GitHub Repo Ready
- New public GitHub repo with PAT token
- Repo URL accessible
- Used for all doc/audit saves

### Step D: Repo Structure Understood
- **Version 1:** Single master `docker-compose.yml` with everything
- **Version 2:** Multiple compose files by project/component + README with deployment order
- Both versions in the same repo, clearly labeled
- Agent OS uses **Version 2** (multiple compose files — safer for VPS)

---

## The Core Loop (D1–D8)

### D1: Analyze YouTube Video (If Provided)

**Input:** YouTube link from Julian Goldie's Skool post

**Process:**
1. Fetch video metadata (title, views, duration, description, published date)
2. Fetch or read the full transcript
3. Analyze the video content meticulously:
   - What is being demonstrated?
   - What are the key technical details?
   - What installation commands are shown?
   - What tools/services are mentioned?
   - What's the "what's possible" vs "how to build it" distinction?
4. Note any links in the video description

**Output:** D1 Analysis containing:
- Video metadata table
- Module/chapter breakdown with timestamps
- Key technical details for installation
- Links referenced
- Critical observations (is it a demo or a tutorial?)

**Important:** These videos are typically **live demo/training sessions**, not pre-produced tutorials. The full course content is inside the paid AI Profit Boardroom community. The video gives you the "what's possible" and architecture understanding. The Skool post text (D2) gives you the "how to build it."

---

### D2: Analyze Skool Post Text + Links

**Input:** The full text of the Skool post (pasted or attached) + any links

**Process:**
1. Read the entire post meticulously
2. Identify and categorize the content types:
   - **Conceptual framework** — the big idea, mental model
   - **Step-by-step walkthrough** — actual implementation instructions (→ QuickStart)
   - **Launch plan** — structured timeline, day-by-day or week-by-week (→ Launch Plan)
   - **AI prompts** — ready-to-use prompts (→ Prompt Library)
   - **Belief shifts** — limiting beliefs and replacements (→ Limiting Beliefs)
   - **Tool references** — specific tools, apps, services mentioned
   - **Use cases** — practical applications
   - **Troubleshooting** — common issues and fixes
   - **Comparisons** — vs other tools
   - **Resources** — downloads, links, update files
3. Cross-reference with D1 video analysis for completeness
4. Note all links, GitHub repos, URLs mentioned

**Output:** D2 Analysis containing:
- Content type classification
- Key findings for documentation
- Cross-reference with video (if applicable)
- Clarifying questions for D5

---

### D3: Analyze Attachments One By One

**Input:** Files attached to the Skool post (zip files, markdown files, images, etc.)

**Process:**
1. For each attachment:
   a. Download/read the file
   b. Analyze its contents
   c. Determine how it relates to the post
   d. Note any additional instructions, templates, or resources
2. Common attachment types:
   - **ZIP files** — contain project files, READMEs, update guides
   - **Markdown files** — supplementary guides, SOPs
   - **Images** — diagrams, screenshots, reference material
   - **Transcript files** — full video transcripts (often .docx or .txt)

**Output:** D3 Analysis for each attachment

---

### D4: Produce Step-by-Step Installation Plan for Hostinger VPS

**Input:** All D1-D3 analyses

**Process:**
1. Synthesize all technical details into a Hostinger VPS-specific installation plan
2. Adapt any Mac/Windows instructions to Linux/Docker equivalents
3. Note where the VPS setup differs from the "recommended" local approach
4. Include Traefik + n8n integration notes
5. Specify which compose project the post belongs to (or if a new one is needed)

**Output:** D4 Installation Plan

**For documentation-only posts** (like Posts #3 and #4): This step produces a brief note confirming no new installation is needed, plus any VPS-specific annotations for the capability reference.

---

### D5: Ask Clarifying Questions (Until 98% Understanding)

**Input:** All previous analyses

**Ask about:**
1. **Obsidian vault path** — where to save notes
2. **GitHub repo path** — where to save docs
3. **Document format** — single note vs multiple linked notes
4. **Technical depth** — general reference vs VPS-annotated vs both
5. **Cross-references** — should we link to existing Agent OS docs?
6. **Scope** — any specific focus areas or exclusions?
7. **QuickStart/Launch/Prompt extraction** — does the post contain walkthroughs, timelines, or prompts that should be separately extracted?

**Rule:** Keep asking until you have 98% mutual understanding. Never proceed with assumptions.

---

### D6: Execute Continuously (One Run)

This is the main execution phase. Work continuously — only pause if you need something from the user.

#### Part A: Obsidian Vault Notes

Create notes in the Obsidian vault following this structure:

```
obsidian-vault/<Post-Name>/
├── 00-index.md                    — Parent node with links to all sub-notes
├── 01-quickstart.md              — Step-by-step walkthrough (if post has walkthrough)
├── 02-launch-plan.md             — Structured timeline (if post has timeline)
├── 03-prompt-library.md          — Ready-to-use prompts (if post has prompts)
├── 04-capability-reference.md    — Full capability reference
├── 05-limiting-beliefs.md       — Belief shifts (if post has them)
├── 06-framework.md              — Conceptual framework (if post has one)
├── 07-<topic-specific>.md        — Any additional topic-specific notes
└── NN-<name>.md                  — Numbered sub-notes for any additional content
```

**Rules:**
- Only create files when content exists — no empty/placeholder files (saves VPS storage)
- Use wiki-links (`[[note-name]]`) to link between notes
- The index note must list all sub-notes with brief descriptions
- Each note should reference the source Skool post

#### Part B: GitHub Repo Docs

Create docs in the repo following this structure:

```
docs/
├── <topic>-capabilities-general.md        — General capability reference (anyone can use)
├── <topic>-capabilities-vps-annotated.md  — Same + VPS/Docker annotations
├── <topic>-agentos-ecosystem.md           — How it fits into Agent OS (separate, doesn't confuse future users)
├── <topic>-quickstart.md                 — Step-by-step walkthrough (if content exists)
├── <topic>-launch-plan.md                — Structured timeline (if content exists)
├── <topic>-prompts.md                    — Ready-to-use prompts (if content exists)
├── <topic>-sop.md                        — Full SOP with all steps (if post has detailed steps)
├── <topic>-limiting-beliefs.md           — Belief shifts (if post has them)
├── <topic>-framework.md                  — Conceptual framework (if post has one)
├── <topic>-omi-tool.md                   — Tool reference (if OMI is covered)
└── <topic>-<name>.md                     — Any additional docs
```

**Rules:**
- **General version** is the primary document — complete, accessible to anyone
- **VPS-annotated version** adds technical notes for the Hostinger VPS Docker setup
- **Ecosystem cross-reference** is ALWAYS a separate file — never mix VPS-specific details into the general reference
- Only create files when content exists — no empty/placeholder files

#### Part C: README Update

After creating all files:
1. Update the repo README.md with new entries
2. Organize by category (QuickStarts, Launch Plans, Prompt Libraries, Capability References, etc.)
3. Ensure all links work

---

### D7: Audit VPS Post-Install

**For deployment posts:**
1. Run `docker ps` to verify all containers are running
2. Check `docker compose logs` for any errors
3. Verify Traefik routing for new services
4. Push updated VPS audit to GitHub

**For documentation-only posts:**
1. Confirm no new containers were deployed
2. Note that existing containers are unchanged
3. Optionally push an updated audit

---

### D8: Repeat for Next Skool Post

After D7 is complete:
1. Provide a summary of what was created
2. Note any security flags or action items
3. Confirm readiness for the next post
4. Wait for the user to provide the next Skool post

---

## Content Type Extraction Guide

Different Skool posts contain different types of content. Here's how to handle each:

### Type 1: Build Guide (e.g., Post #1 — Agent OS Base)
**Contains:** Build prompts, setup instructions, agent connection steps, first-run checks
**Extract:**
- QuickStart → build prompts in order, connecting agents, first-run check
- Prompt Library → build prompts + usage prompts + test prompts
- Launch Plan → if not explicitly provided, create a sensible Day 1-3 → Week 1-2 → Month 1 structure

### Type 2: Infinite Memory System (e.g., Post #2 — Goldie Stack)
**Contains:** Conceptual framework, full SOP, 30-day roadmap, 100+ prompts, limiting beliefs
**Extract:**
- QuickStart → Docker deployment steps (VPS-specific)
- SOP → Full step-by-step process with all phases
- Launch Plan → Day-by-day, week-by-week timeline
- Prompt Library → ALL prompts, organized by category
- Limiting Beliefs → Wrong vs right beliefs
- Framework → The conceptual layers/model
- Capability Reference → Tool overview, use cases, comparisons

### Type 3: Capability Reference (e.g., Post #3 — OpenClaw)
**Contains:** What the tool is, installation, provider setup, skills, security, use cases, workflows
**Extract:**
- QuickStart → Installation steps, provider selection, messaging setup, skills
- Launch Plan → Day 1-3 → Week 1-2 → Month 1 onboarding timeline
- Prompt Library → All ready-to-use prompts from the post
- Capability Reference → Full feature reference with all sections
- Ecosystem Cross-Reference → How it fits into Agent OS

### Type 4: Capability Reference (e.g., Post #4 — Hermes Agent)
**Contains:** What the tool is, installation, model selection, messaging, training period, skills, scheduling, external tools, profiles, migration
**Extract:**
- QuickStart → Installation, setup, model selection, messaging, skills
- Launch Plan → Phase 1-4 timeline (7 days → 14 days → 21 days → 30 days)
- Prompt Library → All ready-to-use prompts
- Capability Reference → Full feature reference
- Ecosystem Cross-Reference → How it relates to OpenClaw, n8n, Obsidian, Agent OS Dashboard

---

## File Naming Conventions

| Content Type | File Pattern | Example |
|-------------|-------------|---------|
| QuickStart | `<topic>-quickstart.md` | `openclaw-quickstart.md` |
| Launch Plan | `<topic>-launch-plan.md` | `goldie-stack-launch-plan.md` |
| Prompt Library | `<topic>-prompts.md` | `hermes-prompts.md` |
| Capability Reference (General) | `<topic>-capabilities-general.md` | `openclaw-capabilities-general.md` |
| Capability Reference (VPS) | `<topic>-capabilities-vps-annotated.md` | `openclaw-capabilities-vps-annotated.md` |
| Ecosystem Cross-Reference | `<topic>-agentos-ecosystem.md` | `hermes-agent-agentos-ecosystem.md` |
| SOP | `<topic>-sop.md` | `goldie-stack-sop.md` |
| Limiting Beliefs | `<topic>-limiting-beliefs.md` | `goldie-stack-limiting-beliefs.md` |
| Framework | `<topic>-framework.md` | `goldie-stack-framework.md` |
| Tool Reference | `<topic>-<tool>-tool.md` | `goldie-stack-omi-tool.md` |
| Tutorial/Master Guide | `tutorial-<name>.md` | `tutorial-skool-post-conversion.md` |
| Master System | `master-<name>-system.md` | `master-skool-post-conversion-system.md` |

---

## Obsidian Vault Naming Conventions

| Post | Obsidian Parent Folder |
|------|----------------------|
| #1 — Agent OS Base | `Agent-OS-Base/` |
| #2 — Goldie Stack | `Goldie-Stack/` |
| #3 — OpenClaw | `OpenClaw-6-Hour-Course/` |
| #4 — Hermes Agent | `Hermes-Agent-Full-Course/` |

---

## Quality Checklist

Before marking D6 as complete, verify:

- [ ] All content types present in the post have corresponding files
- [ ] No empty/placeholder files exist (content-only creation)
- [ ] General capability reference is complete and accessible to anyone
- [ ] VPS-annotated version has all relevant technical notes
- [ ] Ecosystem cross-reference is a separate file
- [ ] QuickStart has step-by-step walkthrough (if post has one)
- [ ] Launch Plan has structured timeline (if post has one)
- [ ] Prompt Library has ALL prompts organized by category (if post has them)
- [ ] Obsidian notes are linked via wiki-links
- [ ] GitHub README is updated with all new entries
- [ ] All files pushed to GitHub
- [ ] Security flags noted (hardcoded passwords, exposed services, etc.)

---

## Security Flags to Watch For

Always check for these in Skool posts and flag them in the VPS-annotated version:

- 🔴 Hardcoded passwords (e.g., `ADMIN_PASSWORD=admin123`)
- 🔴 Exposed API keys in examples
- 🔴 Services running without authentication
- 🔴 Default credentials that should be changed
- 🔴 Open ports that should be behind Traefik

---

## Summary

This system is designed to be **future-proof** — it works for any Skool post from Julian Goldie, whether it's a build guide, a capability reference, a memory system, or something entirely new. The key principles are:

1. **Extract everything** — capabilities, walkthroughs, timelines, prompts, beliefs, frameworks
2. **Separate concerns** — general reference vs VPS-specific vs ecosystem cross-reference
3. **Only create when content exists** — no empty files, no placeholder content
4. **Link everything** — Obsidian wiki-links, GitHub README, cross-references
5. **Flag security issues** — always check for hardcoded credentials and exposed services

---

## Related

- For the original tutorial: `tutorial-skool-post-conversion.md`
- For Post #1 docs: `agentos-base-quickstart.md` | `agentos-base-launch-plan.md` | `agentos-base-prompts.md`
- For Post #2 docs: `goldie-stack-sop.md` | `goldie-stack-launch-plan.md` | `goldie-stack-prompts.md` | `goldie-stack-limiting-beliefs.md` | `goldie-stack-framework.md`
- For Post #3 docs: `openclaw-quickstart.md` | `openclaw-launch-plan.md` | `openclaw-prompts.md`
- For Post #4 docs: `hermes-quickstart.md` | `hermes-launch-plan.md` | `hermes-prompts.md`
