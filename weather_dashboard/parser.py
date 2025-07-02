def parse_weather(data: dict) -> dict:
    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    return {
        "city": data.get("name"),
        "temp": main.get("temp"),
        "humidity": main.get("humidity"),
        "pressure": main.get("pressure"),
        "description": weather.get("description")
    }
