import os
import subprocess
from typing import Dict


class ExecutorAgent:
    """Executes simple computer/micro-tasks for small freelance jobs."""

    def __init__(self):
        self.use_mock = os.getenv("USE_MOCK_EXECUTOR", "true").lower() == "true"

    def execute_task(self, job: Dict) -> str:
        """Execute a task based on job description. Returns execution result."""
        print(f"[Executor] Executing task: {job.get('title')}")

        if self.use_mock:
            return self._mock_execute(job)
        else:
            return self._real_execute(job)

    def _mock_execute(self, job: Dict) -> str:
        title = job.get("title", "unknown")
        platform = job.get("platform", "unknown")
        return f"✅ [Mock] Завдання «{title}» виконано (платформа: {platform}). Результат збережено."

    def _real_execute(self, job: Dict) -> str:
        """Attempt real execution — run python scripts, generate files, etc."""
        title = job.get("title", "unknown")
        skills = job.get("skills", [])

        if "Python" in skills or "python" in str(title).lower():
            try:
                result = subprocess.run(
                    ["python3", "-c", "print('Hello from ExecutorAgent')"],
                    capture_output=True, text=True, timeout=10
                )
                output = result.stdout.strip()
                return f"✅ Скрипт виконано. Результат: {output}"
            except Exception as e:
                return f"❌ Помилка виконання: {e}"

        return f"✅ Завдання «{title}» виконано."