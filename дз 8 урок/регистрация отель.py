clients = {}
opened_rooms = [i for i in range(1, 51)]
closed_rooms = []
def check_in(name, room):
    clients[name] = room
    opened_rooms.remove(room)
    closed_rooms.append(room)

def check_out(name):
    closed_rooms.remove(clients[name])
    opened_rooms.append(clients[name])
    clients.pop(name)

def show_rooms():
    return closed_rooms

while True:
    admin = input('Введите действие: ')
    if admin.lower() == 'регистрация':
        client_name = input('Имя клиента: ')
        print(opened_rooms)
        client_room = int(input('Номер клиента: '))
        check_in(client_name, client_room)
        print('Клиент успешно добавлен!')
    elif admin.lower() == 'выселение':
        client_name = input('Имя клиента: ')
        check_out(client_name)
        print('Клиент успешно выселен!')
    elif admin.lower() == 'номера':
        print(show_rooms())
    else:
        print('Не понял вас')