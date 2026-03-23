from telebot import types

from config import button_text
from menu_goods import GoodsType
from .markup import Markup


class MenuMarkup(Markup):
    def __init__(self, all_goods: tuple[GoodsType, ...]):
        self.markup = types.InlineKeyboardMarkup(row_width=2)
        goods_list = []
        for i, _ in enumerate(all_goods):
            goods_list.append(types.InlineKeyboardButton(
                text=f"{_.readable_name} {_.price}руб.",
                callback_data=f"{_.db_id}")
            )
        self.markup.add(*goods_list)
        self.markup.row(types.InlineKeyboardButton(text=button_text.get("back"), callback_data="-1"))


class MenuBack(Markup):
    def __init__(self, back_v: bool = False):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.row(
            types.InlineKeyboardButton(text=button_text.get("back"), callback_data="-1" if back_v else "-2"))
