# Goldie Stack — Full SOP (30 Steps, 7 Phases)

> The complete step-by-step process to set up The Infinite Context Engine™
> Source: Julian Goldie SEO — Skool Post #2
> Related: [[01-quickstart]] | [[02-launch-plan]] | [[00-index]]

---

## Phase 1: Set Up OMI (Steps 1-5)

1. Go to [omi.me](https://omi.me) and download the app
2. Create a free account
3. Grant microphone access
4. Enable screen recording permission
5. Let OMI run for at least one full working day

## Phase 2: Set Up Obsidian (Steps 6-9)

6. Go to [obsidian.md](https://obsidian.md) and download Obsidian
7. Open Obsidian and create a new vault
8. Name the vault (e.g., "My AI Memory Vault")
9. Note down the folder location

## Phase 3: Connect OMI To Obsidian (Steps 10-15)

10. Inside OMI, navigate to Memories
11. Find the integration/export option
12. Select Obsidian as export destination
13. Point OMI to your Obsidian vault folder
14. Hit export
15. Check the vault for the memories file

## Phase 4: Get Your File Path (Steps 16-20)

16. Open vault folder in Finder/File Explorer
17. Right-click on the memories file
18. Select "Get Info" (Mac) or "Properties" (Windows)
19. Copy the full file path
20. Save the path for later

## Phase 5: Connect Hermes Agent (Steps 21-24)

21. Open Hermes Agent
22. Type: "Use this file path for your memory and context: [PASTE PATH]"
23. Hermes confirms it read the file
24. Test by asking Hermes something specific about you

## Phase 6: Repeat For Other AI Tools (Steps 25-27)

25. Open OpenClaw or any other AI agent
26. Give it the same file path command
27. One vault. All tools. Infinite context.

## Phase 7: Let It Run (Steps 28-30)

28. Leave OMI running every day
29. Weekly: export fresh memories from OMI to Obsidian
30. Over time: your AI gets smarter with zero extra effort

---

## The Four-Layer Framework

| Layer | What Happens | Tool |
|-------|-------------|------|
| 🔵 CAPTURE | OMI records everything | OMI |
| 🟣 ORGANISE | OMI processes into structured notes | OMI |
| 🟢 STORE | Obsidian holds your vault | Obsidian |
| 🟡 DEPLOY | AI agents read vault → know you | Hermes, OpenClaw |

## For VPS / Docker Users

- Obsidian vault lives in Docker volume (`obsidian-vault-data`)
- OMI is not needed on the VPS
- Hermes Agent and OpenClaw both mount the same vault
- File path inside container: `/data/obsidian-vault/`
