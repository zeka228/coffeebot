from os import environ

BOT_VERBOSE = environ.get('COFFEE_VERBOSE', False)
BOT_AUTH = environ.get('BOT_AUTH', '')
