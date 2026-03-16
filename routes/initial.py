from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from markups.main_markup import MainMenuMarkup


async def start_handler(event: Message, bot: AsyncTeleBot):
    await bot.send_message(
        event.from_user.id,
        parse_mode="MarkdownV2",
        reply_markup=MainMenuMarkup().get_markup(),
        text=
        (
            "_**Добро пожаловать в нашу кофейню\!**_ ☕️\n"
            "_Мы готовим ароматный кофе из отборных зерен, свежую выпечку и десерты\._\n\n"
            "У нас можно быстро взять кофе с собой или уютно провести время с друзьями, поработать или отдохнуть\."
        )
    )
