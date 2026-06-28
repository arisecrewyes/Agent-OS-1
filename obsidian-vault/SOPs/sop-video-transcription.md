# SOP: Video Transcription & Media Extraction

**Purpose:** Extract text content from any online video — courses, tutorials, webinars, YouTube, Vimeo, Wistia, and custom video players.

**Trigger:** "Transcribe this video" / "Extract text from course videos" / "Get captions from [URL]" / "Convert video to text"

---

## Overview

This SOP defines a **platform-agnostic approach** to extracting text from online video content. It uses a cascading strategy — trying the fastest, most reliable method first, then falling back to more intensive approaches.

### Capability Matrix

| Method | Speed | Accuracy | Works On | Requirements |
|---|---|---|---|
| 1. Platform transcript API | ⚡ Instant | ★★★★★ | YouTube, some LMS | yt-dlp / youtube-transcript-api |
| 2. DOM caption scraping | ⚡ Instant | ★★★★☆ | Players with captions (Plyr, Video.js, etc.) | Browser automation |
| 3. yt-dlp audio download + Whisper | 🐢 Slow | ★★★★★ | Any platform yt-dlp supports | yt-dlp + ffmpeg + whisper |
| 4. Screen recording + OCR fallback | 🐢🐢 Slowest | ★★★☆☆ | Any visible video | ffmpeg + tesseract |

---

## Method 1: Platform Transcript API (YouTube & Supported Sites)

### When to use
- Video is hosted on YouTube, or any of the 1000+ sites yt-dlp supports
- Platform provides auto-generated or manual captions

### Process

```bash
# Install tools (one-time)
pip install --break-system-packages youtube-transcript-api yt-dlp

# Get YouTube auto-captions
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "%(id)s" "VIDEO_URL"

# OR using Python for more control
python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
import sys
video_id = sys.argv[1]
transcript = YouTubeTranscriptApi.get_transcript(video_id)
for entry in transcript:
    print(f'[{entry[\"start\"]:.1f}] {entry[\"text\"]}')
" "VIDEO_ID"
```

### Output
- Raw VTT/SRT file with timestamps
- Plain text transcript
- JSON with timing data

---

## Method 2: DOM Caption Scraping (Browser-Based)

### When to use
- Video is embedded in a course platform (ClientClub, Teachable, Kajabi, Thinkific, etc.)
- Player has captions/subtitles toggle (Plyr, Video.js, JW Player, etc.)
- Captions exist but aren't directly downloadable

### Process

**Step 1: Detect the video player and caption state**
```javascript
// Run in browser console or via browser evaluate
const tracks = document.querySelectorAll('track');
const video = document.querySelector('video');
const textTracks = video ? Array.from(video.textTracks) : [];
const hasPlyr = document.querySelector('.plyr') !== null;
const hasVideoJS = document.querySelector('.video-js') !== null;
```

**Step 2: Enable captions if they exist**
```javascript
// For Plyr.js players
const captionBtn = document.querySelector('.plyr__controls__item.plyr__control');
if (captionBtn) captionBtn.click();

// For native HTML5 video
if (video && video.textTracks.length > 0) {
    video.textTracks[0].mode = 'showing';
}
```

**Step 3: Extract caption text from the DOM**
```javascript
// After enabling captions, the caption text appears in a display element
const captions = document.querySelector('.plyr__captions, .vjs-text-track-display, .mejs-captions-text');
if (captions) {
    // Capture text over time as video plays
    const interval = setInterval(() => {
        console.log(captions.textContent);
    }, 2000);
}
```

**Step 4: For blob URL videos with no captions**
If the video source is a `blob:` URL and no captions exist, proceed to Method 3.

---

## Method 3: yt-dlp Audio Download + Whisper Transcription

### When to use
- No transcripts available from the platform
- Video is downloadable via yt-dlp
- Highest accuracy is needed

### Process

**Step 1: Install dependencies**
```bash
# ffmpeg (required by Whisper for audio processing)
brew install ffmpeg

# Whisper (OpenAI's speech recognition)
pip install --break-system-packages openai-whisper

# yt-dlp (video/audio downloader)
pip install --break-system-packages yt-dlp
```

**Step 2: Download audio only**
```bash
# Extract audio as MP3 (smallest, fastest)
yt-dlp -x --audio-format mp3 -o "audio.%(ext)s" "VIDEO_URL"

# OR for authenticated/private videos, use cookies
yt-dlp --cookies-from-browser openclaw -x --audio-format mp3 -o "audio.%(ext)s" "VIDEO_URL"
```

