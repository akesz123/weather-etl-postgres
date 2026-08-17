import json
from pathlib import Path
from extract import extract_weather


def transform_weather_data(file_path):

    print(f"Transforming weather data from {file_path}...")
    with open(file_path,"r",encoding="utf-8") as file:
        data=json.load(file)

    validate_weather_data(data)

    hourly=data["hourly"]

    rows=list(zip(
        hourly["time"],
        hourly["temperature_2m"],
        hourly["relative_humidity_2m"],
        hourly["wind_speed_10m"],
        hourly["weather_code"],
    ))

    return rows

def validate_weather_data(data):
    hourly=data["hourly"]

    required_fields=["time","temperature_2m","relative_humidity_2m","wind_speed_10m","weather_code"]

    for field in required_fields:
        if field not in hourly:
            raise ValueError(f"Missing required field: {field}")

    lengths={
        field: len(hourly[field]) for field in required_fields
    }

    if len(set(lengths.values())) != 1:
        raise ValueError("All required fields must have the same length")
    else:
        print(f"All required fields have the same length: {lengths[required_fields[0]]} entries.")

if __name__=="__main__":
    file_path=extract_weather()
    rows=transform_weather_data(file_path)
    print(f"Transformed {len(rows)} rows.")