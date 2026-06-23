import os
import random
import time
from typing import List, Dict


class ScoutAgent:
    """Scout that searches for freelance jobs across multiple platforms."""

    PLATFORMS = {
        "kwork": {"base_url": "https://kwork.ru/projects", "search_param": "search_query"},
        "freelancehunt": {"base_url": "https://freelancehunt.com/projects", "search_param": "q"},
        "upwork": {"base_url": "https://www.upwork.com/search/projects", "search_param": "q"},
    }

    def __init__(self):
        self.use_mock = os.getenv("USE_MOCK_SCOUT", "true").lower() == "true"

    def _mock_search(self, keywords: str, limit: int) -> List[Dict]:
        """Return realistic mock jobs for development/testing."""
        mock_jobs = [
            {
                "id": "job_001",
                "title": "Python AI Telegram Bot",
                "description": "Потрібен Telegram бот на Python з інтеграцією OpenAI API для автоматизації відповідей.",
                "platform": "Upwork",
                "url": "https://upwork.com/jobs/001",
                "budget": 150,
                "currency": "USD",
                "skills": ["Python", "AI", "Telegram API", "OpenAI"],
                "posted": "2026-06-22",
            },
            {
                "id": "job_002",
                "title": "Скрапінг даних для ML моделі",
                "description": "Зібрати дані з 5 сайтів для навчання моделі машинного навчання.",
                "platform": "Kwork",
                "url": "https://kwork.ru/projects/002",
                "budget": 80,
                "currency": "USD",
                "skills": ["Python", "Scraping", "BeautifulSoup", "ML"],
                "posted": "2026-06-23",
            },
            {
                "id": "job_003",
                "title": "Fullstack Web App PWA",
                "description": "Розробити PWA для обліку завдань з React + FastAPI backend.",
                "platform": "Freelancehunt",
                "url": "https://freelancehunt.com/projects/003",
                "budget": 500,
                "currency": "USD",
                "skills": ["React", "FastAPI", "PWA", "PostgreSQL"],
                "posted": "2026-06-21",
            },
            {
                "id": "job_004",
                "title": "Налаштувати CI/CD pipeline",
                "description": "Налаштувати GitHub Actions для автоматичного деплою Python сервісу на VPS.",
                "platform": "Upwork",
                "url": "https://upwork.com/jobs/004",
                "budget": 200,
                "currency": "USD",
                "skills": ["DevOps", "Docker", "CI/CD", "Linux"],
                "posted": "2026-06-23",
            },
            {
                "id": "job_005",
                "title": "Ремонт та доопрацювання скрипту Python",
                "description": "Виправити баги та додати нові функції в існуючий Python скрипт парсингу.",
                "platform": "Kwork",
                "url": "https://kwork.ru/projects/005",
                "budget": 50,
                "currency": "USD",
                "skills": ["Python", "Debugging", "Parsing"],
                "posted": "2026-06-22",
            },
        ]
        random.shuffle(mock_jobs)
        return mock_jobs[:limit]

    def search_jobs(self, keywords: str = "Python AI freelance", limit: int = 5) -> List[Dict]:
        """
        Search for freelance jobs. Returns a list of job dicts.
        Each job has: id, title, description, platform, url, budget, currency, skills, posted.
        """
        if self.use_mock:
            print(f"[Scout] Mock mode: searching for '{keywords}', limit={limit}")
            return self._mock_search(keywords, limit)

        # Real implementation placeholder — will use Playwright/requests per platform
        print(f"[Scout] Real mode: would search {keywords} on {list(self.PLATFORMS.keys())}")
        return self._mock_search(keywords, limit)