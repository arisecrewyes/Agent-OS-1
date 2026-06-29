---
tags: [ai, obsidian, second-brain, claude, context-engine, infinite-context]
date: 2026-06-29
source: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1
series: skool-posts
aliases: [Infinite Context Engine, Claude Obsidian, AI Second Brain]
---

# Claude + Obsidian: The Infinite Context Engine

> [!summary] Core Idea
> Every AI agent works at ~10% power because it starts every chat with zero context. The Infinite Context Engine fixes this with three free tools: OMI (capture) + Obsidian (storage) + Claude (reader/organizer). Two-way loop compounds intelligence daily.

---

## The Three Tools

### OMI — The Listener
- **URL:** https://www.omi.me
- **Role:** Runs in background, captures what you do every few minutes
- **Features:** Auto-notes on conversations/decisions/tasks, screen recording, voice notes, task summaries
- **Key point:** Zero manual work. You just work, it captures everything.
- **Pricing:** Free open-source app (skip the OMI chat subscription — not needed)

### Obsidian — The Brain
- **URL:** https://obsidian.md
- **Role:** Stores everything as plain markdown files on your local computer
- **Key features:** Knowledge graph, wikilinks, tags, graph view, local-first
- **Why it matters:** Every AI agent speaks markdown natively. Obsidian = universal memory layer for all agents.
- **Critical:** Files are on YOUR machine, not behind a service. Survives any app shutdown.

### Claude — The Reader & Organizer
- **URL:** https://claude.ai
- **Role 1:** Reads vault before answering → contextualized responses
- **Role 2:** Writes useful notes back into the vault after every conversation
- **Result:** Vault grows and improves daily with no manual effort

---

## The Two-Way Loop

```
�─────────────┐     ┌─────────────┐     ┌─────────────┐
│     OMI     │────▶│   Obsidian  │────▶│    Claude   │
│  (captures) │     │  (stores)   │     │   (reads)   │
└─────────────┘     └─────────────┘     └──────┬──────┘
       ▲                                        │
       │           ┌─────────────┐              │
       └───────────│  New Notes  │�─────────────�
                   │  written    │
                   └─────────────┘

Loop runs daily → compounds over months
By month 6: vault contains more useful business context than you can hold in your head
```

---

## PARA Organization

> From Tiago Forte's Building a Second Brain methodology. Claude already understands it natively.

| Letter | Category | Contents |
|--------|----------|----------|
| **P** | 📌 Projects | Active work, this quarter's goals, current campaigns, live projects |
| **A** | 📌 Areas | Ongoing responsibilities: Marketing, Clients, Team management |
| **R** | � Resources | Reference material: Books, Frameworks, Articles, Tools, Prompts |
| **A** | 📌 Archive | Inactive: Old projects, outdated notes (still searchable, out of the way) |

---

## 30-Day Rollout

### Week 1: Foundation (Days 1–7)

**Day 1: Create Vault**
- Download Obsidian from https://obsidian.md
- Create vault named "Second Brain"
- Prompt: `I just created an Obsidian vault. Help me create a PARA folder structure for a solopreneur who runs an online business. Give me the exact folders to create and what goes in each one.`

**Day 2: Populate Vault**
- Dump existing notes, emails, ideas, goals, project info into right PARA folders
- Prompt: `Here are my raw notes from my business [paste notes]. Organise them into clean markdown files for an Obsidian second brain using PARA structure. Add relevant tags and links between related notes.`

**Day 3: Install OMI**
- Download from https://www.omi.me
- Let it run during your work day
- End of day: export OMI memories → Obsidian Daily Notes
- Prompt: `Here are today's raw OMI memory notes [paste them]. Clean these up into a structured daily log for my Obsidian vault. Highlight any decisions made, tasks to follow up on, and tools I used.`

