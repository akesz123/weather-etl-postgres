import json
from pathlib import Path
import psycopg


def create_weather_table():
    conn = psycopg.connect(
    host="localhost",
    port=55432,
    dbname="appdb",
    user="appuser",
    password="apppass"
)

    with conn.cursor() as cur:
        with open("init.sql", "r", encoding="utf-8") as f:
            cur.execute(f.read())

    conn.commit()
    conn.close()


def insert_weather_data(file_path):
    with open(file_path) as f:
        data = json.load(f)

    rows = list(zip(
        data["time"],
        data["temperature_2m"],
        data["relative_humidity_2m"],
        data["windspeed_10m"],
        data["weathercode"],
    ))

    with psycopg.connect(
        host="localhost",
        port=55432,
        dbname="appdb",
        user="appuser",
        password="apppass",
    ) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO weather_data
                    (time, temperature_2m, relative_humidity_2m, windspeed_10m, weathercode)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (time) DO NOTHING
                """,
                rows,
            )
        conn.commit()

    print(f"Inserted {len(rows)} rows.")

def main():
    # Assuming the JSON file is in the 'data/raw' directory and has a timestamped name

    latest_file = max(
        (f for f in Path("data/raw").glob("weather_budapest_collected_at*.json")),
        key=lambda f: f.stat().st_mtime,
    )

    print(f"Inserting data from {latest_file}")
   # create_weather_table()
    insert_weather_data(latest_file) 


if __name__ == "__main__":
    main()