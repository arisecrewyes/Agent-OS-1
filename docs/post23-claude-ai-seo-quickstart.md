# Skool Post #23: Claude AI SEO + Agent OS

**Date:** 19th May  
**Series:** AI SEO Automation  
**Topic:** Claude AI SEO + Agent OS — rank #1 with a 5-layer content gravity system  

---

## TL;DR

The Goldie Search Gravity Stack™ is a 5-layer system for ranking on Google, YouTube, and AI search engines simultaneously. One keyword → articles deployed across 5 websites automatically. One video transcript → 5 unique blog posts. Zero manual writing. Built on Claude AI + Agent OS (GoStackBase). The system is designed to run on your laptop, publishing content you fully own.

---

## What You're About To Learn

This is a live, working system with real traffic results behind it:

- One website went from **0 → 71 clicks/day**
- Another went from **4 → 95 clicks/day**
- Another peaked at **346 clicks/day**
- Another peaked at **1,134 clicks/day**

All from Google and AI search engines using the exact system described here.

---

## The Goldie Search Gravity Stack™

### The Old Way (Broken)

> ❌ Write article → Hope Google likes it → Maybe rank → Maybe get traffic

### The New Way

A 5-layer system that creates **content gravity** — pulling people, clicks, and rankings toward you automatically.

> "Most people are still manual workers in the AI age. They're still typing into a chat window and switching between tools. This system makes you the owner of the factory." — Julian Goldie

### 🔵 Layer 1 — The Content Engine
- One keyword + one real case study → fully optimised articles
- Deploy across **five different websites** automatically
- Five chances to rank for the same keyword from one click

### 🟢 Layer 2 — The Visual Authority Layer
- Generate custom images using Grok Studio
- Embed directly into blog posts
- Dwell time is a ranking signal — images keep people on the page longer
- Unlocks Google Image Search as a separate traffic source

### � Layer 3 — The Video Gravity Layer
- Videos rank on Google, YouTube, AND AI search engines
- Three ranking surfaces from one piece of content
- Deploy videos and embed them in blog posts simultaneously

### � Layer 4 — The Agent Task Army
- Kanban board with Hermes Agent
- Assign big project → system breaks it into tasks
- Each agent handles a different piece simultaneously
- Weeks of work done in hours

### ⚪ Layer 5 — The Infinite Context Engine
- Obsidian-based knowledge graph about you and your business
- Agents read it daily, export new learnings back
- Content gets more personal every day
- Personal content converts better, ranks better, gets shared more

---

## 5 Ways To Rank With Claude AI SEO

### Way #1 — The SEO Content Agent
Open Agent OS → type keyword + case study → hit deploy → 5 articles across 5 sites.

### Way #2 — The Visual Ranking Layer (Grok Studio)
Connect Grok Studio to Agent OS → generate custom images → embed in posts → rank higher.

### Way #3 — The Video Ranking Engine
Create videos inside Agent OS → deploy to YouTube → embed in blog posts → triple ranking power (Google + YouTube + AI search).

### Way #4 — The Kanban Agent Army
Assign "Build me a complete blog on [topic]" → system breaks into 50+ tasks → agents work simultaneously → full blog built while you sleep.

### Way #5 — The Infinite Context Engine
Build your knowledge graph in Obsidian → agents learn your voice daily → content sounds like you wrote it personally.

---

## SEO Content Pipeline Setup (Step-by-Step)

The same SEO system AIPB uses to publish to 5 sites in one click. You will not write any code. You will talk to Claude.

**Time:** ~45 minutes | **Skill level:** Zero

### What You Need

1. � Agent OS already running on your laptop (`localhost:3737`)
2. 🟢 5 websites (works with Eleventy, Astro, Hugo, Jekyll — any static site generator)
3. � A free Netlify account (connect each site to a Netlify project)
4. � A way to record video (Riverside, Loom, Descript, or phone)
5. � A transcript of your video (most tools output one for free)

### Step 1: Download the SEO Pack

Open Agent OS → Click SEO in sidebar → Click "Download SEO Pack" → Unzip.

