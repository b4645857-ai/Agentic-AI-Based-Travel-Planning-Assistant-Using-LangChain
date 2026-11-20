# ✈️ Agentic AI-Based Travel Planning Assistant Using LangChain

<p align="center">

**An intelligent, tool-driven travel planning system that transforms natural-language travel requests into structured, budget-aware itineraries.**

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/Framework-LangChain-1C3C3C)
![Streamlit](https://img.shields.io/badge/Interface-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![AI](https://img.shields.io/badge/AI-Agentic%20AI-purple)
![Status](https://img.shields.io/badge/Project-Academic%20Prototype-blue)

</p>

---

## 🌍 01. Project Overview

Planning a trip involves comparing transportation, accommodation, tourist attractions, weather conditions, and expenses across multiple sources. Doing this manually can be time-consuming and overwhelming.

The **Agentic AI Travel Planning Assistant** aims to simplify this process through an intelligent assistant powered by Large Language Models (LLMs), LangChain, and structured travel datasets.

Instead of relying entirely on static responses, the system is designed around a tool-driven workflow in which an AI agent interprets user requirements, selects relevant tools, retrieves information, and assembles a personalized travel plan.

The objective is simple: **turn a travel idea into an organized, practical itinerary.**

## 🎯 02. Core Objectives

- Interpret natural-language travel requests.
- Retrieve relevant flight information from structured datasets.
- Recommend hotels based on destination and budget.
- Discover tourist attractions and activities.
- Retrieve weather information using the Open-Meteo API.
- Estimate overall trip expenses.
- Generate organized, day-wise itineraries.
- Present travel information through an interactive interface.

## 🧠 03. System Architecture

The proposed system follows a modular agent-based architecture.

```text
             USER TRAVEL QUERY
                     |
                     ▼
          STREAMLIT USER INTERFACE
                     |
                     ▼
           LANGCHAIN AI AGENT
                     |
             QUERY ANALYSIS
                     |
                     ▼
             TOOL SELECTION
                     |
       ┌─────────────┼──────────────┐
       ▼             ▼              ▼
  FLIGHT TOOL    HOTEL TOOL     PLACES TOOL
       |             |              |
       └─────────────┼──────────────┘
                     |
                WEATHER TOOL
                     |
                     ▼
             BUDGET ESTIMATOR
                     |
                     ▼
          ITINERARY GENERATION
                     |
                     ▼
          STRUCTURED TRAVEL PLAN
```

The architecture separates user interaction, reasoning, data retrieval, and result presentation to support modular development and future expansion.

## ⚙️ 04. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| AI Framework | LangChain |
| Language Model | Google Gemini (when configured) |
| Frontend | Streamlit |
| Data Processing | Pandas |
| Weather Integration | Open-Meteo API |
| Data Storage | JSON datasets |
| Visualization | Matplotlib, Seaborn |
| Development Environment | VS Code / Google Colab |
| Version Control | Git and GitHub |

## 🛠️ 05. Intelligent Travel Tools

The application is organized around five major travel-planning capabilities.

**✈️ Flight Search**

Retrieves matching flight records using departure city and destination. Sample flight prices support route comparisons and budget estimation.

**🏨 Hotel Recommendation**

Filters accommodation records according to destination, star rating, amenities, and price per night.

**📍 Places Discovery**

Explores tourist attractions and places of interest using destination and attraction information.

**🌤️ Weather Lookup**

Uses the Open-Meteo weather service to retrieve weather information when the integration is configured and available.

**💰 Budget Estimation**

Combines relevant travel expenses into an estimated trip budget, helping users understand the approximate cost of their journey.

## 📂 06. Dataset Structure

The project uses structured JSON files for its sample travel information.

| Dataset | Purpose |
|---|---|
| `flights.json` | Flight details, routes, timings, and sample prices |
| `hotels.json` | Hotel names, cities, ratings, amenities, and prices |
| `places.json` | Tourist attractions, categories, cities, and ratings |

These datasets provide a controlled environment for testing filtering, recommendations, and travel-planning logic.

**Data transparency:** Flight and hotel records are sample data, not live inventory. Prices and routes must not be interpreted as confirmed booking availability.

## 🔄 07. Agent Workflow

The intended agent workflow consists of the following stages:

1. **Input Understanding:** Interpret the destination, travel duration, preferences, and budget.
2. **Requirement Analysis:** Identify the information required to construct the travel plan.
3. **Tool Selection:** Select appropriate flight, hotel, places, weather, and budget tools.
4. **Information Retrieval:** Collect relevant records and external weather information.
5. **Decision Making:** Compare available options against the user's requirements.
6. **Itinerary Construction:** Organize selected activities into a day-wise travel schedule.
7. **Response Generation:** Present the result in a readable and structured format.

## 🚀 08. Installation and Local Setup

### Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code
- Internet connection for external API integrations

### Clone the repository

```bash
git clone https://github.com/b4645857-ai/Agentic-AI-Based-Travel-Planning-Assistant-Using-LangChain.git
cd Agentic-AI-Based-Travel-Planning-Assistant-Using-LangChain
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## 🔐 09. API Configuration and Security

External API integrations may require configuration.

- Store API keys in environment variables or Streamlit secrets.
- Never commit `.env` files or secret credentials.
- Do not expose private API keys in source code or screenshots.
- Keep sample datasets separate from credentials and configuration files.

For Streamlit Cloud, configure required secrets through the application's settings.

## 📊 10. Testing and Evaluation

The system can be evaluated through functional and integration tests rather than conventional supervised-learning accuracy.

Recommended evaluation areas include:

- Flight route matching correctness.
- Hotel and tourist-place dataset validation.
- Budget calculation correctness.
- Weather API response handling.
- Tool execution success rate.
- Agent response completeness.
- Error handling for invalid or unavailable inputs.

These measurements assess application functionality and reliability; they should not be presented as predictive-model accuracy.

## ⚠️ 11. Current Scope and Limitations

This project is an academic prototype, not a commercial booking platform.

- Flight and hotel datasets contain sample records.
- Displayed prices are indicative dataset values.
- Live booking, payment, and reservation confirmation are not provided.
- Weather results depend on external API availability.
- AI-generated recommendations may require user verification.
- Agent capabilities depend on the configured model and available tools.

## 🔮 12. Future Enhancements

Potential improvements include:

- Real-time flight and hotel API integrations.
- Map-based itinerary visualization.
- Personalized recommendations using user preferences.
- Multi-city trip optimization.
- More advanced budget optimization.
- Conversational trip refinement.
- Persistent user profiles and saved itineraries.
- Multilingual travel assistance.
- Automated itinerary export to PDF.

## 👨‍💻 13. Project Information

**Project:** Agentic AI-Based Travel Planning Assistant Using LangChain

**Domain:** Artificial Intelligence / Agentic AI / Travel Technology

**Developer:** Vishal B.

**Institution:** SRM Institute of Science and Technology, Ramapuram, Chennai.

**Repository:** [GitHub Project](https://github.com/b4645857-ai/Agentic-AI-Based-Travel-Planning-Assistant-Using-LangChain)

---

<p align="center">

**Built with Python, LangChain, and the vision of making travel planning more intelligent.** 🌍

</p>