**Day 4: Wire Claude to Vault**
- **Option A (simple):** Copy text from key notes → paste into Claude conversation
- **Option B (clean):** Install Obsidian MCP plugin from GitHub
- Prompt: `Here is my Obsidian vault context [paste your main notes]. Based on this, what are the three most important things I should be working on this week? What is my biggest current constraint?`

**Day 5: Graph View Colour Coding**
- Prompt: `I want to colour code my Obsidian graph. Here are my main notes [paste a sample]. Give me a list of tags I should add to each type of note so that tools, people, projects and resources are all colour coded correctly in the graph view.`
- Scheme: People=Blue, Tools=Orange, Projects=Green, Archive=Red

**Day 6: Personal Context Document**
- Prompt: `I want to create a personal context document for my Obsidian vault. This will be loaded at the start of every AI conversation so agents understand who I am. Ask me 20 questions about my business, goals, team, tools, projects and working style. Then use my answers to write a clean personal context document in markdown.`
- Save as "About Me" in vault root

**Day 7: First Automated Daily Note**
- Let OMI run all day → export memories → Claude → Obsidian
- Prompt: `Here are today's OMI memory notes [paste]. Convert these into a structured Obsidian daily note with these sections: What I worked on today, decisions made, follow-up tasks, tools used, ideas worth keeping. Format it in clean markdown.`

---

### Week 2: Automate (Days 8–14)

**Day 8: Project Tracking**
- Prompt: `Create a project template for my Obsidian vault. Every project should have: project goal, deadline, current status, team members involved, next action, relevant tools, and linked notes. Give me the markdown template.`
- Save as `_Project Template` → create note per active project

**Day 9: Tool Library**
- Prompt: `I use these tools in my business: [list your tools]. Create an Obsidian note for each one that includes: what it does, how I use it, key prompts I use with it, links to alternatives, and any limitations I have noticed.`
- Save in Resources > Tools

**Day 10: Prompt Library**
- Prompt: `Based on my business context [paste your About Me document], create 20 high-value prompts I should save in my Obsidian vault under a Prompt Library folder. These should be prompts I will use repeatedly for content creation, business decisions, client work, and automation ideas.`
- Save in Resources > Prompt Library

**Day 11: Weekly Review** (every Sunday)
- Prompt: `Here are my daily notes from this week [paste them]. Run a weekly review. Give me: top 3 wins, top 3 problems, biggest lessons, what to carry forward next week, and what to archive. Format this as a clean Obsidian weekly review note.`

**Day 12: People Vault**
- Prompt: `Create a contact note template for my Obsidian people vault. It should include: name, role, company, how we work together, key preferences and communication style, last conversation summary, action items, and linked projects.`
- Create notes for top 10 contacts

**Day 13: SOP Library**
- Prompt: `I run [describe your business]. Create a list of the 10 most important SOPs I should document for my Obsidian vault. For each one, give me a template with steps, tools used, and what a successful outcome looks like.`
- Build first 3 SOPs → store in Resources > SOPs

**Day 14: Vault Audit**
- Prompt: `Here is a summary of my Obsidian vault structure [describe it or paste your folder names and note titles]. Audit this second brain. What is missing? What connections am I not making? What should I add in the next two weeks to make this more powerful?`

---

### Week 3: Scale (Days 15–21)

**Day 15: Wire Vault Into Every Agent**
- Start every session with: `Before answering anything, here is my full context: [paste About Me + current project notes]. Use this as your operating context for this entire conversation.`

**Day 16: Content Idea System**
- Prompt: `Based on my business, audience, and current projects [from your vault], generate 30 content ideas I could create this month. For each idea include: the title, the core insight, the hook, and which part of my audience it helps most.`
- Save in Projects > Content Ideas

**Day 17: Decision Log**
- Prompt: `Create a decision log template for my Obsidian vault. Every entry should include: date, decision made, why I made it, what alternatives I considered, expected outcome, and a place to review the outcome in 30 days.`

