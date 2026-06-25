"""
Obsidian Vault Web Server
- Web GUI for browsing/editing vault Markdown files
- REST API for agent read/write access
- Compatible with Obsidian vault format
"""
import os
import json
import re
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

VAULT_PATH = os.getenv("VAULT_PATH", "/data/obsidian-vault")
Path(VAULT_PATH).mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Obsidian Vault Server", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── HTML GUI ───────────────────────────────────────────────────────

VAULT_GUI_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🗄️ Obsidian Vault</title>
<style>
:root {
  --bg: #1e1e2e; --surface: #262637; --text: #cdd6f4;
  --accent: #89b4fa; --green: #a6e3a1; --red: #f38ba8;
  --border: #45475a; --muted: #6c7086;
}
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }
#sidebar { width: 280px; background: var(--surface); border-right: 1px solid var(--border); display: flex; flex-direction: column; }
#sidebar-header { padding: 16px; border-bottom: 1px solid var(--border); font-weight: 700; font-size: 16px; }
#sidebar-header span { color: var(--accent); }
#file-list { flex: 1; overflow-y: auto; padding: 8px; }
.file-item { padding: 8px 12px; cursor: pointer; border-radius: 6px; font-size: 13px; display: flex; align-items: center; gap: 8px; }
.file-item:hover { background: var(--border); }
.file-item.active { background: rgba(137,180,250,0.15); color: var(--accent); }
.file-folder { font-weight: 600; color: var(--green); }
.file-icon { font-size: 14px; }
#main { flex: 1; display: flex; flex-direction: column; }
#toolbar { padding: 10px 16px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 12px; }
#toolbar button { background: var(--surface); color: var(--text); border: 1px solid var(--border); padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 13px; }
#toolbar button:hover { border-color: var(--accent); color: var(--accent); }
#toolbar .file-title { font-weight: 600; flex: 1; }
#editor { flex: 1; display: flex; }
#markdown-editor { flex: 1; background: var(--bg); color: var(--text); border: none; padding: 20px; font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 14px; line-height: 1.6; resize: none; outline: none; }
#preview { flex: 1; padding: 20px; overflow-y: auto; border-left: 1px solid var(--border); display: none; }
#preview.active { display: block; }
#preview h1, #preview h2, #preview h3 { color: var(--accent); margin: 16px 0 8px; }
#preview p { margin: 8px 0; line-height: 1.7; }
#preview code { background: var(--surface); padding: 2px 6px; border-radius: 4px; }
#preview pre { background: var(--surface); padding: 16px; border-radius: 8px; overflow-x: auto; }
#preview a { color: var(--accent); }
#status-bar { padding: 4px 16px; border-top: 1px solid var(--border); font-size: 11px; color: var(--muted); display: flex; gap: 16px; }
#search-box { padding: 8px 16px; border-bottom: 1px solid var(--border); }
#search-box input { width: 100%; padding: 8px 12px; background: var(--bg); color: var(--text); border: 1px solid var(--border); border-radius: 6px; outline: none; font-size: 13px; }
#search-box input:focus { border-color: var(--accent); }
</style>
</head>
<body>

<div id="sidebar">
  <div id="sidebar-header">🗄️ <span>Vault</span></div>
  <div id="search-box"><input type="text" id="search" placeholder="Search files..." oninput="filterFiles()"></div>
  <div id="file-list"></div>
</div>

<div id="main">
  <div id="toolbar">
    <span class="file-title" id="current-file">Select a file...</span>
    <button onclick="newFile()">📄 New</button>
    <button onclick="newFolder()">📁 Folder</button>
    <button onclick="saveFile()">💾 Save</button>
    <button onclick="togglePreview()">👁️ Preview</button>
    <button onclick="deleteFile()">🗑️ Delete</button>
  </div>
  <div id="editor">
    <textarea id="markdown-editor" placeholder="Select a file or create a new one..." oninput="markDirty()"></textarea>
    <div id="preview"></div>
  </div>
  <div id="status-bar">
    <span id="status-lines">Lines: 0</span>
    <span id="status-words">Words: 0</span>
    <span id="status-saved">✅ Saved</span>
    <span id="status-vault">Vault: /data/obsidian-vault</span>
  </div>
</div>

<script>
let files = [];
let currentFile = null;
let dirty = false;

async function loadFiles() {
  const r = await fetch('/api/files');
  files = await r.json();
  renderFiles();
}

function renderFiles() {
  const list = document.getElementById('file-list');
  const filter = document.getElementById('search').value.toLowerCase();
  list.innerHTML = files
    .filter(f => f.name.toLowerCase().includes(filter))
    .map(f => `<div class="file-item ${currentFile===f.path?'active':''}" onclick="openFile('${f.path}')">
      <span class="file-icon">${f.is_dir?'📁':'📄'}</span>
      <span class="${f.is_dir?'file-folder':''}">${f.name}</span>
    </div>`).join('');
}

function filterFiles() { renderFiles(); }

async function openFile(path) {
  if (dirty && !confirm('Unsaved changes will be lost. Continue?')) return;
  const r = await fetch('/api/file?path=' + encodeURIComponent(path));
  const data = await r.json();
  if (data.error) return alert(data.error);
  currentFile = path;
  document.getElementById('markdown-editor').value = data.content;
  document.getElementById('current-file').textContent = path;
  dirty = false;
  updateStatus();
  renderFiles();
}

