import os
import requests

from dotenv import load_dotenv
from logic_c import BussinesLogic


load_dotenv()


class YandexParser:
    def __init__(self):
        self.logic = BussinesLogic()

        self.api_key = os.getenv("YANDEX_MAPS_API_KEY")

        self.url = "https://search-maps.yandex.ru/v1/"

    def parse(self, query):
        pass

    def parse_businesses(self):
        queries = [
            "кафе Караганда",
            "кофейня Караганда",
            "ресторан Караганда",
            "фастфуд Караганда",
            "пекарня Караганда",
            "столовая Караганда",
            "бар Караганда",
            "гостиница Караганда",
        ]

        for query in queries:
            print(f"Парсинг категории: {query}")

            data = self.parse(query)


def parser_yandex():
    parser = YandexParser()
    parser.parse_businesses()


if __name__ == "__main__":
    parser_yandex()