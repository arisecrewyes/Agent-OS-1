---
tags:
  - hermes
  - hyperframes
  - ai-video
  - skool
  - video-production
  - free-tools
  - kokoro-tts
  - heygen
  - gsap
  - automation
  - content-creation
source: "Skool Post #34 — AI Profit Boardroom"
author: Julian
date: 2026-05-06
converted: 2026-06-29
platform: hermes-agent
---

# Hermes + Hyperframes

> [!info] Metadata
> - **Source:** [6th May: Hermes + Hyperframes](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=5a347e7ae7ba484f840d31d534235c11)
> - **Author:** Julian (AI Profit Boardroom)
> - **Date:** 6th May (original post)
> - **Topics:** Hermes Agent, HyperFrames, AI Video Creation, Free Tools, Kokoro TTS, HeyGen, GSAP Animations
> - **Related:** [[Hermes-Agent]], [[Agent-OS]], [[HyperFrames]], [[Kokoro-TTS]], [[Content-Automation]]

---

## Overview

**Hermes Agent + HyperFrames** = a fully automated, 100% free AI video production system. You describe what you want in plain English, and Hermes writes the script, generates the voiceover, builds animated scenes, and renders a professional MP4 — all without human intervention.

> "The future of content creation isn't hiring a video editor. It's teaching an AI to be one."

### The Two Tools

| Tool | What It Does | Cost |
|------|-------------|------|
| **Hermes Agent** | AI robot that runs tasks in plain English (183 skills, 30 tool categories) | Free |
| **HyperFrames** | Turns HTML into MP4 video using GSAP animations + Puppeteer rendering | Free, open-source (14,700+ GitHub stars) |

### Why They Work Together

> "Agents already speak HTML. HyperFrames just gives them a video renderer."

Hermes installs HyperFrames as a **skill**. When you ask for a video, Hermes:
1. Writes the script
2. Generates AI voiceover (Kokoro TTS)
3. Builds 7 animated HTML scenes
4. Renders final 1920x1080 MP4 in ~15 seconds

---

## How It Works — Real Session Breakdown

### Step-by-Step Flow

| Step | Action | Notes |
|------|--------|-------|
| 1 | `hermes update` | Always update first — downloads latest improvements |
| 2 | `hermes skills install hyperframes` | Security scan runs; sudo warnings are normal (FFmpeg) |
| 3 | `hermes` | Launch; confirm hyperframes appears under creative skills |
| 4 | Type video prompt | "create a beautiful video about [TOPIC] using the hyperframes skill" |
| 5 | Hermes writes script | YouTube-ready copy in seconds |
| 6 | Hermes generates voiceover | Uses `af_sky` voice via Kokoro TTS (free, local, offline) |
| 7 | Hermes builds 7 scenes | Animated text, neon accents, GSAP transitions |
| 8 | Hermes renders MP4 | `npx hyperframes render --quality high --output final.mp4` |

### The 7 Auto-Generated Scenes

1. Big bold title
2. Keyword research cards
3. Content creation
4. Backlink building
5. Tracking & analytics
6. Results screen
7. End screen with CTA

### Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `Could not fetch 'official/creative/hyperframes'` | Run `hermes update` first |
| Sudo/admin permission warnings | Normal for FFmpeg — type `y` to confirm |
| Hermes times out on command | Type `allow` to continue |
| Black/empty scenes in render | Hermes auto-fixes on next render pass |
| `---NEEDS SETUP---` | Let Hermes run the setup script |

---

## HyperFrames vs Alternatives

| Feature | HyperFrames | Traditional Editors | Remotion |
|---------|-------------|-------------------|----------|
| **Cost** | FREE | $$$$ | Paid license |
| **AI Agent support** | ✅ Built-in | ❌ | ❌ |
| **Build step needed** | ❌ None | N/A | ✅ Required |
| **Renders locally** | ✅ | ❌ | ✅ |
| **HTML-based** | ✅ | ❌ | ❌ |

### The 50+ Catalog Blocks

Pre-built video blocks (like LEGO pieces):

```bash
npx hyperframes add flash-through-white   # cinematic transition
npx hyperframes add instagram-follow      # social overlay
npx hyperframes add data-chart            # animated chart
```

---

## Full SOP — Setup Guide

### Pre-Requirements

- [ ] Mac or PC (Mac Studio recommended)
- [ ] Node.js v22+
- [ ] FFmpeg (`brew install ffmpeg` on Mac)
- [ ] Hermes Agent installed
- [ ] 2GB+ free disk space

### Installation

```bash
# Step 1: Update Hermes (REQUIRED — don't skip)
hermes update

# Step 2: Install HyperFrames skill
hermes skills install hyperframes

# Step 3: Launch Hermes
hermes
```

### Creating a Video

