# Hermes Agent — OpenClaw Migration

> Part of the [[00 - Index|Hermes Agent Full Course]] knowledge base.

## Migration Tool

If you are coming from OpenClaw, Hermes can **automatically import everything**:

```bash
hermes claw migrate
```

### What Gets Migrated

- **SOUL.md** — Persona file
- **Memories** — All stored memory
- **Skills** — All installed skills
- **Command allowlist** — Permissions
- **Messaging settings** — Connected platforms and configs
- **API keys** — Provider credentials
- **TTS assets** — Text-to-speech configuration
- **Workspace instructions** — Custom instructions

## Preview Before Migrating

```bash
hermes claw migrate --dry-run
```

This shows you **what would be migrated** without actually changing anything.

## Auto-Detection

During first-time setup, Hermes **automatically detects** if you have OpenClaw installed and offers to migrate.

## Key Notes

- Migration is **one-directional** (OpenClaw → Hermes)
- Original OpenClaw data is preserved (not deleted)
- You can run both agents side-by-side after migration
- API keys are transferred securely

---

## Metadata

- Tags: `hermes`, `migration`, `openclaw`, `import`
- Related: [[01 - Installation & Setup]] | [[11 - Hermes vs OpenClaw]]
