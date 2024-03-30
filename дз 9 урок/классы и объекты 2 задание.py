
# 2-задание
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_info = Person("'Pavel'", 21)
print(f'Имя {new_info.name}\n'
      f'Возраст {new_info.age}')

new_info.name = 'Sasha'
new_info.age = 19
print(f'Новое имя "{new_info.name}"\n'
      f'Новый возраст {new_info.age}')