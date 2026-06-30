# QuickStart: N8N MCP Agents — AI-Powered Workflows

> Converted from Julian Goldie Skool Post #45 — "N8N MCP Agents"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/37b1b0ba?md=e7fe95496c8f4a659f572b84446ece82
> Duration: 31:31 video

---

## What You're Building

**N8N MCP Agents** — connecting N8N workflows to AI agents via Model Context Protocol for real-time web searches, property listings, and automated tasks.

---

## SOP: Setting Up N8N MCP Agents

### Step 1: Deploy N8N on Elestio (Self-Hosted)

1. Go to [Elest.io](https://elest.io) and log in
2. Navigate to **Services** → **Create New Service**
3. Choose **N8N** and select a location (e.g., Singapore)
4. Select **Medium** package (recommended)
5. Complete setup (no charge unless you upgrade)
6. Copy your **CNAME URL** (self-hosted N8N workspace)

---

### Step 2: Configure N8N for MCP Agents

1. Go to N8N **Settings** → **Community Nodes**
2. Install the MCP package:
   - Click **Install**
   - Enter: `n8n-nodes-mcp`
   - Click **Install** again
3. **Restart** N8N to apply changes
4. Set environment variable:
```
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE: true
```

---

### Step 3: Create Your AI Agent Workflow

1. Create a new workflow: **Create Workflow** → **Add Node** → **MCP Client**
2. Add MCP List Available Tools:
   - Add a credential for the MCP server (e.g., Airbnb, Brave Search)
   - **Command:** `npx`
   - **Arguments:** `-y @openbnb-org/mcp-server-airbnb --ignore-robots-txt`

---

### Step 4: Execute MCP Tools (Run AI Searches)

1. Add **MCP Execute Tool** node:
```
Tool Name: {{ $json.tools[0].name }}
Parameters: { "location": "Manchester" }
```
2. Connect to AI Agent:
   - Add ChatGPT/OpenAI API Key
   - Link to the MCP tool execution node

---

### Step 5: Brave Search for Real-Time Web Searches

1. Get a free API key at [Brave API](https://brave.com/search/api/)
2. In N8N, add Brave Search MCP node:
```
Command: npx
Arguments: -y @modelcontextprotocol/server-brave-search
Environment: BRAVE_API_KEY=YOUR_API_KEY
```
3. Test: `"Tell me about Gemini 3"` → AI fetches real-time results

---

### Step 6: Publish & Automate

1. **AI Agent Settings** → **Activate Workflow**
2. Share the public chatbot link or embed on your website

---

## MCP Server Examples

| MCP Server | Command | Use Case |
|-----------|---------|----------|
| Airbnb | `npx -y @openbnb-org/mcp-server-airbnb --ignore-robots-txt` | Property listings |
| Brave Search | `npx -y @modelcontextprotocol/server-brave-search` | Real-time web searches |

---

## Key Tools

| Tool | Purpose | URL |
|------|---------|-----|
| N8N | Workflow automation | https://elest.io |
| MCP | AI tool connection protocol | https://modelcontextprotocol.io |
| Brave Search API | Real-time web searches | https://brave.com/search/api/ |
| Elestio | Self-hosted N8N hosting | https://elest.io |
| Airbnb MCP | Property search | https://github.com/openbnb-org/mcp-server-airbnb |

---

## Example AI Queries

```
"Find me a 2-bedroom apartment in Manchester"
"Show me the best Airbnbs for New Year's Eve"
"Search the web for the latest news on Gemini 3"
```

---

## Related

- [[sop-universal-lc-integration|SOP: Universal LC Integration]]
- [[post43-hermes-codex-quickstart|Post #43: Hermes + Codex]]
- [[Agent-OS-Ecosystem|Ecosystem: N8N + MCP]]
