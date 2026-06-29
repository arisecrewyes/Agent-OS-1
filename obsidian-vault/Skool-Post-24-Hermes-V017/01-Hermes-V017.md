---
title: Hermes Agent V0.17 "Reach"
source: Skool Post #24 — AI Profit Boardroom
date: 2026-06-20
version: 0.17
tags:
  - hermes-agent
  - ai-agent
  - release-notes
  - skool
  - async-sub-agents
  - loop-engineering
  - automation
---

# Hermes Agent V0.17 "Reach" — The Complete Guide

> Hermes just dropped version 0.17, called the "Reach" release. Here is everything that changed, what it means for you, and how to use it.

---

## How to Update

### Option 1: Dashboard
1. Go to your Hermes dashboard
2. Click **Manage**
3. Scroll down and click **"Update Hermes"**
4. It starts updating immediately

### Option 2: Terminal
```bash
hermes update
```

Once done, it will show `0.17` instead of `0.16`. You are good to go.

---

## The Big Features

### 1. iMessage Reach

Hermes can now send and receive iMessages. This means you can run your Hermes agent right from your phone.

Run the login and authenticate. After that, Hermes works inside iMessage. If you have tried putting AI inside iMessage before, you know it was clunky. Now it is smooth.

### 2. Raft Network Gateway

Hermes can now join the Raft network as a gateway channel. A bundled Raft adapter lets Hermes connect as an external agent through a wake channel bridge.

**In plain terms:** Humans and AI agents can now build together on that platform with Hermes plugged in.

### 3. Better Desktop App

The desktop app got a solid upgrade this week. Open Hermes desktop, click "Update now," and you get the latest version.

**What is new:**
- Native OS notifications
- Live sub-agent watch windows so you can see your agents working in real time

### 4. Async Sub-Agents (one of the best updates)

You can now delegate work and keep going. Hermes fans out tasks to multiple sub-agents at once.

**How it works:**
1. One lead agent (your main Hermes profile) receives a task
2. It spawns 4–5 sub-agents, each handling a different part
3. Results are pulled back into your chat

**Example use case — building a webpage:**

> "Go research this topic for this keyword, optimize the page, post it to my website, and create a video at the same time."

| Sub-Agent | Task |
|-----------|------|
| Agent 1 | Keyword research |
| Agent 2 | Build the page |
| Agent 3 | Create the video |

They all run together. You get the finished work back in one place.

**Role-based setup:** You can set roles like an editor, a judge, a video writer, and a script writer all working at once.

### 5. Image Editing Skill

You can now edit images, not just generate them. The new image-to-image skill lets you transform a source image instead of only creating one from scratch.

**Supported providers:** Fal, OpenAI, Grok, Codex, and more. One tool that handles text-to-image and image-to-image both.

### 6. Automation Blueprints

Blueprints let you schedule tasks without writing or understanding the code behind them.

Grab a blueprint from the official portal. Plug it into Hermes. Hermes walks you through setup step by step. You do not need to be technical.

**Example — an AI News Digest blueprint** (runs every 7 days in four simple parts):

| Part | Description |
|------|-------------|
| Task | What to do |
| Steps | How to do it |
| Output structure | Format of results |
| Wording rules | Example: keep it under 600 words, one to two sentences per item |

Copy, paste, done. Better outputs without being a better coder.

### 7. New Models via X (Twitter)

Cursor's Composer model is now available through your X subscription. If you already pay for Twitter, you can use Grok Composer 2.5 Fast inside Hermes.

**Setup:**
```bash
hermes model
```

1. Scroll to **XAI Grok**
2. Log in
3. Go back to the terminal and select **Grok Composer 2.5 Fast** from the list

Switching models is that easy.

### 8. Full Profile Builder

You can now manage multiple agent profiles inside the dashboard. Assign different profiles to different tasks or even different APIs.

**Each profile can have:**
- Its own skills
- Custom instructions
- Tasks assigned from your kanban board

**To build one:** Go to **Manage → Profiles**. Switch between profiles in chat with one click. You can run GLM 5.2, Jarvis, Kimi K2.7, and more, and flip between them instantly.

**Real example — a content team that checks its own work:**

| Profile | Role |
|---------|------|
| Video Director | Comes up with ideas |
| Build Team | Builds the blog post and video |
| Content Judge | Scores the work |

If it scores too low (say 4 out of 10), the team loops back and tries again until it passes. That is quality control baked into your workflow.

### 9. Skill Browser Overhaul

The skill browser got a full redesign. Open it with:

```bash
hermes dashboard
```

Scroll to the Skills section. Now you can:
- Search skills by keyword
- See everything you have installed
- Toggle skills on and off
- Sort by category

Much easier to manage.

### 10. Memory and Small Updates

Memory got a major upgrade, so your agents remember and use context better.

**Smaller additions worth knowing:**
- Better dashboard login
- Official WhatsApp support
- Rich text for Telegram
- Token optimization options
- New UI options

### 11. Loop Engineering (Quality Control on Autopilot)

This is the standout. Loop engineering means one agent builds and one agent judges, on a loop, until the work is good enough.

**How it works:**
1. Give your agent a goal (you can run this on a free or cheap API)
2. Give it a starting point
3. The **builder** acts
4. The **judge** grades it
5. If it fails, it loops back and tries again
6. When it passes your bar, you get the final output

You set the standard. The agents do the back-and-forth. You never sit in the middle as the quality checker.

**Real loop example:** The judge scored each round harder.

| Round | Score |
|-------|-------|
| 1 | 54 |
| 2 | 71 |
| 3 | 83 |
| 4 | 92 ✓ |

Once it passed 92, the work was done. No manual feedback needed.

---

## The Bottom Line

Hermes v0.17 turns your setup from a single agent into an **orchestrated team**:

- **Async sub-agents** fan out the work
- **Profiles** give each agent a job
- **Loop engineering** checks the quality

You go from idea to finished build without sitting in the middle of every step.

If you saw everything covered here, you are already ahead of 99% of people using AI agents.

---

## Related Posts

- [[Skool-Post-23-Hermes-Email-Agent|Hermes Email Agent]] (23rd June)
- [[Loop Engineering]] (19th June)
- [[Hermes Shopping Assistant]] (17th June)
- [[How To Use Async Sub Agents In Hermes]] (16th June)
