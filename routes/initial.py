from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from markups.main_markup import MainMenuMarkup, GoBackMarkup


async def start_handler(event: Message, bot: AsyncTeleBot):
    sent = await bot.send_message(
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
    prev_msg = await bot.get_state(event.from_user.id)
    if prev_msg:
        await bot.delete_message(event.from_user.id, int(prev_msg))
        await bot.delete_state(event.from_user.id)
    await bot.set_state(
        user_id=event.from_user.id,
        state=sent.message_id
    )


async def about_handler(event: Message, bot: AsyncTeleBot):
    await bot.send_message(
        event.from_user.id,
        parse_mode="MarkdownV2",
        reply_markup=GoBackMarkup().get_markup(),
        text=
        (
            "_Связь с нами:_\nhttps://vk\.com/club236728142\n\n"
            "🏘 Где нас найти: Московское Шоссе д\. 228\n\n"
            "🕰 Режим работы:\nЕжедневно с 8:00 до 21:00\."
        )
    )
    prev_msg = await bot.get_state(event.from_user.id)
    if prev_msg:
        await bot.delete_message(event.from_user.id, int(prev_msg))
        await bot.delete_state(event.from_user.id)
