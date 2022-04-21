from telebot import types
from telebot.apihelper import ApiTelegramException

from tbot.dispatcher import *


@bot.message_handler(commands=['start'])
def start_handler(message):
    start(message)


@bot.message_handler(commands=['help'])
def help_handler(message):
    help(message)


@bot.message_handler(func=lambda message: True if message.text == ASK_LINK else False)
@bot.message_handler(commands=["send_link"])
def ask_link_handler(message):
    ask_link_by_message(message)


@bot.callback_query_handler(func=lambda call: True if call.data == ASK_LINK else False)
def ask_link_by_button_handler(call: types.CallbackQuery):
    ask_link_by_button(call)


@bot.message_handler(func=lambda message: True)
def text_messages(message: types.Message):
    bot.send_message(message.from_user.id, 'I don`t know people language so well.😢\b'
                                           'If you need instruction to use me then send me "/help"!🙃')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    bot.send_message(call.from_user.id, 'I don`t know people language so well.😢\b'
                                        'If you need instruction to use me then send me "/help"!🙃')
    # remove the "clock" on the inline button
    try:
        bot.answer_callback_query(callback_query_id=call.id, text='')
    except ApiTelegramException:
        pass
