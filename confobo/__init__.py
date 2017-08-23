from functools import partial

import telepot
from telepot.loop import MessageLoop

from confobo.command.handlers import on_chat_message, on_callback_query
from confobo.secret import API_KEY


def get_message_loop():
    bot = telepot.Bot(API_KEY)
    loop = MessageLoop(bot, {
        'chat': partial(on_chat_message, bot=bot),
        'callback_query': partial(on_callback_query, bot=bot)
    })

    return loop
