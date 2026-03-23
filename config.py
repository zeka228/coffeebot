from os import environ

button_text = {
    "menu": "📖 Меню",
    "about": "❗️ О нас",
    "back": "🔙 Назад"
}

BOT_VERBOSE = environ.get('COFFEE_VERBOSE', False)
BOT_PROXY = environ.get('COFFEE_PROXY', None)
BOT_AUTH = environ.get('COFFEE_AUTH', '')
