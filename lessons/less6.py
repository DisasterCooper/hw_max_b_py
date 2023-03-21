import random
#
#
n = 10
list_ = []
for _ in range(n):
    list_.append(random.randint(-10, 10))
print(list_)

list_ = [random.randint(-10, 10) for _ in range(n)]
print(list_)

symbols = ['a', 'g', '4', 'p', 'k']
random_dict = {s: random.randint(-10, 10) for s in symbols}
print(random_dict)


# Рекурсия # внутри функции вызываем саму функцию
def foo():
    print('in foo')
    foo()


# foo()

# посмотреть последовательность Фибоначчи
# 0, 1, 1, 2, 3, 5, 8, 13 ...(n-1) + (n-2) - n-ный элемент


def get_fib(n):
    if n in {0, 1}:
        return n
    return get_fib(n - 1) + get_fib(n - 2)


print(get_fib(0))
print(get_fib(1))
print(get_fib(2))
''' пояснение задачи выше
1. get_fib(2)
    get_fib(1) + get_fib(0):
        get_fib(1):
            return 1
    1 + get_fib(0):
        get_fib(0):
            return 0
    1 + 0 = 1
    return 1
'''
# Разные строки по len, чтобы определить какую строку вызываем первой -> рекурсия
a = "abcd"
b = "abc"


def foo(a: str, b: str) -> bool:
    if len(a) < len(b):
        return foo(b, a)
    # ....

foo(b, a)
print(foo(b, a))

# Дан словарь. Создать новый и поменять местами ключ и значение
dict_ = {'a': 4, 'b': 6, 'c': 8}


def change_dict(dict_2: dict) -> dict:
    dict_2 = {}
    for key in dict_:
        print(dict_[key])
        dict_2[dict_[key]] = key
    return dict_2


print(change_dict(dict_))

new_dict = {dict_[key]: key for key in dict_}
print(new_dict)


# Факториал
# 3! = 1 * 2 * 3


def fact(number: int) -> int | None:
    if number < 0:
        return
    if number == 1 or number == 0:
        return 1
    return number * fact(number - 1)


print(fact(3))


# map, filter

list_ = [-2, 4, 1, 12, -22]
print(list_)
positive_list_ = [item for item in list_ if item > 0]
print(positive_list_)


def is_positive(num: int) -> bool:
    return num > 0


positive_list2 = list(filter(is_positive, list_))  # без lista будет filter
print(positive_list2)

# Лямбда-функции lambda functions
positive_list3 = list(filter(lambda num: num > 0, list_))  # Lambda то же самое что is_positive
print(positive_list3)

print(list(filter(lambda num: num < 0, list_)))
print(list(filter(lambda num: num % 2 == 0, list_)))
print(list(filter(lambda num: num % 2 == 0 and num > 0, list_)))

new_list = []
for num in list_:
    if num % 2 == 0 and num > 0 and num % 3 == 0:
        new_list.append(num)
print(new_list)


# import random as r  # при необходимости можно рандом "назвать"
#
# print(r.randint(-5, 5))


list_ = [-2, 4, 1, 12, -22]
print(list(map(lambda num: num ** 2, list_)))
print(list(map(lambda num: num > 0, list_)))

# num1, num2 = map(int, [input('Первое число: '), input('Первое число: ')])
# print(num1, num2)

numbers_string = input('Введите числа через пробел: ')
numbers = list(map(int, numbers_string.split()))
print(numbers)

###################################################
# Closure, замыкание  !! Любят задавать на собесах
# def add(a, b):
#     return a + b

# функция add высшего порядка (возвращает inner)
# def add(a):
#     def inner(b):
#         return a + b
#     return inner  # вернули объект, а не вызвали функцию
#
#
# add_one = add(1)
# print(add_one(2))
# print(add_one(5))
#
# add_five = add(5)
# print(add_one(2))
# print(add_one(5))

#######################################
# Декоратор (использует замыкание)

import time
from typing import Callable


def decorator(func: Callable) -> Callable:
    def inner(a, b):
        print('до вызова функции add')
        time1 = time.time()
        result = func(a, b)  # тут вызываем функцию, к-ю декорируем (у нас add)
        time2 = time.time()
        print(f'после вызова функции add = , результат = {result}, время выполнения = {time2 - time1}')
        return result
    return inner


@decorator
def add(a, b):
    return a + b


# add = decorator(add)
print(add(2, 3))
print(add.__name__)
# print(add(2, 3))

