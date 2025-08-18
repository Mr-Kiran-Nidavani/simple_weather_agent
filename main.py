from agents.location_extractor.extractor import LocationExtractor
from agents.weather_extractor.extractor import WeatherExtractor
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def run_agent():
    extractor = LocationExtractor()
    weather_extractor = WeatherExtractor()
    user_input = input("Ask about the weather: ")
    location = extractor.extract_location(user_input)
    weather_info = weather_extractor.get_weather(location)
    print("Weather information:", weather_info)

if __name__ == "__main__":
    run_agent()
