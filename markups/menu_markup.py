from telebot import types

from config import button_text
from menu_goods import goods_data
from .markup import Markup


class MenuMarkup(Markup):
    def __init__(self):
        self.markup = types.InlineKeyboardMarkup(row_width=2)
        goods_list = []
        for i, _ in enumerate(goods_data.items()):
            goods_list.append(types.InlineKeyboardButton(
                text=f"{_[1][0]} {_[1][1]}руб.",
                callback_data=f"{_[0].value}")
            )
        self.markup.add(*goods_list)
        self.markup.row(types.InlineKeyboardButton(text=button_text.get("back"), callback_data="-1"))


class MenuBack(Markup):
    def __init__(self, back_v: bool = False):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.row(
            types.InlineKeyboardButton(text=button_text.get("back"), callback_data="-1" if back_v else "-2"))
