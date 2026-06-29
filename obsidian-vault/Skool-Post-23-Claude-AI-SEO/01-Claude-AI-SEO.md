---
tags:
  - skool
  - ai-seo
  - claude-ai
  - agent-os
  - gostackbase
  - content-automation
  - goldie-search-gravity-stack
  - seo-pipeline
  - kanban-agents
  - obsidian
  - post-23
date: 2025-05-19
source: https://www.skool.com/ai-profit-lab-7462/classroom/42d25f4b?md=b812c05b958d46ff837950126f65fa79
---

# Claude AI SEO + Agent OS (Post #23)

> Converted from Julian Goldie Skool Post #23 — "19th May: Claude AI SEO + Agent OS"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/42d25f4b?md=b812c05b958d46ff837950126f65fa79

## The Core Idea

> "Most people are still manual workers in the AI age. They're still typing into a chat window and switching between tools. This system makes you the owner of the factory." — Julian Goldie

Build a **complete SEO content pipeline** using Claude AI + Agent OS (GoStackBase). One keyword → 5 unique blog posts across 5 websites → all deployed automatically. One video transcript → 5 articles. Zero manual writing.

## Why It Matters

- � **5 chances to rank** for every keyword (one article per site)
- 📹 **One video = 5 posts** — film once, publish everywhere
- 🚀 **Deploy to 5 sites in one click** via Netlify
- 🧠 **Infinite Context Engine** — content gets more personal every day
- 💰 **Free to run** — Hermes Agent is open source, Netlify has free tier
- 🏠 **Everything stays on your laptop** — you own the content, sites, and traffic

---

## The Goldie Search Gravity Stack™

A 5-layer system that creates **content gravity** — pulling rankings, clicks, and traffic toward you automatically.

### Layer Architecture

| Layer | Name | Function |
|-------|------|----------|
| 🔵 1 | Content Engine | One keyword → articles across 5 sites |
| � 2 | Visual Authority | Grok Studio images embedded in posts |
| 🟡 3 | Video Gravity | Videos rank on Google + YouTube + AI search |
| 🔴 4 | Agent Task Army | Kanban board agents build full blogs |
| ⚪ 5 | Infinite Context | Obsidian knowledge graph personalises all content |

### Layer 1 — The Content Engine

You give the system one keyword + one real case study. Hit deploy. It writes fully optimised articles and publishes across five different websites automatically.

**Real results:**
- Site 1: 0 → 71 clicks/day
- Site 2: 4 → 95 clicks/day
- Site 3: peaked at 346 clicks/day
- Site 4: peaked at 1,134 clicks/day

> "Content without a system is just noise. Content with a system is an asset that compounds every single day."

### Layer 2 — The Visual Authority Layer

Most SEO guides ignore images. Google Images drives millions of clicks daily. Inside the system, generate custom images using Grok Studio, embed directly into blog posts.

**Why it works:**
- Dwell time is a ranking signal
- Images keep people on the page longer
- Google Image Search = separate traffic source

### Layer 3 — The Video Gravity Layer

Videos rank on Google, YouTube, AND AI search engines. Three ranking surfaces from one piece of content.

**Triple ranking power:**
- Google owns YouTube → video priority in search
- Video + article for same keyword = two first-page spots
- AI search engines favour multi-format content

### Layer 4 — The Agent Task Army

Kanban board connected to Hermes Agent. Assign one massive project → system breaks it into tasks → each agent handles a piece simultaneously.

**Example:** "Build me a complete blog on [topic]" → 50 articles + outlines + images + meta descriptions → all built while you sleep.

> "A hammer alone doesn't build a house. But a hammer, nails, wood, and a blueprint together — that builds something real." — Julian Goldie

### Layer 5 — The Infinite Context Engine

Obsidian-based knowledge graph. Agents read it daily, export new learnings back. Every day your AI understands you better.

**What lives in the memory system:**
- ✅ Business goals and target audience
- ✅ Tone of voice and writing style
- ✅ Tools and how you use them
- ✅ Previous high-performing content
- ✅ Products, services, website structure
- ✅ Team members and roles
- ✅ Case studies, testimonials, real results

> "My AI is taking notes every single day, exporting to Obsidian, and making better and better outputs." — Julian Goldie

---

## 5 Ways To Rank With Claude AI SEO

### Way #1 — The SEO Content Agent
Open Agent OS → type keyword + case study → deploy → 5 articles across 5 sites. Content designed for Google AI Overview results.

