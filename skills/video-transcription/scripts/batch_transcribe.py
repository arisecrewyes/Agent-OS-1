#!/usr/bin/env python3
"""
batch_transcribe.py - Transcribe multiple videos from a course or playlist.

Usage:
    python3 batch_transcribe.py --urls-file urls.txt --output ./transcripts --model tiny
    python3 batch_transcribe.py --url "https://youtube.com/watch?v=abc" --url "https://vimeo.com/xyz"

Input file format (urls.txt):
    # Comment
    Module 1 - Intro | https://youtube.com/watch?v=abc123
    Module 2 - Setup | https://vimeo.com/456789
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def extract_video_id_youtube(url: str) -> str | None:
    """Extract YouTube video ID from various URL formats."""
    patterns = [
        r'(?:v=|youtu\.be/|embed/|shorts/)([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_youtube_transcript(video_id: str, output_path: Path) -> bool:
    """Try to get YouTube captions via youtube-transcript-api."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        txt_path = output_path.with_suffix('.txt')
        srt_path = output_path.with_suffix('.srt')
        
        # Write plain text
        with open(txt_path, 'w') as f:
            for entry in transcript:
                f.write(f"{entry['text']}\n")
        
        # Write SRT with timestamps
        with open(srt_path, 'w') as f:
            for i, entry in enumerate(transcript, 1):
                start = entry['start']
                duration = entry.get('duration', 3.0)
                end = start + duration
                
                def fmt_time(t):
                    h = int(t // 3600)
                    m = int((t % 3600) // 60)
                    s = t % 60
                    return f"{h:02d}:{m:02d}:{s:06.3f}".replace('.', ',')
                
                f.write(f"{i}\n")
                f.write(f"{fmt_time(start)} --> {fmt_time(end)}\n")
                f.write(f"{entry['text']}\n\n")
        
        return True
    except ImportError:
        print("  youtube-transcript-api not installed, skipping")
        return False
    except Exception as e:
        print(f"  YouTube transcript failed: {e}")
        return False


def download_audio(url: str, output_path: Path, cookies_file: str | None = None) -> bool:
    """Download audio from URL using yt-dlp."""
    cmd = ["yt-dlp", "-x", "--audio-format", "mp3", "-o", str(output_path.with_suffix('.mp3'))]
    
    if cookies_file and os.path.exists(cookies_file):
        cmd.extend(["--cookies", cookies_file])
    
    cmd.append(url)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0 and output_path.with_suffix('.mp3').exists()


def transcribe_audio(audio_path: Path, output_dir: Path, model: str = "base") -> bool:
    """Transcribe audio file using Whisper."""
    cmd = [
        "whisper", str(audio_path),
        "--model", model,
        "--output_format", "txt",
        "--output_dir", str(output_dir)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def parse_urls_file(filepath: Path) -> list[tuple[str, str]]:
    """Parse a URLs file with optional titles."""
    entries = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '|' in line:
                title, url = line.split('|', 1)
                entries.append((title.strip(), url.strip()))
            else:
                entries.append(("", line))
    return entries


def main():
    parser = argparse.ArgumentParser(description="Batch transcribe videos")
    parser.add_argument("--urls-file", type=Path, help="File with URLs (one per line, optional 'Title | URL' format)")
    parser.add_argument("--url", action="append", help="Individual URL (can repeat)")
    parser.add_argument("--output", type=Path, default=Path("./transcripts"), help="Output directory")
    parser.add_argument("--model", default="tiny", choices=["tiny", "base", "small", "medium", "large"], help="Whisper model")
    parser.add_argument("--cookies", type=Path, help="Cookies file for authenticated content")
    args = parser.parse_args()
    
    # Collect URLs
    entries = []
    if args.urls_file:
        entries.extend(parse_urls_file(args.urls_file))
    if args.url:
        for u in args.url:
            entries.append(("", u))
    
    if not entries:
        print("No URLs provided. Use --urls-file or --url")
        sys.exit(1)
    
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Metadata
    metadata = {
        "created": datetime.now().isoformat(),
        "model": args.model,
        "total_videos": len(entries),
        "results": []
    }
    
    print(f"=== Batch Transcription ===")
    print(f"Videos: {len(entries)}")
    print(f"Model: {args.model}")
    print(f"Output: {args.output}")
    print()
    
    for i, (title, url) in enumerate(entries, 1):
        video_id = extract_video_id_youtube(url) or f"video_{i:03d}"
        display_name = title or video_id
        
        print(f"[{i}/{len(entries)}] {display_name}")
        print(f"  URL: {url}")
        
        result = {
            "title": title,
            "url": url,
            "video_id": video_id,
            "method": None,
            "success": False,
            "output_file": None
        }
        
        # Method 1: YouTube transcript API
        if extract_video_id_youtube(url):
            print("  Trying YouTube transcript API...")
            out_path = args.output / f"{video_id}_captions"
            if get_youtube_transcript(extract_video_id_youtube(url), out_path):
                result["method"] = "youtube_transcript_api"
                result["success"] = True
                result["output_file"] = str(out_path.with_suffix('.txt'))
                print("  ✅ Captions downloaded!")
                metadata["results"].append(result)
                continue
        
        # Method 2: yt-dlp + Whisper
        print("  Downloading audio via yt-dlp...")
        audio_path = args.output / f"{video_id}_audio"
        if download_audio(url, audio_path, str(args.cookies) if args.cookies else None):
            print("  Audio downloaded. Transcribing with Whisper...")
            if transcribe_audio(audio_path.with_suffix('.mp3'), args.output, args.model):
                result["method"] = "yt_dlp_whisper"
                result["success"] = True
                result["output_file"] = str(args.output / f"{video_id}_audio.txt")
                print("  ✅ Transcription complete!")
                # Cleanup
                audio_path.with_suffix('.mp3').unlink(missing_ok=True)
            else:
                print("  ❌ Whisper transcription failed")
        else:
            print("  ❌ Audio download failed (may need cookies or screen recording)")
        
        metadata["results"].append(result)
    
    # Save metadata
    meta_path = args.output / "batch_metadata.json"
    with open(meta_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    # Summary
    succeeded = sum(1 for r in metadata["results"] if r["success"])
    failed = sum(1 for r in metadata["results"] if not r["success"])
    
    print()
    print(f"=== Complete ===")
    print(f"✅ Success: {succeeded}/{len(entries)}")
    print(f"❌ Failed: {failed}/{len(entries)}")
    print(f"Metadata: {meta_path}")


if __name__ == "__main__":
    main()
