from telebot import types

def main_menyu():
    kyeboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Перевод')
    button2 = types.KeyboardButton('Википедия')
    kyeboard.add(button1, button2)
    return kyeboard