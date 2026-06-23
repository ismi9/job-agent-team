# Dockerfile для Job Agent Team
# Оптимізовано для VPS (Hetzner, DigitalOcean тощо)

FROM python:3.11-slim

# Встановлюємо системні залежності для Playwright та браузера
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    fonts-liberation \
    libappindicator3-1 \
    libnspr4 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо файли проекту
COPY requirements.txt .
COPY . .

# Встановлюємо Python залежності
RUN pip install --no-cache-dir -r requirements.txt

# Встановлюємо Playwright браузери (chromium)
RUN playwright install chromium --with-deps

# Відкриваємо порт для Telegram бота (якщо потрібно)
EXPOSE 8080

# Налаштування змінних середовища
ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Встановлюємо cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Копіюємо cron файл
COPY cronjob /etc/cron.d/job-agent-cron
RUN chmod 0644 /etc/cron.d/job-agent-cron && crontab /etc/cron.d/job-agent-cron

# Точка входу — запускаємо cron
CMD ["sh", "-c", "cron && tail -f /dev/null"]
