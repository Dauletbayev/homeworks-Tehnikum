class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f'Брэнд: {self.brand}\n'
              f'Год: {self.year}')

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f'Масса: {self.model}')

class Motorcycle(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f'Цвет: {self.color}')

car1 = Car("Chevrolet", 2022, "Malibu")
motorcycle1 = Motorcycle("Suzuki", 2021, "Black-Metalic")

print("Car Information:")
car1.display_info()

print("\nMotorcycle Information:")
motorcycle1.display_info()

