# Hermes Agent — AI Prompt Library

> Ready-to-use prompts for common Hermes Agent tasks.
> Source: Julian Goldie SEO — Skool Post #4
> Related: [[hermes-agent-capabilities-general]] | [[hermes-quickstart]]

---

## Social Media

### X/Twitter Post with Trending Content + Image
```
Every 30 minutes, check trending topics on these two subreddits,
draft a tweet, generate an image, and post it to X.
Send me a Telegram confirmation with the live link.
```

### TikTok Post
```
Create a TikTok post about [topic].
include 3 relevant hashtags and a caption that drives engagement.
```

### Instagram Post
```
Create an Instagram post about [topic].
Write a compelling caption with hashtags.
```

### X/Twitter Manual Post
```
Create a post about [topic] and post to X using the Chrome extension.
Include 3 relevant hashtags and an image.
```

---

## Research & Monitoring

### Reddit Trending Topics
```
Research Reddit for the newest trending topics in [niche].
Show me what's trending, who posted, and why it's popular.
```

### Competitor Analysis
```
Every 24 hours, analyze my competitors' social media,
show me what content is trending, what is working,
who posted, and their analytics breakdown.
```

### Web Browsing & Research
```
Using Firecrawl, go to [URL] and extract the main information.
Summarize it in a concise format.
```

### Visual Web Browsing
```
Using Browser Base, go to [website] and [describe what to do].
Take screenshots and report back what you found.
```

### Daily AI News Summary
```
Every morning at 8am, scan AI news sources and send me
a summary of what matters.
```

### Weekly X Analytics
```
Every Friday, pull my X analytics for the last 14 days,
analyze top performing tweets, and send me a breakdown
in Telegram with screenshots.
```

---

## Content Pipeline

### Automated Content Creation
```
Research trending topic → Draft post → Generate image →
Post to platform → Send confirmation
```

### Content Idea Generation
```
Watch folder: /content/drop
When new files appear (PDFs, notes, transcripts),
scan them and group by topic.
Each morning, send me the top 3 content ideas
with titles and hooks based on the scanned content.
```

### Script Creation
```
Create a script for a video about [topic] based on
the latest trending news.
```

---

## Lead Management

### Lead Scanning
```
Scan my inbox every 30 minutes for new leads.
Extract: name, company, need, timeline, budget.
Add to Google Sheet.
Draft a personalized response.
Send me Telegram message with lead details.
I'll approve the response, it sends.
```

---

## Productivity

### Jarvis Daily Briefing
```
Generate a Jarvis briefing from my Obsidian vault.
Show me open to-dos, what I worked on recently,
recent memory captures, and the day's top 3 priorities.
Speak it in Jarvis voice.
```

### Goal Tracking
```
In Goal Mode, work toward this goal: [describe goal].
Break it into steps and report progress after each step.
```

### Image Generation
```
Using Nana Banana 2, create an image for [purpose].
Make it eye-catching and professional.
```

---

## Advanced

### Multi-Agent Profile Task
```
Use the [profile-name] profile to handle [task].
Use [model-name] for this task.
```

### MCP Server Mode
```
hermes mcp serve
```
Then connect Claude Desktop, Cursor, or VS Code to use Hermes as backend.

### OpenClaw Migration
```
hermes claw migrate --dry-run
```
Preview what would be migrated before committing.

---

## The 3-Step Automation Blueprint

1. **Where do you spend your time?** Identify the repetitive task.
2. **What's one thing you can automate this week?** Pick one.
3. **Ask Hermes:**
```
Based on what you know about me,
what could you help me automate day-to-day specifically for me?
```

Then: Define trigger → Give data sources → Test once → Schedule it.

---

## Tips for Better Prompts

1. **Give real tasks, not toy examples** during the first week
2. **Give feedback every time** — this is the self-improving loop
3. **String skills together** for compound automation power
4. **Be specific** about what you want and when
5. **Save winning prompts** as templates for reuse
6. **Back up skill.md files weekly** — don't lose your custom skills

---

## Related

- For the full capability reference: `hermes-agent-capabilities-general.md`
- For implementation steps: `hermes-quickstart.md`
- For the timeline: `hermes-launch-plan.md`
