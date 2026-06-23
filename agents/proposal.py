import os
from typing import Dict, Optional


class ProposalAgent:
    """Generates tailored proposals for freelance jobs using AI."""

    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.llm_provider = os.getenv("LLM_PROVIDER", "mock")

    def _mock_proposal(self, job: Dict, analysis: Dict) -> str:
        title = job.get("title", "Проєкт")
        budget = job.get("budget", "договірна")
        return (
            f"👋 Доброго дня!\n\n"
            f"Зацікавив ваш проєкт «{title}».\n"
            f"Маю досвід у подібних задачах, можу зробити якісно та в строк.\n"
            f"Бюджет: {budget} USD.\n\n"
            f"Готовий обговорити деталі в чаті.\n"
            f"Дякую за увагу!"
        )

    def _ai_proposal(self, job: Dict, analysis: Dict) -> str:
        """Generate proposal via OpenAI-compatible API."""
        import requests

        title = job.get("title", "Проєкт")
        desc = job.get("description", "")
        budget = job.get("budget", "договірна")
        skills = ", ".join(job.get("skills", []))

        system_prompt = "Ти — досвідчений фрілансер. Пишеш короткі, професійні пропозиції українською мовою."
        user_prompt = (
            f"Створи пропозицію для проєкту:\n"
            f"Назва: {title}\n"
            f"Опис: {desc}\n"
            f"Бюджет: {budget} USD\n"
            f"Потрібні навички: {skills}\n\n"
            f"Напиши 2-3 речення, чому я підходжу."
        )

        try:
            resp = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.openai_api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": 0.7,
                    "max_tokens": 300,
                },
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"[Proposal] AI generation failed: {e}, falling back to mock")
            return self._mock_proposal(job, analysis)

    def generate_proposal(self, job: Dict, analysis: Dict) -> str:
        """Generate a tailored proposal for a job."""
        print(f"[Proposal] Generating proposal for: {job.get('title')}")

        if self.llm_provider == "openai" and self.openai_api_key:
            return self._ai_proposal(job, analysis)
        else:
            return self._mock_proposal(job, analysis)