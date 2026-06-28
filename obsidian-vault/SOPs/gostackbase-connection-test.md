# GoStackBase Connection Test Results

**Date:** 2026-06-28 20:57 UTC
**Platform:** GoStackBase (LeadConnector derivative)
**Dashboard URL:** https://app.gostackbase.com

## Test B: GoStackBase Connection — ✅ PASSED

### Login
- **Login URL:** https://app.gostackbase.com (NOT gostackbase.com/login — that 404s)
- **SSO System:** LeadConnector shared SSO (Puppeteer-based OTP auth)
- **Email:** dan.bk46@proton.me
- **2FA:** OTP sent to email — ✅ Code accepted
- **Login result:** ✅ Successful — redirected to dashboard

### Dashboard Access
- **Location ID:** huqxBD72T6Abd4AJxAni
- **Full sidebar navigation accessible:**
  - Dashboard, Conversations, Calendars, Contacts, Opportunities
  - Payments, AI Agents, Marketing, Automation, Sites
  - Memberships (Client Portal), Media Storage, Reputation
  - Reporting, App Marketplace
  - Settings (Company)
- **Dashboard widgets loaded:** Tasks, Manual Actions, Lead Sources, Google Analytics, Opportunity Value, Facebook Ads, Conversion Rate, Sales Efficiency, Funnel, Stage Distribution, Google Ads, Google Business Profile

### Key Discoveries
1. **GoStackBase shares LC SSO at app.gostackbase.com** — same auth system as GHL, uses OTP via email
2. **Location ID confirmed:** `huqxBD72T6Abd4AJxAni` — embedded in all dashboard URLs
3. **URL Pattern:** `/v2/location/{locationId}/{section}` — identical to GHL URL structure
4. **Feature parity with GHL:** Full CRM, automations, funnels, calendars, contacts, AI agents, client portals
5. **No public funnel share links** (confirmed — known limitation)

### Connection Details (Store Securely)
- **Dashboard URL:** https://app.gostackbase.com
- **Location ID:** huqxBD72T6Abd4AJxAni
- **Auth Method:** Email + Password + OTP (LC SSO)
- **API Base:** services.leadconnectorhq.com (shared LC infrastructure — same Private Integration system)
- **Needs for API access:** Private Integration API key (JWT) — must be generated in Settings → API / Integrations

## Next Steps
1. ✅ GoStackBase browser login confirmed
2. ⏳ Generate Private Integration API key for programmatic access (Settings → API)
3. ␳ Update Lead Connector Bridge skill with app.gostackbase.com login URL
4. ⏳ Proceed to Skool Post #6
