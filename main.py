import asyncio
from telebot.async_telebot import AsyncTeleBot

import routes
from config import BOT_AUTH

bot = AsyncTeleBot(BOT_AUTH)

bot.register_message_handler(
    routes.start_handler,
    chat_types=['private'],
    pass_bot=True
)

if __name__ == "__main__":
    asyncio.run(bot.polling(skip_pending=True))
