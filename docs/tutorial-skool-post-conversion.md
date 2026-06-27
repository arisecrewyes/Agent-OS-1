# Tutorial: How to Convert a Skool Post into Agent OS Documentation

> A DIY step-by-step dummy-proof guide based on the actual process used for Skool Posts #3 and #4.
> Date: 2026-06-27

---

## Overview

This guide explains how to take a Julian Goldie Skool post (video + text) and convert it into:
1. **Obsidian Vault notes** — for your infinite memory system
2. **GitHub repo docs** — for public reference and reproducibility
3. **VPS audit** — for tracking changes (when applicable)

This process is for **knowledge capture posts only** (posts that teach capabilities/concepts without installing new software).

---

## Prerequisites

Before you start, make sure you have:

- ✅ **Public GitHub repo** with PAT token and repo URL
- ✅ **Obsidian Vault** path on your VPS (for local note storage)
- ✅ **YouTube link** to the Skool course video
- ✅ **Skool post text** (copy-paste from the Skool community post)
- ✅ **Any attachments** (transcript files, GitHub links, etc.)

---

## Phase 1: Analysis (D1-D3)

### Step D1 — Analyze the YouTube Video

1. You provide me with a **YouTube link**.
2. I attempt to fetch the video title, metadata, and description using web tools.
3. **YouTube descriptions are loaded dynamically via JavaScript**, so I may not get the full description automatically.
4. If a **transcript file (.docx)** is provided:
   - I read the ENTIRE transcript (often 3000+ lines for multi-hour courses)
   - I analyze it meticulously, noting every section, timestamp, command, and technical detail
5. If no transcript is provided:
   - I ask you to paste the YouTube description text manually
   - I analyze what I can and ask clarifying questions

**Output:** Complete breakdown of video content — every module, timestamp, command, and technical detail.

---

### Step D2 — Analyze the Skool Post Text

1. You provide me with the **full Skool post text** (copy-paste from Skool).
2. This is often a written version of the video course — structured, detailed, with headers and steps.
3. I cross-reference the text with the video transcript to fill any gaps.
4. I identify:
   - Installation steps
   - Configuration details
   - Commands and code snippets
   - External tools and APIs mentioned
   - Security warnings
   - Use cases
   - Comparison tables
   - Troubleshooting steps

**Output:** Structured analysis of all written content.

---

### Step D3 — Analyze Attachments

1. You provide attachments **one by one** (GitHub repo links, .docx files, URLs, etc.).
2. For each attachment:
   - **GitHub repos:** I check the README, structure, stars, license, and key features
   - **Transcript files (.docx):** I read and analyze the full content
   - **URLs:** I fetch and analyze the content
3. I integrate attachment findings into the overall analysis.

---

## Phase 2: Clarification (D5)

### Step D5 — Ask Clarifying Questions

Before producing documentation, I ask you clarifying questions to reach **98% mutual understanding**. Common questions:

1. **Purpose:** Is this a pure documentation/knowledge capture, or does it involve installing new software?
2. **Obsidian vault:** Where should notes go? Create a new parent node or use existing structure?
3. **GitHub repo:** Where should docs go? Create a new file or folder?
4. **Document format:** Single comprehensive note or multiple linked sub-notes?
5. **Technical depth:** Keep general, add VPS-specific annotations, or both?
6. **Cross-reference:** Should I create a separate file showing how this fits into the existing Agent OS ecosystem?

**Do NOT proceed to Phase 3 until you are satisfied with the answers.** We iterate until we're at 98%.

---

## Phase 3: Execution (D6)

### Step D6 — Produce All Documentation in One Continuous Run

Once clarifications are locked in, I create **all documentation** in one shot.

#### Part A: Obsidian Vault Notes

Create a folder structure in your Obsidian vault:

```
obsidian-vault/<Course-Name>/
  ├── 00-index.md                    ← Parent node (links to all sub-notes)
  ├── 01-<topic-1>.md               ← Sub-note
  ├── 02-<topic-2>.md               ← Sub-note
  ├── ...
  └── NN-<topic-N>.md               ← Sub-note
```

**Each note includes:**
- Title linking back to the index (`[[00 - Index|<Course> Full Course]]`)
- Content organized with headers, tables, code blocks
- Links between related sub-notes
- Metadata footer with tags and related notes

**The index (00-index.md) includes:**
- Course overview and source links
- Links to all sub-notes using Obsidian `[[wiki-link]]` syntax
- Quick start commands (if applicable)
- External resource links
- Metadata (tags, source, date)

