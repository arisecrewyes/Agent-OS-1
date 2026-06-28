# Hermes Agent — Community Skills

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## What Are Skills?

Skills are folders with a **skill.md** file that tells the agent how to handle a specific type of task. Think of them like plugins or apps for Hermes.

## One-Click Upgrade: Wonderly Skills

Hermes comes with **40+ skills out of the box**. To massively upgrade in one command:

```bash
hermes skills install wonderly-skills
```

This installs the **Wonderly Skills** library:
- 250+ GitHub stars
- Actively maintained
- Cross-platform compatible

## Browse Available Skills

```bash
hermes skills browse
```

Skills cover: web research, PDF processing, GitHub PR workflows, email, diagramming, Jupyter notebooks, and much more.

## How Skills Load (Efficiency)

- At startup, the agent only sees **skill names and short descriptions**
- Full content is loaded **only when the skill is actually needed**
- Having dozens installed does **not** slow anything down

## Open Standard: agentskills.io

Skills follow the open standard at [agentskills.io](https://agentskills.io), meaning:
- Skills you create are **compatible with Claude Code and Cursor**
- Cross-agent portability
- Community collaboration

## Security

- Security scanner checks every skill before install
- Skills are sandboxed and isolated

---

## Metadata

- Tags: `hermes`, `skills`, `wonderly`, `plugins`
- Related: [[06 - Creating Custom Skills]] | [[08 - External Tools]]
