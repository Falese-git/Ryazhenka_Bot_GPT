import os
from aiogram import Bot, Dispatcher, types, executor
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN") or "7887382137:AAGQt-uyPa4mLu3A8d9VxHQipYEujmjuq24"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Используем бесплатный Hugging Face Inference API
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_HEADERS = {"Authorization": "Bearer hf_xxx"}  # Можно без токена для публичных моделей

def ask_ai(text):
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": text})
    if response.ok:
        result = response.json()
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            return "[Ошибка генерации ответа]"
    return "[Ошибка подключения к ИИ]"

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бесплатный ИИ-бот. Напиши мне любой вопрос!")

@dp.message_handler()
async def handle_message(message: types.Message):
    user_text = message.text
    await message.reply("Генерирую ответ...")
    answer = ask_ai(user_text)
    await message.reply(answer)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
