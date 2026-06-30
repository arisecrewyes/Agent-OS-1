# VoiceWave AI — Capability Audit

> **Audit Date:** 2026-06-30
> **Audit Status:** ✅ Complete
> **Platform:** https://space.voicewave.ai
> **Account:** Without (WithoutRecourse)

---

## 1. PLAN & LIMITS

| Resource | Limit |
|----------|-------|
| Voices | 2495+ professional voices |
| Languages | 38 |
| Characters per generation | 20,000 |
| Editor modes | Simple / Conversation |
| Export formats | WAV, MP3 (toggle in toolbar) |
| Workspace duration | Adjustable (01:00 default, expandable) |
| Background music library | Included |
| Commercial rights | Full (YouTube, courses, audiobooks, client work) |
| License | Lifetime |

---

## 2. TOOLS & FEATURES AUDIT

### ✅ 2.1 Text-to-Speech Generator
- Type or paste text (up to 20,000 chars)
- Select from 2495+ voices
- AI auto-detects emotion from punctuation/context ("I can't believe it!" → surprised tone)
- Click "Generate" → audio appears in editor as a clip

### ✅ 2.2 Multi-Track Audio Editor
- **Interface:** Full waveform DAW (Digital Audio Workstation)
- **Tracks:** Multiple (Voice 1, Track 0, Track 1 visible)
- **Playback:** Play button, time display (00:00 / 01:00)
- **Editing:** Cut, drag, trim, timing adjustment
- **Undo/Redo:** Full history
- **Zoom:** Visual zoom slider for waveform
- **Labels:** Toggle voice name labels on clips
- **Clear:** Remove all tracks

### ✅ 2.3 Voice Cloning
- **Method 1:** Upload audio file (MP3, WAV, M4A, OGG — 10s min, 20MB max)
- **Method 2:** Record voice directly in browser (tab: "Record Voice")
- **Requirements:** 10-15 seconds of clean speech, complete sentences, no pauses
- **Capture:** Emotion, energy, tone, pacing all carry through
- **Languages:** All 38 supported
- **Consent checkbox:** Must confirm ownership/permission
- **Status:** Cloning just got more expressive (recent update per announcement)

### ✅ 2.4 Voice Design (Create From Scratch)
- Describe voice in natural language
- AI generates custom voice instantly
- Examples from landing page:
  - "Male, 60s, deep voice with slight rasp, slow and steady"
  - "Young female, bright American accent, bubbly tone"
  - "Eccentric male, British accent, high-pitched, enthusiastic"
- 30+ preset voice archetypes available

### ✅ 2.5 Conversation Mode
- Toggle: Simple ↔ Conversation mode
- Switch in editor mode selector
- Purpose: Multi-voice conversations / dialogues

### ✅ 2.6 Background Music Library
- Add background music from library
- Layer under voice tracks

### ✅ 2.7 Export
- **Formats:** WAV, MP3 (toggle in toolbar)
- **One click export** from toolbar

### ✅ 2.8 Default Voice
- Currently selected: Luna Smith (Warm, engaging female voice)

---

## 3. LANGUAGES (38)

English, Afrikaans, Arabic, Bulgarian, Catalan, Chinese, Chinese Cantonese, Croatian, Czech, Danish, Dutch, Filipino, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Malay, Norwegian, Norwegian Nynorsk, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Spanish, Swedish, Thai, Turkish, Ukrainian, Vietnamese

---

## 4. POPULAR VOICES

| Voice | Style | Best For |
|-------|-------|----------|
| Luna | Warm, engaging female | Storytelling, narration |
| Marcus | Deep, professional male | Documentaries, explainers |
| Oliver | Expressive, versatile male | Any content |

---

## 5. WHAT VOICEWAVE AI CAN DO (Confirmed)

1. **Generate professional voiceovers** — 2495+ voices, 38 languages
2. **Clone custom voices** — 10-15s audio sample
3. **Design custom voices** — natural language description
4. **Multi-track editing** — layer voices, trim, cut, timing
5. **Background music** — add from library
6. **Export audio** — WAV, MP3
7. **Conversation mode** — multi-voice dialogues
8. **Emotion detection** — automatic from text context
9. **Commercial use** — full rights, YouTube, courses, client work
10. **Record voice input** — browser microphone
11. **Upload audio files** — MP3, WAV, M4A, OGG

---

## 6. WHAT VOICEWAVE AI CANNOT DO (Confirmed Limitations)

1. **No public API** — browser only
2. **No direct social media integration** — no auto-post
3. **No real-time generation** — requires Generate click each time
4. **No pronunciation editor** — can't manually adjust phonemes
5. **No SSML support** — no speech synthesis markup
6. **No batch processing** — one generation at a time
7. **No direct video integration** — audio only (export then import to video tool)
8. **No webhook/callback** — no automation triggers
9. **20,000 char limit per generation** — must split long content
10. **No collaboration** — single user session only

---

## 7. INTEGRATION POTENTIAL

### For Agent OS / OpenClaw
- **Browser automation** — can generate voiceovers on demand
- **Workflow:** Write script (Pyxa AI/Hermes) → Generate voiceover (VoiceWave) → Download WAV/MP3
- **Content pipeline:** Scripts → VoiceWave → video editor (Pyxa AI Video Pro/ArtSpace)

### For n8n / Hermes
- **No direct API** — must use browser automation
- **Possible workaround:** Pre-generate voice libraries, store as assets
- **Batch limitation:** Must generate one script at a time

---

## 8. CONTENT PIPELINE POSITION

```
[Script Writing] → [VoiceWave AI (voiceover)] → [Video Editor] → [Content 360 (post)]
                      ↓
               [Download WAV/MP3]
```

---

## 9. RELIABILITY & NOTES

- **Session stability:** Good — lifetime license, session persists
- **UI quality:** Professional DAW-style interface
- **Voice quality:** Described as "not robotic" — natural emotion
- **New features:** Announcement says voices "just got significantly better"
- **Recommendation:** Primary voice AI for Agent OS content pipeline
