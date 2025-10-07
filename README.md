# Бесплатный Telegram ИИ-бот для Railway

## Быстрый старт

1. Склонируй репозиторий на Railway или локально:
   ```bash
   git clone https://github.com/Falese-git/Ryazhenka_Bot_GPT.git
   ```
2. Укажи свой токен Telegram в `.env` (или используй пример):
   ```env
   TELEGRAM_TOKEN=7887382137:AAGQt-uyPa4mLu3A8d9VxHQipYEujmjuq24
   ```
3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запусти локально:
   ```bash
   python app/bot.py
   ```
5. Для Railway просто деплой — Procfile уже готов.

## Бесплатный ИИ
Используется Hugging Face Inference API (GPT-2, без токена). Можно заменить на любую open-source модель.

## Файлы
- `app/bot.py` — основной код бота
- `requirements.txt` — зависимости
- `.env.example` — пример переменных окружения
- `Procfile` — для Railway

## Вопросы? Пиши!
