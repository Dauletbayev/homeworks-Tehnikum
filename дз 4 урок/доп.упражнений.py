#Сдаем бутылки
morelitr1 = int(input('Сколько у вас бутылок объемом больше чем 1 литр: '))
lesslitr1 = int(input('Сколько у вас бутылок объемом 1 литр и меньше: '))

first_action = morelitr1 * 0.25
second_action = lesslitr1 * 0.1
result = first_action + second_action

print(f'${first_action} + ${second_action} = ${result:.2f}')

#Налоги и чаевые

thesum = int(input('Сумма вашего заказа в ресторане: '))

tax = thesum * 0.12
tips = thesum * 0.18
all = tax + tips + thesum

print(f'Налог: ${tax:.2f}\n'
      f'Чаевые: ${tips:.2f}\n'
      f'Общая сумма: ${tax} + ${tips} + ${thesum} = '
      f'${all:.2f}')


#Сумма чисел
num = int(input('Введите число: '))
result = 0

for x in range(1, num + 1):
    result = result + x
print(f'Сумма от 1 до введенного вами числа равна: {result}')


#Сувениры и безделушки
bezdelushki = int(input('Введите количество безделушек: '))
suveniri = int(input('Введите количество сувениров: '))

thesum1 = bezdelushki * 112
thesum2 = suveniri * 75
thesum = thesum1 + thesum2
thesum_in_kg = thesum / 1000

print(f'Вес всего что вы купили: {thesum} граммов или {thesum_in_kg} кг')