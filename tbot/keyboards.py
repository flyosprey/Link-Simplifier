from telebot import types


########################################### KEYBOARDS ##################################################################

ASK_LINK = "🔗 Cut Link Now 🔗"


def menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton(ASK_LINK))
    return keyboard


# def inline_button_url():
#     keyboard = types.InlineKeyboardMarkup(row_width=5)
#     keyboard.add(types.InlineKeyboardButton(ASK_LINK, callback_data=ASK_LINK))
#     return keyboard
