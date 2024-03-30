all_products = {'Весь склад': {}}
basket = []

while True:
    action = input('Что вы хотите сделать?: ')
    if action.title() == 'Добавить':
        name_product = input('Введите название продукта: ')
        product_count = int(input('Введите количество продукта: '))
        all_products['Весь склад'][name_product] = product_count
        print(f'Продукт и его количество успешно добавлено\n'
              f'{all_products}')
    elif action.title() == 'Изменить':
        old_name = input('Введите название товара который хотите изменить: ')
        new_name = input('Введите новый товар вместо этого: ')
        new_name_count = input('Введите количество этого товара: ')
        all_products['Весь склад'][new_name] = all_products['Весь склад'].pop(old_name)
        all_products['Весь склад'][new_name] = int(new_name_count)
        print(all_products)
    elif action.title() == 'Удалить':
        product_to_del = input('Введите название товара который хотите удалить: ')
        if product_to_del in all_products['Весь склад']:
            all_products['Весь склад'].pop(product_to_del)
            print(f'товар успешно удален \n'
                  f'{all_products}')
        else:
            print('Такого товара итак нету в складе')
    elif action.title() == 'Склад':
        print(all_products)
        add_to_basket = input('Хотите что нибудь добавить в корзину из склада? ')
        if add_to_basket.lower() == 'да':
            name_add_product = input(f'Введите название продукта: ')
            if name_add_product in all_products['Весь склад']:
                quantity_to_add = int(input(f'Введите количество: '))
                if quantity_to_add <= all_products['Весь склад'][name_add_product]:
                    all_products['Весь склад'][name_add_product] -= quantity_to_add
                    print(f'{quantity_to_add} {name_add_product} добавлено в корзину. \n'
                          f'Остаток на складе: {all_products["Весь склад"][name_add_product]}')
                    basket.append({name_add_product: quantity_to_add})
                else:
                    print('Недостаточно товара на складе.')
            else:
                print('Такого товара нет на складе.')
        elif add_to_basket.lower() == 'нет':
            continue
        else:
            print('Я не понял что мне делать (')
    elif action.title() == 'Корзина':
        print(basket)
    else:
        print('Я не понял что сделать (')