**Day 18: Constraint Tracker**
- Prompt: `Based on my business context [paste your vault notes], what appears to be my main current constraint? Give me a breakdown of what is slowing my growth the most based on what you can see in my notes.`
- Then: `Create a constraint tracking template for my Obsidian vault. It should track: the constraint identified, the date found, what I tried to fix it, what worked, what did not work, and the date resolved.`

**Day 19: Morning Briefing**
- Prompt: `Good morning. Based on my Obsidian vault context [paste relevant notes], give me a morning briefing. Include: my top priority today, open loops from yesterday, any decisions I need to make, and the most important thing I should focus on in the next 90 minutes.`

**Day 20: Client Delivery System**
- Prompt: `I work with clients in [your niche]. Create a client folder template for my Obsidian vault. Each client folder should include: onboarding notes, project notes, communication log, deliverables tracker, and a notes section for what I know about their business.`
- Set up top 5 clients

**Day 21: Mid-Point Audit**
- Prompt: `Here is my full Obsidian vault structure after 21 days [describe it]. What patterns do you notice? What is well connected? What looks isolated? What should be linked that is not? Give me specific actions to improve the vault this week.`

---

### Week 4: Systematise (Days 22–30)

**Day 22: Vault Maintenance Routine** (10 min/week on Sunday)
1. Export OMI memories from the week
2. Paste into Claude with weekly review prompt
3. Save output to Weekly Reviews
4. Ask Claude to flag items for Archive
5. Archive them

**Day 23: NotebookLM Integration**
- Export Obsidian notes as text files → upload to https://notebooklm.google.com
- Prompt: `Based on the notes I have uploaded, what are the most important patterns and insights about my business? What opportunities am I missing?`

**Day 24: Agent Operating System**
- Prompt: `Based on my Obsidian vault [paste context], design an agent operating system for my business. Which tasks should be handled by Claude? Which by a research agent? Which by a content agent? Map out the workflow and which vault notes each agent should read before starting.`
- Save in Projects > Agent OS

**Day 25: Knowledge Compounding**
- Prompt: `I just read/watched/heard [describe it]. Extract the 5 most useful insights for my business specifically. Format them as concise notes I can save in my Obsidian resources folder.`

**Day 26: Win/Testimonial Tracker**
- Prompt: `Create a wins and testimonials tracker for my Obsidian vault. Every win should be logged with: date, what happened, what led to it, and how replicable it is. Give me the markdown template.`

**Day 27: Audience Intelligence**
- Prompt: `Based on my business context [paste vault notes], help me build an audience intelligence document for my Obsidian vault. Include: who my audience is, their biggest fears, their biggest goals, the questions they ask most, the beliefs that are holding them back, and what they most want to hear from me.`
- Save in Resources > Audience Intelligence

**Day 28: Compounding Agent Network**
- Prompt: `Based on everything in my vault [paste full context summary], design a compounding agent network. Which agents should I be using daily? What context should each one load? What should each agent produce and where should the output be stored in my vault?`

**Day 29: "Read Me First" Note**
- Prompt: `Based on my vault context [paste it], write a 'Read Me First' document for my second brain. This is for any new AI agent or team member who needs to get up to speed on my business quickly. Cover: who I am, what my business does, what my current priorities are, what my communication style is, and the most important things to know before working with me.`
- Save as first file in vault

**Day 30: Full Second Brain Review**
- Prompt: `You have full context on my business and my Obsidian vault. What is the single highest leverage thing I should build next to get even more out of this system? What is the one thing that, if I did it, would make everything else easier?`
- Save answer → make it Day 31 priority

---

## Complete Prompt Library

