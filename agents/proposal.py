class ProposalAgent:
    def generate_proposal(self, job, analysis):
        print("✍️ Генерую пропозицію...")
        return f"""Вітаю! Я фахівець з {job.get('title', '')}.
Готовий виконати завдання швидко та якісно.
Бюджет: {job.get('budget', '')} USD.
Мої навички: Python, AI, автоматизація."""
