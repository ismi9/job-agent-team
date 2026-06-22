import requests
from bs4 import BeautifulSoup

class ScoutAgent:
    def search_jobs(self, keywords="Python freelance", limit=5):
        print(f"🔍 Пошук завдань за ключовими словами: {keywords}")
        # Приклад симуляції (реально використовувати API або scraping)
        mock_jobs = [
            {"title": "Написати скрипт Python", "platform": "Kwork", "budget": 50, "link": "https://example.com/1"},
            {"title": "Аналіз даних AI", "platform": "Upwork", "budget": 200, "link": "https://example.com/2"},
        ]
        return mock_jobs[:limit]
