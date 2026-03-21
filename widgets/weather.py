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

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        # Coordinates from Bern
        "latitude": 46.9486,
        "longitude": 7.4363,
        "current": "temperature_2m,weathercode,windspeed_10m",
        "timezone": "Europe/Zurich"
    }

    response = requests.get(url, params=params)
    data = response.json()

    current = data["current"]
    current["description"] = weathercode_to_description(current["weathercode"])

    return current