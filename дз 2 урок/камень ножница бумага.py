print('Добро пожаловать в игру "Камень, ножница, бумага"')
print('')

first_player = input('Игрок 1 выберите действие: ')
second_player = input('Игрок 2 выберите действие: ')

if first_player == 'Ножница' and second_player == 'Камень':
    print('Второй игрок выиграл )')
elif first_player == 'Ножница' and second_player == 'Бумага':
    print('Первый игрок выиграл )')
elif first_player == 'Камень' and second_player == 'Ножница':
    print('Первый игрок выиграл )')
elif first_player == 'Камень' and second_player == 'Бумага':
    print('Второй игрок выиграл )')
elif first_player == 'Бумага' and second_player == 'Ножница':
    print('Второй игрок выиграл )')
elif first_player == 'Бумага' and second_player == 'Камень':
    print('Первый игрок выиграл )')
elif first_player == second_player:
    print('Ничья )')
else:
    print('Выберите существуещий инструмент 😡')