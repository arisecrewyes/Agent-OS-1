# QuickStart: Bolt.DIY — Build Anything for Free

> Converted from Julian Goldie Skool Post #8 — "NEW Bolt DIY is INSANE (FREE)!"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/607e02e8?md=e42238d31aba48d5b35720885f9363b5
> YouTube: https://www.youtube.com/watch?v=B_MikzCqS2c (13:52)

---

## What You're Building

**Bolt.DIY** — A free, open-source AI coding tool that lets you build:
- Web apps
- Landing pages
- Calculators
- SEO tools
- Games
- Full websites (rankable on Google)

**Cost:** $0 (free APIs available)
**Time to set up:** ~10 minutes
**Difficulty:** Intermediate

---

## Prerequisites

| Requirement | Install |
|---|---|
| Docker | `curl -fsSL https://get.docker.com \| sh` |
| Node.js v18+ | `brew install node` or `nvm install 18` |
| Git | Usually pre-installed |

---

## Step 1: Clone & Install Bolt.DIY

```bash
# Clone the repo
git clone https://github.com/stackblitz-labs/bolt.diy.git
cd bolt.diy

# Install dependencies
npm install
# OR (recommended)
pnpm install
```

> **VPS Tip:** If npm install fails due to memory, add swap:
> ```bash
> fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
> ```

---

## Step 2: Run Bolt.DIY Locally

```bash
# Start the development server
npm run dev
# OR
pnpm dev
```

The terminal will output a localhost URL (e.g., `http://localhost:5173`). Open it in your browser.

---

## Step 3: Get a Free API Key

### Option A: Google AI Studio (Recommended — Free)
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in with Google
3. Click **"Get API Key"** → Create new key
4. Copy the key

**Free models available:**
- Gemini 2.0 Flash (latest)
- Gemini Experimental 1206

### Option B: OpenRouter (Multi-model)
1. Go to [openrouter.ai](https://openrouter.ai)
2. Sign up → Keys → Create
3. Copy the key

**Free models via OpenRouter:**
- Google Flash 2.0
- Mistral AI
- DeepSeek Light / DeepSeek Go

### Option C: Anthropic (Paid, best for coding)
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Create API key
3. Use for final polish/design improvements

---

## Step 4: Connect API to Bolt.DIY

1. Inside Bolt.DIY, click the **API dropdown** (top of the chat)
2. Select your provider (e.g., Google, OpenRouter, Anthropic)
3. Paste your API key
4. Select the model (e.g., Gemini 2.0 Flash)
5. Start building!

---

## Step 5: Build Your First Project

Type a prompt in the chat:
```
Build me a magical keyboard app
```

Bolt.DIY will:
1. Generate the code (HTML, CSS, JS, React, etc.)
2. Show a live preview on the right
3. Let you iterate with follow-up prompts

**Example workflow:**
```
Prompt: "Create a job board website"
→ Bolt builds it
Prompt: "Make the buttons bright orange and add rainbow animations"
→ Bolt updates the existing project
```

---

## Step 6: Deploy Your Project

### Option A: Netlify (Free)
1. In Bolt.DIY, go to **Code** → **Download Code** (ZIP)
2. Go to [Netlify.com](https://netlify.com) → **New Site** → **Import Existing Project**
3. Upload the unzipped folder
4. Get a free `*.netlify.app` domain

### Option B: GitHub + Hosting
1. In Bolt.DIY, click **Push to GitHub**
2. Connect your GitHub account
3. Link the repo to any hosting provider (Netlify, Vercel, etc.)

### Option C: Custom Domain
1. In Netlify, click **"Add Domain"**
2. Purchase or connect your domain
3. Done!

---

## Pro Tips from the Video

### 1. Switch APIs Mid-Project
- Start with **free Google API** for initial build
- Switch to **Anthropic (Claude)** for design polish
- Each API has different strengths

### 2. Emulate Any Design
1. Take a screenshot of a website you like
2. Upload it to Bolt.DIY chat
3. Prompt: *"Follow the same design style as this screenshot"*
4. Bolt emulates the style for your project

### 3. Build Multiple Projects at Once
- Open Bolt.DIY in **multiple browser tabs**
- Each tab = separate project with its own chat history
- Run different APIs per tab

### 4. SEO Advantage
- Bolt.DIY generates **clean code** (no WordPress bloat)
- PageSpeed scores of **99%** vs WordPress failing Core Web Vitals
- Faster sites = better Google rankings

### 5. Iterate on Previous Projects
- Bolt.DIY stores **30 days of chat history**
- Go back to any previous project
- Prompt changes: *"Make this yellow"*, *"Add animations"*
- Bolt updates the existing project in place

---

## Bolt.DIY vs Bolt.new (Paid)

| Feature | Bolt.DIY (Free) | Bolt.New (Paid) |
|---------|-----------------|-----------------|
| Cost | Free | Paid (tokens) |
| API Selection | ✅ Full control | ❌ Limited |
| Local hosting | ✅ Yes | ❌ Cloud only |
| Upload links for AI prompts | ✅ Yes | ❌ No |
| Voice commands | ❌ No | ✅ Yes |
| Export chat | ❌ No | ✅ Yes |
| Attachments | ❌ No | ✅ Yes |

> **Key insight:** Bolt.DIY gives you MORE control over APIs and local hosting. Bolt.new has voice/attachments but locks you into their API selection.

---

## Example Prompts (Copy-Paste Ready)

### Magical Keyboard App
```
Build me a magical keyboard app
```

### Dad Jokes Keyboard
```
Create a dad jokes keyboard app that displays a random joke when you press each key. Make it fun and colorful.
```

### Affiliate SEO Blog
```
Create an affiliate SEO blog about bird watching. My name is Julian Goldie. Here's my Amazon affiliate ID. Build out the blog with multiple posts and affiliate links.
```

### SEO Cost Calculator
```
Build an SEO pricing calculator where users enter project details (number of pages, keyword research, link building) and get an estimated cost. Multiple pages, clean design.
```

### Design Emulation
```
[Upload screenshot of a website you like]
Follow the same design style as this screenshot but customize it for a [your niche] website.
```

---

## VPS Deployment (Docker)

```bash
# Run Bolt.DIY in Docker on your VPS
cd bolt.diy
docker compose up -d

# Access at http://localhost:5173
# Or set up Traefik reverse proxy for domain access
```

---

## Key Links

- GitHub: https://github.com/stackblitz-labs/bolt.diy
- Google AI Studio (free API): https://aistudio.google.com
- OpenRouter: https://openrouter.ai
- Netlify (free hosting): https://netlify.com
- Free SEO course (200+ lessons): https://www.skool.com/ai-profit-lab-7462
