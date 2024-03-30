import sqlite3

# Подключение к БД
conn = sqlite3.connect('userdata.db')
sql = conn.cursor()

# Создание таблицы clients
sql.execute('CREATE TABLE IF NOT EXISTS clients(name TEXT, phone TEXT, balance REAL)')
# Создание таблицы deposits для расчета вкладов
sql.execute('CREATE TABLE IF NOT EXISTS deposits(principal_amount REAL, annual_rate REAL, investment_period INTEGER, '
            'future_value REAL)')
conn.commit()

# Функция для регистрации нового клиента
def register_client():
    name = input('Введите имя клиента: ')
    phone = input('Введите номер телефона клиента: ')
    balance = float(input('Введите начальный баланс: '))
    sql.execute('INSERT INTO clients VALUES (?, ?, ?)', (name.title(), phone, balance))
    print(f'Регистрация клиента по имени "{name.title()}" прошла успешно!')
    conn.commit()

# Функция для поиска клиента
def search_client():
    search_by = input('Искать по имени или номеру телефона? (имя/телефон): ')
    if search_by.lower() == 'имя':
        name_to_search = input('Введите имя для поиска: ')
        sql.execute('SELECT * FROM clients WHERE name=?', (name_to_search.title(),))
    elif search_by.lower() == 'телефон':
        phone_to_search = input('Введите номер телефона для поиска: ')
        sql.execute('SELECT * FROM clients WHERE phone=?', (phone_to_search,))
    else:
        print('Некорректный выбор. Повторите попытку.')
        return
    result = sql.fetchone()
    if result:
        print(result)
    else:
        print('Клиент не найден.')

# Функция для пополнения баланса клиента
def deposit():
    name = input('Введите имя клиента: ')
    amount = float(input('Введите сумму для пополнения: '))
    sql.execute('UPDATE clients SET balance = balance + ? WHERE name = ?', (amount, name.title()))
    print(f'Баланс клиента по имени "{name.title()}" успешно пополнен на {amount}.')
    conn.commit()

# Функция для снятия средств с баланса клиента
def withdraw():
    name = input('Введите имя клиента: ')
    amount = float(input('Введите сумму для снятия: '))
    sql.execute('UPDATE clients SET balance = balance - ? WHERE name = ?', (amount, name.title()))
    print(f'Сумма "{amount}" успешно снята с баланса клиента по имени "{name.title()}".')
    conn.commit()

# Функция для просмотра баланса клиента
def view_balance():
    name = input('Введите имя клиента: ')
    sql.execute('SELECT balance FROM clients WHERE name=?', (name.title(),))
    result = sql.fetchone()
    if result:
        print(f'Баланс клиента по имени "{name.title()}": {result[0]}')
    else:
        print('Клиент не найден.')

# Функция для расчета будущей стоимости вклада и добавления информации в базу данных
def calculate_deposit():
    principal_amount = float(input("Введите сумму вклада: "))
    annual_rate = float(input("Введите годовую процентную ставку: "))
    investment_period = int(input("Введите количество месяцев: "))
    monthly_interest_rate = annual_rate / 12 / 100
    future_value = principal_amount * (1 + monthly_interest_rate) ** investment_period

    # Добавление информации о вкладе в базу данных
    sql.execute('INSERT INTO deposits(principal_amount, annual_rate, investment_period, future_value) VALUES (?, ?, '
                '?, ?)',
                (principal_amount, annual_rate, investment_period, future_value))
    conn.commit()

    print(f"Через {investment_period} месяцев ваш вклад составит: {future_value:.2f}")


# Функция для выполнения действии с личным кабинетом клиента
def personal_cabinet():
    while True:
        print('\nЛичный кабинет:')
        print('1. Пополнить баланс')
        print('2. Снять деньги')
        print('3. Просмотр баланса')
        print('4. подсчет вклада на 12-24-36 месяцев')
        print('5. Выйти из личного кабинета')

        choice = input('Выберите действие (1-5): ')

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            view_balance()
        elif choice == '4':
            calculate_deposit()
        elif choice == '5':
            break
        else:
            print('Некорректный выбор. Повторите попытку.')

# Функция для просмотра всех клиентов
def all_clients():
    all_info = sql.execute('SELECT * FROM clients').fetchall()
    if all_info:
        for info in all_info:
            print(info)
    else:
        print('Список клиентов пуст!')

conn.commit()

# Основная часть программы
while True:
    print('\nДоступные действия:')
    print('1. Регистрация клиента')
    print('2. Поиск клиента')
    print('3. Личный кабинет клиента')
    print('4. Все клиенты')
    print('5. Выйти')

    action = input('Выберите действие (1-5): ')

    if action == '1':
        register_client()
    elif action == '2':
        search_client()
    elif action == '3':
        personal_cabinet()
    elif action == '4':
        all_clients()
    elif action == '5':
        print('До свидания!')
        conn.close()
        exit()
    else:
        print('Некорректный выбор. Повторите попытку.')
