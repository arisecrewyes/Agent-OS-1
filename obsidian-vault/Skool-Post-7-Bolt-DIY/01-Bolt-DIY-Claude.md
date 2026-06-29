# Bolt DIY + Claude 3.7 Sonnet (Post #7)

> Converted from Julian Goldie Skool Post #7
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/71efa175?md=aaa6a9f332074ee38f5d8ec231ca6811

## Overview

Free AI coding environment using Bolt DIY (open-source Bolt.new alternative) + Claude 3.7 Sonnet via OpenRouter. Includes prompt library with 8 example prompts.

## Key Links

- Bolt DIY GitHub: https://github.com/stackblitz-labs/bolt.diy
- OpenRouter: https://openrouter.ai/
- Netlify (free hosting): https://netlify.com
- Prompt Forge GPT: https://chatgpt.com/g/g-67a822b07c708191a9f9d5e967c6dd5a-promptforge-ai

## Setup Commands

```bash
git clone https://github.com/stackblitz-labs/bolt.diy.git
cd bolt.diy
npm install
cp .env.example .env.local
# Add OPENROUTER_API_KEY to .env.local
npm run dev
```

## Free AI Models (no cost tier)

- Google Flash 2.0 (Experimental)
- Mistral AI
- DeepSeek Light / DeepSeek Go

## Claude 3.7 Sonnet Modes

- **Thinking Mode** — Complex logic, architecture decisions (slower, better)
- **Normal Mode** — Simple components, boilerplate (faster)

## VPS Deployment Notes

- May need 2GB swap for npm install on smaller VPS
- Run behind Traefik reverse proxy for production
- Deploy static exports to Netlify (free) or VPS nginx

## Prompt Library Categories

1. **Web Apps** — Job board, pricing calculator, title/meta generator
2. **Games** — SEO quiz, SEO simulation game
3. **Tools** — Audit checklist, assessment quiz
4. **Landing Pages** — Case studies with interactive elements

See: [[post7-bolt-diy-prompts|Full Prompt Library]]

## Related

- [[01-Client-Onboarding-Automation|Post #6: Client Onboarding]]
- [[Agent-OS-Ecosystem|Ecosystem: Bolt DIY Integration]]
- [[SOP - Universal LC Integration]]
