import requests
import os
import json

class WeatherExtractor:
    def __init__(self):
        self.api_key = os.getenv("OPEN_WEATHER_API_KEY")
        self.api_url = os.getenv("OPEN_WEATHER_URL")

    def get_weather(self, obj):
        params = {
            "q": obj.get("location"),
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.api_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_desc = data['weather'][0]['description']
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                return {
                    "location": obj.get("location"),
                    "weather": weather_desc,
                    "temperature": f"{temp}°C",
                    "feels_like": f"{feels_like}°C"
                }
            else:
                # Handle API errors (like 401, 404, etc.)
                return {
                    "error": data.get("message", "Unknown error"),
                    "code": data.get("cod", response.status_code)
                }

        except requests.RequestException as e:
            # Handle network errors
            return {
                "error": str(e),
                "code": "network_error"
            }