async function saveFile() {
  if (!currentFile) return;
  const content = document.getElementById('markdown-editor').value;
  await fetch('/api/file', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({path: currentFile, content})
  });
  dirty = false;
  document.getElementById('status-saved').textContent = '✅ Saved';
  updateStatus();
}

async function newFile() {
  const name = prompt('File name (e.g., My Note.md):');
  if (!name) return;
  if (!name.endsWith('.md')) name += '.md';
  const path = name;
  await fetch('/api/file', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({path, content: '# ' + name.replace('.md','') + '\n\n'})
  });
  await loadFiles();
  openFile(path);
}

async function newFolder() {
  const name = prompt('Folder name:');
  if (!name) return;
  await fetch('/api/folder', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({path: name})
  });
  await loadFiles();
}

async function deleteFile() {
  if (!currentFile) return;
  if (!confirm('Delete ' + currentFile + '?')) return;
  await fetch('/api/file?path=' + encodeURIComponent(currentFile), {method:'DELETE'});
  currentFile = null;
  document.getElementById('markdown-editor').value = '';
  document.getElementById('current-file').textContent = 'Select a file...';
  await loadFiles();
}

function togglePreview() {
  const preview = document.getElementById('preview');
  const editor = document.getElementById('markdown-editor');
  preview.classList.toggle('active');
  editor.style.display = preview.classList.contains('active') ? 'none' : 'block';
  if (preview.classList.contains('active')) {
    const content = document.getElementById('markdown-editor').value;
    preview.innerHTML = renderMarkdown(content);
  }
}

function renderMarkdown(md) {
  return md
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
    .replace(/\\*(.+?)\\*/g, '<em>$1</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\\[([^\\]]+)\\]\\((.+?)\\)/g, '<a href="$2">$1</a>')
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/\\n/g, '<br>');
}

function markDirty() {
  dirty = true;
  document.getElementById('status-saved').textContent = '⚠️ Unsaved';
  updateStatus();
}

function updateStatus() {
  const content = document.getElementById('markdown-editor').value;
  document.getElementById('status-lines').textContent = 'Lines: ' + content.split('\\n').length;
  document.getElementById('status-words').textContent = 'Words: ' + content.split(/\\s+/).filter(Boolean).length;
}

document.addEventListener('keydown', e => {
  if ((e.ctrlKey || e.metaKey) && e.key === 's') { e.preventDefault(); saveFile(); }
});

loadFiles();
</script>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def gui():
    return HTMLResponse(content=VAULT_GUI_HTML)

# ─── API Endpoints ──────────────────────────────────────────────────

@app.get("/api/files")
async def list_files():
    """List all files and folders in the vault"""
    items = []
    vault = Path(VAULT_PATH)
    for item in sorted(vault.rglob("*")):
        rel = item.relative_to(vault)
        items.append({
            "name": item.name,
            "path": str(rel),
            "is_dir": item.is_dir(),
            "size": item.stat().st_size if item.is_file() else 0,
            "modified": datetime.fromtimestamp(item.stat().st_mtime).isoformat() if item.is_file() else None
        })
    return JSONResponse(items)

@app.get("/api/file")
async def read_file(path: str):
    """Read a file from the vault"""
    file_path = Path(VAULT_PATH) / path
    if not file_path.exists():
        raise HTTPException(404, "File not found")
    if file_path.is_dir():
        raise HTTPException(400, "Path is a directory")
    return JSONResponse({
        "path": path,
        "content": file_path.read_text(encoding="utf-8"),
        "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
    })

@app.post("/api/file")
async def write_file(data: dict):
    """Write/create a file in the vault"""
    path = data.get("path", "")
    content = data.get("content", "")
    file_path = Path(VAULT_PATH) / path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return JSONResponse({"status": "saved", "path": path})

@app.delete("/api/file")
async def delete_file(path: str):
    """Delete a file from the vault"""
    file_path = Path(VAULT_PATH) / path
    if not file_path.exists():
        raise HTTPException(404, "File not found")
    if file_path.is_dir():
        import shutil
        shutil.rmtree(file_path)
    else:
        file_path.unlink()
    return JSONResponse({"status": "deleted", "path": path})

@app.post("/api/folder")
async def create_folder(data: dict):
    """Create a new folder in the vault"""
    path = data.get("path", "")
    folder_path = Path(VAULT_PATH) / path
    folder_path.mkdir(parents=True, exist_ok=True)
    return JSONResponse({"status": "created", "path": path})

@app.get("/api/search")
async def search(query: str):
    """Search vault content"""
    results = []
    vault = Path(VAULT_PATH)
    for file in vault.rglob("*.md"):
        content = file.read_text(encoding="utf-8")
        if query.lower() in content.lower():
            rel = str(file.relative_to(vault))
            # Find matching lines
            matches = []
            for i, line in enumerate(content.split("\n")):
                if query.lower() in line.lower():
                    matches.append({"line": i+1, "text": line.strip()})
            results.append({"file": rel, "matches": matches})
    return JSONResponse(results)

@app.get("/api/memories")
async def get_memories():
    """Get all memory files (files in Memories/ folder or with memory tags"""
    memories = []
    vault = Path(VAULT_PATH)
    mem_folder = vault / "Memories"
    if mem_folder.exists():
        for f in sorted(mem_folder.rglob("*.md")):
            memories.append({
                "path": str(f.relative_to(vault)),
                "name": f.name,
                "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            })
    return JSONResponse(memories)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "obsidian-vault", "vault_path": VAULT_PATH}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8200)
