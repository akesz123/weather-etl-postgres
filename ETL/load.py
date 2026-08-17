import psycopg

from transform import transform_weather_data
from extract import extract_weather

def load_weather_data(rows):

    inserted=0
    skipped=0

    with psycopg.connect(
        host="localhost",
        port=65433,
        dbname="appdb",
        user="appuser",
        password="apppass",
    ) as conn:
        
        with conn.cursor() as cur:

            
            for row in rows:
     
                    cur.execute(
                        """
                        INSERT INTO weather_data
                            (time,
                             temperature_2m,
                             relative_humidity_2m,
                             windspeed_10m,
                             weathercode)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (time) DO NOTHING
                        RETURNING id
                        """,
                        row,
                    )

                    inserted_row = cur.fetchone()
                    if inserted_row is not None:
                        inserted += 1
                    else:
                         skipped += 1

        conn.commit()
        skipped = len(rows) - inserted
    
    print(f"Rows received: {len(rows)}")
    print(f"Inserted {inserted} rows.")
    print(f"Skipped {skipped} rows.")

if __name__ == "__main__":
    final_rows = transform_weather_data(file_path=extract_weather())
    load_weather_data(final_rows)