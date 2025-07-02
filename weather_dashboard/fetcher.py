import requests

API_KEY = "YOUR_API_KEYS"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str) -> dict:
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    resp = requests.get(BASE_URL, params=params)
    resp.raise_for_status()
    return resp.json()
