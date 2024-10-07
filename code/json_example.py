import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEAHTER_API_KEY")

city = "Wellesley"
country_code = "us"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}"

# print(url)  # Open this URL in your browser to see the data

with urllib.request.urlopen(url) as response:
    response_text = response.read().decode("utf-8")
    weather_data = json.loads(response_text)

print(weather_data)

# How do we get current temperature?
