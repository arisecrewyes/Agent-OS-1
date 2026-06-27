# Goldie Stack — OMI Tool Reference

> Complete reference for OMI — the memory capture engine of the Infinite Context Engine™
> Source: Julian Goldie SEO — Skool Post #2
> Related: [[goldie-stack-sop]] | [[goldie-stack-framework]] | [[goldie-stack-capabilities-general]]

---

## What Is OMI?

OMI is a free app that runs in the background of your computer. It:
- **Listens** through your microphone
- **Watches** your screen
- **Quietly takes notes** on everything you do, say, and work on all day long
- **Organises** those notes into clean, readable memories
- **Exports** those memories to Obsidian (your memory vault)

It literally knows:
- What time you go to sleep
- What projects you're working on
- What music you like
- Your goals

---

## How OMI Works In The Stack

```
OMI (Capture + Organise) → Obsidian (Store) → Hermes/OpenClaw (Deploy)
```

OMI is **Layer 1 (Capture)** and **Layer 2 (Organise)** of the Infinite Context Engine™ framework.

---

## Setup Steps

1. Go to [omi.me](https://omi.me) and download the app
2. Create a free account
3. Grant microphone access
4. Enable screen recording permission
5. Let it run for at least one full working day
6. Connect to Obsidian via the Memories → Export flow

---

## Key Features

- **Background operation** — runs silently while you work
- **Audio capture** — listens to conversations and meetings
- **Screen capture** — watches what you do on your screen
- **Automatic organisation** — processes raw data into structured memories
- **Obsidian export** — sends memories directly to your vault
- **Optional chat** — you can chat directly with OMI (paid feature, not required)

---

## Important Notes

- OMI is **completely free** for the memory capture + Obsidian export feature
- The only optional paid feature is chatting directly with OMI — you don't need this for the Goldie Stack
- OMI requires **microphone** and **screen recording** permissions to work
- For best results, let it run for at least one full working day before expecting meaningful output

---

## For VPS / Docker Users

In the Agent OS system, OMI is **not needed on the VPS** because:
- The Obsidian vault is directly mounted as a Docker volume
- Memory capture happens via manual note-taking in Obsidian
- Agent logs and conversation history are automatically saved to the vault
- The Memory Engine indexes vault content for semantic search

OMI is designed for **local/desktop** use. On a VPS, the Obsidian vault itself serves as the capture and storage layer.

---

## Related

- For the full SOP: `goldie-stack-sop.md`
- For the framework: `goldie-stack-framework.md`
- For the quickstart: `goldie-stack-quickstart.md`
