import telebot
import buttons

bot = telebot.TeleBot('7169163056:AAG6ZGUYDLFaZVXMHSfkYrWq9zyvW6fUxpM')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Привет, {message.from_user.first_name}, чем могу помочь?',
                     reply_markup=buttons.main_menyu())


@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'перевод':
        bot.send_message(user_id, 'Перевести с какого языка?\n'
                                  'Доступные языки: Русский, Английсикй!')
        bot.register_next_step_handler(message, choose_language)
    elif message.text.lower() == 'википедия':
        bot.send_message(user_id, 'Что вы хотите узнать?\n'
                                  'Доступные вопросы:\n'
                                  '"Что такое пайтон?"\n'
                                  '"Зачем нам нужен пайтон?"')
        bot.register_next_step_handler(message, search_viki)
    else:
        bot.send_message(user_id, 'Нажмите на одну из кнопок ниже!')


def choose_language(message):
    user_id = message.from_user.id
    if message.text.lower() == 'русский':
        bot.send_message(user_id, 'Введите слово для перевода\n'
                                  'Доступные слова: "Привет", "Пока"')
        bot.register_next_step_handler(message, russian_translate)
    elif message.text.lower() == 'английский':
        bot.send_message(user_id, 'Send me a word to translate\n'
                                  'Available words: "Hello", "Bye"')
        bot.register_next_step_handler(message, english_translate)
    else:
        bot.send_message(user_id, 'Введите доступный язык!')


def russian_translate(message):
    user_id = message.from_user.id
    if message.text.lower() == 'привет':
        bot.send_message(user_id, 'Перевод слова "Привет": Hello')
    elif message.text.lower() == 'пока':
        bot.send_message(user_id, 'Перевод слова "Пока": Bye')
    else:
        bot.send_message(user_id, 'Я не знаю перевод этого слова (')


def english_translate(message):
    user_id = message.from_user.id
    if message.text.lower() == 'hello':
        bot.send_message(user_id, 'The translated version of the word "Hello": Привет')
    elif message.text.lower() == 'bye':
        bot.send_message(user_id, 'The translated version of the word "Bye": Пока')
    else:
        bot.send_message(user_id, "I don't know the translation of this word :(")


def search_viki(message):
    user_id = message.from_user.id
    if message.text.lower() == 'что такое пайтон?':
        bot.send_message(user_id, 'Python — высокоуровневый язык программирования общего назначения с динамической '
                                  'строгой типизацией и автоматическим управлением памятью, ориентированный на '
                                  'повышение производительности разработчика, читаемости кода и его качества, '
                                  'а также на обеспечение переносимости написанных на нём программ.')
    elif message.text.lower() == 'зачем нам нужен пайтон?':
        bot.send_message(user_id, 'Специалисты по работе с данными используют библиотеки Python ML для моделей '
                                  'машинного обучения и создания классификаторов, которые точно классифицируют '
                                  'данные. Классификаторы на основе Python используются в различных областях и '
                                  'применяются для выполнения таких задач, как классификация изображений, '
                                  'текста и сетевого трафика, распознавание речи и распознавание лиц. Специалисты по '
                                  'работе с данными также используют Python для глубокого обучения — передовой '
                                  'техники машинного обучения.')
    else:
        bot.send_message(user_id, 'Я не знаю (')

bot.polling(none_stop=True)
