# Задача - 2
class Student:
    def __init__(self, name='Ivan', age=18,  groupNumber='10A'):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def setGroupNumber(self, new_GroupNumber):
        self.groupNumber = new_GroupNumber

Student1 = Student()
Student2 = Student('John', 22, '12C')
Student3 = Student('Anna', 20, '11B')
Student4 = Student('Eva', 19, '11A')
Student5 = Student('Peter', 21, '12B')

print(f'Имя: {Student1.name}, Возраст: {Student1.age}, Номер группы: {Student1.groupNumber}')
print(f'Имя: {Student2.name}, Возраст: {Student2.age}, Номер группы: {Student2.groupNumber}')
print(f'Имя: {Student3.name}, Возраст: {Student3.age}, Номер группы: {Student3.groupNumber}')
print(f'Имя: {Student4.name}, Возраст: {Student4.age}, Номер группы: {Student4.groupNumber}')
print(f'Имя: {Student5.name}, Возраст: {Student5.age}, Номер группы: {Student5.groupNumber}')


# Задача - 3
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def substraction(self):
        print(self.a - self.b)

name = Math(1, 2)
name.addition()
name.multiplication()
name.division()
name.substraction()


# Задача - 4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def off_car(self):
        print('Автомобиль заглушен')

    def thecolor(self, new_color):
        self.color = new_color

    def thetype(self, new_type):
        self.type = new_type

    def theyear(self, new_year):
        self.year = new_year
