# 03 — GHL to BuildwithOS Conversion

> Convert GoHighLevel funnel templates to BuildwithOS equivalents.
> Source: Julian Goldie SEO — Skool Post #6
> Parent: [[Lead-Connector-Derivatives/00-index]]

---

## BuildwithOS Overview

BuildwithOS is the most AI-forward Lead Connector derivative. It offers:
- AI voice & chat agents
- Phone calls (Platinum plan)
- MCP support for external agents (Claude Code, Codex, OpenClaw)
- Highest affiliate payouts (up to 50% tier 1)
- Project-based ontology instead of traditional CRM
- Pre-built business kit templates

**Key Links:**
- BuildwithOS: https://buildwithos.com
- Docs: https://build-os.com/docs
- Agent Keys: https://build-os.com/docs/connect-agents
- Integrations: https://build-os.com/integrations

## Template Mapping

| GHL Template | BuildwithOS Equivalent | How |
|-------------|----------------------|-----|
| Book a Call | AI Agent + Google Calendar | AI agent books calls automatically |
| ChatGPT Opt-In | AI Chat Widget + Automation | Chat widget captures leads |
| Mastermind | AI Agent + Project | AI qualifies applicants |
| Course Tripwire | Pre-built Business Kit | Template-based setup |
| Free Book | AI Agent + Email | AI delivers resource |

## BuildwithOS MCP Integration

BuildwithOS speaks Model Context Protocol (MCP) at `/mcp/buildos`:
- **Local clients** (Claude Code, Codex): Auth via API key
- **Browser/cloud clients** (Claude.ai, ChatGPT): Auth via OAuth
- **OpenClaw connector:** In progress (same key will work once shipped)
- **Direct tools:** `list_onto_projects`, `list_onto_tasks`, `create_onto_task`, `update_onto_task`

## Feature Comparison

| Feature | GHL | BuildwithOS |
|---------|-----|-------------|
| AI Agents | AI Employee | Voice + Chat agents |
| Phone | ✅ | ✅ (Platinum) |
| MCP | ❌ | ✅ |
| REST API | V2 | ✅ |
| Affiliate Payout | Standard | **Highest (50%)** |
| Starting Price | $97/mo | $97/mo |

---

## Sub-Notes

- [[Lead-Connector-Derivatives/00-index]] — Back to index
- [[Lead-Connector-Derivatives/01 - Platform Comparison]] — Full comparison
- [[Lead-Connector-Derivatives/04 - Agent OS Integration Guide]] — OpenClaw + Hermes integration
