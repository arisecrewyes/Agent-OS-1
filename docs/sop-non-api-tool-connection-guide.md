# SOP: Non-API Tool Connection Guide for AI Agents

> **Created:** 2026-06-30
> **Status:** ✅ Complete
> **Purpose:** Universal guide for any AI agent (OpenClaw, Hermes, Claude Code, n8n, Agent OS) to connect to and operate non-API tools
> **Trigger:** "Connect to [tool]" / "Use [tool]" / "Generate content with [tool]"

---

## 1. WHAT ARE NON-API TOOLS?

Non-API tools are web-based platforms that:
- Have **no public REST API** for programmatic access
- Require **browser-based interaction** (login, click, type, generate)
- Store data in **cloud sessions** (not local files)
- May have **2FA, CAPTCHA, or session expiry**

### The 5 Tools in This Ecosystem

| # | Tool | URL | Purpose | Status |
|---|------|-----|---------|--------|
| 1 | Pyxa AI | https://v2.pyxa.ai | AI writing, images, video | ✅ Connected |
| 2 | VoiceWave AI | https://space.voicewave.ai | AI voiceovers, voice cloning | ✅ Connected |
| 3 | ArtSpace AI | https://space.artspace.ai | 282 AI image editing tools | ✅ Connected |
| 4 | Content 360 | https://app.content360.io | Social media management | ✅ Connected |
| 5 | Typeset | https://app.typeset.com | AI content creation, PDF/PPTX | ⏸️ Subscription paused |

---

## 2. CONNECTION METHODS (For AI Agents)

### Method 1: Browser Automation (Primary)
**For:** OpenClaw, Claude Code, any agent with browser access

```
1. Navigate to tool URL
2. Enter credentials (from secredential store)
3. Handle 2FA if required (prompt user for code)
4. Wait for dashboard to load
5. Interact with tool UI (click, type, select, generate)
6. Download/export results
7. Close tab or keep session alive
```

**OpenClaw Browser Tool Example:**
```
browser action=open url=https://v2.pyxa.ai/login
browser action=snapshot (see login form)
browser action=act kind=fill fields=[{ref, email}, {ref, password}]
browser action=act kind=click ref=signInButton
browser action=snapshot (see 2FA page)
browser action=act kind=type ref=2faField text=[USER_PROVIDED_CODE]
browser action=act kind=click ref=verifyButton
```

### Method 2: Session Persistence
**For:** Tools that stay logged in (lifetime licenses)

```
1. Log in once via browser automation
2. Keep tab alive (don't close)
3. Reuse tab for subsequent actions
4. If session expires, re-login with stored credentials
```

### Method 3: Webhook Bridge (Content 360 only)
**For:** n8n, Agent OS, any system that can receive webhooks

```
1. In Content 360 → Webhooks → Create Webhook
2. Set callback URL to your n8n webhook endpoint
3. Events will POST to your URL when triggered
4. Process in n8n → trigger other workflows
```

### Method 4: RSS Campaign Bridge (Content 360)
**For:** Automated content syndication

```
1. Create RSS feed with your content (blog, podcast, etc.)
2. In Content 360 → RSS Campaigns → Add feed URL
3. Content 360 auto-posts new RSS items to connected accounts
```

---

## 3. CREDENTIAL MANAGEMENT

### Storage Rules
1. **NEVER store credentials in plain text** — no .env files, no config files, no repos
2. **Use secredential storage** — OpenClaw's built-in secret manager
3. **Never log credentials** — no console.log, no debug output
4. **Never commit to git** — all credential files in .gitignore

### Retrieval Pattern
```
When user says "log into [tool]":
1. Check secredential store for [tool]_email, [tool]_password
2. If found → use them
3. If not found → ask user, then store as secredential
4. For 2FA → ask user each time (30s window)
```

---

## 4. TOOL-SPECIFIC CONNECTION SOPs

### 4.1 Pyxa AI Login SOP
```
URL: https://v2.pyxa.ai/login
Email: [SECREDENTIAL]
Password: [SECREDENTIAL]
2FA: ProtonMail TOTP (30s rotation) — ask user each time
Dashboard: https://v2.pyxa.ai/dashboard/user
Session: Persists across browser restarts
Special: Keep 2FA page open while user retrieves code
```

### 4.2 VoiceWave AI Login SOP
```
URL: https://space.voicewave.ai
Login: https://www.voicewave.ai/signin
Email: [SECREDENTIAL]
Password: [SECREDENTIAL]
2FA: None observed
Dashboard: https://space.voicewave.ai (auto-redirects when logged in)
Session: Persists (lifetime license)
```

### 4.3 ArtSpace AI Login SOP
```
URL: https://space.artspace.ai
Login: https://www.artspace.ai/signin
Email: [SECREDENTIAL]
Password: [SECREDENTIAL]
2FA: None observed
Dashboard: https://space.artspace.ai (auto-redirects when logged in)
Session: Persists (lifetime license)
```

### 4.4 Content 360 Login SOP
```
URL: https://app.content360.io/os/login
Email: [SECREDENTIAL]
Password: [SECREDENTIAL]
2FA: None observed
Workspace: /os/00b01979-8f24-4fd4-8600-4495bca7a813
Session: Persists
```

### 4.5 Typeset Login SOP (When Subscription Resumes)
```
URL: https://app.typeset.com/auth
Email: genius.scroll287@slmails.com
Password: [SECREDENTIAL]
Status: ⏸️ Subscription on pause — skip until resumed
```

---

