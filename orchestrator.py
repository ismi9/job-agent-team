import os
from dotenv import load_dotenv
from agents.scout import ScoutAgent
from agents.analyzer import AnalyzerAgent
from agents.proposal import ProposalAgent
from agents.executor import ExecutorAgent

load_dotenv()

class Orchestrator:
    def __init__(self):
        self.scout = ScoutAgent()
        self.analyzer = AnalyzerAgent()
        self.proposal = ProposalAgent()
        self.executor = ExecutorAgent()
    
    def run_cycle(self):
        print("🚀 Запуск циклу пошуку роботи...")
        
        # Крок 1: Пошук
        jobs = self.scout.search_jobs(keywords="Python AI freelance", limit=5)
        
        # Крок 2: Аналіз
        for job in jobs:
            analysis = self.analyzer.analyze_job(job)
            if analysis['viable']:
                # Крок 3: Пропозиція
                proposal = self.proposal.generate_proposal(job, analysis)
                print("📝 Пропозиція готова:", proposal[:200])
                
                # Крок 4: Виконання (якщо мікро-завдання)
                if analysis['simple']:
                    result = self.executor.execute_task(job)
                    print("✅ Завдання виконано:", result)
        
        print("Цикл завершено. Перевірте Telegram для сповіщень.")

if __name__ == "__main__":
    orch = Orchestrator()
    orch.run_cycle()
