# Skool Post #34: Hermes + Hyperframes

> **Source:** [6th May: Hermes + Hyperframes](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=5a347e7ae7ba484f840d31d534235c11)
> **Date:** 6 May 2025
> **Category:** AI Video / Hermes Agent / HyperFrames / Free Tools

---

## What This Post Covers

How to combine **Hermes Agent** (free AI agent) with **HyperFrames** (free open-source video renderer) to create a fully automated AI video production system — generating professional MP4 videos from a plain English prompt, at zero cost.

---

## The Big Idea

> "The future of content creation isn't hiring a video editor. It's teaching an AI to be one."

You type: *"Make me a video about AI SEO."*

And it just... makes it. No camera. No editing software. No video editor to hire. No skills needed.

**It's 100% free. It runs on your Mac or PC.**

---

## What Are the Two Tools?

### 🐍 Hermes Agent

Hermes Agent is a super-smart AI robot that lives in your computer's command line.

- You are the boss. Hermes is your employee.
- You give it a job in plain English.
- It does the job automatically — writing code, browsing the web, making files, even creating videos.
- Currently runs on **Kimi K2.6** by Nous Research (one of the most powerful free AI models).
- Has **183 skills** built in and **30 tool categories**.
- Can do everything from sending emails to building entire websites.

### 🎬 HyperFrames

HyperFrames is a free, open-source video creation tool built by **HeyGen**.

- **14,700+ stars** on GitHub.
- You write HTML → HyperFrames turns it into a real MP4 video.
- The AI writes the HTML FOR you. You just describe what you want.
- Like telling someone: *"Make me a video about keyword research"* — and getting back a polished, animated, professional video in under 2 minutes.

### 🔗 Why They Work Together

Hermes Agent can install HyperFrames as a **skill**. That means Hermes learns how to use HyperFrames automatically.

So when you say *"create a video about AI SEO"* — Hermes:

1. ✍️ Writes the script
2. 🎙️ Generates the voiceover (using AI text-to-speech)
3. 🎨 Builds the animated slides
4. 🎬 Renders the final MP4 video

**All while you sit back and watch.**

---

## How It Actually Works (Real Session Breakdown)

Here's exactly what happens when Hermes makes an AI SEO video from scratch:

| Step | What Happens | Time |
|------|-------------|------|
| 1 | User runs `hermes update` (always update first!) | ~30s |
| 2 | Hermes downloads 473 new commits/improvements | ~30s |
| 3 | User runs `hermes skills install hyperframes` | ~1min |
| 4 | Hermes runs security scan, installs skill | ~30s |
| 5 | User types video prompt inside Hermes | instant |
| 6 | Hermes writes the script automatically | ~10s |
| 7 | Hermes generates AI voiceover (Kokoro TTS) | ~20s |
| 8 | Hermes builds 7 animated HTML scenes | ~1min |
| 9 | Hermes renders final 1920x1080 MP4 | ~15s |

**Total time: ~5–15 minutes depending on your machine.**

### The 7 Scenes Hermes Built Automatically

1. Big bold title (AI SEO)
2. Keyword research cards
3. Content creation
4. Backlink building
5. Tracking & analytics
6. Results screen
7. End screen with CTA

Each scene had animated text, glowing colour accents (neon green, magenta, cyan), and smooth GSAP transitions.

---

## What Makes HyperFrames Special

### HyperFrames vs Other Video Tools

| Feature | HyperFrames | Traditional Editors | Remotion |
|---------|-------------|-------------------|----------|
| **Cost** | FREE | $$$$ | Paid license |
| **AI Agent support** | ✅ Built-in | ❌ | ❌ |
| **Build step needed** | ❌ None | N/A | ✅ Required |
| **Renders locally** | ✅ | ❌ | ✅ |
| **HTML-based** | ✅ | ❌ | ❌ |

> **The Big Idea:** "Agents already speak HTML. HyperFrames just gives them a video renderer."

This is why it's so powerful for AI workflows. Most AI tools can write HTML easily. HyperFrames converts that HTML directly into video. **AI + HyperFrames = instant video factory.**

### The 50+ Catalog Blocks

HyperFrames includes pre-built video blocks you can add instantly:

```bash
npx hyperframes add flash-through-white   # cinematic transition
npx hyperframes add instagram-follow      # social overlay
npx hyperframes add data-chart            # animated chart
```

These are like LEGO pieces for your videos. Mix and match them. Build anything.

---

## Full SOP — Set This Up Yourself

> **Standard Operating Procedure. Follow in order. Don't skip steps.**

### ✅ Pre-Requirements

Before you start, make sure you have:

- [ ] A Mac or PC (Mac Studio works great)
- [ ] Node.js version 22 or higher installed
- [ ] FFmpeg installed (`brew install ffmpeg` on Mac)
- [ ] Hermes Agent already installed on your machine
- [ ] At least 2GB of free disk space

