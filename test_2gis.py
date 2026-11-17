import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("TWOGIS_API_KEY")

url = "https://catalog.api.2gis.com/3.0/items"

params = {
    "q": "кафе",
    "location": "73.085,49.806",
    "locale": "ru_KZ",
    "page_size": 5,
    "key": API_KEY
}

response = requests.get(url, params=params)

print("Status:", response.status_code)
print(response.text[:5000])