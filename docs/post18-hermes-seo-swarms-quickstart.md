# QuickStart: Hermes Agent SEO Swarms

> Converted from Julian Goldie Skool Post #18 — "Hermes Agent SEO Swarms"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/42d25f4b?md=3ace71b669104e8fb7b92dbcff0aaa95

---

## What You're Building

**The Goldie SEO Swarm System** — a complete, automated, end-to-end blog system using free AI agents working together inside Hermes Agent. It plans your content, writes it, and helps your blog get found on Google.

> "The people winning online aren't working harder. They're running better systems. This is yours." — Julian Goldie

---

## What Is Hermes Agent?

Hermes Agent is a **free, open source AI tool** that runs locally on your computer. It lets you build AI agents and connect them together into a swarm — each agent has one job, and together they form a complete automated system.

### What Can Hermes Agent Do?

- 🔍 Research topics for your blog
- 📅 Plan a full content calendar
- ✍️ Write complete blog posts from scratch
- 🔎 Optimise posts for Google
- 🔄 Repurpose content into social media posts
- 🤖 Run the entire process on autopilot

All free. All local. No monthly fees.

---

## 🏆 The Goldie SEO Swarm System (S.E.O.W.A.R.)

The system uses 5 agents + 1 repeat step, each with a specific role:

| Step | Agent | Role |
|------|-------|------|
| 🅢 | **Strategy** | Researches niche, identifies topics, builds content plan |
| 🅔 | **Execute** | Writes complete blog posts with proper structure |
| 🅞 | **Optimise** | Optimises posts for Google (keywords, meta, headings) |
| 🅦 | **Workflow** | Connects all agents, runs the system on repeat |
| 🅐 | **Amplify** | Turns one post into social media content (Twitter, LinkedIn, IG) |
| 🅡 | **Repeat** | Compounds content library over time |

### The Full Flow

```
Strategy Agent → Writer Agent → SEO Agent → Workflow Agent → Amplify Agent → Repeat
   (research)      (write)       (optimise)    (automate)      (repurpose)    (compound)
```

---

## ⚙️ Installation

### Step 1: Download Hermes Agent
1. Go to the official Hermes Agent GitHub page
2. Click the green "Code" button → "Download ZIP"
3. Extract the folder to your Desktop

