from telebot import types

from .markup import Markup
from config import button_text


class MainMenuMarkup(Markup):
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        self.markup.row(types.KeyboardButton(button_text.get("menu"), style="primary"))
        self.markup.row(types.KeyboardButton(button_text.get("about")))


class GoBackMarkup(Markup):
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        self.markup.row(types.KeyboardButton(button_text.get("back")))
