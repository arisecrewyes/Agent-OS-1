# Client Onboarding Automation (Post #6)

> Converted from Julian Goldie Skool Post #6 — GHL → GoStackBase
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/71efa175?md=763adb112ce34394944d1eeebdcedf50
> YouTube: https://www.youtube.com/watch?v=uXf_GNkriZ0

## Core Concept

Simple 3-step automation:
1. **Form submitted** (onboarding form) → triggers workflow
2. **Send email** (customizable welcome email based on form data)
3. **Tag contact** (categorize in CRM)

Optional: **7-day delay** → send follow-up check-in email

## Key Steps (GoStackBase)

1. **Sites** → Forms → Add Form → Name it "Client Onboarding"
2. **Automations** → Create Workflow → Start from Scratch
3. Trigger: **Form Submitted** → filter to your onboarding form only
4. Action 1: **Send Email** (name, email, subject, body with merge fields)
5. Action 2: **Tag** (add contact tag for CRM segmentation)
6. Action 3 (optional): **Wait** 7 days → **Send Email** (follow-up)
7. **Publish** → Save

## Pro Tips

- Use **form-specific filters** — one workflow per form
- Tags enable downstream segmentation for re-engagement campaigns
- Test with your own email before going live via Execution Logs
- GoStackBase (like GHL) can't export templates — build from scratch

## GHL → GoStackBase Mapping

| Feature | GHL | GoStackBase |
|---------|-----|-------------|
| Form creation | Sites → Forms | Sites → Forms |
| Workflow trigger | Form Submitted | Form Submitted |
| Email | Send Email | Send Email |
| Tagging | Add Contact Tag | Tag |
| Delay | Wait | Wait |
| Execution logs | Automations → Logs | Automations → Execution Logs |

## Security Notes

- No secrets involved in this automation
- Form submissions go to your GoStackBase CRM
- Execution logs contain PII (client names/emails) — restrict team access

## Related

- [[00 - Skool Post Conversion Index]]
- [[Agent-OS-Ecosystem|Ecosystem: GoStackBase Integration]]
- [[SOP - Universal LC Integration]]