### Step 2: Install Ollama (Free Local AI)
1. Download Ollama from [ollama.com](https://ollama.com)
2. Follow the install instructions for your OS
3. Pull a free model: `ollama pull llama3`

### Step 3: Connect
1. Open Hermes Agent
2. Connect it to your Ollama instance
3. You now have a fully free, fully local AI system

---

## 🐝 Building Your Swarm — Agent-by-Agent

### Agent 1: Strategy Agent

**What it does:** Researches your niche, identifies what people are searching for, builds a full content plan.

**System Prompt:**
```
You are an expert SEO content strategist. Your job is to research [niche] and produce a full content strategy. Identify the top 20 blog topics that real people are searching for right now. For each topic, write the target keyword, the search intent, and a one-sentence summary of what the post should cover. Format everything as a numbered list.
```

### Agent 2: Writer Agent

**What it does:** Takes topics from Agent 1 and writes complete, structured blog posts (1,500+ words).

**System Prompt:**
```
You are an expert blog writer. Your job is to write a complete, high-quality blog post on the topic provided. The post must be at least 1,500 words. Use H1, H2, and H3 headings. Write in a friendly, conversational tone that a beginner can understand. Include an introduction, main body sections, and a clear conclusion. Target keyword: [keyword]. Write the full post now.
```

### Agent 3: SEO Optimisation Agent

**What it does:** Optimises finished posts for Google — keyword placement, meta descriptions, headings, internal links.

**System Prompt:**
```
You are an expert on-page SEO specialist. Take the blog post provided and optimise it fully for search engines. Check that the target keyword appears in the title, first paragraph, at least two subheadings, and the conclusion. Write a meta title under 60 characters. Write a meta description under 160 characters. Suggest three internal linking opportunities. Return the fully optimised post with all changes made.
```

### Agent 4: Workflow Automation Agent

**What it does:** Connects all agents together — triggers Strategy → Writer → SEO in sequence automatically.

**System Prompt:**
```
You are a workflow coordinator. When given a niche or topic, your job is to coordinate the following sequence: First, run a content strategy analysis and return 5 blog topic ideas. Second, take the top topic and write a full blog post. Third, take that post and run a full SEO optimisation pass. Return the final, optimised post ready to publish. Begin now with this niche: [niche].
```

### Agent 5: Amplify Agent

**What it does:** Takes one finished post and turns it into Twitter thread, LinkedIn post, Instagram captions, YouTube description.

**System Prompt:**
```
You are a content repurposing expert. Take the blog post provided and create the following: 1) A Twitter/X thread of 8 tweets summarising the key points. 2) A LinkedIn post of 150 words based on the main insight. 3) Five short Instagram captions under 50 words each. 4) A YouTube video description of 200 words. Return all four formats clearly labelled.
```

---

## 📋 Weekly SOP — Run This Every Week

| Day | Task |
|-----|------|
| **Monday** | Run Strategy Agent → Choose 5 topics → Add to content calendar |
| **Tuesday–Thursday** | Run Writer Agent for each post → Review → Run SEO Agent → Save optimised posts |
| **Friday** | Publish posts → Run Amplify Agent → Post social content → Track clicks |
| **Sunday** | Check analytics → Note top performers → Feed data back into Strategy Agent |

### Daily Checklist

- [ ] Open Hermes Agent
- [ ] Run at least one agent task
- [ ] Review and approve output
- [ ] Publish or schedule content
- [ ] Note one learning from today

---

## 🗓️ 30-Day Roadmap

### Week 1: Setup and First Posts (Days 1–7)

| Day | Focus |
|-----|-------|
| 1 | Install Hermes Agent + Ollama, connect model, explore dashboard |
| 2 | Build Strategy Agent, run with your niche, pick top 5 topics |
| 3 | Build Writer Agent, write first full blog post |
| 4 | Build SEO Agent, optimise first post, publish |
| 5 | Build Workflow Agent, run full swarm end-to-end |
| 6 | Build Amplify Agent, repurpose first post |
| 7 | Review what you published, note what worked, rest |

### Week 2: Build the Habit (Days 8–14)

| Day | Focus |
|-----|-------|
| 8–10 | Run full swarm for 3 new posts (aim: 1 post/day) |
| 11–12 | Check analytics, write 2 more posts on best-performing topics |
| 13 | Repurpose all 5 posts with Amplify Agent, schedule social content |
| 14 | Weekly review — what's working? Tweak agent prompts |

### Week 3: Optimise and Scale (Days 15–21)

| Day | Focus |
|-----|-------|
| 15–17 | Run swarm daily, improve Strategy Agent output quality |
| 18–19 | Add internal links between posts, re-run SEO Agent |
| 20–21 | Review full blog, identify top 3 posts, create 2 related posts |

### Week 4: Compound and Repeat (Days 22–30)

| Day | Focus |
|-----|-------|
| 22–25 | Build content clusters (groups of posts around one main topic) |
| 26–28 | Audit every post for SEO improvements, re-run Amplify on top 5 |
| 29 | Full monthly review — posts published, traffic, next month focus |
| 30 | 🎉 First month complete — scale output in month two |

---

## 💬 100+ Prompts for Your Swarm

### 🔍 Strategy & Research Prompts

1. Identify the top 20 blog topics in [niche] that beginners search for most
2. What are the most common questions people ask about [topic] on Google?
3. List 10 long-tail keywords for [niche] with low competition and high search intent
4. What content gaps exist in [niche] that most blogs aren't covering?
5. Create a 3-month content calendar for a [niche] blog posting 3x per week
6. What are the top 5 pain points of someone new to [niche]?
7. What are 10 "how to" blog post ideas for [niche]?
8. List 10 comparison post ideas for [niche] (e.g. "X vs Y")
9. What are the trending topics in [niche] right now?
10. Generate 20 blog post titles for [niche] targeting beginners
11. What are the best content pillars for a blog about [niche]?
12. List 10 evergreen blog topics in [niche] that will stay relevant for years
13. What topics in [niche] have the highest commercial intent?
14. Generate a keyword cluster around the main topic of [keyword]
15. What related topics should a blog about [niche] cover to build authority?
16. List 5 blog post ideas targeting awareness stage for [niche]
17. List 5 blog post ideas targeting people ready to buy in [niche]
18. What questions does someone ask before they buy [product/service]?
19. Create a content strategy for a brand new blog in [niche] with zero traffic
20. What are the top 10 mistakes beginners make in [niche]?

### ✍️ Writing Prompts

1. Write a complete 1,500-word blog post on [topic] for beginners
2. Write an attention-grabbing introduction for a post about [topic]
3. Write a compelling conclusion with a clear next step
4. Rewrite this paragraph to make it easier to read: [paragraph]
5. Write 5 alternative headlines for a post about [topic]
6. Write a blog post outline for [topic] with 5 main sections
7. Write the main body of a post about [topic] in 1,000 words
8. Write a "beginner's guide" style post about [topic]
9. Write a "step-by-step tutorial" post about how to [task]
10. Write a "best tools for [task]" post covering 7 options
11. Write a "common mistakes" post about [topic] covering 10 mistakes
12. Write a "pros and cons" post about [topic]
13. Write a "what is [topic]" explainer post for complete beginners
14. Write a "how does [topic] work" post in simple language
15. Write a listicle: "10 Ways to [achieve result] With [tool/method]"
16. Write a case study showing how someone used [method] to get [result]
17. Write an opinion post on whether [controversial topic] is worth it
18. Write a "quick wins" post — 5 things readers can do today
19. Write a "complete guide" post about [topic] from beginner to advanced
20. Rewrite this introduction to be more engaging: [introduction]

### 🔎 SEO Optimisation Prompts

1. Write a meta title under 60 characters for a post about [topic]
2. Write a meta description under 160 characters for a post about [topic]
3. Check this post and suggest where to naturally add the keyword [keyword]
4. Rewrite this heading to include the keyword [keyword] naturally
5. Suggest 5 internal linking opportunities for a post about [topic]
6. Write an SEO-friendly URL slug for a post about [topic]
7. Suggest image alt text for an image in a post about [topic]
8. Identify keyword stuffing issues in this post and fix them
9. Write a schema markup description for a blog post about [topic]
10. Suggest 3 external authoritative sources to link to
11. Rewrite this introduction to include the target keyword in the first 100 words
12. List the top LSI keywords to include in a post about [topic]
13. Check this post's structure and suggest improvements for readability and SEO
14. Write a FAQ section for a post about [topic] with 5 questions and answers
15. Suggest a featured snippet optimisation for the keyword [keyword]
16. Rewrite this subheading as a question that matches search intent
17. Analyse this post and give it an SEO score out of 10 with suggestions
18. Suggest a title tag A/B test for a post currently titled [title]
19. Write a "people also ask" style section for a post about [topic]
20. What structured data markup would help this post rank better?

### 🔄 Repurposing & Amplify Prompts

1. Turn this blog post into a Twitter/X thread of 8 tweets
2. Turn this blog post into a LinkedIn post of 150 words
3. Turn this blog post into 5 Instagram captions under 50 words each
4. Turn this blog post into a YouTube video script
5. Turn this blog post into a podcast episode outline
6. Summarise this blog post into 3 bullet points for a newsletter
7. Turn this blog post into a Pinterest pin description
8. Create a Facebook post based on the key insight
9. Turn this blog post into a short-form video script under 60 seconds
10. Create a slide deck outline based on this blog post
11. Turn this blog post into an email newsletter
12. Extract the 5 most shareable quotes from this blog post
13. Turn these 5 blog posts into a free PDF guide
14. Create a content upgrade offer based on this blog post
15. Write a social media bio that reflects this blog's niche

### 🏗️ Blog Structure & Conversion Prompts

1. Suggest a site structure for a blog about [niche] with 5 main categories
2. Write a compelling homepage headline for a blog about [niche]
3. Write an "About" page for a blog about [niche] that builds trust
4. Write a lead magnet offer for a blog about [niche]
5. Write a pop-up opt-in headline for a blog about [niche]
6. Write a call-to-action for the end of a post about [topic]
7. Suggest 3 ways to improve the conversion rate of this blog post

---

## 🧠 Breaking Limiting Beliefs

| ❌ Wrong Belief | ✅ Right Belief |
|----------------|-----------------|
| "Blogging takes too long" | The swarm writes posts in minutes, not months |
| "I'm not a good enough writer" | You don't write — you direct |
| "AI content gets penalised by Google" | Strategic, structured content gets ranked |
| "This is too technical" | If you can copy-paste, you can run this |
| "I need expensive tools" | Hermes Agent is 100% free and open source |
| "Blogging is dead" | 8.5 billion Google searches/day — blogging isn't dead |
| "AI tools didn't work before" | One tool alone ≠ a swarm working together |
| "I need a big audience first" | Good content + strategy comes first, audience follows |
| "I don't have time" | 30 min setup, agents do the rest |
| "Results only happen for successful people" | Real people just like you are getting results |

---

## Key Takeaways

1. **One AI tool alone = calculator. A swarm = full-time team.**
2. **The Goldie SEO Swarm System** uses 5 specialised agents working in sequence
3. **Hermes Agent is free, open source, and runs locally** — no monthly fees
4. **The system runs on repeat** — set it up once, it compounds over time
5. **Better prompts = better results** — 100+ prompts included above
6. **30-day roadmap** takes you from zero to a working blog system
7. **Content clusters** (groups of related posts) build authority faster
