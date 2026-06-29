# QuickStart: Hermes + Qwen 3.7 Max — Infinite Context Engine

> Converted from Julian Goldie Skool Post #11 — "27th May: Hermes + Qwen 3.7 Max"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=efa884e824d041f5bb2b7d6fef764aaa

---

## What You're Building

The **Infinite Context Engine** — a 3-part system:
1. **Brain:** Qwen 3.7 Max (1M token context, 35-hour autonomous runs)
2. **Agent:** Hermes Agent (free, open-source, Goal Mode with 50 turns)
3. **Memory:** Obsidian Vault via MCP (your notes feed the agent)

Combined: an AI that knows your business, works autonomously for hours, and gets smarter every day.

---

## Why Qwen 3.7 Max?

| Spec | Detail |
|------|--------|
| Built by | Alibaba's AI team |
| Context window | 1 million tokens |
| Best for | Long-horizon agentic tasks |
| Autonomous run | 35 hours (kernel optimization benchmark) |
| Performance | Beats Opus 4.6 on Terminal Bench, MCP tool use, long-context recall |
| Cost | Free tier available on OpenRouter |
| Rank | #1 app using Qwen on OpenRouter = Hermes Agent |

---

## Quick Setup (10 minutes)

### Step 1: Install Hermes Agent# Clone and install
git clone https://github.com/crawlab-team/hermes
cd hermes
# Follow install instructions in README

# Verify installation
hermes --help
```

### Step 2: Get OpenRouter API Key
1. Go to [openrouter.ai](https://openrouter.ai)
2. Create free account
3. Navigate to **Keys** → Create API key
4. Copy the key

### Step 3: Connect Qwen 3.7 Max to Hermes
```bash
# Update Hermes
hermes update

# In Hermes:
# Settings → Model → OpenRouter → Qwen 3.7 Max
# Paste your OpenRouter API key
```

### Step 4: Install Obsidian
1. Go to [obsidian.md](https://obsidian.md)
2. Download (free)
3. Create vault called "My Second Brain"

### Step 5: Connect Obsidian to Hermes via MCP
```bash
# Install Obsidian MCP bridge
git clone https://github.com/calclavia/mcp-obsidian
cd mcp-obsidian
# Follow setup guide
```

---

## 30-Day Plan

### Week 1: Foundation (Set Up Your Brain)

| Day | Task |
|-----|------|
| 1 | Install Hermes Agent |
| 2 | Get OpenRouter API key |
| 3 | Plug in Qwen 3.7 Max |
| 4 | Install Obsidian + create vault |
| 5 | Write first 10 notes (business, customers, problems, tools, bottlenecks) |
| 6 | Connect Obsidian to Hermes via MCP |
| 7 | Run first Infinite Context test |

### Week 2: Automate (First Autonomous Workflows)

| Day | Task |
|-----|------|
| 8 | Discover Goal Mode (`/goal`) — set a goal, walk away, 50 turns |
| 9 | Build visual dashboard (neon HTML) |
| 10 | Automate morning brief (trends + content ideas + task list) |
| 11 | Build knowledge map of your business |
| 12 | Automate content research (Google Trends cross-ref with notes) |
| 13 | 35-minute autonomous run (blog outline) |
| 14 | Review Week 2 results |

### Week 3: Scale (Business Applications)

| Day | Task |
|-----|------|
| 15 | SEO content machine (full blog structure for target keyword) |
| 16 | Lead gen content brief system (reusable template) |
| 17 | Visual AI automation showcase (diagram of your stack) |
| 18 | Client onboarding document template |
| 19 | Personal SOPs library (document manual tasks for AI) |
| 20 | Connect second MCP tool (GitHub, Google Drive, Notion, Brave) |
| 21 | Weekend Goal Mode task (build full SEO site overnight) |

### Week 4: Systematise (Run Without You)

| Day | Task |
|-----|------|
| 22 | Audit automation stack (find remaining manual tasks) |
| 23 | Document your Infinite Context Engine SOP |
| 24 | Weekly agent review system (what worked, what failed) |
| 25 | Neon visual automation report dashboard |
| 26 | Share a win in the community |
| 27 | Add new niche knowledge base |
| 28 | Competitor research automator (via Brave Search MCP) |
| 29 | Full 3-hour autonomous build (content calendar + SEO outlines) |
| 30 | Review and systematise |

---

## Key Hermes Commands

| Command | What It Does |
|---------|-------------|
| `/help` | List all available commands |
| `/goal` | Set an autonomous goal (50 turns to complete) |
| `hermes update` | Update to latest version |
| `hermes model` | Switch AI model |

---

## Key Frameworks

### Goal Mode
```
Type /goal → Set target → Walk away
→ Agent gets 50 autonomous turns
→ Returns completed work
```

### MCP Connections
Obsidian MCP bridges your notes to the agent:
- Agent **reads** your notes for context
- Agent **writes** new notes back to vault
- Creates a **feedback loop** — smarter every day

### The Infinite Context Loop
```
Qwen 3.7 Max (brain) → Hermes Agent (worker) → Obsidian Vault (memory)
     ↑_________________________________________________↓
                    (feedback loop)
```

---

## Example Prompts

### First Test
```
Read my Obsidian vault and give me a summary of everything you now know about my business.
```

### Goal Mode
```
Research the top 10 AI automation tools for solopreneurs in 2025,
summarise each in 3 bullet points, and save to Obsidian as AI Tool Research.
```

### SEO Content Machine
```
Create a complete SEO blog post structure for the keyword 'AI automation for small business'.
Include: title tag, meta description, H1, 5 H2 subheadings, 300-word intro,
3 FAQs, conclusion with CTA. Ready to copy into WordPress. Save to Obsidian.
```

### Automated Research
```
Go to Google Trends and find the top 5 trending topics in AI automation.
Cross-reference with my Obsidian notes on content.
Give me 10 YouTube video ideas ranked by potential interest. Save to Obsidian.
```

---

## VPS Deployment

```yaml
# docker-compose for Hermes + Obsidian MCP
services:
  hermes:
    image: crawlab/hermes:latest
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - MODEL=openrouter/qwen/qwen3.7-max
    volumes:
      - ./obsidian-vault:/vault
    restart: unless-stopped
```

---

## Related

- [[post10-hermes-obsidian-quickstart|Post #10: Hermes + Obsidian Second Brain]]
- [[Agent-OS-Ecosystem|Ecosystem: Hermes Agent]]
- [[SOP - Infinite Memory Setup]]
- GitHub: https://github.com/crawlab-team/hermes
- Obsidian MCP: https://github.com/calclavia/mcp-obsidian
- OpenRouter: https://openrouter.ai
