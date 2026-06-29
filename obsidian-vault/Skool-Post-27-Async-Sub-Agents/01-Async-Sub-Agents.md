---
title: "Skool Post #27: How To Use Async Sub Agents In Hermes"
date: 2026-06-16
source: "https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=dcdc4a2b236c4709b91aa66c7f1d3049"
author: "Dan B (AI Profit Boardroom)"
tags:
  - hermes-agent
  - async-sub-agents
  - delegate-task
  - parallel-agents
  - orchestration
  - tutorial
category: "Hermes Agent"
---

# Skool Post #27: How To Use Async Sub Agents In Hermes

Hermes got a major upgrade: the `delegate_task` tool no longer freezes your chat. You can now spawn sub-agents, walk away, and keep working while they run in the background.

## What Changed

**Before:** Delegating a task froze your chat. You had to wait until the work was done. One task blocked the next.

**Now:** Work runs in the background. You dispatch the job and get control back in ~2ms. You keep chatting while sub-agents do their thing.

## Step 1: Update Hermes

You need the latest version first.

```bash
hermes update
```

Or open your Hermes dashboard and click the update button.

## Step 2: Give It A Goal

Talk to your lead agent in plain English. Hand it one goal. The lead agent decides how to split the work.

**Example:**

```
Run an SEO funnel for "how to build an AI agent"
```

The lead agent never does the work itself — it fans the goal out to workers. Each worker gets one tight job, its own thread, and its own context.

## How The Flow Works

1. The lead calls `delegate_task` with `background=true`
2. It returns a handle in about 2 milliseconds
3. The sub-agent runs on its own background thread
4. The result flies back into your chat as a new message

You can dispatch one worker per job. All workers run at the same time.

## A Real Example

**Goal:** 5 blog articles live on your site.

**Old way:** Write one article → wait → check it → write the next one. Slow and painful.

**New way:** One command spawns 5 workers. All 5 write at once. A deploy worker pushes the finished content live. You walk away and everything comes back on its own.

Same 5 articles. A fraction of the time.

## What Comes Back

When a worker finishes, the result re-enters your chat. It is self-contained, so you can read it on its own.

Each result block shows:
- The original goal
- The context you gave it
- The tools, role, and model used
- The status and the result

Workers do not finish together. Each one flies back the moment it's done. One might finish first, another later, two at the same time.

## Why It Stays Under Control

Parallel agents won't go off the rails:
- You are the lead. You set the jobs and walk away.
- Every result comes back for you to check.
- It rides the same rail as a background terminal job.
- Message order stays intact. Nothing gets spliced mid-loop.

## Money-Saving Tip

Point different sub-agents at different APIs:
- For small/simple tasks, use a cheaper API (or a free one, or a local model).
- Keeps costs down when the job doesn't need a heavy model.

## Quick Recap

1. Run `hermes update`
2. Hand your lead agent one goal
3. It delegates with `delegate_task background=true`
4. Dispatch returns in about 2 milliseconds
5. Workers run in parallel in the background
6. Results fly back into your chat as they finish
7. You stop babysitting and start shipping

## Key Takeaway

This is the same orchestrator pattern you see in Claude Code: one main brain, many workers, one big goal.

---

## Related Posts in Series

- [[Skool-Post-26-Hermes-Agent-V0.17|Post #26: Hermes Agent V0.17]] (20th June)
- [[Skool-Post-28-Loop-Engineering|Post #28: Loop Engineering]] (19th June)
- [[Skool-Post-29-Hermes-Shopping-Assistant|Post #29: Hermes Shopping Assistant]] (17th June)
