# Template Mapping — Cross-Platform Equivalence

> Maps each GHL funnel template to its equivalent in GoStackBase and BuildwithOS.
> Source: Julian Goldie SEO — Skool Post #6 + platform research

---

## Book a Call

| Element | GoHighLevel | GoStackBase | BuildwithOS |
|---------|-------------|-------------|-------------|
| **Opt-in Page** | Funnel step (GHL builder) | Landing Page + Smart Form | Project with form task |
| **Booking** | GHL Calendar widget | Smart Calendar | Google Calendar sync |
| **Confirmation** | Funnel step + email | Thank You page + email | Task completion + notification |
| **Automation** | GHL Workflow | Revenue Automation | BuildOS automation |
| **API Endpoint** | `POST /calendars/` | N/A (dashboard) | `create_onto_task` |

**GoStackBase Build Steps:**
1. Create Landing Page → Add Smart Form (name, email, phone)
2. Connect Smart Calendar for booking
3. Create Thank You page
4. Set automation: form submit → book appointment → send confirmation

**BuildwithOS Build Steps:**
1. Create Project: "Book a Call Funnel"
2. Create Form Task: "Collect lead info"
3. Create Calendar Task: "Schedule appointment"
4. Create Notification Task: "Send confirmation"

---

## ChatGPT Opt-In (Lead Magnet)

| Element | GoHighLevel | GoStackBase | BuildwithOS |
|---------|-------------|-------------|-------------|
| **Opt-in Page** | Funnel step | Landing Page + Smart Form | Project with form task |
| **Delivery** | Email with download link | Email automation | Email automation |
| **Thank You** | Funnel step | Thank You page | Task completion |
| **Automation** | GHL Workflow | Revenue Automation | BuildOS automation |
| **API Endpoint** | `POST /contacts/` + Workflow | N/A (dashboard) | `create_onto_task` |

**GoStackBase Build Steps:**
1. Create Landing Page → Add Smart Form (name, email)
2. Set automation: form submit → send email with resource link
3. Create Thank You page
4. Set up nurture sequence in Email Marketing

**BuildwithOS Build Steps:**
1. Create Project: "Lead Magnet: [Resource Name]"
2. Create Form Task: "Collect email"
3. Create Automation Task: "Deliver resource via email"
4. Create Task: "Add to nurture sequence"

---

## Mastermind Application

| Element | GoHighLevel | GoStackBase | BuildwithOS |
|---------|-------------|-------------|-------------|
| **Application** | Multi-step funnel step | Multi-step Smart Form | Project with form tasks |
| **Booking** | GHL Calendar | Smart Calendar | Google Calendar |
| **Payment** | GHL Order Form | Checkout (Premium+) | N/A (no payments) |
| **Welcome** | Funnel step + email | Welcome page + email | Task + notification |
| **Automation** | GHL Workflow | Revenue Automation | BuildOS automation |

**GoStackBase Build Steps:**
1. Create Landing Page → Multi-step Smart Form (qualification questions)
2. Connect Smart Calendar for interview booking
3. Set up Checkout page (Premium+ plan required)
4. Create Welcome page
5. Set up automation: application → qualification → booking → payment → welcome

**BuildwithOS Build Steps:**
1. Create Project: "Mastermind Application"
2. Create Form Tasks: "Step 1: Basic Info", "Step 2: Qualification", "Step 3: Goals"
3. Create Calendar Task: "Schedule interview"
4. Create Automation: "Send welcome on approval"

---

## Course Tripwire

| Element | GoHighLevel | GoStackBase | BuildwithOS |
|---------|-------------|-------------|-------------|
| **Sales Page** | Funnel step (long-form) | Landing Page | Project page |
| **Checkout** | GHL Order Form | Checkout (Premium+) | N/A (no checkout) |
| **Upsell** | Funnel step (OTO) | Upsell page | N/A (no OTO) |
| **Thank You** | Funnel step + email | Thank You page + email | Task + notification |
| **Automation** | GHL Workflow | Revenue Automation | BuildOS automation |

**GoStackBase Build Steps:**
1. Create Sales Page (long-form with testimonials, guarantee)
2. Set up Checkout page (Premium+ required)
3. Configure Upsell page (premium offer)
4. Create Thank You page
5. Set automation: purchase → deliver → upsell → thank you

**BuildwithOS Build Steps:**
1. Create Project: "Course Tripwire: [Course Name]"
2. Create Page Task: "Write sales copy"
3. Create Task: "Set up course delivery"
4. Create Automation: "Deliver on enrollment"

---

## Free Book (Lead Magnet)

| Element | GoHighLevel | GoStackBase | BuildwithOS |
|---------|-------------|-------------|-------------|
| **Opt-in Page** | Funnel step | Landing Page + Smart Form | Project with form task |
| **Download** | Email with download link | Email automation | Email automation |
| **Thank You** | Funnel step | Thank You page | Task completion |
| **Automation** | GHL Workflow | Revenue Automation | BuildOS automation |
| **API Endpoint** | `POST /contacts/` + Workflow | N/A (dashboard) | `create_onto_task` |

**GoStackBase Build Steps:**
1. Create Landing Page with book cover/description
2. Add Smart Form (name + email)
3. Set automation: form submit → send email with download link
4. Create Thank You page
5. Set up nurture sequence

**BuildwithOS Build Steps:**
1. Create Project: "Free Book: [Book Title]"
2. Create Form Task: "Collect email"
3. Create Automation Task: "Deliver book via email"
4. Create Task: "Add to nurture sequence"

---

## Feature Parity Matrix

| Feature | GHL | GoStackBase | BuildwithOS |
|---------|-----|-------------|-------------|
| Landing Pages | ✅ | ✅ | ✅ (Project pages) |
| Multi-step Forms | ✅ | ✅ | ✅ |
| Smart Calendar | ✅ | ✅ | ✅ (Google sync) |
| Email Automation | ✅ | ✅ | ✅ |
| SMS Automation | ✅ | ✅ | ✅ |
| Payment Collection | ✅ | ✅ (Premium+) | ❌ |
| Upsell/OTO | ✅ | ✅ (Premium+) | ❌ |
| Course/LMS | ✅ | ✅ (Digital Products) | ✅ |
| Client Portal | ❌ | ✅ **Key diff** | ❌ |
| AI Agents | ✅ | ❌ | ✅ **Key diff** |
| Funnel Share Links | ✅ | ❌ | ❌ |
| Project Management | ❌ | ❌ | ✅ **Key diff** |
| White-Label | ✅ (higher plans) | ✅ (Elite) | ✅ (Partner+) |

---

## Key Limitations

### GoStackBase
- ❌ No public funnel share links (can't import GHL templates with one click)
- ❌ No AI agents
- ❌ No phone system
- ❌ API only on Premium+ plans
- ✅ Client portal is unique differentiator

### BuildwithOS
- ❌ No traditional CRM (uses project ontology)
- ❌ No payment collection
- ❌ No OTO/upsell pages
- ❌ Different paradigm (projects, not funnels)
- ✅ AI voice/chat agents built-in
- ✅ MCP support for external agents
- ✅ Highest affiliate payouts

### GoHighLevel
- ✅ Most complete feature set
- ✅ Funnel share links work perfectly
- ✅ AI Employee built-in
- ❌ Most expensive for full features
- ❌ No client portal