### Way #2 — The Visual Ranking Layer
Connect Grok Studio → generate custom images → embed in posts → rank higher via dwell time + image search.

### Way #3 — The Video Ranking Engine
Create videos in Agent OS → deploy to YouTube → embed in blog posts → triple ranking power.

### Way #4 — The Kanban Agent Army
Assign big project → system breaks into tasks → agents work simultaneously → full blog built automatically.

### Way #5 — The Infinite Context Engine
Build knowledge graph → agents learn daily → content sounds like you personally wrote it.

---

## SEO Content Pipeline Setup

**Time:** ~45 minutes | **Skill level:** Zero | **Cost:** Free

### Prerequisites

1. 🟢 Agent OS running on laptop (`localhost:3737`)
2. � 5 websites (Eleventy, Astro, Hugo, Jekyll — any static site generator)
3. � Free Netlify account (connect each site)
4. 🟢 Video recording tool (Riverside, Loom, Descript, phone)
5. � Video transcript (plain text file)

### Step-by-Step Setup

#### Step 1: Download the SEO Pack
Open Agent OS → Click SEO → Download SEO Pack → Unzip. Contains:
- `blog-post.md` — Claude skill for writing posts
- `seoPipeline.ts.template` — Agent OS config
- `example-transcript.txt` — transcript format example
- `README.md` — file map

#### Step 2: Clone 5 Sites
```bash
cd ~
git clone https://github.com/juliangoldie/AIProfitBoardroom-public.git my-site-1
cd my-site-1 && npm install && npm run dev
```
Repeat 4 more times. Map each folder to a domain.

#### Step 3: Configure seoPipeline.ts
```typescript
{ id: "site1", name: "your-domain.com", url: "https://your-domain.com",
  path: "$HOME/my-site-1", postsDir: "$HOME/my-site-1/src/blog/posts" }
```
Replace all 5 blocks with your real values.

#### Step 4: Install the Skill
```bash
cd ~/my-site-1
mkdir -p .claude/skills .claude/transcripts
cp /path/to/seo-pack/blog-post.md .claude/skills/blog-post.md
```
Edit `blog-post.md`:
- Replace `## YOUR BRAND VOICE` with your tone
- Replace `## YOUR VIDEO LIBRARY` with YouTube IDs

#### Step 5: Add Transcript
```bash
cp ~/Downloads/my-transcript.txt ~/my-site-1/.claude/transcripts/your-slug.txt
```
Format: lowercase, hyphens, no spaces.

#### Step 6: Connect Agent OS
Open Agent OS → SEO sidebar → see your 5 sites. If not:
```bash
cd ~/Agentic\ OS/agentic-os && npm run dev
```

#### Step 7: Generate Posts
Click **Generate** → keyword → slug → transcript → **Generate Posts**. Each post gets:
- Unique title
- Different opening hook
-
- Video embeds
- 4 CTAs to your offer
- Schema markup
- Bio block

#### Step 8: Deploy
Click **Deploy** → **Deploy All** → builds push to Netlify → 2-3 minutes all 5 posts live.

#### Step 9: Watch the Funnel
Traffic → blog post → video → CTA → offer. One video = 5 posts = 5 SEO domains = 5 funnels.

---

## Limiting Beliefs — Debunked

| ❌ Myth | ✅ Reality |
|---------|-----------|
| "AI content doesn't rank" | AI + real system ranks better than manual (proven: 0→1,134 clicks/day) |
| "I'm not technical enough" | If you can open a browser, you can use this |
| "AI tools create more work" | System eliminates entire workflows |
| "This is expensive" | Hermes Agent is open source, free APIs available |
| "Tried AI, didn't work" | You used individual tools, not a connected system |
| "No time to learn" | Day 1 content, Day 7 results |
| "Niche too competitive" | Volume + quality + speed wins in any niche |
| "AI sounds the same" | Infinite Context Engine makes it sound like you |

---

## SOP — Standard Operating Procedure

### Phase 1: Setup (One Time)
- [ ] Install Agent OS + connect integrations
- [ ] Set up Hermes Agent + Kanban board
- [ ] Set up Obsidian for Infinite Context Engine
- [ ] Build memory knowledge graph
- [ ] Set up 5 websites + deploy system

### Phase 2: Daily Content Workflow
1. Pick one keyword in Agent OS
2. Find one real case study
3. Hit deploy → articles generated
4. Generate image in Grok Studio
5. Create short video → YouTube → embed
6. Review → approve → publish

