# N8N MCP Agents — AI-Powered Workflows (Post #45)

> Converted from Julian Goldie Skool Post #45 — 31:31 video
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/37b1b0ba?md=e7fe95496c8f4a659f572b84446ece82

## Overview

Setting up N8N MCP agents to automate tasks using AI, connect with multiple services (Airbnb, Brave Search), and execute real-time web searches.

## 6-Step SOP

1. **Deploy N8N on Elestio** — Self-hosted, copy CNAME URL
2. **Configure MCP** — Install `n8n-nodes-mcp`, restart, set env var
3. **Create Workflow** — MCP Client → Add credentials (Airbnb/Brave)
4. **Execute Tools** — MCP Execute Tool node → Connect AI API key
5. **Brave Search** — Free API key → Real-time web searches
6. **Publish** — Activate workflow → Share public chatbot link

## MCP Servers

- Airbnb: `npx -y @openbnb-org/mcp-server-airbnb --ignore-robots-txt`
- Brave Search: `npx -y @modelcontextprotocol/server-brave-search`

## Key Tools

- N8N: https://elest.io
- MCP: https://modelcontextprotocol.io
- Brave Search: https://brave.com/search/api/
- Airbnb MCP: https://github.com/openbnb-org/mcp-server-airbnb

## Related

- [[sop-universal-lc-integration|SOP: Universal LC Integration]]
- [[post43-hermes-codex|Post #43: Hermes + Codex]]