**Typical sub-note topics (from Posts #3 and #4):**
- Overview & Key Differences
- Installation & Setup
- AI Provider / Model Selection
- Messaging Platform Integration
- Security Best Practices
- Practical Use Cases
- Advanced Features
- Workflow Examples
- Cost Optimization
- Comparisons & Troubleshooting

#### Part B: GitHub Repo Docs

Create a folder structure in the Agent OS repo:

```
Agent-OS-1/docs/<course-name>/
  ├── <topic>-capabilities-general.md           ← General reference
  ├── <topic>-capabilities-vps-annotated.md     ← VPS-specific annotations
  └── <topic>-agentos-ecosystem.md              ← Integration cross-reference
```

**General reference (`-general.md`):**
- Same content as Obsidian notes, formatted in Markdown
- No VPS-specific annotations — accessible to ANY user
- Includes all sections from the course

**VPS-annotated reference (`-vps-annotated.md`):**
- Same content as general, PLUS `[VPS]` annotation tags
- Annotations highlight:
  - Where the VPS setup differs from the "recommended" course approach
  - Docker-specific configuration notes
  - Security warnings specific to the deployment
  - Networking and port considerations
  - Volume persistence requirements
- Security issues (hardcoded passwords, exposed ports) are **explicitly flagged**

**Ecosystem cross-reference (`-agentos-ecosystem.md`):**
- Architecture diagram showing how the topic fits into the existing Agent OS stack
- Integration points with other agents (OpenClaw, n8n, Memory Engine, etc.)
- Communication paths (Docker network, APIs, webhooks)
- Container configuration details
- Summary of coexistence with other agents

#### Part C: README Update

Update the main `README.md` to:
- Add the post as completed in the Posts table
- List new documentation files in the Documentation table
- Update the quick start commands if applicable

---

## Phase 4: Review & Publish (D7-D8)

### Step D7 — VPS Audit (When Applicable)

For **documentation-only posts** (like Posts #3 and #4):
- No new containers were deployed
- Audit step is minimal — just confirm no changes were made
- Can be skipped or a brief note pushed to the repo

For **deployment posts** (like Posts #1 and #2):
- Run `docker ps` to verify all containers are healthy
- Check `docker logs` for any errors
- Verify Traefik routing is correct
- Test that the service is accessible via domain
- Push updated audit to GitHub (`docs/VPS-AUDIT.md`)

### Step D8 — Final Review & Commit

1. Review all created files for completeness
2. Push everything to GitHub with a clear commit message:
   ```
   docs: Add <Course Name> capability reference (Skool Post #N)

   - <file1>.md: <description>
   - <file2>.md: <description>
   - <file3>.md: <description>

   Source: <Original Source> - Skool Post #N '<Title>'
   Video: <YouTube URL>
   ```
3. Update README.md
4. Report to user with full summary of what was created

---

## Summary Checklist

Use this checklist for every Skool post conversion:

- [ ] **D1:** YouTube video analyzed (title, metadata, transcript read fully)
- [ ] **D2:** Skool post text analyzed (cross-referenced with transcript)
- [ ] **D3:** All attachments analyzed
- [ ] **D5:** Clarifying questions asked and answered (98% understanding)
- [ ] **D6-A:** Obsidian vault parent note created with links to sub-notes
- [ ] **D6-A:** All Obsidian sub-notes created with metadata footers
- [ ] **D6-B:** GitHub general reference doc created (`-general.md`)
- [ ] **D6-B:** GitHub VPS-annotated doc created (`-vps-annotated.md`)
- [ ] **D6-B:** GitHub ecosystem cross-reference created (`-agentos-ecosystem.md`)
- [ ] **D6-C:** README.md updated with new post and file links
- [ ] **D7:** VPS audit performed (minimal for doc-only posts)
- [ ] **D8:** All files pushed to GitHub with clear commit messages
- [ ] **D8:** Summary provided to user with full file listing

---

## Tips for Best Results

1. **Always provide the transcript file** if available — it contains far more detail than the video alone
2. **Include the Skool post text** even if you have a transcript — the written version is often better structured
3. **Be specific in D5 answers** about where you want files and what format you prefer
4. **Review the D4 plan** (if asked for) before I execute D6 — this is your chance to catch misunderstandings
5. **Check GitHub after D8** to verify all files are correctly pushed and formatted

---

## Metadata

- Tags: `agent-os`, `tutorial`, `documentation`, `skool`, `process-guide`
- Created: 2026-06-27
- Based on: Skool Post #3 (OpenClaw) and Skool Post #4 (Hermes Agent)
