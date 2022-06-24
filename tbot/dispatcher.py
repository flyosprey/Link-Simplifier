import validators
from tbot.link_service_api import *
from tbot_base.bot import tbot as bot
from tbot_base.models import BotUsers

from tbot.keyboards import *


def start(message):
    register_user(message)
    bot.send_message(message.chat.id, "Hi there!👋", parse_mode='HTML', reply_markup=menu(bot))
    bot.send_message(message.chat.id, "Do you want to simplify a url?🔗\n I am ready to work!🙂")


def register_user(message):
    if BotUsers.objects.filter(user_id=message.from_user.id).exists():
        return
    user_id, user_name, first_name = message.from_user.id, message.from_user.username, message.from_user.first_name
    last_name, is_bot = message.from_user.last_name, message.from_user.is_bot
    first_name = "" if first_name is None else first_name
    last_name = "" if last_name is None else last_name
    user_name = "" if user_name is None else user_name
    BotUsers(user_id, user_name, first_name, last_name, is_bot).save()


def help(message):
    bot.send_message(message.chat.id,
                     """Here you can see all available commands:
                     /start - To start bot.
                     /help - To view all available commands.
                     /send_link - To send link. 
                     """
                     )


def ask_link_by_message(message):
    bot.send_message(message.chat.id, "Send me your long link!🧐")
    bot.register_next_step_handler(message, get_link)


def ask_link_by_button(call):
    bot.send_message(call.from_user.id, "Send me your long link!🧐")
    bot.register_next_step_handler(call.message, get_link)


def get_link(message):
    bot.send_message(message.chat.id, "Processing...")
    if validators.url(message.text):
        simplified_url = simplify_url(message.text)
        bot.send_message(message.chat.id, "Your short link!😱")
        bot.send_message(message.chat.id, simplified_url)
    else:
        bot.reply_to(message, "The link is not valid! Choose /send_link command and try again!")