### Vault Setup
- `Create a PARA folder structure for an Obsidian second brain for a solopreneur who runs [describe your business]. Give me every folder and subfolder in markdown format.`
- `Here are my raw business notes [paste them]. Organise these into a clean Obsidian second brain using PARA structure. Add relevant tags and wikilinks between related notes.`
- `Create a personal context document for my Obsidian vault. Ask me 20 questions about my business, goals, team, tools, and working style. Then write the document using my answers.`
- `Audit my Obsidian vault structure [describe it]. What is missing? What should be better connected? Give me specific improvements to make today.`
- `Create a 'Read Me First' document for my second brain. Any new AI agent or team member should read this to understand my business, my priorities, my working style, and the most important context about me.`
- `Here is my Obsidian vault [paste a sample]. Suggest 20 new wikilinks I should add between existing notes to strengthen the knowledge graph.`
- `Convert my brain dump [paste it] into structured Obsidian notes. Each note should have a clear title, relevant tags, and links to related notes.`
- `I want to colour code my Obsidian graph. Give me a list of tags to add to each type of note so that tools, people, projects, and resources display in different colours.`
- `Create a master index note for my Obsidian vault that links to every major section. This should be the starting point whenever I open the vault.`

### Daily Workflow
- `Good morning. Here is my vault context [paste it]. Give me a morning briefing: my top priority today, open loops from yesterday, decisions to make, and the most important 90-minute focus block.`
- `Here are my OMI memories from today [paste them]. Create my daily log for Obsidian with sections: work done, decisions made, tasks to follow up, ideas worth keeping.`
- `End of day review. Here is what I worked on [paste notes]. Summarise my day into three wins, three things to improve, and tomorrow's most important first task.`
- `Based on my current project notes [paste them], what should I be working on right now? Rank by impact and urgency.`
- `Here is my weekly calendar [describe it]. Based on my vault context, am I spending time on the right things? What is misaligned with my goals?`
- `Create 5 high-leverage tasks for tomorrow based on my current projects and constraints [paste relevant notes].`
- `Flag any open loops in my vault [paste notes]. What has not been resolved? What decisions are still pending? What tasks have no next action?`
- `Based on my vault context, what is my single biggest constraint right now? What would eliminating it unlock?`
- `Write my end of week reflection for Obsidian. This week I [describe your week]. Format it with wins, lessons, and next week's intention.`
- `Review my decision log from the past month [paste it]. What patterns do you see? Which types of decisions led to the best outcomes?`

### Content Creation
- `Based on my audience intelligence document [paste it], generate 30 content ideas for this month. Each idea should include a title, core insight, hook, and which audience pain point it addresses.`
- `Using my personal context document [paste it], write a YouTube hook for a video about [topic]. The hook should feel like it was written by me, not by a generic AI.`
- `Here is my content idea [describe it]. Using my communication style and audience notes [paste them], write a full video script outline with hook, main sections, and call to action.`
- `Generate 10 contrarian angles on the topic of [topic] that would resonate specifically with solopreneurs who already use AI but feel stuck.`
- `Based on my vault context, what content topics am I most credible to talk about? Rank them by potential audience value and my unique angle.`
- `Write 5 different hook variations for this video topic [describe it]. Each hook should start with a specific claim or result, not a soft opener.`
- `Using my audience intelligence notes [paste them], write a belief-breaking opening for a video about [topic]. Break the most common limiting belief in the first 30 seconds.`
- `Create a 90-day content calendar for my business based on my current projects, audience, and goals [paste context]. Include video titles, post topics, and key messages.`
- `Here is a rough transcript of my video [paste it]. Edit it for clarity and punch. Keep my voice. Every sentence on its own line. Short. Direct.`
- `Create 10 YouTube thumbnail text options for a video about [topic]. Each should be under 5 words and create maximum curiosity.`

