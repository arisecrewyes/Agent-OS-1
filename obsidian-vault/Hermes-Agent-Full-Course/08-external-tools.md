# Hermes Agent — External Tools

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Firecrawl (Web Browsing & Research)

- Get an API key from [firecrawl.dev/app](https://firecrawl.dev/app)
- Give the key to Hermes and tell it to set up the Firecrawl skill
- Enables: web search, page crawling, real-time information extraction
- **Use case:** Reddit monitoring, trending news, competitor analysis

## Browser Base (Visual Web Browsing)

- Gives the agent a **proper browser with vision**
- Can see pages, interact with them
- You can even **watch recordings** of what it did
- **Use case:** Visual verification, complex web interactions

## Nana Banana 2 (Image Generation)

- Connect this API so Hermes can generate images
- **Use case:** Social media post images, thumbnails, featured images
- Example: Create a tweet with an AI-generated image about trending AI news

## X/Twitter Developer API

- Go to [developer.x.com](https://developer.x.com)
- Set up a developer account
- Create an app
- Give Hermes the API credentials
- Hermes can then **post directly to X** on your behalf

## MCP (Model Context Protocol)

Hermes supports MCP in two ways:

### As MCP Client
Connect Hermes to any external tool or service that has an MCP server.

### As MCP Server
```bash
hermes mcp serve
```
This makes Hermes itself an **MCP server** that other tools (Claude Desktop, Cursor, VS Code) can connect to as a backend brain.

## The Compound Effect

String multiple skills together for exponential power:

```
Skill 1: Research with Firecrawl
    + Skill 2: Post to X
    + Skill 3: Generate image with Nana Banana 2
    = Full automated content pipeline
```

The more skills you combine, the more powerful the automation becomes.

---

## Metadata

- Tags: `hermes`, `external-tools`, `firecrawl`, `browser-base`, `mcp`, `nana-banana`
- Related: [[07 - Scheduled Tasks]] | [[13 - Automation Blueprint]]
