# Capability Reference: Bolt.DIY + AI Coding APIs

> Extracted from Skool Post #8 — Technical reference

---

## Bolt.DIY Specifications

| Spec | Detail |
|---|---|
| License | Open-source (free) |
| Based on | Next.js |
| Requirements | Node.js v18+, Docker |
| Hosting | Local, VPS (Docker), GitHub → any host |
| Chat history | 30 days |
| Code export | ZIP download, GitHub push |

---

## Supported AI APIs

### Free Tier APIs

| API | Provider | Models | Best For | Setup |
|-----|----------|--------|----------|-------|
| Flash 2.0 | Google | gemini-2.0-flash-exp | General coding, speed | aistudio.google.com |
| Gemini Exp | Google | gemini-experimental-1206 | Latest capabilities | aistudio.google.com |
| Mistral AI | Mistral | mistral-light | Coding, reasoning | openrouter.ai |
| DeepSeek Light | DeepSeek | deepseek-r1-light | Lightweight coding | openrouter.ai |
|  |  |  |  |  |

### Paid APIs (Recommended for Quality)

| API | Provider | Models | Best For | Cost |
|-----|----------|--------|----------|------|
| Anthropic | Claude | claude-3.5-sonnet | Best coding, design polish | ~$3/1M tokens |
| OpenAI | GPT | gpt-4o | General purpose | ~$5/1M tokens |
| Google (paid) | Gemini | gemini-pro | Complex reasoning | ~$2.50/1M tokens |
| Perplexity | Online | llama-3.1-sonar | Internet-connected tools | ~$2/1M tokens |

---

## API Selection Strategy (from Video)

**Step 1: Build** → Use free Google Gemini 2.0 Flash
- Fast, free, good enough for initial build

**Step 2: Polish** → Switch to Anthropic Claude 3.5 Sonnet
- Better design sense
- Cleaner code output
- Worth the small cost for final touches

**Step 3: Research** → Use Perplexity (online access)
- For tools that need internet data
- Real-time information integration

---

## Project Types & Best API Pairing

| Project Type | Best API | Why |
|---|---|---|
| Landing page | Gemini Flash (free) → Claude (polish) | Speed + design quality |
| Calculator/tool | Gemini Flash | Simple logic, free is fine |
| Multi-page website | Claude 3.5 Sonnet | Architecture understanding |
| SEO blog | Gemini + Claude | Content + formatting |
| Game | Gemini Flash | Fast iteration |
| Affiliate site | Claude | Design + conversion focus |
| App (PWA) | Claude 3.5 Sonnet | Complex logic |

---

## Performance Metrics (from Video)

### AI-Coded vs WordPress

| Metric | Bolt.DIY (AI) | WordPress |
|--------|--------------|-----------|
| PageSpeed | 99% | Variable |
| Accessibility | 99% | Depends on theme |
| Best Practices | 100% | Plugin-dependent |
| Core Web Vitals | ✅ Pass | ❌ Often fail |
| Code cleanliness | ✅ Minimal | ❌ Bloated |

### SEO Impact

AI-coded sites:
- Faster load times = better rankings
- Clean HTML = easier for Google to crawl
- No plugin conflicts = stable performance

---

## Bolt.DIY Workflow Patterns

### Pattern 1: Quick Build
```
1. Open Bolt.DIY
2. Select Gemini Flash (free)
3. Prompt: "Build me [project]"
4. Download ZIP
5. Deploy to Netlify
Time: 5-10 minutes
```

### Pattern 2: Iterative Build
```
1. Start with Gemini Flash (free)
2. Build basic structure
3. Switch to Claude (paid)
4. Prompt: "Make the design more beautiful"
5. Iterate until satisfied
Time: 15-60 minutes
```

### Pattern 3: Design Emulation
```
1. Find a design you like
2. Take screenshot
3. Upload to Bolt.DIY
4. Prompt: "Follow the same design style"
5. Customize for your niche
Time: 10-20 minutes
```

### Pattern 4: Multi-API Rotation
```
Tab 1: Gemini Flash → Build main structure
Tab 2: DeepSeek → Build secondary features
Tab 3: Anthropic → Polish final design
Time: Parallel = fastest results