### Phase 3: Weekly Project Workflow
1 project
2. Input into Kanban board
3. Agents work tasks in background
4. Review → publish

### Phase 4: Memory Maintenance
- **Daily:** Agents export learnings to Obsidian
- **Weekly:** Add case studies, results, audience insights
- **Monthly:** Full memory audit

---

## 30-Day Roadmap

### Week 1 — Foundation
| Day | Focus |
|-----|-------|
| 1 | Agent OS setup + integrations |
| 2 | Obsidian knowledge graph |
| 3 | First content deployment |
| 4 | First image in Grok Studio |
| 5 | First video → YouTube |
| 6 | Review + Search Console check |
| 7 | Rest + plan Week 2 |

### Week 2 — Acceleration
| Day | Focus |
|-----|-------|
| 8 | 3 keywords/day, 2 sites |
| 9 | First Kanban project (10 articles) |
| 10 | Batch image creation |
| 11 | Video creation for top 3 |
| 12 | Review + publish Kanban output |
| 13 | Deep memory update |
| 14 | Check rankings, double down |

### Week 3 — Scale
| Day | Focus |
|-----|-------|
| 15 | 5 keywords/day, all 5 sites |
| 16 | Second Kanban (25 articles) |
| 17 | Internal linking structure |
| 18 | Video series from top performers |
| 19 | Review all content |
| 20 | Full system audit |
| 21 | Share results in community |

### Week 4 — Optimisation
| Day | Focus |
|-----|-------|
| 22 | Update top 10 articles |
| 23 | Add case studies + data |
| 24 | Infographics from NotebookLM |
| 25 | YouTube channel expansion |
| 26 | Content gap analysis |
| 27 | Full memory update |
| 28 | Calculate results |
| 29 | Plan Month 2 |
| 30 | Celebrate — system is live |

---

## 100+ Prompts For Claude AI SEO

### Content Creation (1–15)
1. Create SEO-optimised article for "[keyword]" using case study: [paste]
2. Write complete blog post on "[keyword]" with unique data: [data]
3. Create introduction targeting "[keyword]" — hook with pain point
4. Write 5 SEO title options for "[keyword]" — under 60 chars
5. Create full content outline for "[keyword]" — 10 subheadings
6. Write conclusion for "[keyword]" with strong CTA
7. Create FAQ section — 10 questions, 2-3 sentence answers
8. Rewrite for readability: [paste text]
9. Create meta description for "[keyword]" — under 155 chars
10. Write listicle: "10 Ways To [achieve result]"
11. Article intro with shocking statistic about "[keyword]"
12. Beginner's guide to "[keyword]" — simple words
13. "[Tool A] vs [Tool B]" comparison article
14. "Common mistakes" article — 7 mistakes + fixes
15. Case study: how [business] achieved [result] using [method]

### Keyword Research (16–30)
16. 20 long-tail variations for "[keyword]" — informational intent
17. Top 10 questions people ask about18. Keyword cluster for "[topic]" — 5 subtopic categories
19. Biggest content gaps in "[niche]"
20. 10 comparison keywords "[A] vs [B]" for "[niche]"
21. Top "best [category]" keywords for "[niche]"
22. 20 "how to" keywords for "[topic]" — beginner to advanced
23. Best keywords for Google AI Overview in "[niche]"
24. 3-month keyword roadmap for new "[niche]" site
25. 15 "free [tool/resource]" keywords in "[niche]"
26. Buying-decision keywords in "[niche]"
27. 10 evergreen keywords in "[niche]"
28. Top keywords related to "[tool name]"
29. 20 "for beginners" keywords in "[niche]"
30. First 90 days keywords for new "[niche]" blog

### Image & Visual (31–38)
31. Grok Studio prompt for "[keyword]" article image
32. Best image types for "[keyword]" blog post
33. Alt text for "[keyword]" image
34. 10 image ideas for "[topic]" article
35. Image caption for "[describe graphic]"
36. Grok Studio infographic prompt for "[process]"
37. Best visuals for shares + backlinks on "[keyword]"
38. Three Grok Studio hero image prompts for "[topic]"

### Video SEO (39–48)
39. YouTube script for "[keyword]" — under 5 min + timestamps
40. YouTube title, description, 10 tags for "[keyword]"
41. YouTube description for "[keyword]" — under 300 words
42. Ideal video structure for "[keyword]" on YouTube
43. 5 hook ideas for "[keyword]" YouTube video
44. Closed captions for 60-second "[keyword]" video
45. YouTube Shorts script for "[keyword]" — under 60 sec
46. Most searched YouTube keywords in "[niche]"
47. Video intro script for "[niche]" channel — under 30 sec
48. 30-video content calendar for "[topic]" channel

