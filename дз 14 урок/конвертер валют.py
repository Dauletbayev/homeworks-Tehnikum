import requests
import telebot
import buttons_converter

url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'

USD = requests.get(url).json()[0]
print(USD)

bot = telebot.TeleBot('7199452062:AAGfh1cln3zyXNrdycgpm2TJMHINtx00FzI')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Привет, {message.from_user.first_name}, выбери валюту для конвертации в '
                              f'"Узбекские сумы"', reply_markup=buttons_converter.main_menyu())

@bot.message_handler(content_types=['text'])
def currency_sum(message):
    user_id = message.from_user.id
    if message.text.lower() == 'евро':
        bot.send_message(user_id, 'Введите сумму')
        bot.register_next_step_handler(message, eur_sum)
    elif message.text.lower() == 'доллар':
        bot.send_message(user_id, 'Введите сумму')
        bot.register_next_step_handler(message, usd_sum)
    elif message.text.lower() == 'рубль':
        bot.send_message(user_id, 'Введите сумму')
        bot.register_next_step_handler(message, rub_sum)
def eur_sum(message):
    user_id = message.from_user.id
    eur = int(message.text)
    convert = eur * 13520
    bot.send_message(user_id, f'{eur} € * 13520 = {convert} сумов')

def usd_sum(message):
    user_id = message.from_user.id
    usd = int(message.text)
    convert = usd * 12505
    bot.send_message(user_id, f'{usd} $ * 12505 = {convert} сумов')

def rub_sum(message):
    user_id = message.from_user.id
    rub = int(message.text)
    convert = rub * 135.20
    bot.send_message(user_id, f'{rub} ₽ * 135.20 = {convert} сумов')

bot.polling(none_stop=True)
