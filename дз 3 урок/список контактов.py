contacts = ['Антон', 'Саша', 'Ваня', 'Дима', 'Денис']
print('Вот ваш список контактов'), print(contacts)
print('')
action = input('Что хотите сделать (Добавить, Изменить или Удалить): ')

if action == 'Добавить':
    new_contact = input('Введите имя нового контакта: ')
    contacts.append(new_contact)
    print(contacts)
elif action == 'Изменить':
    edit_contact = input('Введите имя контакта которую хотите изменить: ')
    name_index = contacts.index(edit_contact)
    newname_contact = input('Введите новую имю для этого контака: ')
    contacts[name_index] = newname_contact
    print(contacts)
elif action == 'Удалить':
    del_contact = input('Введите имя контакта которую хотите удалить: ')
    index_delcontact = contacts.index(del_contact)
    contacts.pop(index_delcontact)
    print(contacts)
else:
    print('Я не понял что мне нужно делать :(')