---
tags:
  - skool
  - hermes-agent
  - shopping
  - stripe
  - payments
  - ai-agent
  - automation
date: 2026-06-17
source: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=86c546094fe1423faec08702e5009d64
author: Dan B
community: AI Profit Boardroom
post_number: 26
---

# 🛒 Hermes Shopping Assistant

> Hermes can now shop AND buy for you. It finds the product, fills the cart, and stops at the till — waiting for YOUR tap. Your card never even touches the agent.

---

## What You're Building

A "shopper" agent that searches every store, finds the best price, and pays through **Stripe Link** — where every purchase needs your approval in the Link app.

---

## Setup Guide (10 minutes)

### 1. Create a shopping agent profile

```bash
hermes profile create shopper
```

### 2. Install the shopping skill

Search, checkout, and order tracking:

```bash
hermes -p shopper skills install official/productivity/shop-app
```

### 3. Install the payment skill (approval-gated)

```bash
hermes -p shopper skills install official/payments/stripe-link-cli
```

### 4. Install the Stripe Link CLI

```bash
npm install -g @stripe/link-cli
```

### 5. Link your card

```bash
link-cli auth login --client-name "Hermes"
```

- Open the printed link
- Approve "Hermes"
- Add your card inside Link

> 🔐 The agent never sees your card — it only ever gets a one-time token.

### 6. Set the guardrails

Add to the agent's `SOUL.md` or tell it directly:

- Always confirm the exact item + total before any spend
- Never buy without my approval in the Link app
- Stay under [your budget] — stop and ask before going over

### 7. Use it

```bash
shopper "find me a standing desk under $400"
```

→ It searches every store, shows you the total, you tap approve in Link. Done.

---

## Security Model

| Feature | Detail |
|---|---|
| Card storage | Lives in Stripe Link — never in the agent |
| Approval | Every spend needs YOUR tap — agent CANNOT self-approve |
| Token model | One-time tokens only — real card number never touches the AI |

---

## ⚠️ Limitation

Stripe Link is **US-only** (requires a US-based Link account — a US card alone isn't enough).

**Non-US workaround:** Use the browser-checkout route — the agent finds the product + checkout link, and you pay at the merchant with your own card.

---

## Related Links

- [Twitter post](https://x.com/NousResearch/status/2066647737613832624)
- [Hermes Docs: Payments](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#payments)

---

## Key Takeaways

- Hermes Agent now supports a full shopping workflow: search → cart → checkout → pay
- Stripe Link integration provides approval-gated payments (human-in-the-loop)
- Security-first design: card never touches the agent, one-time tokens only
- US-only limitation for Stripe Link; browser-checkout fallback for international users
- Setup takes ~10 minutes with a dedicated `shopper` profile
