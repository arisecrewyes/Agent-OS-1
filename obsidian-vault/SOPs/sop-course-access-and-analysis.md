# SOP: Course Access & Analysis — Agent Procedure

**Created:** 2026-06-28
**Version:** 1.0
**Trigger:** Anytime the user mentions a "course" and provides access
**Purpose:** Standardized process for any AI agent (OpenClaw, Hermes, etc.) to access, extract, and analyze online course content

---

## Overview

When the user mentions a course they want analyzed, this SOP governs how the agent accesses, extracts, and processes all course material into actionable documentation and system improvements.

---

## Step 1: Access the Course

### Method A: Browser Login (PREFERRED)
When the user provides login credentials for a course platform:

1. **Open the browser** (OpenClaw browser tool)
2. **Navigate** to the course URL
3. **Log in** with the provided credentials
4. **Verify access** — confirm all modules/lessons are visible
5. **Document** the platform type (Skool, Teachable, Kajabi, Black Umbrella, custom, etc.)

### Method B: File/Document Provision
When the user provides course content as files or transcripts:

1. **Accept all files** (Google Drive, direct upload, paste)
2. **Organize by module/lesson order**
3. **Document** any gaps between provided content and full course

### Method C: Hybrid
When some content is accessible and some requires credentials:

1. Process what's available immediately
2. List what's behind login walls
3. Request credentials for remaining content

### ⚠️ Credential Security
- **Never store credentials in plain text** in code, commits, or memory files
- **Use browser session** — credentials are handled by the browser, not stored
- **If credentials must be noted:** Store only in MEMORY.md with a flag like `[CREDENTIAL — do not expose]`
- **After course analysis is complete:** Log out of the course platform via browser
- **Remind the user** to change their password if they shared it temporarily

---

## Step 2: Systematic Course Extraction

### Iterate Through Every Module
For each module/lesson in the course:

1. **Open the module**
2. **Capture ALL content:**
   - Video transcripts (if available)
   - Text/lesson content
   - Attached files (PDFs, JSON, images, ZIP)
   - Embedded links
   - Code snippets
   - Screenshots/diagrams
3. **Save** to organized directory: `course-analysis/<course-name>/`
4. **Extract all URLs** from each module
5. **Note module order and dependencies**

### File Organization
```
course-analysis/
  <course-name>/
    Module-01-<title>.md          # Clean transcript/content
    Module-02-<title>.md
    ...
    attachments/                   # All downloaded files
      workflow-1.json
      prompt-template.md
      ...
    urls/                          # Extracted URLs + fetched content
    ANALYSIS-Complete.md           # Final combined analysis
```

### URL Extraction & Analysis
For every URL found in course content:

1. **Categorize:** API docs, tool signup, video, diagram, reference, payment
2. **Fetch accessible URLs** via `web_fetch`
3. **Flag inaccessible URLs** (login walls, JS-rendered SPAs needing browser)
4. **Try browser** for JS-rendered content
5. **Analyze content** for technical details, architecture patterns, API endpoints

---

## Step 3: Deep Analysis

For each module, extract:

### Technical Architecture
- System components and their relationships
- Data flow diagrams
- API endpoints and authentication methods
- Integration patterns (webhooks, API calls, etc.)
- Error handling and fallback mechanisms

### Configuration Details
- Required accounts/APIs and their URLs
- Credential types and setup steps
- Environment variables and custom values
- Per-channel configurations

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

## Step 4: Systemize & Universalize

### Pattern Extraction
Identify and document all reusable patterns:
- Connection patterns (how systems communicate)
- Configuration patterns (how settings are stored/used)
- Workflow patterns (how processes are structured)
- Deployment patterns (how systems are provisioned)

### Universal Adaptation
For each pattern, document:
- **What's universal** (works on any platform)
- **What's platform-specific** (needs adaptation)
- **How to adapt** for each known variant
- **What to test** when adapting

### SOP Creation
Transform analysis into:
1. **Standard Operating Procedure** — step-by-step anyone can follow
2. **Quick Start Guide** — fastest path to working system
3. **Troubleshooting Guide** — common issues and fixes
4. **Reference Documentation** — API endpoints, configs, patterns

---

## Step 5: Save & Distribute

### GitHub Repository
Push all documentation to the Agent OS repository:
- SOPs → `docs/`
- Analysis → `docs/course-analysis/`
- Updated README.md with new content references

### Obsidian Vault
Sync key documents to the Obsidian Vault for human-accessible reference:
- Created/updated notes in appropriate vault folders
- Cross-references and backlinks

### OpenClaw Skill
If the course enables a new capability:
- Create/update skill in `skills/` directory
- Include SKILL.md with connection patterns and procedures
- Include any scripts or reference files needed

### Memory Update
Update MEMORY.md with:
- Course analyzed (name, date, key findings)
- New skills/capabilities discovered
- Any credentials or access notes (securely)
- Cross-references to created documentation

---

## Quick Reference: Course Platform Types

| Platform | Access Method | Notes |
|---|---|---|
| Skool | Browser login | Video-heavy, transcripts available |
| Teachable | Browser login | Structured modules, downloadable PDFs |
| Kajabi | Browser login | All-in-one, course + community |
| Black Umbrella | Browser login | JS-rendered, needs browser tool |
| Udemy | Browser login | Video captions available |
| Coursera | Browser login | Some content paywalled |
| Custom/Django | Browser login | Varies widely |
| Google Drive | Direct download | Files only, no video |
| YouTube | web_fetch | Public content, transcripts available |

---

## Trigger Phrase

**Any time the user says something like:**
- "I have a course for you to analyze"
- "Let me give you access to this course"
- "Here's a course I want you to go through"
- "I want you to take this course"

**→ This SOP activates automatically.**

1. Confirm understanding
2. Request access method (credentials, files, or URL)
3. Follow Steps 1-5
4. Deliver systematic output
