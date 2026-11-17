import requests

from logic_c import BussinesLogic


class TwoGISParser:
    def __init__(self):
        self.logic = BussinesLogic()

        self.api_key = ""

        self.url = "https://catalog.api.2gis.com/3.0/items"

    def parse(self, query):
        params = {
            "q": query,
            "key": self.api_key,
            "fields": "items.point, items.rubics, items.reviews", 
            "page_size": 50,
            "page": 1,
        }

        response = requests.get(
            self.url,
            params=params
        )

        response.raise_for_status()

        data = response.json()

        return data

    def parse_businesses(self):
        queries = [
            "кафе",
            "кофейня",
            "ресторан",
            "фастфуд",
            "пекарня",
            "столовая",
            "бар",
        ]


        for query in queries:
            print(f"Парсинг категории: {query}")

            data = self.parse(query)

            for item in data.get("result", {}).get("items", []):
                business = {
                    "business_id": item.get("id"),
                    "name": item.get("name"),
                    "address": item.get("address_name"),
                    "latitude": item.get("point", {}).get("lat"),
                    "longitude": item.get("point", {}).get("lon"),
                    "category": "HoReCa",
                    "subcategory": query,
                }
                print(business)

                

def parser_2gis():
    parser = TwoGISParser()
    parser.parse_businesses()

if __name__ == "__main__":
    parser_2gis()