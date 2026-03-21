from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# test
# Creates App with FastAPI
app = FastAPI()

# CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templatesfolder
templates = Jinja2Templates(directory="templates")

@app.get("/") # Homepage
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/configure/") # Configurepage
def configure(request: Request):
    return templates.TemplateResponse("configure.html", {"request": request})
