import psycopg

def load_weather_data(rows):

    with psycopg.connect(
        host="localhost",
        port=65433,
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
        conn.close()
    print(f"Inserted {len(rows)} rows.")

if __name__ == "__main__":

    test_rows = [
        (
            "2026-08-17T10:00",
            25.5,
            60,
            10.2,
            1,
        )
    ]

    load_weather_data(test_rows)