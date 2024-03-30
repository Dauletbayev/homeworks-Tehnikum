from telebot import types

def main_menyu():
    kyeboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('евро')
    button2 = types.KeyboardButton('доллар')
    button3 = types.KeyboardButton('рубль')
    kyeboard.add(button1, button2, button3)
    return kyeboard