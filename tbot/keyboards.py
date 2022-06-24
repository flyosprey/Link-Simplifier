from telebot import types


########################################### KEYBOARDS ##################################################################

ASK_LINK = "🔗 Cut Link Now 🔗"


def menu(bot):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton(ASK_LINK))
    bot.set_my_commands([
        types.BotCommand("/start", "start"),
        types.BotCommand("/help", "help"),
        types.BotCommand("/send_link", "send link")
    ])
    return keyboard
