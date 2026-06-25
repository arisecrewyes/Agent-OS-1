import os
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import requests


class ExtractRequest(BaseModel):
    text: str


class MemoryRequest(BaseModel):
    category: str = "fact"
    content: str
    tags: list = []

VAULT_PATH = os.getenv("VAULT_PATH", "/data/obsidian-vault")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
LLM_MODEL = os.getenv("LLM_MODEL", "openrouter/owl-alpha")

Path(VAULT_PATH).mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Memory Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def call_llm(prompt, max_tokens=500):
    if not OPENROUTER_API_KEY:
        return json.dumps({"error": "No API key"})
    try:
        r = requests.post(
            OPENROUTER_BASE_URL + "/chat/completions",
            headers={
                "Authorization": "Bearer " + OPENROUTER_API_KEY,
                "Content-Type": "application/json",
                "HTTP-Referer": "https://agentos.srv1121935.hstgr.cloud",
                "X-Title": "Memory Engine",
            },
            json={
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a memory extraction AI. Always respond with valid JSON."},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": max_tokens,
                "temperature": 0.3,
            },
            timeout=30,
        )
        if r.status_code == 200:
            data = r.json()
            return data["choices"][0]["message"]["content"]
        return json.dumps({"error": "API error: " + str(r.status_code)})
    except Exception as e:
        return json.dumps({"error": str(e)})


def parse_llm_response(response):
    # Strip whitespace
    response = response.strip()
    # Try to extract JSON from markdown code blocks
    code_block = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", response, re.DOTALL)
    if code_block:
        json_str = code_block.group(1).strip()
    else:
        # Find the first { to last }
        start = response.find("{")
        end = response.rfind("}")
        if start != -1 and end != -1:
            json_str = response[start:end+1]
        else:
            return []
    try:
        data = json.loads(json_str)
        # Try memories key first
        if "memories" in data:
            return data["memories"]
        # Some models return entities or results instead
        for key in ["entities", "results", "data", "items", "extracted"]:
            if key in data and isinstance(data[key], list):
                # Try to normalize the format
                normalized = []
                for item in data[key]:
                    if isinstance(item, dict):
                        normalized.append({
                            "category": item.get("category", item.get("type", "fact")),
                            "content": item.get("content", item.get("text", item.get("name", str(item)))),
                            "tags": item.get("tags", []),
                        })
                return normalized
        return []
    except (json.JSONDecodeError, AttributeError):
        return []


EXTRACT_PROMPT = (
    "Your ONLY job is to extract memorable information from the text below. "
    "Return a raw JSON object and nothing else. Do not wrap in markdown. Do not add explanations.\n\n"
    "Use this EXACT JSON structure (copy the key names exactly):\n"
    '{"memories": [{"category": "goal or preference or project or task or person or habit or fact or quote", '
    '"content": "the extracted memory as a short sentence", "tags": ["keyword1", "keyword2"]}]}\n\n'
    "Examples of good output:\n"
    '{"memories": [{"category": "person", "content": "Julian Goldie is an SEO expert", "tags": ["SEO", "expert"]}]}\n\n'
    "Now analyze this text:\n"
)


async def extract_memories(text):
    response = call_llm(EXTRACT_PROMPT + text)
    return parse_llm_response(response)


def get_memory_file(category):
    today = datetime.now().strftime("%Y-%m-%d")
    mem_dir = Path(VAULT_PATH) / "Memories" / category
    mem_dir.mkdir(parents=True, exist_ok=True)
    return mem_dir / (today + ".md")


def get_all_memories_file():
    mem_dir = Path(VAULT_PATH) / "Memories"
    mem_dir.mkdir(parents=True, exist_ok=True)
    return mem_dir / "Memory_Index.md"


