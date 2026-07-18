from datetime import datetime, timedelta
from pathlib import Path
import json
import requests

API_URL = "https://api.open-meteo.com/v1/forecast"
today = datetime.now()+ timedelta(days=1)
params = {
    "latitude": 47.4979,
    "longitude": 19.0402,
    "hourly": ("temperature_2m",
                "relative_humidity_2m",
                "windspeed_10m",
                "weathercode"
    ),
    "start": today.strftime("%Y-%m-%dT%H:%M"),
    "end": today.strftime("%Y-%m-%dT%H:%M"),
    "timezone": "Europe/Budapest",
    "forecast_days": 2
}

response = requests.get(API_URL,params=params)
file_name=f"weather_budapest_collected_at{datetime.now().strftime('%Y-%m-%dT%H:%M')}.json"
file_path = Path("data/raw") / file_name

with file_path.open("w", encoding="utf-8") as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=4)

print(f"Weather data saved to {file_path}")
print(json.dumps(response.json()["hourly"], ensure_ascii=False, indent=2))
