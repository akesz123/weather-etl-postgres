from datetime import datetime, timedelta
from pathlib import Path
import json
import requests
import pandas as pd

# API endpoint for the weather forecast service
API_URL = "https://archive-api.open-meteo.com/v1/archive"

# We request the forecast for tomorrow so the script can collect fresh data
# for Budapest and store it in a timestamped file.
#today = datetime.now() + timedelta(days=1)
date_from=datetime(2026, 5, 1)  # Start date for the forecast
date_to=datetime(2026, 7, 31)  # End date for the forecast

# Request parameters for the Open-Meteo API
params = {
	"latitude": 47.4979,
	"longitude": 19.0402,
	"start_date": date_from.strftime("%Y-%m-%d"),
	"end_date": date_to.strftime("%Y-%m-%d"),
	"hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "weather_code"],
}

# Send the HTTP request to the weather API
response = requests.get(API_URL, params=params)
response.raise_for_status()  # Stop the script if the request fails

# Create a unique filename with a timestamp; hyphens are used instead of colons
# because Windows does not allow ':' in file names.
file_name = f"weather_budapest_at_month_{date_from.strftime('%Y-%m')}.json"
file_path = Path("data/raw") / file_name
file_path.parent.mkdir(parents=True, exist_ok=True)  
# Ensure the folder exists

# Write the hourly weather data to a JSON file
with file_path.open("w", encoding="utf-8") as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=2)

# Print the save location and the JSON content for quick inspection
print(f"Weather data saved to {file_path}")