**Step 3: Transcribe with Whisper**
```bash
# Basic transcription (uses 'base' model — good balance of speed/accuracy)
whisper audio.mp3 --model base --output_format txt -o transcript

# Higher accuracy (slower)
whisper audio.mp3 --model medium --output_format txt -o transcript

# With timestamps
whisper audio.mp3 --model base --output_format srt -o transcript
```

**Step 4: For blob URL videos (not directly downloadable)**
```bash
# Use ffmpeg to capture the browser audio output
# First, get the actual media URL from browser network tab or JS:
# video.src or video.currentSrc (if not blob)

# If truly blob-only, use screen recording (Method 4)
```

### Performance Notes
| Model | Speed | Accuracy | VRAM Needed |
|---|---|---|---|
| tiny | ⚡⚡⚡ Fastest | ★★★☆☆ | ~1GB |
| base | ⚡⚡ Fast | ★★★★☆ | ~1GB |
| medium | 🐢 Slow | ★★★★★ | ~5GB |
| large | 🐢🐢 Slowest | ★★★★★ | ~10GB |

For a 2-core, 8GB VPS: use `tiny` or `base` model.

---

## Method 4: Screen Recording + OCR (Universal Fallback)

### When to use
- Video is DRM-protected or blob-only
- yt-dlp doesn't support the platform
- All other methods fail

### Process

**Step 1: Record the video playback**
```bash
# Record screen area while video plays (Linux/X11)
ffmpeg -f x11grab -video_size 1920x1080 -i :0.0+0,0 -t 300 -r 15 output.mp4

# OR record specific window
ffmpeg -f x11grab -i :0.0+100,100 -t 300 recording.mp4
```

**Step 2: Extract audio from recording**
```bash
ffmpeg -i recording.mp4 -vn -acodec mp3 audio.mp3
```

**Step 3: Transcribe with Whisper**
```bash
whisper audio.mp3 --model base --output_format txt -o transcript
```

**Step 4: OCR on-screen text (optional, for slides/demos)**
```bash
# Install tesseract
brew install tesseract

# Extract frames every 5 seconds
ffmpeg -i recording.mp4 -vf "fps=1/5" frame_%03d.png

# OCR each frame
for frame in frame_*.png; do
    tesseract "$frame" "${frame%.png}" >> ocr_output.txt
done
```

---

## Platform-Specific Notes

### ClientClub / GHL Membership (learn.blackumbrella.app, etc.)
- Video player: Plyr.js
- Captions: UI button exists but often no caption data
- Video source: blob URLs (not directly downloadable)
- **Best method:** Method 4 (screen record + Whisper) or check if platform has a "download" option

### YouTube
- **Best method:** Method 1 (youtube-transcript-api or yt-dlp --write-auto-sub)
- Supports auto-generated and manual captions in 100+ languages

### Vimeo
- **Best method:** Method 1 (yt-dlp) or Method 3
- Some videos have downloadable captions via Vimeo API

### Teachable / Kajabi / Thinkific
- **Best method:** Method 2 (DOM scraping) or Method 3 (yt-dlp)
- Often use Wistia or Video.js players with caption tracks

### Wistia
- **Best method:** Method 3 (yt-dlp supports Wistia)
- Captions often available as .vtt files in page source

### Custom/Proprietary Players
- **Best method:** Method 4 (screen recording fallback)

---

## Output Format

All methods produce a standardized output:

```
transcripts/
├── {video_id}_metadata.json    # Title, URL, duration, platform, method used
├── {video_id}_transcript.txt   # Plain text transcript
├── {video_id}_transcript.srt   # Timestamped SRT (when available)
└── {video_id}_ocr.txt          # OCR text from slides (when applicable)
```

---

## Integration with Course Access SOP

When the Course Access SOP encounters video content:

1. Check if video lessons have transcripts (Method 2 — quick DOM check)
2. If yes → scrape and save transcript text
3. If no → flag for transcription via Method 3 or 4
4. Save all transcripts alongside the course analysis docs
5. Reference transcripts in the course analysis for deeper pattern extraction

---

## Security & Ethics

- Only transcribe content you have legitimate access to
- Don't redistribute transcripts of paid content
- Respect platform Terms of Service
- Use transcripts for personal/educational analysis only
- Delete temporary audio/video files after transcription