### Agent & Kanban (49–58)
49. Break into tasks: [describe project] + priority + time estimates
50. Project plan for 30-article blog on "[topic]"
51. Pillar + cluster pages for "[topic]" content hub
52. Content brief for agent to write on "[keyword]"
53. SOP for keyword → published article automation
54. Quality checklist for AI agent before publishing
55. Priority order for 50 keywords using: [logic]
56. SEO tasks best for AI automation — ranked by impact
57. Weekly content production workflow for agent team
58. Delegation brief for internal linking across 20 posts

### Memory System (59–68)
59. Summarise business info into memory note: [paste]
60. Create style guide from tone examples: [paste]
61. Patterns in top 5 articles: [paste] — what to replicate
62. Audience profile from: [paste audience info]
63. Top 20 knowledge graph categories for: [describe business]
64. Memory update from recent results: [paste]
65. Questions to answer for best AI context
66. Memory node template for new tools
67. Fix generic tone — instructions from real writing: [paste]
68. Weekly "lessons learned" memory update template

### SEO Strategy (69–78)
69. 90-day SEO strategy for new "[niche]" site
70. Competitive analysis for "[keyword]" — how to win
71. Top on-page SEO factors for 2026
72. Internal linking strategy for 50-article "[topic]" blog
73. Push page-2 article to page 1 — top 3 actions
74. Structure for Google AI Overview — formatting checklist
75. Perfect SEO blog post structure for 2026
76. Backlink strategy for new "[niche]" site
77. Top technical SEO issues — audit checklist
78. Use existing content for more keywords — step-by-step

### Content Refresh & Repurposing (79–85)
79. Rewrite 2022 article for 2026: [paste]
80. Turn blog post into YouTube script: [paste]
81. Turn article into 5 social posts: [paste]
82. Turn article into podcast script: [paste]
83. Turn article into infographic brief: [paste]
84. Combine 10 posts into pillar page: [paste]
85. Turn article into email newsletter: [paste]

### Reporting & Analysis (86–90)
86. GSC data patterns: [paste] — what to do more
87. Patterns in top 10 articles: [paste]
88. 90-day traffic summary: [paste]
89. Page-2 keywords action plan: [paste]
90. Competitor content gap analysis: [paste]

### Niche Authority (91–95)
91. 6-month authority-building plan for "[topic]"
92. Top 10 questions in "[niche]" — content briefs
93. Top 10 controversies in "[niche]" for opinion pieces
94. "State of the industry" article for "[niche]" 2026
95. Definitive resource page on "[topic]" for backlinks

### Technical SEO (96–100)
96. Schema markup for "[topic]" — Article + FAQ schema
97. Optimised meta titles + descriptions for 10 pages: [paste]
98. robots.txt for "[niche]" content site
99. XML sitemap for categories: [paste]
100. Top 5 page speed fixes: [paste audit]

### Bonus Prompts (101–105)
101. 30-day content calendar for "[niche]"
102. 500-word article optimised for featured snippet on "[keyword]"
103. Top 10 AI SEO tools in 2026
104. Reusable content brief template
105. Best 5 content types for "[niche]" SEO

---

## Pro Tips

- 🔥 **One video = 5 posts = 5 sites.** Film once, let the pipeline do the rest.
- 🎯 **Low competition first.** Ahrefs keyword generator. KD < 20.
- 📺 **Embed same video on all 5 posts.** Video dwell time = cheat code.
- 🪝 **Different titles, same body.** CTR varies by formula, not content.
- 💰 **Always link to offer.** 4 times minimum per post.
- 🧠 **Obsidian vault for transcripts.** Searchable, forever.
- 🚀 **Deploy daily.** 1 transcript = 5 posts = 35 posts/week.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Sites not in SEO tab | Restart Agent OS. Check seoPipeline.ts paths. |
| Deploy fails | `netlify status` → `netlify login` if needed |
| Same content all 5 sites | Check "5 different titles" in blog-post.md + unique names in config |
| Transcript missing | Lowercase, hyphens only, no spaces in filename |

---

## Key Takeaways

> "It's not a tool. It's a system. And a system is what changes everything." — Julian Goldie

The old way: write manually, one piece at a time, hope it ranks.
The new way: keyword + case study + system → content, images, videos deploy themselves.

**People who win in the AI era build smarter systems that work 24/7 without them.**
