import json
import time

print('hw_10_task_1')  # class auto с атрибутами


class Auto:

    def move(self):
        print('The car is moving')

    def stop(self):
        print('The car stopped')

    def birth(self):
        self.age += 1

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight


auto = Auto('Volvo', 5, 'Xc90', 'black', 2300)
auto.birth()
auto.move()
auto.stop()

print('hw_10_task_2')


class Truck(Auto):

    def move(self):
        print('Attention!')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        self.max_load = max_load
        super().__init__(brand, age, mark, color, weight)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        self.max_speed = max_speed
        super().__init__(brand, age, mark, color, weight)

    def move(self):
        super().move()
        print(f'{self.brand}{self.mark} max speed is {self.max_speed}')


truck1 = Truck('MACK', 10, 'rw', 500)
truck2 = Truck('Mercedes-Benz', 5, 'Flat Bed Trailer', 1000)
truck1.move()
truck2.move()
truck1.load()
truck2.load()
print(truck1.max_load)
print(truck2.max_load)
car1 = Car('BMW', 7, 'x5', 260)
car2 = Car('Porsche', 1, '911 Turbo S', 330)
car1.move()
car2.move()
