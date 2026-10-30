import requests
import json
from pathlib import Path

def fetch_weather(latitude: float, longitude: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "timezone": "Europe/Paris",
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    weather_data = fetch_weather(48.8566, 2.3522)

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "weather_raw.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(weather_data, file, ensure_ascii=False, indent=4)

    print(f"Données météo sauvegardées dans : {output_file}")
