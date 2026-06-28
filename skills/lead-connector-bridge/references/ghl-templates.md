# GHL Funnel Templates — Detailed Specs

> Specifications for the 5 GoHighLevel funnel templates referenced by the Lead Connector Bridge skill.
> Source: Julian Goldie SEO — Skool Post #6 + GoHighLevel affiliate links

---

## Template 1: Book a Call

**Affiliate Link:** https://affiliates.gohighlevel.com/?fp_ref=goldie-agency54&funnel_share=65914bbf139166048fcfe1ba

**Page Flow:** Opt-in → Booking → Confirmation

| Page | Elements | Notes |
|------|----------|-------|
| **Opt-in** | Headline, subheadline, benefits list, CTA button | Single-step lead capture |
| **Booking** | Calendar widget, time slot selector, form fields | Embedded GHL calendar |
| **Confirmation** | Appointment details, what-to-expect, next steps | Can trigger automation |

**Standard Headline:**
```
Book Your Free Strategy Call
Discover How to [Achieve Result] in [Timeframe]
```

**Automations Triggered:**
- Form submit → Book calendar event
- Booking confirmed → Send confirmation email
- 24h before → Send reminder email
- No-show → Send reschedule email

---

## Template 2: ChatGPT Opt-In

**Affiliate Link:** https://affiliates.gohighlevel.com/?fp_ref=goldie-agency54&funnel_share=656e6e2df0c86b78a686659f

**Page Flow:** Opt-in → Delivery/Thank You

| Page | Elements | Notes |
|------|----------|-------|
| **Opt-in** | Headline about AI/ChatGPT, resource description, name + email form | Lead magnet delivery |
| **Delivery** | Download link, next steps, optional upsell | Immediate gratification |

**Standard Headline:**
```
200+ FREE AI SEO Strategies & VIDEO COURSE
Steal The EXACT SEO Strategies That 2X'd My Traffic in 11 Days!
```

**Automations Triggered:**
- Form submit → Send email with download link
- After 1 day → Send "Did you read it?" email
- After 3 days → Soft pitch for main offer

---

## Template 3: Mastermind

**Affiliate Link:** https://affiliates.gohighlevel.com/?fp_ref=goldie-agency54&funnel_share=659cb7e834165c150b02f723

**Page Flow:** Application → Booking → Payment → Welcome

| Page | Elements | Notes |
|------|----------|-------|
| **Application** | Multi-step form, qualification questions, social proof | Filters unqualified leads |
| **Booking** | Calendar for interview call | Only shown to qualified applicants |
| **Payment** | Payment form for mastermind fee | Optional (can be free) |
| **Welcome** | Onboarding info, community access, next steps | Triggers onboarding sequence |

**Standard Headline:**
```
Apply Now: [Mastermind Name]
An Exclusive Program for [Target Audience] Who Want [Result]
```

**Automations Triggered:**
- Application submitted → Tag as "applicant"
- Qualified → Send booking link
- Payment received → Send welcome sequence + community invite
- Rejected → Send polite decline + alternative offer

---

## Template 4: Course Tripwire

**Affiliate Link:** https://affiliates.gohighlevel.com/?fp_ref=goldie-agency54&funnel_share=659d112e5e5d54211a93ae69

**Page Flow:** Sales → Checkout → Upsell → Thank You

| Page | Elements | Notes |
|------|----------|-------|
| **Sales** | Course description, benefits, testimonials, pricing, guarantee | Long-form sales page |
| **Checkout** | Order form, payment details, order bump | GHL order form |
| **Upsell** | Premium offer (one-time offer), bonus stack, countdown | OTO (one-time offer) |
| **Thank You** | Access details, next steps, support info | Course delivery |

**Standard Headline:**
```
Get [Course Name] for Just $[Price]
[Value Stack Description] — Yours for $[Price] Today Only
```

**Automations Triggered:**
- Checkout complete → Deliver course access
- Upsell accepted → Deliver premium offer
- Upsell declined → Send "special offer" email sequence
- Refund request → Trigger retention sequence

---

## Template 5: Free Book

**Affiliate Link:** https://affiliates.gohighlevel.com/?fp_ref=goldie-agency54&funnel_share=659d112e5e5d54211a93ae69

**Page Flow:** Opt-in → Download/Thank You

| Page | Elements | Notes |
|------|----------|-------|
| **Opt-in** | Book cover image, description, benefits of reading, name + email form | Lead magnet delivery |
| **Download** | Download link, book summary, next steps, social share | Immediate delivery |

**Standard Headline:**
```
Free: [Book Title]
The Complete Guide to [Topic] That Will Help You [Result]
```

**Automations Triggered:**
- Form submit → Send email with download link
- After 2 days → "What did you think?" email
- After 5 days → Soft pitch for related offer

---

## Common Elements Across All Templates

### Forms
- Standard fields: First Name, Last Name, Email
- Optional fields: Phone, Company, Custom questions
- All forms use GHL's Smart Forms (drag-and-drop builder)

### Email Sequences
- All templates include pre-built email sequences
- Sequences are triggered by form submissions
- Emails use GHL's email builder with merge tags

### Design
- All templates use GHL's responsive page builder
- Mobile-optimized by default
- Pre-written copy included (DO NOT copy verbatim — personalize)

### Customization
- All headlines, body copy, and images are customizable
- Color schemes match your brand
- Custom domains supported
