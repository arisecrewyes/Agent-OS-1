# QuickStart: Hermes Agent + ElevenLabs Voice Phone

> Converted from Julian Goldie Skool Post #33 — "6th June: Hermes Agent + ElevenLabs"
> Original: https://www.skool.com/ai-profit-lab-7462/classroom/9daf24e1?md=c4dabc4ba5dd4564b425e24b20b10609

---

## What You're Building

A **phone number that lets you call your Hermes AI agent** and have a real conversation.

ElevenLabs handles the voice (text-to-speech + speech-to-text), Hermes does the thinking on your Mac, and a Cloudflare tunnel connects the two. Takes about 10 minutes.

**Cost:** ElevenLabs account (free tier available) + cheap Twilio number (~$1/month)
**Time to build:** ~10 minutes
**Difficulty:** Intermediate (requires Mac + terminal comfort)

---

## What You'll Need

| Requirement | Details |
|---|---|
| **ElevenLabs account** + API key | Get key from profile → starts with `sk_` |
| **Hermes Agent** installed | Signed into a model provider |
| **Twilio phone number** | Cheap (~$1/month) — for the inbound phone line |
| **Homebrew** on Mac | For installing the tunnel tool |

---

## Step-by-Step Setup

### Step 1 — Get Your ElevenLabs API Key

1. Log into [ElevenLabs](https://elevenlabs.io)
2. Go to your profile → copy your API key
3. Key starts with `sk_` — keep it handy

### Step 2 — Enable Hermes's API Server

Hermes needs to expose a local endpoint that ElevenLabs can talk to.

```bash
# Find your active profile name
cat ~/.hermes/active_profile
# (If that file doesn't exist, your profile is "main")
```

Open that profile's `.env` file:
```
~/.hermes/profiles/<your-profile>/.env
```

Add these lines:
```
API_SERVER_ENABLED=true
API_SERVER_PORT=8642
API_SERVER_KEY=PASTE_A_RANDOM_KEY_HERE
ELEVENLABS_API_KEY=sk_your_elevenlabs_key
```

Generate a random API key:
```bash
openssl rand -hex 24
```

> 💡 The `API_SERVER_KEY` is just a password so only your setup can connect.

### Step 3 — Pick a Fast Model

A phone call needs **quick replies**. Set Hermes to a fast model — not a slow "reasoning" model, and not a free-tier one. Those stall mid-call and you'll get silence on the line.

The phone uses whatever model Hermes is currently set to, so keep a fast one pinned.

### Step 4 — Start the Gateway + Tunnel

**Install the tunnel tool (once):**
```bash
brew install cloudflared
```

**Start the Hermes gateway:**
```bash
hermes gateway start
```

**Check it's up:**
```bash
curl http://127.0.0.1:8642/health
```
You should see `{"status":"ok"}` or similar.

**Start the tunnel (leave this running):**
```bash
cloudflared tunnel --url http://localhost:8642
```

It prints a public address ending in `.trycloudflare.com`. **Copy it** — that's your link.

### Step 5 — Create the ElevenLabs Agent

1. In the ElevenLabs dashboard → **Conversational AI** → create a new agent
2. In its **LLM settings**, choose **Custom LLM** and set:
   - **URL:** your tunnel address with `/v1` on the end  
     e.g. `https://your-tunnel.trycloudflare.com/v1`
   - **API key:** the `API_SERVER_KEY` you generated in Step 2
3. Save it — ElevenLabs now sends every call to Hermes

### Step 6 — Connect Your Phone Number

1. In ElevenLabs → **Phone** → connect your Twilio account
2. Import your number
3. Assign that number to the agent you just made

### Step 7 — Call It! 📞

Dial your number. The agent picks up. Try:
- *"What can you do?"*
- *"Check my balance."*

It runs the task on your Mac and answers out loud.

---

## ⚠️ Important — Keep It Safe

This number is a **live line to an agent that can run commands on your Mac**. Treat it like a key to your computer.

- 🔒 **Keep the number private.** Don't read it out on a recording.
- ✍️ Say **"draft"** not **"send"** until you trust it.

---

## How to Turn It Off (Kill Switch)

| Action | Command |
|---|---|
| Stop the tunnel | `Ctrl+C` in the cloudflared window (or `pkill -f cloudflared`) |
| Unassign number | In ElevenLabs → Phone → unassign the number from the agent |

> No tunnel = no line. That's your instant kill-switch. Anyone who had the number now reaches nothing. To turn it back on, start the tunnel again and re-assign the number.

---

## Voice AI Alternatives

ElevenLabs isn't the only option for adding voice to your AI agent. Here's a comparison of three popular platforms:

| Feature | **ElevenLabs** | **VoiceWave AI** | **PYXA AI** |
|---|---|---|---|
| **Core Strength** | Ultra-realistic voice cloning & expressive speech | Voice generation with API-first approach | AI voice agents for business automation |
| **Voice Quality** | Industry-leading, highly natural | High quality, good for most use cases | Business-grade, professional tone |
| **API / Integration** | REST API, SDKs, Conversational AI platform | REST API, developer-friendly | REST API, built for agent workflows |
| **Custom Voice Cloning** | ✅ Yes (premium) | ✅ Yes | ✅ Yes |
| **Real-time Streaming** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Phone/Twilio Integration** | ✅ Native phone number support | ⚠️ Via custom setup | ✅ Built for telephony |
| **Pricing** | Free tier (10k chars/mo), paid from $5/mo | Competitive, usage-based | Custom pricing (business-focused) |
| **Best For** | Creators, developers, most polished output | Developers wanting quick API integration | Businesses automating customer-facing calls |
| **Conversational AI** | ✅ Full agent platform with LLM integration | ⚠️ Requires external LLM | ✅ Built-in conversation design |

### When to Choose an Alternative

- **VoiceWave AI** — Choose if you want a simpler API, lower cost, or are building a custom voice pipeline without needing the full ElevenLabs ecosystem.
- **PYXA AI** — Choose if you're building business-grade voice agents (customer service, sales calls) and want purpose-built telephony features out of the box.

> 💡 **Tip:** All three can work with Hermes via the same Custom LLM pattern. Just swap the ElevenLabs agent URL for your chosen provider's endpoint.

---

## Related

- [[01-Hermes-Agent-OS|Post #1: Hermes Agent OS System]]
- [[01-Hermes-Email-Agent|Hermes Email Agent]]
- [[SOP - Agent OS Setup]]
