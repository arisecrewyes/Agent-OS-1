# QuickStart: Client Onboarding Automation Through GoStackBase

> Converted from Julian Goldie Skool Post #6 — "Client Onboarding Automation Through GHL"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/71efa175?md=763adb112ce34394944d1eeebdcedf50
> YouTube: https://www.youtube.com/watch?v=uXf_GNkriZ0

---

## What You're Building

A **Client Onboarding Automation** that:
1. Triggers when a client submits an onboarding form
2. Sends a customized welcome email
3. Tags and categorizes the contact in your CRM
4. (Optional) Follows up 7 days later with a check-in email

**Time to build:** ~15 minutes
**Difficulty:** Beginner

---

## Step-by-Step Build (GoStackBase)

### Step 1: Create the Onboarding Form

1. Go to **GoStackBase Dashboard** → **Sites** (left sidebar)
2. Click **Forms** → **Add Form**
3. Name it: `Client Onboarding`
4. Add fields as needed (Name, Email, Phone, etc.)
5. Save the form

> **GHL Difference:** In GHL the path is `Sites → Forms → Add Form`. Identical in GoStackBase.

### Step 2: Create the Welcome Email

1. Go to **Marketing** → **Emails** → **Templates**
2. Create a new email template
3. Set:
   - **From Name:** Your name/company
   - **From Email:** Your email
   - **Subject:** "Welcome aboard, {{contact.first_name}}!"
4. Customize the body with form submission data using merge fields
5. Save

### Step 3: Build the Workflow (Automation)

1. Go to **Automations** → **Create Workflow** → **Start from Scratch**
2. Name it: `Client Onboarding Automation`
3. Set the **Trigger:**
   - Click **Add New Trigger**
   - Select **Form Submitted**
   - Add Filter: Form = `Client Onboarding`
   - Save Trigger

4. Add Actions in sequence:

   **Action 1: Send Email**
   - Click **+** → **Send Email**
   - Select your welcome email template
   - Map the recipient to the form submitter

   **Action 2: Add Contact Tag**
   - Click **+** → **Tag**
   - Add tag: `onboarded` (or whatever you prefer)
   - This categorizes the contact in your CRM

   **(Optional) Action 3: Add Delay + Follow-Up**
   - Click **+** → **Wait**
   - Set delay:  - Click **+** → **Send Email**
   - Create a follow-up email: "How was your onboarding experience?"

5. Click **Publish** → **Save**

### Step 4: Test the Automation

1. Go to **Sites** → **Forms** → Open your onboarding form
2. Submit a test entry with your own name/email
3. Go to **Automations** → **Execution Logs**
4. Verify:
   - ✅ Form submitted trigger fired
   - ✅ Email sent to test address
   - ✅ Contact tagged correctly
   - ✅ Removed from workflow after completion

---

## Key Concepts from the Video

| Concept | GHL (Original) | GoStackBase (Converted) |
|---------|---------------| creation | Sites → Forms → Add Form | Sites → Forms → Add Form |
| Workflow trigger | Form Submitted (+ filter) | Form Submitted (+ filter) |
| Email action | Send Email | Send Email |
| Contact tagging | Add Contact Tag | Tag |
| Delay/wait | Wait (7 days) | Wait (7 days) |
| Execution logs | Automations → Logs | Automations → Execution Logs |
| Template export | ❌ Not exportable | ❌ Not exportable |

---

## Pro Tips

1. **Use form-specific filters** — Make sure your trigger only fires for the correct form. Multiple forms sharing one workflow = chaos.

2. **Tag strategically** — Tags like `onboarded`, `new-client`, `form-submitted` let you segment later for re-engagement campaigns.

3. **Delay sequences** — The 7-day follow-up trick is gold. Automate check-in emails, satisfaction surveys, or upsell offers on a delay.

4. **Test before going live** — Always submit a test form to verify the full chain: trigger → email → tag → removal.

5. **Can't export templates** — Julian explicitly notes GHL can't export workflow templates. GoStackBase shares this limitation. Build from scratch using this guide.

---

## Next Steps

- After onboarding, chain to a **nurture sequence** (email drip campaign)
- Add **task creation** for your team when high-value clients onboard
- Integrate with **calendar booking** for onboarding calls
- See also: `sop-universal-lc-integration.md` for full platform setup
