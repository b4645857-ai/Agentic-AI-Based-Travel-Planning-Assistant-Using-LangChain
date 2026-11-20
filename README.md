# Agentic AI-Based Travel Planning Assistant Using LangChain

A Streamlit travel-planning prototype using flight, hotel and attraction JSON datasets, Open-Meteo weather forecasts, budget estimation, and optional Google Gemini itinerary generation.

## Features
- Flight search and lowest sample-fare ranking
- Hotel filtering by city and nightly price, ranked by stars and price
- Tourist attraction discovery ranked by rating
- Open-Meteo weather forecast (no API key required)
- Trip budget estimation
- Optional Gemini-generated day-wise itinerary
- JSON export of trip results

## Run locally

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push this folder to a public GitHub repository.
2. On https://share.streamlit.io, create an app from that repository.
3. Set the main file path to `app.py`.

## Data notice
`flights.json` and `hotels.json` contain sample records and do not represent live availability or bookable offers. Weather is retrieved from Open-Meteo. Gemini itinerary generation is optional and requires a user-provided API key in the app sidebar.