### Agent Operating System
- `Based on my vault context [paste it], design an agent operating system for my business. What should Claude handle? What should a research agent handle? What should a content agent handle?`
- `Write a system prompt for a Claude agent that knows my business. Use my personal context document [paste it] as the base. The agent should understand my tone, priorities, and working style.`
- `Create a context loading prompt I can paste at the start of every AI conversation to give any agent full context on my business in under 200 words.`
- `Based on my SOPs [paste them], create a system prompt for an AI agent that can handle [specific task] for my business without asking clarifying questions.`
- `Design a morning agent routine. When I wake up and open Claude, what should happen automatically based on my vault? What should it surface? What should it prepare?`
- `Create a prompt chain for my content creation workflow: research, outline, draft, edit, repurpose. Each step should load the right vault context for that stage.`
- `Write a project kickoff prompt. When I start a new project, I want to paste this and have Claude immediately understand the project goals, constraints, and first steps based on my vault.`
- `Create a prompt for a client briefing agent. Before every client call I paste the client's vault note and this agent gives me a briefing on where we are and what to discuss.`
- `Design a delegation agent prompt. When I want to delegate a task, I paste this and the agent writes a clear brief for a team member using my communication style.`
- `Create a constraint-busting agent prompt. When I am stuck, I paste my current situation and this agent identifies the real bottleneck and gives me the three highest-leverage moves.`

### Business Strategy
- `Based on my vault context [paste it], what are the three biggest opportunities I am currently underexploiting? Give me specific actions for each.`
- `Run a 90-day business audit based on my vault notes [paste them]. What is working? What is not? What should I stop, start, and continue?`
- `Based on my project notes and goals [paste them], am I working on the right things? What would a top-tier business advisor tell me to change?`
- `Create a prioritisation matrix for my current project list [paste it]. Rank by impact, urgency, and alignment with my 90-day goal.`
- `Here are my business goals for this quarter [paste them]. What is the single most important constraint standing between me and hitting them?`
- `Based on my vault, what decisions am I avoiding? What hard choices am I deferring that are costing me leverage?`
- `Design a 90-day sprint plan based on my current projects and goals [paste context]. What should I focus on in each month to build maximum momentum?`
- `Create a weekly operating rhythm for my business based on my working style and goals [paste vault context]. What should I do each day to make consistent progress?`
- `Analyse my delegation log [paste it]. What am I still doing myself that I should be delegating or automating? Give me specific tasks to remove from my plate.`
- `Based on my business context, what does my ideal day look like in 90 days if I implement everything we have discussed? Describe it hour by hour.`

### Knowledge and Learning
- `I just read [describe a book or article]. Extract the 5 most useful insights for my specific business situation [paste context].`
- `Here are my notes from a podcast or conversation [paste them]. What are the key takeaways I should save in my Obsidian vault? Format them as clean notes.`
- `Create a book summary template for my Obsidian resources folder. Every book I read should have: core thesis, top 10 insights, how it applies to my business, and one action to take.`
- `Based on my learning notes from the past month [paste them], what themes keep appearing? What is my subconscious trying to tell me to focus on?`
- `I want to go deep on [topic]. Based on my current knowledge level [describe it], create a 30-day learning curriculum. Include free resources, key concepts to understand, and daily study tasks.`
- `Convert this dense article [paste it] into 5 clean Obsidian notes. Each note should be a standalone insight with a clear title and relevant tags.`
- `Create a mental model library entry for the concept of [concept]. Explain it simply, give an example from business, and show how I can use it when making decisions.`
- `Here is a framework I want to learn [describe it]. Create a personal implementation guide for my Obsidian vault showing exactly how I would apply this in my specific business.`
- `Based on my vault notes, what skills are most worth developing in the next 90 days to remove my biggest constraints? Rank them by leverage.`
- `Create a weekly learning review template for my Obsidian vault. Each week I should log: what I learned, how it changed my thinking, and what I plan to test based on it.`