## 5. CONTENT PIPELINE WORKFLOW

### Full Pipeline (All Tools)
```
Step 1: Pyxa AI Chat
  → Write script, article, or content plan
  → Export as document
  → Output: Text content

Step 2: ArtSpace AI
  → Generate/edit images for the content
  → Use appropriate tool from 282 options
  → Download final images
  → Output: Image files

Step 3: VoiceWave AI
  → Paste script into text editor
  → Select voice (Luna, Marcus, Oliver, or clone)
  → Generate speech
  → Export as WAV or MP3
  → Output: Audio file

Step 4: Content 360
  → Create new post
  → Upload image from Step 2
  → Add caption from Step 1
  → Schedule or publish
  → Output: Published social media post

Step 5: Webhook (Optional)
  → Content 360 webhook fires on publish
  → n8n receives webhook
  → Update analytics, notify team, log to sheet
```

### Partial Pipeline (Writing + Images Only)
```
Step 1: Pyxa AI → Write content
Step 2: ArtSpace AI → Generate images
Step 3: Manual posting or Content 360
```

### Partial Pipeline (Voice Only)
```
Step 1: Pyxa AI → Write script
Step 2: VoiceWave AI → Generate voiceover
Step 3: Use audio in video/podcast
```

---

## 6. AUTOMATION PATTERNS

### For OpenClaw (Browser Automation)
```
1. OpenClaw browser tool → navigate to tool
2. Login with stored credentials
3. Perform task (generate, edit, create)
4. Download result
5. Store result in workspace or forward to next tool
```

### For Hermes Agent (Browser Automation)
```
1. Hermes uses browser automation (same as OpenClaw)
2. Follow same login flow
3. Hermes can write content → pass to ArtSpace for images
4. Hermes can write scripts → pass to VoiceWave for audio
```

### For n8n (Webhook + API Bridge)
```
1. Content 360 webhooks → n8n webhook node
2. n8n receives event → processes in workflow
3. n8n can trigger OpenClaw agent for content generation
4. n8n can move files between tools (download → upload)
```

### For Claude Code (Browser Automation)
```
1. Claude Code uses browser tool (if available)
2. Same login and interaction patterns
3. Can script repetitive tasks (batch image generation, etc.)
```

---

## 7. TROUBLESHOOTING

### Session Expired
```
Symptom: Redirected to login page
Fix: Re-enter credentials from secredential store
Prevention: Keep tab alive, don't close browser
```

### 2FA Expired (Pyxa AI)
```
Symptom: "Invalid code" or back to login page
Fix: Ask user for fresh code, enter immediately
Prevention: Keep 2FA page open, enter code within 30s
```

### Rate Limited
```
Symptom: Tool slows down or shows error
Fix: Wait 60 seconds, retry
Prevention: Add delays between actions (2-5 seconds)
```

### Browser Tab Lost
```
Symptom: "Tab not found" error
Fix: Open new tab, re-login
Prevention: Use suggestedTargetId from open response
```

### Subscription Expired (Typeset)
```
Symptom: Pricing page instead of dashboard
Fix: Skip tool, use Pyxa AI as alternative
Prevention: Monitor subscription status
```

---

## 8. SECURITY CHECKLIST

- [ ] Credentials stored as secredentials only
- [ ] No plain text passwords in any file
- [ ] No credentials in git history
- [ ] 2FA codes never stored (ephemeral, 30s window)
- [ ] Browser sessions closed when not in use
- [ ] No credential sharing between agents
- [ ] Each agent uses its own session
- [ ] Logs never contain passwords or tokens

---

## 9. TOOL CAPABILITY QUICK REFERENCE

| Capability | Pyxa AI | VoiceWave | ArtSpace | Content 360 | Typeset |
|------------|---------|-----------|----------|-------------|---------|
| Write text | ✅ | — | — | — | ✅ |
| Generate images | ✅ | — | ✅ | — | ✅ |
| Edit images | — | — | ✅ (282 tools) | — | — |
| Generate video | ✅ | — | — | — | — |
| Voiceover | — | ✅ | — | — | — |
| Voice cloning | — | ✅ | — | — | — |
| Social posting | — | — | — | ✅ | — |
| Scheduling | — | — | — | ✅ | — |
| Webhooks | — | — | — | ✅ | — |
| PDF export | — | — | — | — | ✅ |
| PPTX export | — | — | — | — | ✅ |
| API access | ❌ | ❌ | ❌ | ❌ (webhooks only) | ❌ |
| Browser only | ✅ | ✅ | ✅ | ✅ | ✅ |
| Lifetime license | ✅ | ✅ | ✅ | ✅ | ⏸️ Paused |

---

## 10. RECOMMENDED AGENT ASSIGNMENTS

### OpenClaw (This Agent)
- **Primary:** All browser automation for all 5 tools
- **Role:** Orchestrator — logs in, generates, downloads, forwards
- **Strength:** Direct browser access, secredential storage

### Hermes Agent
- **Primary:** Content writing (Pyxa AI), script writing (VoiceWave)
- **Role:** Content creator — writes scripts, articles, plans
- **Strength:** AI agent specialization, can work independently

### n8n
- **Primary:** Webhook receiver (Content 360), workflow automation
- **Role:** Automation bridge — connects tools via webhooks and APIs
- **Strength:** Event-driven automation, scheduling, data routing

### Claude Code
- **Primary:** Batch operations, scripted workflows
- **Role:** Power user — scripts repetitive tasks across tools
- **Strength:** Code generation, automation scripting
