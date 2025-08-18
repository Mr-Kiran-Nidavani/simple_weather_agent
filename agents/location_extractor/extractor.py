import requests
import os
from agents.location_extractor.prompt import LOCATION_EXTRACTION_PROMPT
import json

class LocationExtractor:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.api_url = os.getenv("URL")
        self.model = os.getenv("MODAL")
        self.system_prompt = LOCATION_EXTRACTION_PROMPT

    def extract_location(self, user_input):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ],
            "max_tokens": 20
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            location = response.json()["choices"][0]["message"]["content"].strip()
            return json.loads(location)
        else:
            print("OpenRouter API error:", response.status_code, response.text)
            return None
