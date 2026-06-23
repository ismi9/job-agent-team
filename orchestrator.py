import os
import time
from agents.scout import ScoutAgent
from agents.analyzer import AnalyzerAgent
from agents.proposal import ProposalAgent
from agents.executor import ExecutorAgent
from tools.telegram_notifier import TelegramNotifier
from dotenv import load_dotenv

load_dotenv()


class Orchestrator:
    def __init__(self):
        self.scout = ScoutAgent()
        self.analyzer = AnalyzerAgent()
        self.proposal = ProposalAgent()
        self.executor = ExecutorAgent()
        self.notifier = TelegramNotifier()

    def run_cycle(self):
        print("🔍 Починаю цикл пошуку завдань...")
        self.notifier.send_success("🔄 Job-Agent запущено", {"цикл": "новий пошук"})

        try:
            jobs = self.scout.search_jobs(keywords="Python AI freelance", limit=5)
            print(f"Знайдено {len(jobs)} завдань")
        except Exception as e:
            self.notifier.send_error("ScoutAgent", str(e))
            return

        viable_count = 0
        executed_count = 0

        for job in jobs:
            print(f"📊 Аналізую: {job.get('title', 'unknown')}")
            try:
                analysis = self.analyzer.analyze_job(job)
            except Exception as e:
                self.notifier.send_error(f"Analyzer: {job.get('title', '?')}", str(e))
                continue

            if analysis.get("viable"):
                viable_count += 1
                print(f"✍️ Генерую пропозицію для: {job.get('title')}")
                try:
                    proposal = self.proposal.generate_proposal(job, analysis)
                    print(f"📄 Пропозиція:\n{proposal}\n")
                except Exception as e:
                    self.notifier.send_error(f"Proposal: {job.get('title', '?')}", str(e))
                    continue

                if analysis.get("simple"):
                    print(f"⚡ Виконую просте завдання: {job.get('title')}")
                    try:
                        result = self.executor.execute_task(job)
                        executed_count += 1
                        print(f"✅ Результат: {result}")
                    except Exception as e:
                        self.notifier.send_error(f"Executor: {job.get('title', '?')}", str(e))
            else:
                print(f"⏭ Завдання не підходить: {job.get('title')}")

        summary = {
            "знайдено": len(jobs),
            "життєздатні": viable_count,
            "виконано": executed_count
        }
        self.notifier.send_success("Цикл завершено", summary)
        print(f"✅ Цикл завершено. Підсумок: {summary}")


if __name__ == "__main__":
    orch = Orchestrator()
    orch.run_cycle()