# Goldie Stack — Full SOP (30 Steps, 7 Phases)

> The complete step-by-step process to set up The Infinite Context Engine™
> Source: Julian Goldie SEO — Skool Post #2
> Related: [[goldie-stack-quickstart]] | [[goldie-stack-launch-plan]] | [[goldie-stack-capabilities-general]]

---

## Overview

This SOP covers the entire Goldie Stack setup process from zero to a fully operational infinite memory system. It spans 30 steps across 7 phases.

**The Big Idea:** OMI records your life → Obsidian stores your memories → Hermes Agent reads them → Your AI finally knows you.

---

## ✅ PHASE 1: Set Up OMI (Steps 1-5)

OMI is a free app that runs in the background of your computer. It listens through your microphone and watches your screen, quietly taking notes on everything you do, say, and work on.

**Step 1.** Go to [omi.me](https://omi.me) and download the app for your device.

**Step 2.** Create a free OMI account.

**Step 3.** Open OMI and grant it microphone access when prompted.

**Step 4.** Enable screen recording permission in your system settings.

**Step 5.** Let OMI run for at least one full working day before moving to the next phase. This gives it enough data to generate meaningful memories.

---

## ✅ PHASE 2: Set Up Obsidian (Steps 6-9)

Obsidian is a free note-taking app that acts as your memory vault — the storage layer of the Infinite Context Engine.

**Step 6.** Go to [obsidian.md](https://obsidian.md) and download Obsidian for free.

**Step 7.** Open Obsidian and create a new vault.

**Step 8.** Name the vault something clear — for example: "My AI Memory Vault."

**Step 9.** Note down the folder location of your vault on your computer. You'll need this path in later phases.

---

## ✅ PHASE 3: Connect OMI To Obsidian (Steps 10-15)

This phase bridges the capture layer (OMI) with the storage layer (Obsidian).

**Step 10.** Inside OMI, navigate to the Memories section.

**Step 11.** Find the integration or export option.

**Step 12.** Select Obsidian as your export destination.

**Step 13.** Point OMI to your Obsidian vault folder (the path from Step 9).

**Step 14.** Hit export and watch your memories flow into Obsidian.

**Step 15.** Check the vault — you should see a memories file already there.

---

## ✅ PHASE 4: Get Your File Path (Steps 16-20)

Every AI agent needs the exact file path to read your memory file. This phase gets that path.

**Step 16.** Open your Obsidian vault folder in Finder (Mac) or File Explorer (Windows).

**Step 17.** Right-click on the memories file.

**Step 18.** Select "Get Info" (Mac) or "Properties" (Windows).

**Step 19.** Copy the full file path — it will look something like:
- Mac: `/Users/YourName/ObsidianVault/OMI_Memories.md`
- Windows: `C:\Users\YourName\ObsidianVault\OMI_Memories.md`
- Linux: `/home/yourname/ObsidianVault/OMI_Memories.md`

**Step 20.** Save this file path somewhere easy to access (clipboard, notes app, etc.).

---

## ✅ PHASE 5: Connect Hermes Agent To Your Vault (Steps 21-24)

Now you wire the AI agent (Hermes) to read your memory file.

**Step 21.** Open Hermes Agent.

**Step 22.** In the chat or settings, type a command like this:
```
Use this file path for your memory and context: [PASTE YOUR FILE PATH HERE]
```

**Step 23.** Hermes will confirm it has read your memory file.

**Step 24.** Test it by asking Hermes something specific about you — watch it answer correctly using your memories.

---

## ✅ PHASE 6: Repeat For Other AI Tools (Steps 25-27)

One of the most powerful aspects of this system: the same memory file works with every AI tool.

**Step 25.** Open OpenClaw or any other local AI agent you use.

**Step 26.** Give it the same file path command:
```
Use this file path for your memory and context: [PASTE YOUR FILE PATH HERE]
```

**Step 27.** Every AI tool you use can now share the same memory. One vault. All tools. Infinite context.

---

## ✅ PHASE 7: Let It Run (Steps 28-30)

The system is now live. This phase is about maintenance and growth.

**Step 28.** Leave OMI running every day as you work. It captures memories silently in the background.

**Step 29.** Set a reminder once a week to export fresh memories from OMI to Obsidian.

**Step 30.** Over time, your AI gets smarter and more personalised with zero extra effort from you. The compounding effect kicks in — every day the system knows you better.

---

## The Four-Layer Framework

The SOP above implements the **Infinite Context Engine™** — a four-layer framework:

| Layer | What Happens | Tool |
|-------|-------------|------|
| 🔵 **Layer 1: CAPTURE** | OMI records everything you say, do, and think | OMI |
| 🟣 **Layer 2: ORGANISE** | OMI processes raw recordings into clean, structured memory notes | OMI |
| 🟢 **Layer 3: STORE** | Obsidian holds your memory vault on your local machine | Obsidian |
| 🟡 **Layer 4: DEPLOY** | Your AI agents read the vault and begin every conversation already knowing you | Hermes, OpenClaw, Claude Code, etc. |

---

## Key Principles

1. **Zero manual work after setup** — OMI runs in the background, exports to Obsidian automatically, Hermes reads it automatically
2. **One file path, all tools** — The Obsidian vault is just a folder of text files; any AI that can read a file path can use your memories
3. **Compounding effect** — The longer you use it, the smarter your AI gets
4. **Completely free** — OMI is free, Obsidian is free, Hermes Agent is free

---

## For VPS / Docker Users

If you're running the Goldie Stack on a VPS (like the Agent OS system):
- The Obsidian vault lives in a Docker volume (`obsidian-vault-data`)
- OMI is not needed on the VPS — memory capture happens via the Obsidian vault directly
- Hermes Agent and OpenClaw both mount the same vault volume
- The "file path" inside the container is `/data/obsidian-vault/`
- Memory persistence is handled by Docker volume mounts, not OMI exports

---

## Related

- For the quickstart (Docker/VPS deployment): `goldie-stack-quickstart.md`
- For the 30-day roadmap: `goldie-stack-launch-plan.md`
- For the full prompt library: `goldie-stack-prompts.md`
- For the capability reference: `goldie-stack-capabilities-general.md`
