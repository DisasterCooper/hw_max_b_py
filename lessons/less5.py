#  является ли строка палиндромом
string = 'abc'  # false
string = 'abcba'  # false

left_index = 0
right_index = len(string) - 1
while left_index != right_index:
    if string[left_index] != string[right_index]:
        print(False)
        break
    left_index += 1
    right_index -= 1
else:
    print(True)


def add(a, b):
    return a + b


print(add(2, 3))  # именованные
print(add(a=2, b=3))  # смысла для функции add с позиционными параметрами особо нет
print(add(b=2, a=3))  # позиционные
print(add(2, b=3))

print(add())  # не будет работать
print(add(1))  # не будет работать


def add(a=0, b=0):
    return a + b


print(add())
print(add(2))
print(add(2, 3))
print(add(a=2, b=3))
#########################################################
# Обязательные и опциональные аргументы функции


def ge_list_with_1(a=[]):  # любят на интервью вопрос! для изменяемых типов только
    a.append(1)  # добавляем в список число 1
    return a


print(ge_list_with_1([3, 2]))
print(ge_list_with_1())
print(ge_list_with_1())


def ge_list_with_1(a=None):  # выход - использовать None
    if a is None:
        a = []
    a.append(1)  # добавляем в список число 1
    return a


print(ge_list_with_1([3, 2]))
print(ge_list_with_1())
print(ge_list_with_1())


def get_average(a, b):  # можно через *args
    return (a + b) /2


print(get_average(2, 3))
print(get_average(2, 3, 4))


def get_average(*args):  # через *args
    print(args)
    print(type(args))
    return sum(args) / len(args)


print(get_average(2, 3))
print(get_average(2, 3, 4))
list_ = [2, 3, 4]
a, *b = list_
# d = {10: 'a'}  # для словаря следить, какие ключи (надо одинаковые)
print(a, b)
print(get_average(*list_))  # * передаем в список для распаковки


def get_average(a, *args):  # чтобы исключить о, создать перед *args еще аргумент
    print(args)
    print(type(args))
    return (a + sum(args)) / (a + len(args))


print(get_average())  # выход - создать аргумент, чтобы 0 исключить


def print_items(**kwargs):  # dictionary
    for key in kwargs:
        print(f'{key} is {kwargs[key]}')


print_items(name='Joe', surname='Wood', age=30)  # здесь именованные параметры
print_items()
d = {
    'name': 'Joe',
    'age': 30,
}
print_items(**d)


def foo(*args, **kwargs):  # можно комбинировать
    pass  # для функции, тело которой потом будет написано

# Аннотация


def add(a: int, b: int) -> int:  # типы пишем, но на функцию не влияют
    return a + b


print(add(2, 3))
result = add('a', 'b')
print(add(2, 'a'))  # ошибка, нельзя сложить число и строку

# from typing import List, Dict, Optional, Set  # так было раньше, вызов для аннотации


def get_sum(numbers: list[int]) -> int:
    return sum(numbers)


print(get_sum([1, 2, 3.5, 4, 5]))


def do_smth(a, *args, b=None, **kwargs):
    print(a, type(a))
    print(args, type(args))
    print(b, type(b))
    print(kwargs, type(kwargs))


do_smth(1, 2, 3, [1, 2], 5)  # все пойдет в args, поэтому аргумент отдельно нужно для передачи
do_smth(1, 2, 3, [1, 2], b=5)
do_smth(1, 2, 3, [1, 2], b=5, )
# do_smth()  # так не можем вызвать
do_smth(2, 3)


def do_smth(a, /):  # / - нельзя передавать этот параметр
    print(a, type(a))


do_smth(2)
do_smth(a=2)  # так нельзя


def do_smth(a, *, validator):
    print(a, type(a))
    print(validator, type(validator))


do_smth(2, validator=3)

##############################
# Области видимости функции
# с = 10  # глобальная область видимости
#
#
# def add(a, b):
#     c = 10  # это существует только в локальной области видимости
#     return a + b + с  # это существует только в локальной области видимости
#
#
# print(add(2, 3))
# # print(a)
# # print(c)
# print(add(2, 3))


# c = 1
#
# def add(a, b):
#     c = 10
#     return a + b + c
#
#
# def add_2(a, b):
#     global c
#     c = 100
#     return a + b + c
#
#
# print(add(2, 3))
# print(c)

##############
# LEGB - последовательность, в какой области ищется переменная
# L - local
# E - enclosed - вложенная область видимости
# G - global
# B - built-in

# b = 0
#
#
# def add(a):
#     b = 10
#     def inner_add():
#         c = 20
#         return a + b + c
#
#     return inner_add()
#
#
# print(add(1))


# Дан список чисел. Написать функцию,
# которая вернет сумму только положительных элементов списка
# numbers = [1, -2, 3, -4, 5]
# num2 = []
#
#
# def sum_nums(numbers2: List[int]) -> int:
#     for num in numbers2:
#         if num > 0:
#             num2.append(num)
#
#     return sum(num2)
#
#
# print(sum_nums(numbers))


# Дан список чисел. Написать функцию, которая вернет минимальное значение из списка.
# (Конкретно в этой задаче встроенную функцию min не использовать)


def min_ch(numbers: list[int]) -> int:
    if not numbers:
        return None
    b = numbers[0]
    for num in numbers:
        if num < b:
            b = num
    return b


print(min_ch([1, 15, -34]))


# Написать функцию, которая печатает числа от 0 до n, n - параметр.
# Если число делится на 3, вместо числа печатает fizz,
# если число делится на 5, вместо числа печатает buzz.
# Если число делится и на 3 и на 5, вместо числа печатает fizzbuzz


def print_numb(n: int) -> None:
    for x in range(n):
        if x % 3 and x % 5 == 0:
            print('fizzbuzz', end='')  # если end - то будет в одну строку
        elif x % 3 == 0:
            print('fizz', end='')
        elif x % 5 == 0:
            print('buzz', end='')
        else:
            print(x, end='')


print(print_numb(15))
