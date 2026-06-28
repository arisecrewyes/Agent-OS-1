# LC Platform Private Integrations — Official Documentation

**Source:** https://help.leadconnectorhq.com/support/solutions/articles/155000002774
**Knowledge Base Home:** https://help.leadconnectorhq.com/support/home
**Date Retrieved:** 2026-06-28

---

## Key Discovery: Shared API Infrastructure

**ALL LC derivatives (GHL, LeadConnector, GoStackBase, BuildwithOS) use:**
- Same API base URL: `services.leadconnectorhq.com`
- Same Private Integration system
- Same API v2.0 (v1.0 deprecated)
- Same OAuth2 framework
- Same knowledge base at `help.leadconnectorhq.com`

**This means:** The n8n integration built for GHL works identically on GoStackBase, BuildwithOS, and any other LC derivative. Only the UI/domain changes, not the API.

---

## Private Integrations — Complete Reference

### What Are Private Integrations?
- Custom integrations between LC account and any third-party app (like n8n)
- Two options: App Marketplace (pre-built) OR Private Integration (custom-built)
- Key advantages: Simple (generate from settings) + Secure (restrictable scopes)

### Private Integrations vs API Keys

| Feature | Private Integrations | API Keys |
|---|---|---|
| Security | Restrictable scopes/permissions | Unrestricted access to ALL data |
| API Version | v2.0 (current, maintained) | v1.0 (deprecated, end-of-life) |
| Features | Full API + Webhooks | Limited API, no webhooks |
| **Verdict** | **USE THIS** | **DEPRECATED — DO NOT USE** |

### Private Integrations vs OAuth2 Access Tokens

| Feature | Private Integrations | OAuth2 Tokens |
|---|---|---|
| Generation | UI (Settings page) | Programmatic (API exchange) |
| Token Life | Static/fixed (until rotated) | Expires daily, auto-refreshes |
| **Verdict** | **Easier for n8n** | **For app developers** |

### How to Use Private Integration Tokens

**In HTTP request Authorization header:**

```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/contacts/ocQHyuzHvysMo5N5VsXc \
  --header 'Accept: application/json' \
  --header 'Authorization: <YOUR_PRIVATE_INTEGRATION_TOKEN>' \
  --header 'Version: 2021-07-28'
```

**Required headers:**
- `Authorization: <token>`
- `Version: 2021-07-28` (API version header)
- `Accept: application/json`

**API Base URL:** `https://services.leadconnectorhq.com/`

### Who Can Create Private Integrations?
- Account admins (by default)
- Can be restricted per user: Settings > My Staff > Edit admin > Roles & Permissions

### Where to Find Private Integrations
- Settings > scroll to "Other Settings" > Private Integrations
- If not visible: enable on Labs first

### How to Create a Private Integration

1. Click "Create new Integration"
2. Name + Description (identify what it's for)
3. Select scopes/permissions (**only select required scopes for security**)
4. Copy token (**ONLY SHOWN ONCE — cannot retrieve later**)
5. Share with developer (trusted parties only)

### Token Security Best Practices

- **Rotate every 90 days**
- Rotation process:
  1. Settings > Private Integrations > Click integration
  2. "Rotate and expire this token later"
  3. Confirm → Copy new token
  4. **7-day overlap window** — both old and new tokens work
  5. After 7 days, old token expires
  6. During overlap: can "Cancel rotation" or "Expire Now"

### If Token Compromised

1. Settings > Private Integrations > Click integration
2. "Rotate and expire this token now" (immediate expiration)
3. Confirm → Copy new token
4. Update third-party app immediately

### Edit Permissions Without Changing Token

- Yes! Can edit name, description, scopes WITHOUT regenerating token
- Settings > Private Integrations > Three-dot menu > Edit

### Delete Private Integration

- Settings > Private Integrations > Three-dot menu > Delete
- Only when no longer using the third-party app

---

## API Reference Links

- **API Docs:** https://highlevel.stoplight.io/docs/integrations/
- **Get Access Token API:** https://highlevel.stoplight.io/docs/integrations/00d0c0ecaa369-get-access-token
- **Get Contact Example:** https://highlevel.stoplight.io/docs/integrations/d777490312af4-get-sub-account-formerly-location

---

## Critical Implications for Universal SOP

1. **One API, all platforms.** The Private Integration endpoint `services.leadconnectorhq.com` is shared across GHL, StackBase, BuildwithOS, and ALL LC derivatives. The n8n HTTP Request nodes configured for GHL work identically on any LC platform.

2. **API v2.0 is the standard.** v1.0 (API Keys) is deprecated. Universal SOP must use Private Integrations exclusively.

3. **Webhooks are supported.** Private Integrations support webhooks (v2.0 feature), meaning n8n can RECEIVE events from any LC platform, not just send commands.

4. **Token rotation is built-in.** 7-day overlap window during rotation means zero-downtime token updates.

5. **Scopes are restrictable.** n8n only needs specific scopes (contacts, conversations, calendars, etc.) — Principle of Least Privilege applies.

6. **The knowledge base at help.leadconnectorhq.com applies to ALL LC derivatives.** One documentation source for the entire ecosystem.

---

## GoStackBase Implications

Since GoStackBase uses the same backend:
- Private Integrations work the same way
- Same API endpoints
- Same `services.leadconnectorhq.com` base URL
- Same Location ID system
- Same custom fields, tags, workflows, etc.
- **The entire n8n workflow library from CMAA works on GoStackBase without modification**

The ONLY differences between LC platforms:
- UI theming/branding
- Pricing
- Some features may be enabled/disabled at platform level
- Domain used for web interface

The API layer is IDENTICAL.
