# GoStackBase Platform Capabilities — Agent Automation Matrix

**Generated:** 2026-06-28 21:15 UTC
**Location ID:** huqxBD72T6Abd4AJxAni
**Dashboard URL:** https://app.gostackbase.com
**Auth:** LC SSO (email + password + OTP)

---

## Platform Sections Tour

| Section | Sub-Sections | Status |
|---|---|---|
| Dashboard | Widgets (Tasks, Lead Sources, Analytics, Opp Value, Ads) | ✅ Accessible |
| Contacts | Smart Lists, Bulk Actions, Tasks, Companies, Custom Fields | ✅ Accessible |
| Conversations | Conversations, Manual Actions, Snippets, Trigger Links, Analytics, Settings | ✅ Accessible |
| Calendars | Calendar View, Appointment List, Calendar Settings | ✅ Accessible |
| Opportunities | List, Pipelines, Bulk Actions | ✅ Accessible |
| Payments | Invoices & Estimates, Documents & Contracts, Orders, Subscriptions, Payment Links, Transactions, Products, Coupons, Gift Cards, Settings, Integrations | ✅ Accessible |
| AI Agents | Getting Started, Voice AI, Conversation AI, Knowledge Base, Agent Templates, Content AI, Agent Logs | ✅ Accessible |
| Marketing | Social Planner | ✅ Accessible |
| Automation | Workflows, Global Workflow Settings | ✅ Accessible |
| Sites | Funnels, Websites, Stores, Webinars, Analytics, Blogs, WordPress, Client Portal, Forms, Surveys, Quizzes, Chat Widget, QR Codes, Domain Settings | ✅ Accessible |
| Memberships | Client Portal Dashboard | ✅ Accessible |
| Media Storage | File management | ✅ Accessible |
| Reputation | Overview | ✅ Accessible |
| Reporting | Reports | ✅ Accessible |
| App Marketplace | Integration | ✅ Accessible |
| Settings | Company | ✅ Accessible |

---

## Automation Capability Matrix

### 🤖 What I (OpenClaw Agent) CAN Automate via Browser

| Capability | Section | How |
|---|---|---|
| **Create funnels & landing pages** | Sites → Funnels | Click "New funnel" → select template → customize with builder → publish |
| **Edit existing funnels** | Sites → Funnels | Navigate to funnel → click step → drag/drop elements in builder |
| **Create forms** | Sites → Forms | Form builder → add fields → set actions |
| **Create surveys** | Sites → Surveys | Survey builder → add questions → configure |
| **Create quizzes** | Sites → Quizzes | Quiz builder → add questions → scoring |
| **Create chat widgets** | Sites → Chat Widget | Configure widget → embed code generation |
| **Create QR codes** | Sites → QR Codes | Generate → link to funnel/URL |
| **Create workflows/automations** | Automation → Workflows | Click "Create Workflow" → add triggers + actions |
| **Create contacts** | Contacts | Click "Add Contact" → fill fields |
| **Bulk import contacts** | Contacts → Bulk Actions | CSV upload → field mapping |
| **Send SMS/email** | Conversations | Select contact → compose → send |
| **Create calendar events** | Calendars | Click "New" → configure event |
| **Create invoices** | Payments | Click "New" → fill details → send |
| **Create payment links** | Payments | Configure product → generate link |
| **Configure AI Agents** | AI Agents | Voice AI, Conversation AI, Knowledge Base setup |
| **Upload files** | Media Storage | Upload images, documents, videos |
| **Create blog posts** | Sites → Blogs | Blog editor → publish |
| **Configure client portals** | Memberships | Portal setup → member management |
| **View reports & analytics** | Reporting | Dashboard data extraction |
| **Manage pipeline stages** | Opportunities | Create/edit stages, move opportunities |
| **Create coupons & gift cards** | Payments | Configure → distribute |
| **Domain settings** | Sites → Domain | Add custom domains, SSL |

### ⚡ What I Can Automate FASTER via API (needs Private Integration key)

| Capability | API Method | Speed vs Browser |
|---|---|---|
| CRUD contacts | `POST/GET/PUT/DELETE /contacts/` | 10-100x faster |
| Send messages | `POST /conversations/` | Instant |
| Trigger workflows | `POST /workflows/{id}/trigger` | Instant |
| Create opportunities | `POST /opportunities/` | Instant |
| List funnels & pages | `GET /funnels/` | Instant data |
| Calendar bookings | `POST /calendars/` | Instant |
| Webhook registration | `POST /webhooks/` | Programmatic |

### 🔒 What Only the USER Can Do

| Capability | Why |
|---|---|
| **Change account password** | Requires current password entry |
| **2FA verification** | OTP sent to user's email — I can only enter codes provided by user |
| **Connect payment processors (Stripe, etc.)** | Requires OAuth login to external service |
| **A2P 10DLC registration** | Requires business entity verification |
| **Phone number purchase** | Billing action |
| **Upgrade/downgrade plan** | Billing action |
| **Accept app marketplace terms** | Legal agreement |
| **Delete account** | Irreversible action |
| **Connect social media accounts** | Requires OAuth login to Facebook, Google, etc. |
| **Set up custom domain DNS** | Requires DNS provider access (external) |
| **Provide identity verification** | Requires government ID |

---

## Existing Account Inventory

### Funnels (23 total)
- Custom Song Lessons (0 funnels)
- SBA Music Lessons (5 funnels)
- Bountiful Anonymity - Opt-in Page (1 step)
- Bountiful Anonymity - eBook #1 (3 steps)
- Bountiful Anonymity - eBook #1 Copy (2 steps)
- Copy my AI Agency (0 steps)
- Digital Degens Tools Opt-in Template (3 steps)
- eBook Online Orders (3 steps)
- Funnel Import Test (0 steps)
- Life Coach (3 steps)
- + 13 more (page 2)

### Contacts
- 1 contact: Daniel B (DB)

### Payments
- 1 invoice: INV-000001 ($27.00, Draft status)

### Calendar
- 1 user: Daniel B
- GMT -05:00 timezone

### Installed App Marketplace Integrations
- AI Biz Card Scanner
- Docusign
- PhantomBuster
- V Card Tools
- Vapi for Workflows
- Apify
- Calendly
- Netlify
- Panda Doc
- EventBrite
- E-Signatures
- Instantly
- Age Verification

---

## Template Recreation Capability

Based on the platform tour, I can recreate GHL templates in GoStackBase by:

1. **Analyze the source GHL template** — extract structure, copy, form fields, images, colors
2. **Create a new funnel in GoStackBase** — Sites → Funnels → "New funnel"
3. **Use the funnel builder** — drag/drop elements to match the GHL layout:
   - Headline + subheadline text
   - Images/logos
   - Opt-in forms (name, email, phone)
   - CTA buttons
   - Video embeds
   - Background images/colors
4. **Configure form actions** — connect to calendar, trigger workflow, add tags
5. **Configure funnel steps** — opt-in page → thank you page → upsell
6. **Connect automation** — link to workflows for follow-up sequences

### Limitations
- ❌ Cannot import GHL funnel share links directly (GoStackBase has no share link import)
- ❌ Cannot bulk-export/import via API without Private Integration key
- ✅ Can recreate templates manually via browser automation (click by click)
- ✅ Can use existing accounts funnels as reference (e.g., Life Coach, Digital Degens)
