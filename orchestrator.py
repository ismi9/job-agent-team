import os
import traceback
from dotenv import load_dotenv
from agents.scout import ScoutAgent
from agents.analyzer import AnalyzerAgent
from agents.proposal import ProposalAgent
from agents.executor import ExecutorAgent
from tools.telegram_notifier import TelegramNotifier

load_dotenv()

class Orchestrator:
    def __init__(self):
        self.scout = ScoutAgent()
        self.analyzer = AnalyzerAgent()
        self.proposal = ProposalAgent()
        self.executor = ExecutorAgent()
        self.notifier = TelegramNotifier()
    
    def run_cycle(self):
        try:
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
            
            print("✅ Цикл завершено успішно.")
            
            success_details = {
                "Оброблено завдань": len(jobs),
                "Знайдено перспективних": sum(1 for j in jobs if j.get('viable', False)) if jobs else 0
            }
            self.notifier.send_success("Цикл пошуку та обробки завдань пройшов успішно!", success_details)
            
        except Exception as e:
            error_details = f"{str(e)}\n\n{traceback.format_exc()}"
            print(f"❌ Помилка в циклі: {e}")
            self.notifier.send_error(error_details, context="orchestrator.run_cycle")


if __name__ == "__main__":
    orch = Orchestrator()
    orch.run_cycle()
