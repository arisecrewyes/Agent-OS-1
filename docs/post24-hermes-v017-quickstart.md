# Hermes Agent V0.17 "Reach" — Quickstart Guide

> **Source:** Skool Post #24 — AI Profit Boardroom
> **Published:** 20th June
> **Version:** Hermes v0.17 "Reach"

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

Once done, it will show `0.17` instead of `0.16`.

---

## Feature Summary

| # | Feature | What It Does |
|---|---------|--------------|
| 1 | iMessage Reach | Send/receive iMessages through Hermes |
| 2 | Raft Network Gateway | Join Raft network as a gateway channel |
| 3 | Desktop App Upgrade | Native notifications + live sub-agent watch windows |
| 4 | Async Sub-Agents | Fan out tasks to multiple agents simultaneously |
| 5 | Image Editing Skill | Image-to-image editing across multiple providers |
| 6 | Automation Blueprints | Schedule tasks without code |
| 7 | New Models via X | Cursor Composer / Grok Composer 2.5 Fast via X subscription |
| 8 | Full Profile Builder | Manage multiple agent profiles with custom skills/instructions |
| 9 | Skill Browser Overhaul | Search, toggle, sort skills by category |
| 10 | Memory & Small Updates | Better memory, WhatsApp support, Telegram rich text |
| 11 | Loop Engineering | Builder + judge agents loop until quality threshold is met |

---

## 1. iMessage Reach

Hermes can now send and receive iMessages, letting you run your agent from your phone.

**Setup:**
1. Run the login and authenticate
2. Hermes works inside iMessage — smooth, not clunky

---

## 2. Raft Network Gateway

Hermes can join the Raft network as a gateway channel via a bundled Raft adapter (wake channel bridge).

**Use case:** Humans and AI agents build together on the Raft platform with Hermes plugged in.

---

## 3. Desktop App Upgrade

Open Hermes desktop → click **"Update now"**.

**New features:**
- Native OS notifications
- Live sub-agent watch windows (see agents working in real time)

---

## 4. Async Sub-Agents

Delegate work and keep going. Hermes fans out tasks to multiple sub-agents at once.

**How it works:**
1. One lead agent (your main Hermes profile) receives a task
2. It spawns 4–5 sub-agents, each handling a different part
3. Results are pulled back into your chat

**Example — Building a webpage:**
> "Go research this topic for this keyword, optimize the page, post it to my website, and create a video at the same time."

| Sub-Agent | Task |
|-----------|------|
| Agent 1 | Keyword research |
| Agent 2 | Build the page |
| Agent 3 | Create the video |

**Role-based setup:** Editor, Judge, Video Writer, Script Writer — all working simultaneously.

---

## 5. Image Editing Skill

Edit existing images (not just generate new ones). Image-to-image skill transforms source images.

**Supported providers:** Fal, OpenAI, Grok, Codex, and more.

---

## 6. Automation Blueprints

Schedule tasks without writing code. Grab a blueprint from the official portal, plug it into Hermes, and follow the step-by-step setup.

**Example — AI News Digest Blueprint** (runs every 7 days):

| Part | Description |
|------|-------------|
| Task | What to do |
| Steps | How to do it |
| Output structure | Format of results |
| Wording rules | Keep under 600 words, 1–2 sentences per item |

---

## 7. New Models via X (Twitter)

Cursor's Composer model is available through your X subscription. Use **Grok Composer 2.5 Fast** inside Hermes.

**Setup:**
```bash
hermes model
```
1. Scroll to **XAI Grok**
2. Log in
3. Go back to terminal and select **Grok Composer 2.5 Fast**

---

## 8. Full Profile Builder

Manage multiple agent profiles inside the dashboard. Assign different profiles to different tasks or APIs.

**Each profile can have:**
- Its own skills
- Custom instructions
- Tasks assigned from your kanban board

**Setup:** Go to **Manage → Profiles**. Switch between profiles in chat with one click.

**Supported models:** GLM 5.2, Jarvis, Kimi K2.7, and more.

**Real-world example — Content team with self-check:**

| Profile | Role |
|---------|------|
| Video Director | Comes up with ideas |
| Build Team | Creates blog post and video |
| Content Judge | Scores the work |

**Quality loop:** If score is too low (e.g., 4/10), the team loops back and retries until it passes.

---

## 9. Skill Browser Overhaul

Open with:
```bash
hermes dashboard
```

Scroll to the **Skills** section. Now you can:
- Search skills by keyword
- See everything installed
- Toggle skills on/off
- Sort by category

---

## 10. Memory & Small Updates

- **Memory upgrade:** Agents remember and use context better
- Better dashboard login
- Official WhatsApp support
- Rich text for Telegram
- Token optimization options
- New UI options

---

## 11. Loop Engineering (Quality Control on Autopilot)

One agent builds, one agent judges — loops until work is good enough.

**How it works:**
1. Give your agent a goal (works on free/cheap API)
2. Give it a starting point
3. The **builder** acts
4. The **judge** grades it
5. If it fails → loop back and try again
6. When it passes your bar → you get the final output

**Real loop example:**

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
