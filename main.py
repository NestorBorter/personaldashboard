from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from widgets.weather import get_weather, get_coordinates
from widgets.finance import get_etf


# Creates App with FastAPI
app = FastAPI()

# CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templatesfolder
templates = Jinja2Templates(directory="templates")

@app.get("/") # Homepage
def home(request: Request, city: str = "Bern"):
    coords = get_coordinates(city)
    if coords:
        weather = get_weather(coords["lat"], coords["lon"])
        weather["city"] = coords["city"]
        weather["country"] = coords["country"]
    else:
        weather = get_weather() # Taking Bern as standard
        weather["city"] = "Bern"

    # Getting info from APIs
    financedict = get_etf("VWRA.L")

    return templates.TemplateResponse("home.html", {
        "request": request,
        "weather": weather,
        "financedict": financedict,
        "city": city
    })


@app.get("/configure/") # Configurepage
def configure(request: Request):
    return templates.TemplateResponse("configure.html", {"request": request})