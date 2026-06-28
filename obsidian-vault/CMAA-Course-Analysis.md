# Copy My AI Agency — Course Analysis

**Course Creator:** Zalo Kabche (Black Umbrella)
**Platform:** learn.blackumbrella.app
**Date Analyzed:** 2026-06-28
**Total Modules:** 15
**Files Analyzed:** 111 (from Google Drive)
**URLs Analyzed:** 30+

## Key Architecture

```
CONTACT (SMS/WhatsApp/IG/FB/Live Chat/Phone)
    → LC Platform (GoHighLevel/StackBase/BuildwithOS)
    → n8n (Self-hosted on Hostinger VPS)
        → AI Agent (Claude 4.5 Sonnet + Gemini 3 Pro backup)
        → Tools: booking, DND, escalation, calendar, RAG
    → LC Platform (updates contact, tags, custom fields)
    → Contact (receives response on same channel)
```

## Critical Discovery

**All LC derivatives share the same API:** `services.leadconnectorhq.com`
- Same Private Integration system
- Same API v2.0
- Same OAuth2 framework
- The n8n workflows built for GHL work identically on GoStackBase, BuildwithOS, and any LC derivative

## 12 Universal Integration Patterns
1. Webhook Bridge (LC ↔ n8n)
2. Environment Variables via Custom Values
3. State Management via Tags
4. Per-Channel Architecture
5. Snapshot/Template Deployment
6. Dual LLM Fallback
7. Prompt Forge Systematic Generation
8. RAG Knowledge Expansion
9. Voice AI Bridge (n8n ↔ Retell ↔ LC)
10. A2P/SMS Compliance Pipeline
11. Onboarding QA Checklist
12. Database Reactivation Revenue Model

## Related Files
- [[SOPs/sop-course-access-and-analysis|Course Access SOP]]
- [[Lead-Connector-Derivatives/index|LC Derivatives]]
- [[agent-os-lead-connector-integration|LC Integration Guide]]

## Google Drive (All Course Files)
https://drive.google.com/drive/folders/1b7shAaiiJFKNiP2IpflCzEg9ouH5YQBF
