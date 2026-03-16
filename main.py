import asyncio
from telebot.async_telebot import AsyncTeleBot

import routes
from config import BOT_AUTH, BOT_VERBOSE

bot = AsyncTeleBot(BOT_AUTH)

bot.register_message_handler(
    routes.start_handler,
    commands=['start'],
    chat_types=['private'],
    pass_bot=True
)

if __name__ == "__main__":
    if BOT_VERBOSE:
        asyncio.run(bot.polling(skip_pending=True))
    else:
        asyncio.run(bot.infinity_polling(skip_pending=True))
