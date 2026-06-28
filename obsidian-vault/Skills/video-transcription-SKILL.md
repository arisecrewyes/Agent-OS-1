---
name: video-transcription
description: "Extract text from any online video — courses, tutorials, webinars, YouTube, Vimeo, and custom players. Use DOM caption scraping, platform transcript APIs, yt-dlp + Whisper transcription, or screen recording fallback."
tags: [video, transcription, captions, whisper, yt-dlp, browser]
---

# Video Transcription Skill

Extract text content from any online video. Uses a cascading strategy from fastest to most intensive.

## When to Use

- "Transcribe this video: [URL]"
- "Extract text from course videos"
- "Get captions/subtitles from [platform]"
- "Convert video to text"
- Course Access SOP encounters video content

## Dependencies

| Tool | Install Command | Purpose |
|---|---|---|
| yt-dlp | `pip install yt-dlp` | Download audio from 1000+ sites |
| openai-whisper | `pip install openai-whisper` | Speech-to-text transcription |
| faster-whisper | `pip install faster-whisper` | Faster alternative to openai-whisper |
| ffmpeg | `brew install ffmpeg` | Audio extraction & processing |
| tesseract | `brew install tesseract` | OCR for on-screen text/slides |
| youtube-transcript-api | `pip install youtube-transcript-api` | Get YouTube captions directly |

## Strategy Cascade

Try methods in order. Stop when you get a usable transcript.

### Method 1: Platform Transcript API (⚡ Fastest — YouTube, some LMS)

```bash
# YouTube captions
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "video" "VIDEO_URL"

# OR via Python for YouTube
python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
import json, sys
tid = YouTubeTranscriptApi.get_transcript(sys.argv[1])
for e in tid: print(f'{e[\"start\"]:.1f}s: {e[\"text\"]}')
" "VIDEO_ID"
```

**Output:** `.vtt` or `.srt` file with timed captions.

### Method 2: DOM Caption Scraping (⚡ Fast — Browser players with captions)

For Plyr.js, Video.js, JW Player, and other HTML5 players:

```javascript
// Step 1: Detect captions
document.querySelectorAll('track')  // <track kind="captions">
video.textTracks                    // Native text tracks

// Step 2: Enable captions
video.textTracks[0].mode = 'showing'
// OR click the CC button document.querySelector('.plyr__control--captions')?.click()

// Step 3: Extract caption text over time
setInterval(() => {
  const cap = document.querySelector('.plyr__captions, .vjs-text-track-display')
  if (cap) return cap.textContent
}, 2000)
```

**Works on:** Plyr, Video.js, JW Player, ME.js, native `<video>` with `<track>`.

### Method 3: yt-dlp + Whisper (🐢 Slow — Any downloadable video)

```bash
# Download audio only (no video needed)
yt-dlp -x --audio-format mp3 -o "audio.%(ext)s" "VIDEO_URL"

# For private/authenticated videos, pass browser cookies
yt-dlp --cookies-from-browser openclaw -x --audio-format mp3 -o "audio.%(ext)s" "VIDEO_URL"

# Transcribe
whisper audio.mp3 --model base --output_format txt -o transcript
whisper audio.mp3 --model base --output_format srt -o transcript  # With timestamps

# For VPS with limited RAM (2-4GB), use tiny model
whisper audio.mp3 --model tiny --output_format txt -o transcript
```

**yt-dlp supports:** YouTube, Vimeo, Wistia, Facebook, Twitter, Dailymotion, Twitch, and 1000+ more.

### Method 4: Screen Recording + Whisper (🐢🐢 Slowest — Universal fallback)

When the video is DRM-protected, blob-only, or on an unsupported platform:

```bash
# Step 1: Use browser to play the video, record audio from browser output
# (Browser automation handles playback)

# Step 2: Extract audio from recording
ffmpeg -i recording.mp4 -vn -acodec mp3 audio.mp3

# Step 3: Transcribe
whisper audio.mp3 --model base --output_format txt -o transcript

# Optional: OCR on-screen text from frames
ffmpeg -i recording.mp4 -vf "fps=1/5" frame_%03d.png
for f in frame_*.png; do tesseract "$f" - >> ocr_text.txt; done
```

## Platform-Specific Playbooks

### ClientClub / GHL Membership (learn.blackumbrella.app, etc.)
- Player: Plyr.js
- Video source: blob URLs (not directly downloadable via yt-dlp)
- Captions: UI button exists but often no actual caption data
- **Recommended:** Method 4 (screen record + Whisper) or ask user for supplementary materials

### YouTube
- **Recommended:** Method 1 (auto-captions via youtube-transcript-api)
- Auto-generated captions in 100+ languages
- Manual captions when available

### Teachable / Kajabi / Thinkific
- Player: Often Wistia or Video.js
- **Recommended:** Method 2 (DOM scrape) → Method 3 (yt-dlp)

### Vimeo
- **Recommended:** Method 3 (yt-dlp)
- Some videos have API-accessible captions

### Wistia
- **Recommended:** Method 3 (yt-dlp supports Wistia embeds)
- Captions often in `.vtt` files visible in page source

### Loom
- **Recommended:** Method 3 (yt-dlp supports loom.com)
- Loom also provides auto-captions in-player

### Custom/Proprietary Players (ClientClub, etc.)
- **Recommended:** Method 4 (universal fallback)

## Workflow for Course Video Transcription

When transcribing all videos in a course:

1. **Get the lesson list** from the course syllabus (via browser snapshot)
2. **For each lesson:**
   a. Navigate to the lesson page
   b. Check for `<track>` elements or caption data (Method 2)
   c. If captions found → extract text over playback duration
   d. If no captions → check if video URL is downloadable (Method 3)
   e. If blob/DRM → flag for Method 4 (batch screen recording)
3. **Save to:** `course-analysis/transcripts/{module}_{lesson}_transcript.txt`
4. **Include timestamps** when available for reference

## Output Format

```
transcripts/
├── metadata.json          # Platform, method used, accuracy estimate
├── transcript.txt         # Plain text
├── transcript.srt         # Timestamped (when available)
└── ocr_text.txt          # On-screen text from OCR (when applicable)
```

## Performance Guide for VPS (2-core, 8GB RAM)

| Whisper Model | RAM | Speed on 5-min audio | Quality |
|---|---|---|---|
| tiny | ~500MB | ~30 seconds | Good enough for transcripts |
| base | ~1GB | ~1-2 minutes | Very good |
| medium | ~3GB | ~5-10 minutes | Excellent |
| large | ~6GB | ~15+ minutes | Overkill for most uses |

**Recommendation:** Use `tiny` for batch course transcription, `base` for final output.

## Security Notes

- Only transcribe content the user has legitimate access to
- Don't redistribute transcripts of paid content
- Use `--cookies-from-browser` for authenticated content, never store credentials
- Delete temporary audio/video files after transcription complete
- Respect platform Terms of Service

## Troubleshooting

| Problem | Solution |
|---|---|
| yt-dlp can't find video | Try `--cookies-from-browser openclaw` |
| Whisper out of memory | Use `--model tiny` instead of base |
| blob URL video | Must use Method 4 (screen recording) |
| No captions at all | Method 3 (yt-dlp + Whisper) |
| Partial captions | Combine Method 2 + Method 3 for gaps |

## See Also

- Full SOP: `docs/sop-video-transcription.md`
- Course Access SOP: `docs/sop-course-access-and-implementation.md`