def save_memory(category, content, tags):
    mem_file = get_memory_file(category)
    tag_str = " ".join(["#" + t for t in tags]) if tags else ""
    entry = "- " + content + " " + tag_str + " (" + datetime.now().strftime("%Y-%m-%d %H:%M") + ")\n"
    if mem_file.exists():
        existing = mem_file.read_text(encoding="utf-8")
        mem_file.write_text(existing + entry, encoding="utf-8")
    else:
        header = "# " + category.title() + "\n\n"
        mem_file.write_text(header + entry, encoding="utf-8")
    update_memory_index(category, content, tags)
    return {"status": "saved", "category": category, "file": str(mem_file)}


def update_memory_index(category, content, tags):
    index_file = get_all_memories_file()
    entry = "- **[" + category + "]** " + content + " (" + ", ".join(tags) + ") - " + datetime.now().strftime("%Y-%m-%d") + "\n"
    if index_file.exists():
        existing = index_file.read_text(encoding="utf-8")
        index_file.write_text(existing + entry, encoding="utf-8")
    else:
        header = "# Memory Index\n\n> Auto-maintained by Memory Engine\n\n"
        index_file.write_text(header + entry, encoding="utf-8")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "memory-engine", "vault_path": VAULT_PATH, "model": LLM_MODEL}


@app.post("/api/extract")
async def extract(req: ExtractRequest):
    if not req.text:
        raise HTTPException(400, "No text provided")
    memories = await extract_memories(req.text)
    saved = []
    for mem in memories:
        result = save_memory(mem.get("category", "fact"), mem.get("content", ""), mem.get("tags", []))
        saved.append({**mem, **result})
    return JSONResponse({"extracted": saved, "count": len(saved)})


@app.post("/api/memory")
async def add_memory(req: MemoryRequest):
    if not req.content:
        raise HTTPException(400, "No content provided")
    result = save_memory(req.category, req.content, req.tags)
    return JSONResponse(result)


@app.get("/api/memories")
async def list_memories(category=None):
    memories = []
    mem_dir = Path(VAULT_PATH) / "Memories"
    if not mem_dir.exists():
        return JSONResponse([])
    if category:
        cat_dir = mem_dir / category
        if cat_dir.exists():
            for f in sorted(cat_dir.rglob("*.md")):
                memories.append({
                    "category": category,
                    "file": str(f.relative_to(mem_dir.parent)),
                    "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
                    "size": f.stat().st_size,
                })
    else:
        for f in sorted(mem_dir.rglob("*.md")):
            memories.append({
                "file": str(f.relative_to(mem_dir.parent)),
                "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
            })
    return JSONResponse(memories)


@app.get("/api/memory")
async def read_memory(file):
    mem_file = Path(VAULT_PATH) / file
    if not mem_file.exists():
        raise HTTPException(404, "Memory file not found")
    return JSONResponse({"file": file, "content": mem_file.read_text(encoding="utf-8")})


@app.get("/api/search")
async def search_memories(query):
    results = []
    mem_dir = Path(VAULT_PATH) / "Memories"
    if not mem_dir.exists():
        return JSONResponse([])
    query_lower = query.lower()
    for f in mem_dir.rglob("*.md"):
        content = f.read_text(encoding="utf-8")
        if query_lower in content.lower():
            matches = []
            for i, line in enumerate(content.split("\n")):
                if query_lower in line.lower():
                    matches.append({"line": i + 1, "text": line.strip()})
            results.append({"file": str(f.relative_to(mem_dir.parent)), "matches": matches})
    return JSONResponse(results)


@app.get("/api/summary")
async def daily_summary():
    today = datetime.now().strftime("%Y-%m-%d")
    mem_dir = Path(VAULT_PATH) / "Memories"
    summary_parts = []
    for cat in ["goal", "task", "project", "person", "preference", "habit", "fact", "quote"]:
        cat_file = mem_dir / cat / (today + ".md")
        if cat_file.exists():
            content = cat_file.read_text(encoding="utf-8")
            summary_parts.append("## " + cat.title() + "\n" + content)
    if summary_parts:
        full_summary = "# Daily Memory Summary - " + today + "\n\n" + "\n\n".join(summary_parts)
    else:
        full_summary = "# Daily Memory Summary - " + today + "\n\nNo memories captured yet today."
    return JSONResponse({"date": today, "summary": full_summary})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
