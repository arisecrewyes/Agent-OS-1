# Skool Post #26: Hermes Shopping Assistant — Quickstart

> **Source:** [17th June: Hermes Shopping Assistant](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=86c546094fe1423faec08702e5009d64)
> **Date:** 2026-06-17
> **Author:** Dan B (AI Profit Boardroom)

---

## Overview

Give your Hermes agent a wallet — one it can't run off with. Hermes can now shop AND buy for you. It finds the product, fills the cart, and stops at the till — waiting for **your** tap. Your card never even touches the agent.

**Setup time:** ~10 minutes

---

## What You're Building

A "shopper" agent that:
- Searches every store
- Finds the best price
- Pays through Stripe Link — where every purchase needs your approval in the Link app

---

## Step-by-Step Setup

### Step 1 — Create a shopping agent profile

```bash
hermes profile create shopper
```

### Step 2 — Install the shopping skill

Gives the agent search, checkout, and order tracking capabilities:

```bash
hermes -p shopper skills install official/productivity/shop-app
```

### Step 3 — Install the payment skill (approval-gated)

```bash
hermes -p shopper skills install official/payments/stripe-link-cli
```

### Step 4 — Install the Stripe Link CLI tool

```bash
npm install -g @stripe/link-cli
```

### Step 5 — Link your card (this step is yours, not the agent's)

```bash
link-cli auth login --client-name "Hermes"
```

- Open the link it prints
- Approve "Hermes"
- Add your card inside Link

> **Key security point:** The agent never sees your card — it only ever gets a one-time token.

### Step 6 — Set the guardrails

Tell your agent its rules (or add them to its `SOUL.md`):

- Always confirm the exact item + total before any spend
- Never buy without my approval in the Link app
- Stay under [your budget] — stop and ask before going over

### Step 7 — Use it

```bash
shopper "find me a standing desk under $400"
```

It searches every store, shows you the total, you tap approve in Link. Done.

---

## Why It's Safe

- Your card lives in Stripe Link — never in the agent
- Every spend needs YOUR tap — the agent CANNOT self-approve
- One-time tokens only — your real card number never touches the AI

---

## ⚠️ One Catch

Stripe Link is **US-only** right now. It needs a US-based Link account — a US card alone isn't enough.

**Outside the US?** Skip Link and use the browser-checkout route instead:
- The agent finds the product + checkout link
- You pay at the merchant with your own card

---

## External Links

- [Twitter post](https://x.com/NousResearch/status/2066647737613832624)
- [Documentation](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#payments)
