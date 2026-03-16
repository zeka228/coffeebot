from io import FileIO
from pathlib import Path

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery

from markups.menu_markup import MenuMarkup, MenuBack
from menu_goods import Goods, goods_data


async def menu_handler(event: Message, bot: AsyncTeleBot):
    sent = await bot.send_message(
        event.from_user.id,
        parse_mode="MarkdownV2",
        reply_markup=MenuMarkup().get_markup(),
        text=
        (
            "📖 Наше меню:"
        )
    )
    prev_msg = await bot.get_state(event.from_user.id)
    if prev_msg:
        await bot.delete_message(event.from_user.id, int(prev_msg))
    await bot.set_state(
        user_id=event.from_user.id,
        state=sent.message_id
    )


async def menu_good(event: CallbackQuery, bot: AsyncTeleBot):
    selected_good = goods_data[Goods(int(event.data))]
    good_photo = FileIO((Path.cwd() / "bins" / f"{event.data}.jpg").resolve())
    sent = await bot.send_photo(
        event.from_user.id,
        photo=good_photo,
        reply_markup=MenuBack().get_markup(),
        caption=f"{selected_good[0]}, цена: {selected_good[1]}руб."
    )
    prev_msg = await bot.get_state(event.from_user.id)
    if prev_msg:
        await bot.delete_message(event.from_user.id, int(prev_msg))
    await bot.set_state(
        user_id=event.from_user.id,
        state=sent.message_id
    )
