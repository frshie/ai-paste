# API Reference

## POST /api/project
Create a new project.
```json
{"files": [{"path": "main.py", "content": "print('hello')"}], "title": "My Project"}
```
Returns: `{"id": "abc12345", "url": "/p/abc12345"}`

## GET /api/project/{id}
Get project files.

## PUT /api/project/{id}
Update project files.

## GET /api/project/{id}/zip
Download project as ZIP.

## GET /api/projects
List all projects.
