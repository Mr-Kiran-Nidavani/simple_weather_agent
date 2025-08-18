# Weather Agent

A simple Python agent that extracts a location from user input using OpenRouter.ai LLM API and fetches the current weather for that location using OpenWeatherMap API.

---

## Features

- Extracts location names from natural language queries
- Gets real-time weather info (temperature and description)
- Uses free APIs with easy setup

---

## Requirements

- Python 3.7+
- Pipenv or pip for dependency management
- API keys for:
  - [OpenRouter.ai](https://openrouter.ai)
  - [OpenWeatherMap](https://openweathermap.org/api)

- Here’s how you can get the current weather using OpenWeatherMap with curl:
  - Register at [https://home.openweathermap.org/users/sign_up]
  - After signing in, go to API Keys and copy your key [https://home.openweathermap.org/api_keys]

---

## Setup

1. Clone or download the repository

2. Create a `.env` file in the root folder with your API keys:

   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   OPENWEATHER_API_KEY=your_openweathermap_api_key


## Install dependencies:
pipenv install
pipenv shell

## Run the agent
python main.py