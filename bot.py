import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ChatJoinRequest

# ТУТ МЕНЯЕШЬ СВОИ ДАННЫЕ
BOT_TOKEN = "8511101760:AAGAmeK5nFNRIeiy6dobwcgdrxjJxZXXRvk"  # токен бота
CHANNEL_ID = -1003325257490  # ID канала (обязательно с -100 в начале)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

# Команда /start — просто приветствие (можно не трогать)
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Бот работает! Заявки в канал принимаются автоматически 🚀")

# Главная магия — обработка заявок на вступление
@dp.chat_join_request()
async def approve_join_request(request: ChatJoinRequest):
    # Можно добавить любую проверку, сейчас — принимаем ВСЕХ автоматически
    await request.approve()
    
    # Опционально — пишем человеку в ЛС, что он принят + ссылка на схему
    try:
        await bot.send_message(
            chat_id=request.from_user.id,
            text="🔥 Ты в закрытом канале!\n\n"
                 "Схема, которая уже сделала +500 человек богатыми в 2025–2026 здесь:\n"
                 "https://t.me/mineshackapp3_bot"
                 "Читай закреплённые сообщения — там всё по шагам 💸"
        )
    except:
        pass  # если у юзера закрыты ЛС — просто игнорируем

async def main():
    print("Бот запущен и принимает заявки автоматически...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
