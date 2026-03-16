from telebot.async_telebot import REPLY_MARKUP_TYPES


class Markup:
    markup = None

    def get_markup(self) -> REPLY_MARKUP_TYPES:
        return self.markup
