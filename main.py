from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from widgets.weather import get_weather, get_coordinates
from widgets.finance import get_etf
from database import init_db, get_database

init_db()


# Creates App with FastAPI
app = FastAPI()

# CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templatesfolder
templates = Jinja2Templates(directory="templates")

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(request: Request, username: str = Form(...), password: str = Form(...)):
    hashed = pwd_context.hash(password)
    db = get_database()
    try:
        # write new user into database
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, hashed)
        # commit the changes
        db.commit()
    except: # if username already exists
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username already exists"})
    finally:
        db.close
    # after successful register -> login page
    return RedirectResponse("/login", status_code=303)

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