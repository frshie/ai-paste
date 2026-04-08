<p align="center">
  <img src="https://img.shields.io/badge/AI--Native-Code%20Sharing-6c63ff?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<h1 align="center">🗂️ AI Paste</h1>
<p align="center">
  <b>The fastest way for AI assistants to share code with humans.</b><br>
  AIs upload entire project file trees via a simple REST API.<br>
  You get a clean, shareable link — browse files, read code, download a ZIP.
</p>

---

## ✨ What is this?

AI Paste is a self-hosted code sharing tool built specifically for AI workflows. Instead of dumping hundreds of lines of code into a chat, an AI assistant can upload an entire project in one API call and hand you a single link.

- 📁 **Full file trees** — not just single files, entire projects with folder structures
- 🔗 **Shareable links** — every project gets a short ID you can share anywhere
- 📦 **ZIP download** — grab the whole project as a ZIP in one click
- 🚀 **Self-hosted** — runs locally, expose it publicly via Cloudflare Tunnel if needed
- ⚡ **Zero config** — just run `start.bat` and it works

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip

### 1. Clone the repo
```bash
git clone https://github.com/frshie/ai-paste.git
cd ai-paste
```

### 2. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run it
```bash
# Windows — just double-click or run:
start.bat
```

The server starts at **http://localhost:8000**

> **Want it public?** Use [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) to expose it — then give your AI the public URL.

---

## 🤖 Using with an AI

Once your server is running (locally or publicly), paste this into your AI's system prompt:

```
You have access to a code sharing API at https://your-domain.com

To upload a project:
POST /api/project
{ "files": [{"path": "main.py", "content": "..."}], "title": "My Project" }

To update a project:
PUT /api/project/{id}
{ "files": [...], "title": "..." }

Always upload the full file content, not diffs.
```

The AI will automatically upload projects and give you links like `https://your-domain.com/p/abc12345`.

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/project` | Create a new project |
| `GET` | `/api/project/{id}` | Get project data (JSON) |
| `PUT` | `/api/project/{id}` | Update an existing project |
| `GET` | `/api/project/{id}/zip` | Download project as ZIP |
| `GET` | `/api/projects` | List all projects |

### Example: Create a project
```bash
curl -X POST https://your-domain.com/api/project \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My App",
    "files": [
      {"path": "main.py", "content": "print(\"hello world\")"},
      {"path": "README.md", "content": "# My App"}
    ]
  }'
```

**Response:**
```json
{ "id": "a1b2c3d4", "url": "/p/a1b2c3d4" }
```

See [`API.md`](./API.md) for full documentation.

---

## 🗂️ Project Structure

```
ai-paste/
├── backend/
│   ├── main.py          # FastAPI app — all API endpoints
│   ├── requirements.txt # Python dependencies
│   └── projects.json    # Auto-generated project storage
├── frontend/
│   └── index.html       # Single-page frontend (browse/download UI)
├── start.bat            # One-click Windows launcher
├── AI_INSTRUCTIONS.md   # Drop this into your AI system prompt
├── API.md               # Full API docs
└── README.md            # You are here
```

---

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| Backend | [FastAPI](https://fastapi.dev) + [Uvicorn](https://www.uvicorn.org) |
| Frontend | Vanilla HTML/CSS/JS (zero dependencies) |
| Storage | Local JSON file |
| Tunnel | [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) (optional) |

---

## 📄 License

MIT — do whatever you want with it.
