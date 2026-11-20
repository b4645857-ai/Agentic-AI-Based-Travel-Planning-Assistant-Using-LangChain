import json
import os
from datetime import date, timedelta

import pandas as pd
import requests
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

@st.cache_data
def load_data(filename):
    with open(os.path.join(BASE_DIR, filename), "r", encoding="utf-8") as f:
        return json.load(f)

flights = load_data("flights.json")
hotels = load_data("hotels.json")
places = load_data("places.json")

st.title("✈️ Agentic AI Travel Planning Assistant")
st.caption("Plan smarter trips with travel datasets, weather information and Gemini-powered itinerary generation.")
st.info("Dataset notice: flight and hotel records are sample data, not live availability or bookable offers.")

with st.sidebar:
    st.header("Plan your trip")
    cities = sorted({x["city"] for x in hotels} | {x["from"] for x in flights} | {x["to"] for x in flights})
    source = st.selectbox("Departure city", cities, index=cities.index("Chennai") if "Chennai" in cities else 0)
    destinations = [c for c in cities if c != source]
    destination = st.selectbox("Destination", destinations, index=destinations.index("Mumbai") if "Mumbai" in destinations else 0)
    days = st.slider("Trip duration (days)", 3, 7, 3)
    max_hotel_price = st.number_input("Maximum hotel price per night (₹)", min_value=0, value=5000, step=500)
    api_key = st.text_input("Gemini API key (optional)", type="password", help="Used only for generating an AI-written itinerary. Never saved by this app.")
    generate = st.button("Generate my travel plan", type="primary", use_container_width=True)

if generate:
    st.session_state["trip_request"] = {
        "source": source, "destination": destination, "days": days,
        "max_hotel_price": max_hotel_price, "api_key": api_key
    }

if "trip_request" in st.session_state:
    req = st.session_state["trip_request"]
    source, destination, days = req["source"], req["destination"], req["days"]
    matching_flights = [x for x in flights if x["from"].lower() == source.lower() and x["to"].lower() == destination.lower()]
    matching_flights.sort(key=lambda x: x["price"])
    matching_hotels = [x for x in hotels if x["city"].lower() == destination.lower() and x["price_per_night"] <= req["max_hotel_price"]]
    matching_hotels.sort(key=lambda x: (-x["stars"], x["price_per_night"]))
    matching_places = [x for x in places if x["city"].lower() == destination.lower()]
    matching_places.sort(key=lambda x: x["rating"], reverse=True)

    st.header(f"Your {days}-day trip: {source} → {destination}")
    c1, c2, c3 = st.columns(3)
    c1.metric("Matching sample flights", len(matching_flights))
    c2.metric("Matching hotels", len(matching_hotels))
    c3.metric("Attractions found", len(matching_places))

    st.subheader("✈️ Flight options")
    if matching_flights:
        st.dataframe(pd.DataFrame(matching_flights), use_container_width=True, hide_index=True)
        chosen_flight = matching_flights[0]
        st.success(f"Lowest sample fare: {chosen_flight['airline']} — ₹{chosen_flight['price']:,}")
    else:
        chosen_flight = None
        st.warning(f"No {source} to {destination} route exists in the sample flight dataset.")

    st.subheader("🏨 Hotel recommendations")
    if matching_hotels:
        st.dataframe(pd.DataFrame(matching_hotels), use_container_width=True, hide_index=True)
        chosen_hotel = matching_hotels[0]
        st.success(f"Suggested hotel: {chosen_hotel['name']} ({chosen_hotel['stars']} stars) — ₹{chosen_hotel['price_per_night']:,}/night")
    else:
        chosen_hotel = None
        st.warning("No hotel matches the selected city and price limit. Increase your price limit.")

    st.subheader("📍 Top tourist attractions")
    if matching_places:
        st.dataframe(pd.DataFrame(matching_places[:10]), use_container_width=True, hide_index=True)
    else:
        st.warning("No attractions found in the sample dataset for this city.")

    st.subheader("🌦️ Weather lookup")
    coords = {
        "Delhi": (28.6139, 77.2090), "Mumbai": (19.0760, 72.8777),
        "Goa": (15.2993, 74.1240), "Bangalore": (12.9716, 77.5946),
        "Chennai": (13.0827, 80.2707), "Hyderabad": (17.3850, 78.4867),
        "Kolkata": (22.5726, 88.3639), "Jaipur": (26.9124, 75.7873)
    }
    weather_text = "Weather unavailable for this destination."
    if destination in coords:
        lat, lon = coords[destination]
        try:
            wr = requests.get("https://api.open-meteo.com/v1/forecast", params={
                "latitude": lat, "longitude": lon,
                "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
                "forecast_days": min(days, 7), "timezone": "auto"
            }, timeout=15)
            wr.raise_for_status()
            w = wr.json().get("daily", {})
            weather_df = pd.DataFrame({
                "Date": w.get("time", []),
                "Max temp (°C)": w.get("temperature_2m_max", []),
                "Min temp (°C)": w.get("temperature_2m_min", []),
                "Rain probability (%)": w.get("precipitation_probability_max", [])
            })
            st.dataframe(weather_df, use_container_width=True, hide_index=True)
            weather_text = weather_df.to_string(index=False)
        except Exception as e:
            st.warning(f"Weather API unavailable: {e}")

    hotel_cost = chosen_hotel["price_per_night"] * (days - 1) if chosen_hotel else 0
    flight_cost = chosen_flight["price"] if chosen_flight else 0
    local_cost = days * 1000
    total = flight_cost + hotel_cost + local_cost
    st.subheader("💰 Estimated budget")
    b1, b2, b3, b4 = st.columns(4)
    b1.metric("Sample flight", f"₹{flight_cost:,}")
    b2.metric("Hotel ({days-1} nights)", f"₹{hotel_cost:,}")
    b3.metric("Local expenses", f"₹{local_cost:,}")
    b4.metric("Estimated total", f"₹{total:,}")

    st.subheader("🤖 AI-generated itinerary")
    if req["api_key"]:
        try:
            from google import genai
            client = genai.Client(api_key=req["api_key"])
            context = {
                "route": f"{source} to {destination}", "duration_days": days,
                "flight": chosen_flight, "hotel": chosen_hotel,
                "attractions": matching_places[:10], "weather": weather_text,
                "estimated_budget_inr": total
            }
            prompt = "Create a practical day-wise travel itinerary using ONLY the supplied data where applicable. Do not invent flight/hotel availability or weather. Mark any suggested activities as suggestions. Include budget and explain selections. Data:\n" + json.dumps(context, ensure_ascii=False)
            result = client.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt)
            st.markdown(result.text)
        except Exception as e:
            st.error(f"Gemini itinerary generation failed: {e}")
            st.write("You can still use the flight, hotel, attractions, weather and budget results above.")
    else:
        st.caption("Add a Gemini API key in the sidebar to generate a personalized written itinerary. The dataset search and budget tools work without a key.")

    output = {
        "source": source, "destination": destination, "duration_days": days,
        "flight_options": matching_flights, "hotel_options": matching_hotels,
        "attractions": matching_places, "estimated_budget_inr": total,
        "sample_data_notice": "Flights and hotels are sample dataset records, not live availability."
    }
    st.download_button("Download trip results (JSON)", json.dumps(output, indent=2, ensure_ascii=False),
                       file_name="travel_plan.json", mime="application/json")

with st.expander("About this project"):
    st.write("This prototype demonstrates travel-data retrieval, filtering, ranking, weather API integration, budget estimation and optional Gemini itinerary generation. Flight and hotel data are sample JSON datasets.")
