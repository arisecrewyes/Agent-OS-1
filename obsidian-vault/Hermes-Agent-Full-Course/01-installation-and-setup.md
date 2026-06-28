# Hermes Agent — Installation & Setup

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Phase 1: Installation (5 minutes)

### Step 1: Open Terminal
Mac, Linux, or WSL2 on Windows. **Native Windows is not supported.**

### Step 2: Install
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### Step 3: Reload Shell
```bash
source ~/.bashrc
# Or if you use zsh:
source ~/.zshrc
```

### Step 4: Run Setup Wizard
```bash
hermes setup
```
Walks you through choosing your model provider and configuring everything.

### Step 5: Verify
```bash
hermes doctor
```
Diagnoses any issues before you start.

### Check Version
```bash
hermes --version
```

## System Requirements
- Git installed
- Command-line access
- Python 3.11+ (auto-installed if missing)
- Node.js (auto-installed if missing)

## Key Details
- **Native Windows NOT supported** — use WSL2
- Installs from GitHub: `NousResearch/hermes-agent`
- 11,600+ GitHub stars, 142+ contributors, MIT license
- Created by **Nous Research** — same lab behind Hermes, Nomos, Psyche model families

## Troubleshooting Installation
- If `hermes` command not found after install: run `source ~/.bashrc` or `source ~/.zshrc`
- If install script fails: ensure `curl` and `git` are installed
- Check GitHub Issues for the repo for known problems

---

## Metadata

- Tags: `hermes`, `installation`, `setup`
- Related: [[02 - AI Model Selection]] | [[12 - Troubleshooting & Commands]]
