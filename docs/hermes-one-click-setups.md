# Hermes Agent — One-Click Setups

> Two easy one-click methods to install and run Hermes (Ollama + MaxHermes).
> Source: Julian Goldie SEO — Skool Post #5 (NEW section — not in Post #4)
> Related: [[hermes-quickstart]] | [[hermes-agent-capabilities-general]]

---

## Option 1: Ollama (Recommended)

Ollama lets you run local and cloud models with a single command, and it has a built-in Hermama launch command for Hermes.

### Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Launch Hermes with Ollama
```bash
ollama launch hermes
```

Then select your model and Hermes starts.

### Benefits
- ✅ Use **free models** locally
- ✅ Use **cloud models** (via Ollama's cloud integration)
- ✅ Setup Hermes in **one click**
- ✅ Easily **switch between models**
- ✅ No complex configuration

---

## Option 2: MaxHermes

MaxHermes is another one-click install option for Hermes.

### Benefits
- ✅ Easy to set up
- ✅ Non-technical friendly
- ✅ Can still use scheduled tasks
- ✅ Can still use all tools
- ✅ Can create images and videos straight out of the box

### Drawbacks
- ⚠️ Not as good as running Hermes locally
- ⚠️ Can be buggy sometimes
- ⚠️ Less control over configuration

---

## Comparison

| Feature | Ollama | MaxHermes |
|---------|--------|-----------|
| **Ease of setup** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Performance** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Reliability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Model switching** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Local + Cloud** | ✅ Both | ✅ Both |
| **Scheduled tasks** | ✅ | ✅ |
| **Tools access** | ✅ Full | ✅ Full |
| **Media generation** | ✅ | ✅ |

> **Julian's recommendation:** Use **Ollama** for the best experience. Use MaxHermes only if you can't get Ollama working or want the absolute simplest setup.

---

## For VPS / Docker Users

- **Ollama on VPS:** Requires GPU for local models, or configure it to use cloud models only. Can be added to a Docker compose file with GPU passthrough.
- **MaxHermes on VPS:** Can be run as a Docker container. Less configuration needed but less control.
- The existing Hermes compose project does NOT include Ollama — it uses OpenRouter for cloud models.

---

## Related

- For the main Hermes quickstart: `hermes-quickstart.md`
- For the Hermes dashboard: `hermes-dashboard.md`
- For agent teams: `hermes-agent-teams.md`
