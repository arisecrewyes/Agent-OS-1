# Skool Post #25: Loop Engineering — Quickstart

> **Source:** [19th June: Loop Engineering](https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=95d57624250744db9a1ee1123ba5e7ae)
> **Date:** 2026-06-19
> **Topic:** The Hermes Loop Engine — automated quality control for AI outputs

---

## TL;DR

The **Loop Engine** is a system where you define what "done" looks like once, then a builder AI writes a draft, a separate judge AI grades it, and the loop repeats until the output passes. You stop being the bottleneck in every AI cycle.

---

## The Core Idea

> You set the bar once, you walk away, and you come back to a finished result.

### Old Way vs New Way

| Old Way | New Way |
|---------|---------|
| You ask AI for output | You spend 5 min writing what "done" means |
| You read it, spot what's wrong | You hit run, close the tab |
| You type feedback, paste it back | The builder drafts, the judge grades |
| Repeat 5× until you're tired | It fixes itself round after round |
| You settle for mediocre | You come back to a graded, finished result |

---

## The Five-Part Framework

### Part 1: Define Done
Write down what a great result looks like. Be specific.

**Example:** *"A five-line cold email for agency owners that has one CTA and reads like a human wrote it."*

The more honest you are with the bar, the better the judge can grade it.

### Part 2: The Builder Acts
- Give it a starting point (optional)
- Pick your builder model:
  - **MiniMax** — good default
  - **N2** — free model on news portal
  - **OpenRouter** — free API
  - **Opus 4.8** — frontier model
- It writes the first version

### Part 3: The Judge Grades It
- A **separate** model grades the draft out of 100
- Lists exactly what's wrong
- Told to be adversarial and find holes
- **Key:** The builder never grades its own work

### Part 4: The Loop Runs
- If the draft fails, notes go back to the builder
- Builder fixes them — round after round
- Example: Round 1 → 54, Round 2 → 71, Round 3 → 83, Round 4 → 92
- You set max rounds (e.g., "go four loops and stop")

### Part 5: Come Back to a Finished Result
- When the judge passes it, you get the final result
- Full record of every round: scores, issues fixed
- Everything saved to your agent OS in the loop section

---

## Use Cases

Anything that needs quality control:
- Cold emails
- Ad copy
- Landing pages
- Coding / SaaS tools
- Websites / Apps / Games / Videos

---

## Common Objections

| Objection | Reality |
|-----------|---------|
| "My work is too nuanced for a machine to judge" | You write the bar; the judge just checks against your standard |
| "Loops sound expensive" | Free models on OpenRouter/news portal can run the whole thing |
| "This sounds like coding" | It's a text box — type what good looks like, press a button |

---

## 30-Day Roadmap

| Days | Action |
|------|--------|
| 1–7 | Set up one loop tonight. Use cold email or ad copy as first test. |
| 8–14 | Run a loop every day on something real. Get comfortable switching builder/judge models. |
| 15–21 | Move to harder use cases: landing pages, longer copy, simple app builds. |
| 22–30 | Build loops into daily workflow. Stop checking your own work manually. |

---

## Key Takeaway

> **You stop being the loop. You set the bar, you walk away, you come back when it's done.**

---

## No GHL/GoStackBase Content

This post does not contain GoHighLevel (GHL) references. No conversion needed.