Contains:
- `blog-post.md` — skill that tells Claude how to write posts
- `seoPipeline.ts.template` — config file Agent OS reads
- `example-transcript.txt` — example transcript format
- `README.md` — file map

### Step 2: Set Up Your 5 Sites

```bash
cd ~
git clone https://github.com/juliangoldie/AIProfitBoardroom-public.git my-site-1
cd my-site-1
npm install
npm run dev
```

Repeat 4 more times. Each site in its own folder, mapped to a domain.

### Step 3: Configure Agent OS

Edit `seoPipeline.ts.template`:

```typescript
{ id: "site1", name: "your-domain.com", url: "https://your-domain.com",
  path: "$HOME/my-site-1", postsDir: "$HOME/my-site-1/src/blog/posts" }
```

Replace with your real values for all 5 sites.

### Step 4: Install the Skill

Pick ONE site as "home" → drop skill file there:

```bash
cd ~/my-site-1
mkdir -p .claude/skills .claude/transcripts
cp /path/to/seo-pack/blog-post.md .claude/skills/blog-post.md
```

Edit `blog-post.md`:
- Replace `## YOUR BRAND VOICE` with your actual tone
- Replace `## YOUR VIDEO LIBRARY` with YouTube IDs/titles

### Step 5: Add Your Transcript

```bash
cp ~/Downloads/my-transcript.txt ~/my-site-1/.claude/transcripts/hermes-second-brain.txt
```

Name format: short, lowercase, hyphens only, no spaces.

### Step 6: Connect Agent OS

Open Agent OS → Click SEO in sidebar → you should see your 5 sites. If not, restart Agent OS:

```bash
cd ~/Agentic\ OS/agentic-os
npm run dev
```

### Step 7: Generate Posts

Click **Generate** → type keyword (e.g. "best ai coding agent") → pick slug → pick transcript → click **Generate Posts**.

Each post gets:
- Unique CTR-optimised title
- Different opening hook
- Same core content from transcript
- Video embeds
- 4 CTAs back to your offer
- Schema markup
- Bio block

### Step 8: Deploy

Click **Deploy** → click rocket per site or **Deploy All** → builds push to Netlify → 2-3 minutes all 5 posts are live.

### Step 9: Watch the Funnel Work

Traffic → blog post → video → CTA → offer. One video = 5 posts = 5 SEO domains = 5 funnels.

---

## Limiting Beliefs — Broken

| ❌ Wrong Belief | ✅ Right Belief |
|---|---|
| "AI content doesn't rank" | AI content with a real system ranks better than manual content |
| "I'm not technical enough" | If you can open a browser, you can use this |
| "AI tools create more work" | The right system eliminates entire workflows |
| "This is expensive" | Hermes Agent is open source and free |
| "Tried AI tools, didn't work" | You used individual tools, not a connected system |
| "No time to learn" | Day 1 content, Day 7 results |
| "Niche too competitive" | Volume + quality + speed wins in any niche |
| "AI sounds the same" | Infinite Context Engine makes it sound like you |

---

## Standard Operating Procedure (SOP)

### Phase 1: Setup (One Time)
- [ ] Install Agent OS + connect integrations (NotebookLM MCP, Grok Studio)
- [ ] Set up Hermes Agent + Kanban board
- [ ] Set up Obsidian for Infinite Context Engine
- [ ] Build memory knowledge graph (business, goals, tone, audience)
- [ ] Set up 5 websites + connect to deploy system

### Phase 2: Daily Content Workflow
1. Open Agent OS → SEO section → pick one keyword
2. Find one real case study related to keyword
3. Hit deploy → system generates articles across your sites
4. Generate custom image in Grok Studio → add to post
5. Create short video → deploy to YouTube → embed in post
6. Review asset gallery → approve → publish

### Phase 3: Weekly Project Workflow
1. Define large content project (e.g. "Build 20-article blog on [topic]")
2. Input into Kanban board → system breaks into tasks
3. Agents work tasks in background
4. Review completed work at end of week → publish

