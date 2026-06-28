#!/bin/bash
# transcribe.sh - Transcribe a video URL to text
# Usage: ./transcribe.sh <VIDEO_URL> [MODEL] [OUTPUT_DIR]
# Example: ./transcribe.sh "https://youtube.com/watch?v=abc123" base ./transcripts

set -euo pipefail

URL="${1:?Usage: transcribe.sh <VIDEO_URL> [MODEL] [OUTPUT_DIR]}"
MODEL="${2:-base}"
OUTPUT_DIR="${3:-./transcripts}"
COOKIES_FILE="${4:-}"

mkdir -p "$OUTPUT_DIR"

echo "=== Video Transcription ==="
echo "URL: $URL"
echo "Model: $MODEL"
echo "Output: $OUTPUT_DIR"
echo ""

# Step 1: Try to get captions directly (YouTube, supported platforms)
echo "[1/3] Attempting caption download via yt-dlp..."
if yt-dlp --write-auto-sub --sub-lang en --skip-download \
   -o "$OUTPUT_DIR/captions.%(ext)s" "$URL" 2>/dev/null; then
   echo "✅ Captions downloaded!"
   CAPTION_FILE=$(find "$OUTPUT_DIR" -name "captions.*" | head -1)
   if [ -n "$CAPTION_FILE" ]; then
      echo "Caption file: $CAPTION_FILE"
      exit 0
   fi
fi
echo "⚠️  No captions available, falling back to audio transcription..."

# Step 2: Download audio
echo "[2/3] Downloading audio..."
AUDIO_FILE="$OUTPUT_DIR/audio.mp3"
if [ -n "$COOKIES_FILE" ]; then
   yt-dlp --cookies "$COOKIES_FILE" -x --audio-format mp3 -o "$AUDIO_FILE" "$URL"
else
   yt-dlp -x --audio-format mp3 -o "$AUDIO_FILE" "$URL"
fi

if [ ! -f "$AUDIO_FILE" ]; then
   echo "❌ Failed to download audio. Try with cookies or use screen recording method."
   exit 1
fi

echo "✅ Audio downloaded: $AUDIO_FILE"

# Step 3: Transcribe with Whisper
echo "[3/3] Transcribing with Whisper (model: $MODEL)..."
whisper "$AUDIO_FILE" \
   --model "$MODEL" \
   --output_format txt \
   --output_dir "$OUTPUT_DIR"

echo ""
echo "=== Transcription Complete ==="
echo "Output files in: $OUTPUT_DIR"
ls -la "$OUTPUT_DIR"

# Cleanup
rm -f "$AUDIO_FILE"
echo "Temporary audio file removed."
