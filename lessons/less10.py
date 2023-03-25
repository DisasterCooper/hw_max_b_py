# OOP - Object-oriented programming

# def move():
#     pass
#
#
# class WildAnimal:
#     _is_wild = True  # атрибут класса
#     is_big = True
#
#     def move(self):
#         if self._is_wild:
#             print(f'animal with color {self.color} is moving')
#
#     def __init__(self, color=None):  # магический метод
#         self.color = color  # атрибут объекта
#
#
# my_animal = WildAnimal()  # создали экземпляр класса Animal
# second_animal = WildAnimal()
# print(second_animal.color)
# print(my_animal.color)
#
# print(WildAnimal.is_big)
# print(my_animal.is_big)
# my_animal.is_big = False
# print(WildAnimal.is_big)
# print(my_animal.is_big)


# my_animal.move()
# Animal.move(my_animal)
#
# white_animal = W


# class HomeAnimal:
#     is_wild = False
#############################################
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print()


class Dog(Animal):
    def make_sound(self):
        print('bark')


dog = Dog()
dog.make_sound()

#  экземляр его нельзя создать, тк он абстрактный (неконкретный)
############################
# Task_1


class Auto:

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birth(self):
        self.age += 1

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight


auto = Auto('Toyota', 10, 'Corolla', 'red', 1750)
print(auto.age)
auto.birth()
print(auto.age)
auto.move()
auto.stop()
print(auto.brand)


######################
# Hw_2 - со слайда