### Productivity and Focus
- `Based on my time tracking data [describe your patterns], where is my time best spent? Where am I losing the most leverage?`
- `Create a daily schedule template for my Obsidian vault based on my working style [describe it]. Include focus blocks, communication blocks, and recovery time.`
- `Design a distraction elimination plan for my work environment based on my goals and working style [paste context]. What should I cut, limit, or schedule?`
- `Based on my current projects [paste them], what is the single highest-leverage task I could do in the next 90 minutes? Justify your answer.`
- `Create a weekly planning template for my Obsidian vault. Every Sunday I should fill this in to set myself up for a focused, high-output week.`
- `Review my task list [paste it]. Which items are inputs I control? Which are outputs I am waiting for? Help me focus only on what I can move.`
- `Design a 'deep work' session template for my Obsidian vault. Before each deep work block I should paste this and Claude will help me focus on exactly the right thing.`
- `Based on my goals [paste them], create a not-to-do list. What are the 10 things I should say no to so I can protect my focus?`
- `Analyse my recent daily logs [paste them]. Am I getting to my most important work first? What patterns do you notice about when I am most productive?`
- `Create a meeting template for my Obsidian vault. Every meeting should have: agenda, key decisions to make, who needs to do what, and how long it should last.`

### Team and Client
- `Create an onboarding document for a new team member using my vault context [paste it]. They should understand my communication style, expectations, and how I like things done.`
- `Here are my notes on a team member [describe the situation]. Based on my management style [paste context], how should I approach giving them feedback?`
- `Create a client onboarding template for my Obsidian vault. When a new client starts, this should capture: goals, constraints, communication preferences, and first 30-day milestones.`
- `Based on my client notes [paste them], what patterns do you notice? What do my best clients have in common? What do my most difficult clients have in common?`
- `Write a delegation brief for this task [describe it] using my communication style [paste context]. Include the outcome expected, the constraints to work within, and how to report back.`
- `Create a performance review template for my Obsidian vault. For each team member I should review: what they committed to, what they delivered, what to improve, and what to recognise.`
- `Based on my client context [paste it], prepare a briefing for my next call with them. What are the three most important things to discuss? What decisions need to be made?`
- `Create a team accountability tracker template for my Obsidian vault. Every commitment made by a team member gets logged here with a due date and status.`
- `Based on my vault, what processes do I need to document as SOPs so that my team can operate independently without me involved?`
- `Write a client update email based on this project note [paste it]. Keep it clear, professional, and focused on progress and next steps. Use my communication style.`

### Research and Analysis
- `Research the tool [name it]. Based on my business context [paste it], is this worth adding to my stack? Give me a clear yes or no with specific reasons.`
- `Compare these two tools [name them] for my specific use case [describe it]. Give me a decision framework not just a feature list.`
- `Based on my vault context, what AI tools am I not currently using that would give me the highest leverage? Give me three specific recommendations with reasoning.`
- `Create a tool evaluation template for my Obsidian vault. Every new tool I try should be assessed on: what it does, how it fits my stack, the learning curve, and whether I should keep it.`
- `Here is a trend I noticed [describe it]. Based on my business context, is this relevant to me? Should I pay attention to it or ignore it?`
- `Create a competitive landscape note for my Obsidian vault about [your niche]. What are the main categories of tools? What is emerging? What is declining?`
- `Based on my audience intelligence notes [paste them], what questions is my audience asking right now that I am not yet answering with my content?`
- `Analyse this data [paste it]. Based on my business context, what does it mean? What action should I take based on what you see?`
- `Create a trend tracking template for my Obsidian vault. Every week I should log the most important AI and business trends relevant to my niche and how they affect my strategy.`
- `Based on my project notes [paste them], what risks am I not accounting for? What could go wrong that I have not prepared for?`

### Growth and Scale
- `Based on my vault context [paste it], what is my current highest-leverage growth activity? What single action would create the most compounding effect?`
- `Create a 90-day growth sprint plan based on my goals and constraints [paste context]. Break it into weekly milestones with clear daily actions.`
- `Based on my content notes [paste them], what formats and topics have performed best? What should I do more of? What should I cut?`
- `Design a lead generation system for my business using only free tools. Base it on my audience context [paste it] and my current content strategy.`
- `Based on my vault, what would I do differently if I could only work 4 hours a day? What are the truly high-leverage activities vs the busy work?`
- `Create a monthly business review template for Obsidian. I should review: progress towards goals, what worked, what did not, what to focus on next month, and what to delegate or automate.`
- `Based on my audience intelligence [paste it], design a content funnel. What content brings people in? What converts them to leads? What turns leads into community members?`
- `Create a system for documenting winning formulas in my Obsidian vault. When something works, I want a template that captures exactly what I did so I can replicate it.`
- `Based on my vault context, what do I know that my audience does not? What unique knowledge do I have that would be most valuable to share?`
- `Design my ideal AI stack for 12 months from now based on my current situation [paste context]. What tools, systems, and processes would I have in place? Work backwards from that to give me my next 30 days.`

