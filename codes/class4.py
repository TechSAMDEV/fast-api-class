from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

item_db = [
    {"item": "laptop", "status": "available", "price": 99},
]

name = "Item inventory"

app = FastAPI()

# @app.get("/")
# def display_items():
#     return item_db

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"items": item_db})

