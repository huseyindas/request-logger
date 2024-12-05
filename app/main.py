from fastapi import FastAPI, Request, Body, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json
from typing import List, Dict, Any

app = FastAPI()

LOG_FILE = Path("app/logs/logs.json")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
LOG_FILE.touch(exist_ok=True)

if not LOG_FILE.exists() or LOG_FILE.read_text().strip() == "":
    LOG_FILE.write_text("[]")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


def save_log(data: Dict[str, Any]) -> None:
    try:
        logs = read_logs()
        logs.append(data)
        LOG_FILE.write_text(json.dumps(logs, indent=4))
    except Exception as e:
        print(f"Log kaydedilemedi: {e}")


def read_logs() -> List[Dict[str, Any]]:
    try:
        if LOG_FILE.exists():
            return json.loads(LOG_FILE.read_text())
    except json.JSONDecodeError:
        print("Log dosyası okunamadı veya bozuk.")
    return []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("logs.html", {"request": request})


@app.get("/logs")
async def logs_view():
    logs = read_logs()
    return {"logs": logs}


@app.get("/test")
async def test_get(q: str = Query(None), request: Request = None):
    log_entry = {
        "type": "GET",
        "headers": dict(request.headers),
        "body": None,
        "query": {"q": q},
    }
    save_log(log_entry)
    return {"message": "GET isteği alındı", "query": q}


@app.post("/test")
async def test_post(payload: dict = Body(...), request: Request = None):
    log_entry = {
        "type": "POST",
        "headers": dict(request.headers),
        "body": payload,
        "query": None,
    }
    save_log(log_entry)
    return {"message": "POST isteği alındı", "body": payload}