### Bonus Prompts
- `Create a personal values statement for my Obsidian vault based on how I work, what I prioritise, and what I care about [describe yourself].`
- `Write my 1-year vision for my business in clear simple language. Base it on my current trajectory [paste context] but push me to think bigger.`
- `Based on my vault, what am I doing that is not aligned with my stated goals? Where is there a gap between what I say matters and how I spend my time?`
- `Create a mistakes log template for my Obsidian vault. Every mistake should capture: what happened, why it happened, what I learned, and what system change prevents it recurring.`
- `Design a morning routine checklist for my Obsidian vault based on my goals and working style [describe it]. What are the non-negotiable inputs every morning?`
- `Based on my vault context, write a simple explanation of what I do and why it matters. Something I could use to introduce myself to a new audience.`
- `Create a belief tracking note for my Obsidian vault. These are the beliefs about business and AI that I want to reinforce every day. Based on my goals and context [paste them], what should those beliefs be?`
- `Review my vault from the perspective of someone new to my business. What is confusing? What is missing? What does not make sense yet?`
- `Based on everything in my vault, what is the most important thing I know that I am not yet acting on? What is the gap between my insight and my behaviour?`
- `Create a legacy note for my Obsidian vault. In 5 years, when I look back at this season of my business, what do I want to have built? Write it as if it already happened.`

---

## Core Belief Shifts

| Old Belief | New Belief |
|------------|------------|
| AI gives generic answers, not that useful | AI quality = context quality. Give it a brain, changes the category of tool |
| Too complicated to set up | Just 3 free tools passing notes. Simpler than email. |
| Not enough notes to start | 10 well-written notes give more context than 100 blank conversations. Start small. |
| Platforms will add memory eventually | Even if they do, it is siloed to one platform. Obsidian belongs to you, works with every agent. |
| No time to maintain it | OMI writes notes. Claude organizes. You work. 10 min/week maintenance. |
| Not technical enough | If you can organize a desktop folder, you can build this. No code required. |
| Won\'t change AI performance | Categorical difference, not incremental. Smart stranger becomes smart colleague. |
| Will lose everything if app shuts down | Obsidian = plain text files on your machine. Survives every platform. |

---

## Why This Matters for All AI Builders

Any AI agent (GoStackBase, Claude, Gemini, etc.) benefits from persistent context. An Obsidian vault serves as the **universal memory layer** \-\-\-\ the vault is on your machine, readable by every tool, owned by you.

**Maintenance:** 10 minutes/week (Sunday). Export OMI \-\-\> Claude processes weekly review \-\-\> archive outdated notes. The rest is automated.

---

## Related Notes

- [[Skool-Post-11-Infinite-Context-Engine]] \-\-\ originating post (11th May)
- [[Skool-Post-Hermes-Obsidian]] \-\-\ companion post (30th May)
- [[Agent-OS]] \-\-\ agent operating system design
- [[PARA-Method]] \-\-\ Tiago Forte\'s second brain methodology

---

## Resources

- **OMI:** https://www.omi.me (free capture app)
- **Obsidian:** https://obsidian.md (free markdown vault)
- **Claude:** https://claude.ai (free tier available)
- **Obsidian MCP plugin:** Search on GitHub at https://github.com
- **NotebookLM:** https://notebooklm.google.com (free AI research tool)
- **Building a Second Brain** by Tiago Forte \-\-\ book the PARA method comes from