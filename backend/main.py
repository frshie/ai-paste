from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from typing import List
import uuid, json, os, io, zipfile
from datetime import datetime

app = FastAPI(title="AI Paste", version="1.0.0")

DATA_FILE = "projects.json"

def load_projects():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_projects(projects):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(projects, f, indent=2)

class FileItem(BaseModel):
    path: str
    content: str

class ProjectCreate(BaseModel):
    files: List[FileItem]
    title: str = ""

class ProjectUpdate(BaseModel):
    files: List[FileItem]
    title: str = ""

@app.post("/api/project")
def create_project(payload: ProjectCreate):
    projects = load_projects()
    project_id = str(uuid.uuid4())[:8]
    projects[project_id] = {
        "id": project_id,
        "title": payload.title,
        "files": [{"path": f.path, "content": f.content} for f in payload.files],
        "created_at": datetime.utcnow().isoformat()
    }
    save_projects(projects)
    return {"id": project_id, "url": f"/p/{project_id}"}

@app.get("/api/project/{project_id}")
def get_project(project_id: str):
    projects = load_projects()
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return projects[project_id]

@app.put("/api/project/{project_id}")
def update_project(project_id: str, payload: ProjectUpdate):
    projects = load_projects()
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    projects[project_id]["files"] = [{"path": f.path, "content": f.content} for f in payload.files]
    projects[project_id]["title"] = payload.title or projects[project_id].get("title", "")
    projects[project_id]["updated_at"] = datetime.utcnow().isoformat()
    save_projects(projects)
    return {"id": project_id, "url": f"/p/{project_id}"}

@app.get("/api/project/{project_id}/zip")
def download_zip(project_id: str):
    projects = load_projects()
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    project = projects[project_id]
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in project["files"]:
            zf.writestr(file["path"], file["content"])
    zip_buffer.seek(0)
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=project-{project_id}.zip"}
    )

@app.get("/api/projects")
def list_projects():
    projects = load_projects()
    return [{"id": p["id"], "title": p.get("title", ""), "created_at": p["created_at"], "file_count": len(p["files"])} for p in projects.values()]

app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
