---
tags:
  - skool
  - ai-profit-boardroom
  - post-28
  - fusion
  - openrouter
  - multi-model
  - agent-os
date: 2026-06-29
source: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=3ae6c9941c634617a712601785d18778
original-date: 2025-06-15
---

# 15th June: Fusion Beats Fable 5?

> Fable 5 getting pulled left a gap at the top end. The good news: you don't actually need a single god-tier model to hit that level of output. You need **a panel of models working together** — and that's exactly what Fusion gives you through OpenRouter.

## Useful Links

- https://x.com/i/trending/2065949691368636773
- https://x.com/OpenRouter/status/2065856853989270011
- https://openrouter.ai/fusion

## The Big Idea in One Sentence

Instead of trusting one model to nail a task, Fusion fires your prompt at several models **in parallel**, then a **judge model** reads all the answers and fuses them into one superior response. Three brains beating one — and getting you near-Fable-5 quality without the Fable-5 price tag.

## Why This Matters Right Now

With Fable 5 off the table, everyone's scrambling for that frontier ceiling. The killer insight from the benchmarks is that **a panel of cheaper models can land within 1% of Fable 5** on intelligence tests. A budget trio of Gemini 3.5 Flash + Kimi K2.6 + DeepSeek V4 Pro, fused together, beat *solo* GPT-5.5 and *solo* Opus 4.8 — even though none of those budget models is individually frontier-class.

The reason it works: roughly **three-quarters of the lift comes from synthesis** (the judge combining ideas) and **one-quarter from diversity** (different models catching different things). You're not just averaging answers — you're letting a smart judge extract the best of each.

## How Fusion Actually Works

The flow is simple once you see it:

1. **You send a prompt** to Fusion via API (OpenRouter).
2. **It fans out** to a panel of up to 8 models in parallel, each one with web search and bash tools enabled.
3. **A judge model reads every response** and pulls out the consensus points, the contradictions, the partial coverage, the unique insights, and anything the others missed.
4. **You get one fused answer back** — not five tabs to cross-check yourself.

You pick the panel: a **budget panel** for cheap-and-fast, a **quality panel** for max horsepower, or a **custom panel** where you hand-select which models collaborate.

## The Benchmark Proof

They tested this on **Draco** (by Perplexity) — 100 deep research tasks spanning 10 domains like academic research, technology, and UX design, specifically built to tell the difference between a model that *sounds* smart and one that *is*. The standout numbers:

- **Opus 4.8 solo:** 58.8%
- **Opus 4.8 as a two-model panel:** 65.5% — a clean jump from doing nothing but adding a teammate
- **Opus 4.8 vs. itself:** +6.7% improvement over the original
- **Claude Fable 5 solo:** 65.3%
- **Fable 5 + GPT-5.5 synthesized by Opus 4.8 (judge):** highest score on the board
- **Opus 4.8 + GPT-5.5 + Gemini 3.1 Pro, judged by Opus 4.8:** within *one point* of Fable 5

**Translation:** a Fusion stack with no Fable 5 in it can outscore Fable 5 alone. That's the whole pitch.

## The Real Benefits (Why You'd Actually Use This)

- **Cost.** Budget models sip tokens compared to frontier APIs. You're getting frontier-level *output* off non-frontier *pricing*. For anything running at volume — content, research, SEO — this is the difference between viable and bankrupting.
- **Quality without babysitting.** The judge does the cross-checking for you. No more reading three answers and playing referee. One fused response comes back.
- **Built-in orchestration.** This is secretly an agent-orchestration layer disguised as a model. Eight APIs working as one team, accessed through a single endpoint. Dead simple to wire into anything.
- **Resilience.** One model hallucinating gets caught by the panel and overruled by the judge. Diversity is a safety net, not just a quality boost.

## How to Set It Up via OpenRouter

The magic is that **Fusion is just an API model**. So:

1. Grab your **OpenRouter API key**.
2. Point your tool of choice at the Fusion endpoint through OpenRouter.
3. Plug that into whatever harness you want — and this is the fun part: **free Claude Code** works. Drop the Fusion API in, and now you've got Claude Code's harness driving a fused panel of models underneath.

Because it's a standard API model, it slots into your existing agent OS, your boardroom tools, Paperclip, group-chat agent setups — anything that accepts an OpenRouter key.

## Killer Use Cases

- **SEO content council.** Prompt it like: *"Act as an SEO content council for the keyword [X]. Search the web for what currently ranks, then synthesize search intent, the angle competitors are missing, a recommended H2 outline, and three questions every article forgets to answer."* The panel convenes, the judge fuses, you get a battle-tested brief instead of one model's guess.
- **Landing pages that don't look like Opus built them.** One of the most surprising results — Opus 4.8 alone usually produces clunky page UI, but the *fused* output came back clean and genuinely well-designed off a prompt as lazy as "create a beautiful landing page for an SEO agency." The OpenAI and Google models in the panel pulled the design quality up.
- **A boardroom for your agents.** Set up a "Fusion boardroom" where you paste a question and watch a panel deliberate, surface unique insights and partial coverage, then hand you a single fused decision. Same philosophy as goal mode — agents take a turn, a judge quality-controls and fuses or sends them back to iterate.

## Best Practices

The judge-in-the-loop pattern is the real lesson here, and it generalizes. Whether it's Fusion or goal mode, the winning structure is the same: **multiple agents attempt the work, a judge checks quality, then either fuses the answers or tells the panel to iterate.** Bake that into how you orchestrate everything.

For panel selection: start with a budget panel and only graduate to a quality panel when the budget output isn't cutting it. Most tasks don't need three frontier models — that's the whole point.

## The Honest Caveats

It's **slower.** The fusion step — waiting on the panel, then the judge reading and synthesizing — adds real latency. For "I want the best possible answer" work, worth it. For fast iterative chat, maybe not.

And it's **benchmarks-and-trust at this stage.** This is early. Don't take the charts as gospel — run your own prompts, compare against what you'd normally use, and see if the lift shows up on *your* tasks. It probably will, but verify on your actual workload.

## TL;DR

Fable 5 is gone, but you can rebuild that ceiling with a panel: send one prompt → multiple models answer in parallel → a judge fuses the best of each → one frontier-grade answer comes back. Plug it in via OpenRouter, run it through free Claude Code or your agent OS, and you get near-Fable-5 quality at budget-model prices. Slower, early, but one of the most genuinely interesting techniques out there right now.

---

## Related Posts

- [[01-Fusion-Fable| Fusion Beats Fable 5?]] (this post)
- [[../Skool-Post-27-Sakana-VS-Fable/01-Sakana-Fable]] Sakana VS Fable VS Fusion
- [[../Skool-Post-19-Fable-5/01-Fable-5]] Claude Fable 5