### Step 1: Update Hermes Agent First

```bash
hermes update
```

- Wait for the update to complete
- Say **Y** when asked to restore local changes
- Confirm all skills are updated in the summary

> ⚠️ **Why?** HyperFrames requires the latest version to install correctly. Skipping this step WILL cause errors.

### Step 2: Install the HyperFrames Skill

```bash
hermes skills install hyperframes
```

- Read the security scan results
- The sudo warnings are normal — they're just for FFmpeg installation
- Type **y** to confirm installation
- Wait for confirmation: `Installed: creative/hyperframes`

### Step 3: Launch Hermes

```bash
hermes
```

You'll see the big ASCII logo and the welcome screen. Confirm **hyperframes** appears under creative skills.

### Step 4: Give Your Video Prompt

Type directly in the Hermes interface:

```
create a beautiful video about [YOUR TOPIC] using the hyperframes skill
```

Replace `[YOUR TOPIC]` with anything:
- "how to do keyword research"
- "what is AI automation"
- "why backlinks matter for SEO"
- "3 ways to make money with AI"

### Step 5: Let Hermes Work (Don't Touch Anything)

Hermes will automatically:

- [ ] Read the HyperFrames skill documentation
- [ ] Create a 7-step task plan
- [ ] Run the HyperFrames setup script
- [ ] Write your video script
- [ ] Generate the AI voiceover (narration.wav)
- [ ] Build the HTML composition with animations
- [ ] Fix any errors automatically
- [ ] Render a draft MP4 for quality check
- [ ] Render the final high-quality MP4

### Step 6: Find Your Video

Your finished video will be at:

```
~/ai-seo-video/final.mp4
```

Or whatever folder name Hermes creates for your topic. Open it. Watch it. Upload it.

### Step 7: If Something Goes Wrong

- If Hermes times out on a command, type: `allow` (tells Hermes to continue)
- If the video renders with black/empty scenes, Hermes will fix them automatically on the next render pass
- If you see `---NEEDS SETUP---` during dependency checks, just let Hermes run the setup script — it handles everything

---

## Key Commands Quick Reference

