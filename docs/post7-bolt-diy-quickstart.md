# Quick DIY + Claude 3.7 Sonnet

> Converted from Julian Goldie Skool Post #7 — "Claude 3.7 Sonnet + Bolt DIY"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/71efa175?md=aaa6a9f332074ee38f5d8ec231ca6811

---

## What You're Building

A **free AI coding development environment** using:
- **Bolt DIY** — Open-source alternative to Bolt.new (local/full-stack)
- **Claude 3.7 Sonnet** — via OpenRouter API
- **Netlify** — Free hosting/deployment

**Time to build:** ~20 minutes
**Difficulty:** Intermediate
**Cost:** $0 (using free API tiers)

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js | v18+ installed on VPS or local machine |
| Git | For cloning the repo |
| OpenRouter account | For API keys (free tier available) |
| Netlify account | For free deployment |

---

## Step 1: Install Bolt DIY on VPS

```bash
# Clone the repository
git clone https://github.com/stackblitz-labs/bolt.diy.git
cd bolt.diy

# Install dependencies
npm install

# Install pnpm (recommended by the project)
npm install -g pnpm
```

> **VPS Note:** On your Hostinger VPS, you may need to increase swap space for npm install:
> ```bash
> fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
> ```

---

## Step 2: Configure Environment

```bash
# Copy the example env file
cp .env.example .env.local

# Edit the env file with your settings
nano .env.local
```

**Key environment variables:**
```bash
# OpenRouter API key (get from https://openrouter.ai/keys)
OPENROUTER_API_KEY=your_key_here

# Allow all providers (so you can use free models)
ALLOWED_PROVIDERS=*

# App URL
URL=http://localhost:5173
```

---

## Step 3: Connect to AI API (Claude 3.7 Sonnet)

1. Go to [OpenRouter.ai](https://openrouter.ai/) and sign up
2. Navigate to **Keys** → Create a new API key
3. Copy the key into your `.env.local` file
4. Inside Bolt DIY, go to the API selection dropdown
5. Select **Anthropic → Claude 3.7 Sonnet** under OpenRouter providers

**Claude 3.7 Sonnet Modes:**
| Mode | Use Case | Speed |
|------|----------|-------|
| **Thinking Mode** | Complex logic, architecture decisions | Slower, better quality |
| **Normal Mode** | Simple components, boilerplate | Faster |

---

## Step 4: Start Bolt DIY

```bash
# Run development server
npm run dev

# Or with pnpm (recommended)
pnpm dev
```

This generates a local address (typically `http://localhost:5173`). Open it in your browser.

---

## Step 5: Start Coding with AI

1. Open **Prompt Forge** inside Bolt DIY to generate optimized prompts
2. Enter your project idea (e.g., "Create a job board website")
3. Paste the generated prompt into Bolt DIY
4. Press Enter and let the AI start coding

> **Pro Tip:** Use the AI option in Bolt DIY to refine your prompts for better results.

---

## Step 6: Use Free AI APIs for Unlimited Usage

If you want to avoid paid APIs:
| Model | Provider | Cost |
|-------|----------|------|
| Google Flash 2.0 (Experimental) | Google | Free |
| Mistral AI | Mistral | Free tier |
| DeepSeek Light / DeepSeek Go | DeepSeek | Free tier |

---

## Step 7: Run Multiple Projects Simultaneously

- Open **multiple tabs** in Bolt DIY
- Run different AI models for different projects
- Switch between thinking mode and normal mode per tab

**Example workflow:**
- **Tab 1:** Build a Job Board Website
- **Tab 2:** Generate an Interactive SEO Audit Checklist

---

## Step 8: Deploy to Netlify (Free Hosting)

1. In Bolt DIY, go to **Code** section
2. Click **Download Code** (ZIP file)
3. Go to [Netlify.com](https://netlify.com) → **New Site** → **Import Existing Project**
4. Upload your unzipped project folder
5. Once deployed, you'll get a free test domain!

**Custom Domain:** Click **"Add Domain"** inside Netlify to purchase/connect a custom domain.

---

## Step 9: Track API Usage & Costs

- In Bolt DIY, go to **Activity** to check API usage
- Most projects cost just a few cents
- Use free APIs if you want to avoid any costs

---

## Bonus Features

- ✅ **Export & Save Projects** — Download code anytime
- ✅ **Connect to GitHub** — Auto-publish projects
- ✅ **Prompt Library** — Get optimized AI prompts for different tasks
- ✅ **Switch Between Models** — Use the best model for each project

---

## Example Prompts (Ready to Use)

### SEO Quiz Game
```
Create a fun SEO quiz game using HTML, CSS, and JavaScript. Users answer multiple-choice SEO-related questions, and the game keeps score. Include a timer for each question and display the correct answer after each attempt. Style it with an engaging UI and light animations.
```

### SEO Pricing Calculator
```
Develop a simple pricing calculator for SEO freelancers. Users enter project details (e.g., number of pages, keyword research, link building), and JavaScript calculates an estimated project cost based on predefined pricing logic. Use clean UI design with interactive sliders and checkboxes.
```

### Job Board Website
```
Create a job board website using HTML, CSS, and JavaScript where businesses can post SEO-related jobs, and freelancers can apply. The site should have job categories (e.g., Link Building, Technical SEO, Local SEO), a search filter, and an application form. Jobs should be stored in local storage or a JSON file for simplicity. Use a sleek, minimal design that aligns with Goldie Agency's branding (gold, black, and white color scheme).
```

### SEO Simulation Game
```
Develop a JavaScript-based simulation game where players start with a basic website and earn points by building backlinks, creating content, and optimizing on-page SEO. The game should include different backlink sources (guest posts, HARO, niche edits) with varying effects. Use CSS for engaging animations and a leaderboard tracking the best SEO players.
```

### SEO Audit Checklist
```
Develop an interactive SEO audit checklist where users check off completed tasks, such as optimizing title tags, fixing broken links, and improving page speed. The tool should save progress using local storage and feature a 'Download Report' button. Use HTML, CSS, and JavaScript for a clean, responsive design.
```

### SEO Title & Meta Generator
```
Build a lightweight, browser-based SEO title and meta description generator. Users enter their keyword, and the tool generates optimized titles and meta descriptions based on best practices. Add a 'Copy to Clipboard' button for easy use. Keep the design sleek, minimalist, and in Goldie Agency's signature colors. Orange ff7417 Darker cf5a00 Yellowish ffb40c
```

### SEO Assessment Quiz
```
Develop an SEO assessment quiz where users answer 10 questions, and at the end, they receive a personalized score (Beginner, Intermediate, SEO Pro). Offer a free SEO consultation for those who sign up. Use JavaScript for real-time scoring and CSS for a polished, professional look.
```

### SEO Case Studies Landing Page
```
Build an SEO case studies landing page where Goldie Agency showcases past client success stories. Use interactive elements (before/after ranking charts, testimonial sliders) and a CTA encouraging potential clients to book a free consultation. Design should be sleek, fast, and conversion-optimized.
```

---

## Related

- OpenRouter: https://openrouter.ai/
- Bolt DIY GitHub: https://github.com/stackblitz-labs/bolt.diy
- Netlify: https://netlify.com
- Prompt Forge GPT: https://chatgpt.com/g/g-67a822b07c708191a9f9d5e967c6dd5a-promptforge-ai