1. Inside Hermes, type: `create a beautiful video about [YOUR TOPIC] using the hyperframes skill`
2. Let Hermes work (don't touch anything — ~5–15 min)
3. Find your video at: `~/ai-seo-video/final.mp4`

### Key Commands

```bash
hermes update                          # Always update first
hermes skills install hyperframes      # Install the skill
hermes                                 # Launch Hermes

# Inside a HyperFrames project folder:
npx hyperframes init my-video          # Create new project
npx hyperframes preview                # Preview in browser
npx hyperframes lint                   # Check for errors
npx hyperframes render --quality draft # Fast test render
npx hyperframes render --quality high  # Final quality render
```

---

## 30-Day Implementation Roadmap

### Week 1: Setup & First Videos

| Day | Task |
|-----|------|
| 1 | Install Hermes + HyperFrames. Create first test video. |
| 2 | Business explainer video (homepage). |
| 3 | "How it works" video for main service (sales page). |
| 4 | "Top 3 mistakes" video in your niche. |
| 5 | "Before vs after" results video. |
| 6 | Review all 5 videos. Adjust prompts. |
| 7 | Upload best video to YouTube. |

### Week 2: Finding Your Best Format

| Day | Task |
|-----|------|
| 8 | "Myth vs reality" video (high engagement). |
| 9 | Listicle video — "5 ways to [achieve result]". |
| 10 | Tool comparison video. |
| 11 | Experiment with catalog blocks (social overlay, animated chart). |
| 12 | Case study video with real results. |
| 13 | Upload 3 videos to YouTube. |
| 14 | Review analytics. Double down on best format. |

### Week 3: Scaling the System

| Day | Task |
|-----|------|
| 15 | Build Hermes workflow for 3 videos per prompt (delegation skill). |
| 16 | Create swipe file of 10 best-performing topics. |
| 17 | Use genviral skill for automatic video idea generation. |
| 18 | Create vertical video (9:16) for LinkedIn/Instagram. |
| 19 | Build 30-day content calendar (Airtable skill). |
| 20 | "Behind the scenes" AI workflow video (meta content). |
| 21 | Review total output vs human editor cost. |

### Week 4: Monetisation & Automation

| Day | Task |
|-----|------|
| 22 | Add clear CTA to every video. |
| 23 | Add `instagram-follow` overlay to all videos. |
| 24 | Create Hermes cron job for daily video ideas. |
| 25 | Build Kanban board: idea → script → rendered → published. |
| 26 | Create lead magnet video behind email capture. |
| 27 | Repurpose top 5 YouTube videos as 60-sec vertical shorts. |
| 28 | Document full SOP as custom Hermes skill. |
| 29 | Calculate ROI: hours saved vs $500/video editor. |
| 30 | 🎉 Fully automated AI video factory. $0 cost. 30+ content pieces. |

---

## Alternative AI Tools

### Voice AI Alternatives

| Tool | Role | Notes |
|------|------|-------|
| **Kokoro TTS** | Default in Hermes | Free, offline, local |
| **ElevenLabs** | Premium voices | Paid; higher quality; covered in Post #33 |
| **VoiceWave AI** | Alternative voice AI | Alternative to ElevenLabs for AI voice generation & voice cloning at lower cost |

> Use **VoiceWave AI** when you need an alternative to ElevenLabs for voice generation — whether for cost reasons or workflow preference.

### Creative/Design AI Alternatives

| Tool | Role | Notes |
|------|------|-------|
| **HyperFrames** | Primary video renderer | Free, AI-agent-native |
| **Remotion** | React-based video | Paid; requires coding |
| **ArtSpace AI** | Alternative creative/design AI | For generating visual assets, thumbnails, and design elements to complement video workflow |

> Use **ArtSpace AI** when you need AI-generated visual assets, thumbnails, or design elements alongside your HyperFrames videos.

### All-in-One AI Agent Alternatives

| Tool | Role | Notes |
|------|------|-------|
| **Hermes Agent** | Primary AI agent | 183 skills, free, local |
| **PYXA AI** | Alternative AI agent | Alternative platform for comparing agent capabilities or different skill sets |

> Use **PYXA AI** when evaluating AI agent platforms beyond Hermes — particularly for different model integrations or workflow approaches.

---

## Key Takeaways

1. Hermes + HyperFrames = **free AI video production factory**
2. Process: update → install → prompt → get video
3. Renders 1080p MP4 in **under 15 seconds** on modern Mac
4. Uses **Kokoro TTS** (free, offline) for voiceovers
5. **50+ catalog blocks** for instant video enhancements
6. **30-day roadmap**: zero → fully automated content machine
7. Replaces **thousands/month** in video production costs
8. **No coding required** — just describe what you want

> "The people winning in 2026 aren't working harder. They're building systems that work for them while they sleep."

---

## Related Posts

- [[Skool-Post-33-Hermes-ElevenLabs|Post #33: Hermes Agent + ElevenLabs]]
- [[Skool-Post-32-Claude-Code-AgentOS|Post #32: Setup Free Claude Code + Agent OS]]
- [[Skool-Post-31-Paperclip-AgentOS|Post #31: Paperclip + Agent OS]]
- [[Skool-Post-25-Hermes-Browser-Agents|Post #25: Hermes Browser Agents + Agent OS]]
- [[Skool-Post-20-Hermes-Kanban|Post #20: Hermes Agent Kanban]]