```bash
# Setup
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

## 30-Day Business Implementation Roadmap

> "One video a day keeps the competition away."

### 📅 Week 1 (Days 1–7): Setup & First Videos

| Day | Action |
|-----|--------|
| 1 | Install and update Hermes Agent. Install the HyperFrames skill. Create your first test video on any topic. |
| 2 | Create a video explaining what your business does. This becomes your homepage explainer. |
| 3 | Create a "how it works" video for your main service. Use it on your sales page. |
| 4 | Create a "top 3 mistakes" video in your niche. These perform very well on YouTube. |
| 5 | Create a "before vs after" results video. Show transformation — numbers, outcomes. |
| 6 | Review all 5 videos. Note what looked great and what needs tweaking. Adjust your prompts. |
| 7 | Upload your best video to YouTube. Write the description with AI. Add tags. Hit publish. |

### 📅 Week 2 (Days 8–14): Finding Your Best Format

| Day | Action |
|-----|--------|
| 8 | Create a "myth vs reality" video in your niche. High engagement format. |
| 9 | Create a listicle video — "5 ways to [achieve result]." Easy to script, easy to watch. |
| 10 | Create a tool comparison video. "Tool A vs Tool B — which is better?" |
| 11 | Experiment with the HyperFrames catalog blocks. Add a social overlay or animated chart. |
| 12 | Create a case study video. Show a real result you've achieved. |
| 13 | Upload 3 videos to YouTube from this week. Start building your channel backlog. |
| 14 | Review YouTube analytics. Which video got the most views? Double down on that format. |

### 📅 Week 3 (Days 15–21): Scaling the System

| Day | Action |
|-----|--------|
| 15 | Build a Hermes workflow that creates 3 videos per prompt. Use the delegation skill. |
| 16 | Create a swipe file of your 10 best-performing video topics. Repurpose them into new angles. |
| 17 | Use the genviral skill inside Hermes to generate video ideas automatically. |
| 18 | Create a video specifically for LinkedIn or Instagram. Adjust dimensions to 9:16 for vertical format. |
| 19 | Build a content calendar using Airtable skill inside Hermes. Plan 30 days of video topics in advance. |
| 20 | Create a "behind the scenes" video showing how you use AI. Meta content performs incredibly well. |
| 21 | Review: how many videos have you published? How many views total? Calculate output vs a human editor. |

### 📅 Week 4 (Days 22–30): Monetisation & Automation

| Day | Action |
|-----|--------|
| 22 | Add a clear CTA to every video. Drive viewers to book a call, join a community, or buy a product. |
| 23 | Use the HyperFrames catalog `instagram-follow` overlay on all videos. Build cross-platform following. |
| 24 | Create a Hermes cron job to generate video ideas every morning automatically. |
| 25 | Build a Kanban board in Hermes tracking every video from idea → script → rendered → published. |
| 26 | Create a lead magnet video — a mini training that gives real value. Put it behind an email capture. |
| 27 | Repurpose your top 5 YouTube videos as short-form clips. Use HyperFrames to render 60-second vertical versions. |
| 28 | Document your full video creation SOP inside Hermes as a custom skill. Train your team to use it. |
| 29 | Calculate ROI: hours saved vs traditional video production. If a video editor charges $500/video and you made 30 videos... |
| 30 | 🎉 You now have a fully automated AI video production system. $0 spent on video creation. 30+ pieces of content working 24/7. |

---

## Alternative AI Tools

While Hermes Agent + HyperFrames is a powerful free combo for AI video production, several alternative tools exist for different parts of the workflow:

### Alternative Voice AI Tools

| Tool | Best For | Notes |
|------|----------|-------|
| **Kokoro TTS** (built into Hermes) | Free, offline text-to-speech | Default voice in Hermes + HyperFrames; runs locally, zero API cost |
| **ElevenLabs** | Premium voice cloning & emotive narration | Paid; higher quality voices; used in Post #33 (Hermes + ElevenLabs) |
| **VoiceWave AI** | AI voice generation & voice cloning alternative | Alternative to ElevenLabs; good for creators needing custom voice profiles at lower cost |

> **When to use VoiceWave AI:** If you need an alternative to ElevenLabs for voice generation — whether for cost reasons or workflow preference — VoiceWave AI provides another option in the AI voice space. Compare output quality against Kokoro (free) and ElevenLabs (premium) for your use case.

### Alternative Creative/Design AI Tools

| Tool | Best For | Notes |
|------|----------|-------|
| **HyperFrames** (primary tool) | HTML → MP4 video rendering | Free, open-source, AI-agent-native |
| **Remotion** | Programmatic video with React | Paid; requires React knowledge; no native AI agent support |
| **ArtSpace AI** | AI-powered creative & design generation | Alternative for generating visual assets, thumbnails, and design elements to complement your video workflow |

> **When to use ArtSpace AI:** If you need AI-generated visual assets, thumbnails, or design elements alongside your HyperFrames videos, ArtSpace AI serves as an alternative creative/design tool in your stack.

### Alternative All-in-One AI Tools

| Tool | Best For | Notes |
|------|----------|-------|
| **Hermes Agent** (primary tool) | Multi-skill AI agent with 183 skills | Free, runs locally, plain-English commands |
| **PYXA AI** | Alternative AI agent platform | Alternative to Hermes Agent; explore if you want to compare agent capabilities or need different skill sets |

> **When to use PYXA AI:** If you're evaluating AI agent platforms beyond Hermes, PYXA AI is an alternative worth comparing — particularly for different model integrations or workflow approaches.

---

## Recap — Everything You Learned

- ✅ Hermes Agent is a free AI robot that runs on your computer and does tasks in plain English.
- ✅ HyperFrames is a free, open-source tool from HeyGen that turns HTML into MP4 videos.
- ✅ Installing HyperFrames as a Hermes skill gives you a fully automated video production system — for free.
- ✅ The process is: update Hermes → install skill → type your topic → get your video.
- ✅ HyperFrames uses GSAP animations, Kokoro AI voiceovers, and Puppeteer rendering under the hood.
- ✅ The whole setup renders 1080p video in under 15 seconds on a modern Mac.
- ✅ HyperFrames has 50+ catalog blocks you can add to any video instantly.
- ✅ The 30-day roadmap gets you from zero to a fully automated content machine.
- ✅ This replaces thousands of dollars per month in video production costs.
- ✅ You don't need to know how to code. Just describe what you want. Hermes handles the rest.

> "The people winning in 2026 aren't working harder. They're building systems that work for them while they sleep."

---

## Key Links

| Resource | URL |
|----------|-----|
| HyperFrames (GitHub) | [github.com/hyperframes](https://github.com) (search: HeyGen HyperFrames) |
| Hermes Agent | Installed locally via CLI |
| HyperFrames Catalog Blocks | `npx hyperframes add [block-name]` |
| Kokoro TTS | Built into Hermes (free, offline) |

---

## Related Posts

- [[Skool-Post-32-Claude-Code-AgentOS|Post #32: Setup Free Claude Code + Agent OS]]
- [[Skool-Post-31-Paperclip-AgentOS|Post #31: Paperclip + Agent OS]]
- [[Skool-Post-25-Hermes-Browser-Agents|Post #25: Hermes Browser Agents + Agent OS]]
- [[Skool-Post-20-Hermes-Kanban|Post #20: Hermes Agent Kanban]]
