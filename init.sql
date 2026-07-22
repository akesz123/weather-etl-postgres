

CREATE TABLE  weather_data (
    id SERIAL PRIMARY KEY,
    time timestamptz  NOT NULL UNIQUE,
    temperature_2m REAL,
    relative_humidity_2m REAL,
    windspeed_10m REAL,
    weathercode INTEGER
);