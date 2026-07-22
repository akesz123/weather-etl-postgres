from datetime import datetime, timedelta
from pathlib import Path
import json
import requests

# API endpoint for the weather forecast service
API_URL = "https://api.open-meteo.com/v1/forecast"

# We request the forecast for tomorrow so the script can collect fresh data
# for Budapest and store it in a timestamped file.
today = datetime.now() + timedelta(days=1)

# Request parameters for the Open-Meteo API
params = {
    "latitude": 47.4979,
    "longitude": 19.0402,
    "hourly": (
        "temperature_2m",
        "relative_humidity_2m",
        "windspeed_10m",
        "weathercode"
    ),
    "start": today.strftime("%Y-%m-%dT%H:%M"),
    "end": today.strftime("%Y-%m-%dT%H:%M"),
    "timezone": "Europe/Budapest",
    "forecast_days": 2
}

# Send the HTTP request to the weather API
response = requests.get(API_URL, params=params)
response.raise_for_status()  # Stop the script if the request fails

# Create a unique filename with a timestamp; hyphens are used instead of colons
# because Windows does not allow ':' in file names.
timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M')
file_name = f"weather_budapest_collected_at{timestamp}.json"
file_path = Path("data/raw") / file_name
file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the folder exists

# Write the hourly weather data to a JSON file
with file_path.open("w", encoding="utf-8") as file:
    json.dump(response.json()["hourly"], file, ensure_ascii=False, indent=2)

# Print the save location and the JSON content for quick inspection
print(f"Weather data saved to {file_path}")
print(json.dumps(response.json()["hourly"], ensure_ascii=False, indent=2))
