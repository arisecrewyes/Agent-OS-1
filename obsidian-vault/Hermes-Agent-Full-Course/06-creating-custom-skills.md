# Hermes Agent — Creating Custom Skills

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Why Custom Skills Matter

This is where the real power is. Custom skills are **tailored exactly to your workflow**, not generic community solutions.

## Three Ways to Create Skills

### Option 1: Let Hermes Create Them Automatically
After completing complex tasks (typically 5+ tool calls), Hermes **synthesizes the experience into a permanent skill document** without you asking.

### Option 2: Ask Hermes Directly
```
"Create a skill for posting to X with trending AI news and an image"
```
Hermes will build the skill.md file for you.

### Option 3: Write Your Own
Each skill is just a **markdown file** in `~/.hermes/skills/` that describes how to handle a specific task.

## The Feedback Loop

After creating a skill:
1. Give it **feedback every time it runs**
2. Tell it what worked and what did not
3. It **updates the skill.md file** and gets better at that task over time
4. This is the **self-improving loop** — the core differentiator of Hermes

## Pro Tip: Back Up Your Skills

**Always back up your skill.md files somewhere outside of Hermes once a week.**

Sometimes Hermes can overwrite or lose a skill file. Having a backup saves you hours of rebuilding.

Store backups in:
- GitHub repo
- Obsidian vault
- Cloud storage

## Skill Structure

```
~/.hermes/skills/
  └── your-skill-name/
      ├── skill.md          # Required — describes the skill
      └── (any supporting files)
```

The **skill.md** file contains:
- What the skill does
- When to trigger it
- Step-by-step instructions
- Required tools/APIs
- Examples

---

## Metadata

- Tags: `hermes`, `skills`, `custom-skills`, `self-improving`
- Related: [[05 - Community Skills]] | [[04 - First 7 Days Training]]
