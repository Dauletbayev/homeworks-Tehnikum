#Палиндрома
while True:
    word = input('Введите слово чтобы проверить: ')
    if word == word[::-1]:
        print('Это слово палиндрома')
    else:
        print('Это слово не палиндрома')



#Таблица умножения
# while True:
#     number = int(input('Введите число: '))
#     for x in range(1, 10):
#         result = number * x
#         print(f'{number} * {x} = {result}')