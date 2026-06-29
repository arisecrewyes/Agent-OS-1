# Bolt.DIY Full Course (Post #8)

> Converted from Julian Goldie Skool Post #8 — 13:52 video
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/607e02e8?md=e42238d31aba48d5b35720885f9363b5
> YouTube: https://www.youtube.com/watch?v=B_MikzCqS2c

## Video Chapters

1. **Introduction** (0:00) — Build anything for free with Bolt.DIY
2. **Setup** (0:33) — Docker + Node.js + clone repo + terminal commands
3. **APIs** (1:37) — Connect free/paid AI APIs (Google, OpenRouter, Anthropic)
4. **First Project** (2:41) — Build a magical keyboard app in seconds
5. **Advanced** (3:22) — Full screen, download code, switch APIs
6. **Hosting** (3:47) — Push to GitHub → Netlify
7. **Examples** (4:19) — Real websites ranking on Google
8. **SEO** (9:22) — AI-coded sites get 99% PageSpeed vs WordPress failing
9. **Design** (10:35) — Screenshot emulation technique
10. **Conclusion** (12:19) — Free course link, strategy session

## Key Takeaways

- Bolt.DIY is **free and open-source** (vs Bolt.new paid)
- **More control** over APIs than Bolt.new
- Can build: apps, tools, calculators, websites, games
- **Free APIs:** Google Gemini 2.0 Flash, Mistral, DeepSeek
- **Paid APIs:** Anthropic (best for coding), Perplexity (online access)
- **Deploy:** GitHub → Netlify (free hosting)
- **SEO advantage:** 99% PageSpeed, clean code, fast rankings
- **Design emulation:** Screenshot → Bolt.DIY → "follow this style"
- **30-day chat history** for iterating on previous projects

## Setup Commands

```bash
git clone https://github.com/stackblitz-labs/bolt.diy.git
cd bolt.diy
npm install
npm run dev
# Open localhost URL from terminal
```

## Free API Setup

1. Google AI Studio: https://aistudio.google.com → Get API Key
2. OpenRouter: https://openrouter.ai → Keys → Create
3. Paste into Bolt.DIY API dropdown

## VPS Notes

- Docker recommended for VPS deployment
- May need 2GB swap for npm install
- Traefik reverse proxy for domain access
- See: [[Agent-OS-Ecosystem|Ecosystem: Bolt.DIY Integration]]

## Related

- [[01-Client-Onboarding-Automation|Post #6: Client Onboarding]]
- [[01-Bolt-DIY-Claude|Post #7: Claude 3.7 + Bolt DIY]]
- [[Agent-OS-Ecosystem|Ecosystem: AI Coding Tools]]
