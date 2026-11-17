import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEOAPIFY_API_KEY")

if not api_key:
    raise ValueError("Не найден API-ключ в файле .env")

url = "https://api.geoapify.com/v2/places"

params = {
    "categories": "catering.cafe,catering.restaurant,catering.fast_food",
    "filter": "rect:72.90,49.75,73.20,49.95",
    "limit": 20,
    "apiKey": api_key,
}

response = requests.get(url, params=params, timeout=30)

print("HTTP статус:", response.status_code)

if response.ok:
    data = response.json()
    places = data.get("features", [])

    print("Найдено заведений:", len(places))

    for place in places:
        properties = place.get("properties", {})

        print(
            properties.get("name"),
            "|",
            properties.get("formatted"),
            "|",
            properties.get("lat"),
            properties.get("lon"),
        )
else:
    print(response.text[:1000])