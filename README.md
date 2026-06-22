# Команда Агентів для Пошуку Роботи та Заробітку

## Опис
Це система мульти-агентів на Python для автоматизації пошуку фріланс-роботи, генерації пропозицій та виконання простих завдань.

**Важливо**: Повна автономія без втручання неможлива через політики платформ. Система вимагає:
- Ваші API ключі (OpenAI / Grok / Anthropic)
- Ручне підтвердження на платформах
- Ваш гаманець для виплат

## Структура
- orchestrator.py — головний керуючий
- agents/ — окремі агенти
- tools/ — інструменти (скрапінг, генерація)
- config.py — налаштування

## Як запустити

1. `cd job_agent_team`
2. `python3 -m venv venv`
3. `source venv/bin/activate` (Linux/Mac) або `venv\Scripts\activate` (Windows)
4. `pip install -r requirements.txt`
5. Скопіюйте `.env.example` → `.env` і заповніть ключі
6. `python orchestrator.py`

## Розширення
- Додайте реальний scraping з Playwright/Selenium
- Інтегруйте CrewAI для розумніших агентів
- Налаштуйте Telegram-бота для керування
- Для виплат — TON Wallet API

Система готова до розширення!

## 🚀 Розгортання на VPS (Docker)

### 1. Підготовка VPS (Ubuntu 22.04/24.04)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose git -y
sudo systemctl enable --now docker
```

### 2. Клонування та запуск
```bash
git clone <your-repo> job_agent_team
cd job_agent_team

# Скопіюйте .env.example -> .env і заповніть ключі
cp .env.example .env
nano .env

# Збірка та запуск
docker-compose up --build -d
```

### 3. Перегляд логів
```bash
docker logs -f job-agent-team
```

### 4. Оновлення системи
```bash
git pull
docker-compose down
docker-compose up --build -d
```

### 5. Автозапуск при перезавантаженні
Docker-compose з `restart: unless-stopped` робить це автоматично.
