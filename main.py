import asyncio
from typing import Union, Optional

from telebot.async_telebot import AsyncTeleBot, logger

import routes
from config import BOT_AUTH, BOT_VERBOSE, button_text


class SafeDeleteBot(AsyncTeleBot):
    async def delete_message(
            self,
            chat_id: Union[int, str],
            message_id: int,
            timeout: Optional[int] = None
    ) -> bool:
        try:
            _ = await super().delete_message(chat_id, message_id, timeout)
        except Exception as e:
            logger.log(e)
        else:
            return _
        return False


bot = SafeDeleteBot(BOT_AUTH)

"""Register initial route
- start
- back
- about
- cb=-1
"""
bot.register_message_handler(
    routes.start_handler,
    commands=['start'],
    chat_types=['private'],
    pass_bot=True
)
bot.register_message_handler(
    routes.start_handler,
    func=lambda event: event.text == button_text.get("back"),
    chat_types=['private'],
    pass_bot=True
)
bot.register_message_handler(
    routes.about_handler,
    func=lambda event: event.text == button_text.get("about"),
    chat_types=['private'],
    pass_bot=True
)
bot.register_callback_query_handler(
    routes.start_handler,
    func=lambda cb: cb.data == "-1",
    pass_bot=True
)

"""Register menu route
- menu
- cb=0:10
- cb=-2
"""
bot.register_message_handler(
    routes.menu_handler,
    func=lambda event: event.text == button_text.get("menu"),
    chat_types=['private'],
    pass_bot=True
)
bot.register_callback_query_handler(
    routes.menu_good,
    func=lambda cb: cb.data.isdigit() and int(cb.data) in range(0, 10),
    pass_bot=True
)
bot.register_callback_query_handler(
    routes.menu_handler,
    func=lambda cb: cb.data == "-2",
    pass_bot=True
)

if __name__ == "__main__":
    if BOT_VERBOSE:
        logger.setLevel(10)
        asyncio.run(bot.polling(skip_pending=True))
    else:
        asyncio.run(bot.infinity_polling(skip_pending=True))
