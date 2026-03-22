import requests

def weathercode_to_description(code):
    if code == 0:
        return "Clear"
    elif code == 1:
        return "Mostly clear"
    elif code == 2:
        return "Partly cloudy"
    elif code == 3:
        return "Overcast"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55]:
        return "Drizzle"
    elif code in [61, 63, 65]:
        return "Rain"
    elif code in [71, 73, 75]:
        return "Snow"
    elif code in [80, 81, 82]:
        return "Rain showers"
    elif code == 95:
        return "Thunderstorm"
    else:
        return "Unknown"

def get_coordinates(cityname):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": cityname, "count": 1, "language": "en"}

    response = requests.get(url, params=params)
    data = response.json()

    if not data.get("results"):
        return None

    result = data["results"][0]
    return {
        "lat": result["latitude"],
        "lon": result["longitude"],
        "city": result["name"],
        "country": result["country"]
    }

def get_weather(lat=46.9486, lon=7.4363): # Bern as standard
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        # Coordinates from Bern
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,weathercode,windspeed_10m",
        "timezone": "Europe/Zurich"
    }

    response = requests.get(url, params=params)
    data = response.json()

    current = data["current"]
    current["description"] = weathercode_to_description(current["weathercode"])

    return current