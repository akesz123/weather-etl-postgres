# Weather ETL to Postgres

This project fetches historical weather data from Open-Meteo for Budapest and saves the raw hourly JSON into `data/raw`.

## Prerequisites

- Python 3.10+
- pip
- Virtual environment support
- Docker (optional, only if you want to run the Postgres service locally)

## 1) Create and activate a virtual environment

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2) Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3) Run the ETL script

```powershell
python main.py
```

This script:
- requests weather data from Open-Meteo
- writes the raw file into `data/raw/`
- prints the saved file path and the JSON payload

## 4) Check the output file

Files are created in:

```text
data/raw/
```

Example file name:

```text
data/raw/weather_budapest_collected_at2026-08-17T12-00.json
```

## 5) Run Postgres with Docker (optional)

If you want to start the local Postgres service defined in the project:

```powershell
docker-compose up -d
```

To stop it:

```powershell
docker-compose down
```

## 6) Useful commands

Check Python version:

```powershell
python --version
```

List project files:

```powershell
Get-ChildItem
```

Activate venv again later:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Notes

- The API URL and date range are defined in `main.py`.
- If Open-Meteo changes the endpoint or requires a different parameter set, update the request in `main.py`.
- The script stores raw JSON before any transformation into Postgres.