### Phase 4: Memory System Maintenance
- **Daily:** Agents export learnings to Obsidian
- **Weekly:** Add new case studies, results, audience insights
- **Monthly:** Full memory audit — add products, remove outdated info

---

## 30-Day Roadmap

### Week 1 — Foundation (Days 1–7)
| Day | Task |
|-----|------|
| 1 | Set up Agent OS, connect integrations, dashboard running |
| 2 | Set up Obsidian, start knowledge graph (name, business, audience, tone) |
| 3 | First content deployment — one keyword, one case study, one site |
| 4 | First image in Grok Studio, embed in article, check indexing |
| 5 | First video from content, upload to YouTube, embed in post |
| 6 | Review first week, check Google Search Console for signals |
| 7 | Rest, plan Week 2 keywords, add learnings to memory |

### Week 2 — Acceleration (Days 8–14)
| Day | Task |
|-----|------|
| 8 | Scale to 3 keywords/day, deploy across 2 sites |
| 9 | First Kanban project — assign 10-article blog |
| 10 | Batch-create images for all 10 articles |
| 11 | Create videos for top 3 topics, upload to YouTube |
| 12 | Review Kanban output, edit and publish 10-article blog |
| 13 | Deep memory update — add results, case studies, learnings |
| 14 | Check rankings in Search Console, double down on what's climbing |

### Week 3 — Scale (Days 15–21)
| Day | Task |
|-----|------|
| 15 | Scale to 5 keywords/day across all 5 sites |
| 16 | Second Kanban project — 25 articles on one topic cluster |
| 17 | Build internal linking structure across all articles |
| 18 | Create video series from top 3 performing articles |
| 19 | Review all published content, identify top performers |
| 20 | Full system audit — memory, SEO agent, Kanban |
| 21 | Share first results in community, get feedback |

### Week 4 — Optimisation (Days 22–30)
| Day | Task |
|-----|------|
| 22 | Update top 10 articles with fresh info (Google rewards updates) |
| 23 | Add more case studies + real data to top articles |
| 24 | Create infographics from best content using NotebookLM |
| 25 | Build out YouTube channel — videos on top 5 ranking articles |
| 26 | Content gap analysis — identify missing keywords, assign to Kanban |
| 27 | Full memory system update — test quality difference |
| 28 | Calculate results — new keywords, new traffic, document everything |
| 29 | Plan Month 2 based on Month 1 data |
| 30 | Celebrate progress — fully operational content machine |

---

## Pro Tips

- 🔥 **One video = 5 posts = 5 sites.** Don't film 5 videos. Film one. Let the pipeline do the rest.
- 🎯 **Pick low-competition keywords first.** Use Ahrefs free keyword generator. Aim for KD < 20.
- 📺 **Embed the same video on all 5 posts.** Google rewards dwell time. Video dwell time is the cheat code.
- � **Different titles, same body.** Each site gets a unique title. CTR varies by formula, not content.
- 💰 **Always link back to your offer.** Every post, 4 times minimum (top, middle, end, sidebar).
- 🧠 **Save transcripts in Obsidian.** One folder, searchable, forever.
- 🚀 **Deploy daily.** One transcript/day = 5 posts/day = 35 posts/week.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Can't see sites in SEO tab | Restart Agent OS. Verify `seoPipeline.ts` paths exist locally. |
| Deploy fails | Run `netlify status` → if logged out, run `netlify login` |
| Same content on all 5 sites | Check "5 different titles" section in `blog-post.md`. Verify each site has unique name in config. |
| Transcript not showing | Filename must be lowercase, hyphens only, no spaces. |

---

## Recap

The Goldie Search Gravity Stack™ is a 5-layer system:

| Layer | What It Does |
|-------|-------------|
| 🔵 Content Engine | Deploy articles across 5 websites from one keyword |
| 🟢 Visual Authority | Grok Studio images embedded in every post |
| 🟡 Video Gravity | Videos ranking across Google, YouTube, and AI search |
| 🔴 Agent Task Army | Full blogs built by agents via the Kanban board |
| ⚪ Infinite Context | Memory system that makes all content personal |

> "It's not a tool. It's a system. And a system is what changes everything." — Julian Goldie
