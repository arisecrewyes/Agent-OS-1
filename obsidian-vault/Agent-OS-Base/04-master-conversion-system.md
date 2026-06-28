# Master Skool Post Conversion System

> The complete unified process for converting any Julian Goldie Skool post into Agent OS documentation.
> Source: Derived from Skool Posts #1–#4 conversion experience.
> Related: [[01 - QuickStart Guide]] | [[02 - Launch Plan]] | [[03 - Prompt Library]]

---

## The Combined Workflow

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

## Pre-Setup (Before D1)

- **Step A:** VPS audit live at GitHub link
- **Step B:** Manual cleanup complete
- **Step C:** GitHub repo ready with PAT
- **Step D:** Repo structure understood (Version 1 + Version 2)

## D1: Analyze YouTube Video

- Fetch metadata (title, views, duration, description)
- Read full transcript
- Note: these are live demos, not tutorials — the "what's possible" not "how to build"
- The Skool post text has the actual build instructions

## D2: Analyze Skool Post Text

Content types to identify:
- Conceptual framework → Framework file
- Step-by-step walkthrough → QuickStart
- Structured timeline → Launch Plan
- Ready-to-use prompts → Prompt Library
- Limiting beliefs → Limiting Belives file
- Tool references → Tool Reference file
- Use cases → Capability Reference
- Troubleshooting → Capability Reference

## D3: Analyze Attachments

- ZIP files, markdown files, images, transcripts
- Each one may contain additional instructions or resources

## D4: VPS Installation Plan

- Adapt Mac/Windows → Linux/Docker
- Note VPS differences
- Specify compose project

## D5: Clarifying Questions

Ask about: Obsidian path, GitHub path, format, depth, cross-references, scope.
Keep asking until 98% understanding.

## D6: Execute

### Obsidian Vault
```
<Post-Name>/
├── 00-index.md
├── 01-quickstart.md
├── 02-launch-plan.md
├── 03-prompt-library.md
├── 04-capability-reference.md
└── NN-<name>.md
```

### GitHub Repo
```
docs/
├── <topic>-capabilities-general.md
├── <topic>-capabilities-vps-annotated.md
├── <topic>-agentos-ecosystem.md
├── <topic>-quickstart.md
├── <topic>-launch-plan.md
├── <topic>-prompts.md
├── <topic>-sop.md
└── <topic>-<name>.md
```

**Rules:**
- Only create files when content exists
- Ecosystem cross-reference always separate
- General version is primary document

## D7: VPS Audit

- For deployment: verify containers, check logs, verify Traefik
- For documentation-only: confirm no new containers

## D8: Repeat

- Provide summary
- Note security flags
- Wait for next post

## Content Type → File Mapping

| Content Type | File Pattern |
|-------------|-------------|
| Walkthrough | `<topic>-quickstart.md` |
| Timeline | `<topic>-launch-plan.md` |
| Prompts | `<topic>-prompts.md` |
| Capabilities | `<topic>-capabilities-general.md` |
| VPS-specific | `<topic>-capabilities-vps-annotated.md` |
| Ecosystem | `<topic>-agentos-ecosystem.md` |
| SOP | `<topic>-sop.md` |
| Beliefs | `<topic>-limiting-beliefs.md` |
| Framework | `<topic>-framework.md` |
| Tool ref | `<topic>-<tool>-tool.md` |
