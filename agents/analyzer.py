class AnalyzerAgent:
    def analyze_job(self, job):
        print(f"📊 Аналізую завдання: {job['title']}")
        # Симуляція аналізу
        return {
            'viable': True,
            'simple': job['budget'] < 100,
            'score': 8.5,
            'recommendation': 'Добре підходить під навички Python/AI'
        }
