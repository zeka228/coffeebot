from io import FileIO
from pathlib import Path

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery

from markups.menu_markup import MenuMarkup, MenuBack
from menu_goods import get_all_goods, get_single


async def menu_handler(event: Message, bot: AsyncTeleBot):
    sqlite_menu_goods = await get_all_goods()
    sent = await bot.send_message(
        event.from_user.id,
        parse_mode="MarkdownV2",
        reply_markup=MenuMarkup(sqlite_menu_goods).get_markup(),
        text=
        (
            "📖 Наше меню:"
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


async def menu_good(event: CallbackQuery, bot: AsyncTeleBot):
    selected_good = await get_single(int(event.data))
    good_photo = FileIO((Path.cwd() / "bins" / f"{event.data}.jpg").resolve())
    sent = await bot.send_photo(
        event.from_user.id,
        photo=good_photo,
        reply_markup=MenuBack().get_markup(),
        caption=f"{selected_good.readable_name}, цена: {selected_good.price}руб."
    )
    prev_msg = await bot.get_state(event.from_user.id)
    if prev_msg:
        await bot.delete_message(event.from_user.id, int(prev_msg))
        await bot.delete_state(event.from_user.id)
    await bot.set_state(
        user_id=event.from_user.id,
        state=sent.message_id
    )
