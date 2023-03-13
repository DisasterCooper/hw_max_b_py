from typing import Callable, Any
from functools import wraps
import datetime

print('hw_6_task_1a')  # Лямбда-функция, на четное/нечетное.
# Функция принимает параметр (число), если четное, то выдает
# четное, если нет - нечетное.

some_value = int(input('Введите число: '))
check_parity: Callable[[Any], str] = lambda num: 'Четное' if num % 2 == 0 else 'Нечетное'
result = check_parity(some_value)
print(result)

print('hw_6_task_1b')


def check_parity(number: int) -> str:
    return (lambda num: 'Четное' if num % 2 == 0 else 'Нечетное')(number)


print(check_parity(2))
print(check_parity(3))

print('hw_6_task_2')  # Вернуть список, где при помощи map() число -> в строку.
# В качестве функции map использовать lambda

list_ = [-1, 4, 1, 13, 144]
print(list_)
list_str = list(map(lambda a: str(a), list_))
print(list_str)

print('hw_6_task_3')  # filter -> из кортежа слов отфильтровать палиндромы

list_words = ('people', 'abba', 'kayak', 'wow', 'water', 'cat')
print(list_words)
palindromes = tuple(filter(lambda word: word == word[::-1], list_words))
print(f'palindromes: {palindromes}')

print('hw_6_task_4')  # Декоратор к двум функциям, который считает и выводит время
time = datetime.datetime.now()


def count_time_decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time
        print(f'Начало работы функции {func.__name__}: {start_time}')
        result_ = func(*args, **kwargs)
        end_time = time
        print(f'Функция {func.__name__} загружается {end_time - start_time} секунд')
        print(f'Конец работы функции: {func.__name__}: {end_time}')
        return result_
    return inner


@count_time_decorator
def min_ch(numbers: list[int]) -> int | None:
    if not numbers:
        return None
    b = numbers[0]
    for num in numbers:
        if num < b:
            b = num
    return b


print(min_ch([1, 15, -55555555, 456, 5767, 767676, 6767664, 3322]))


@count_time_decorator
def min_ch2(numbers: list[int]) -> int | None:
    if not numbers:
        return None
    b = numbers[0]
    for num in numbers:
        if num < b:
            b = num
    return b


print(min_ch2([1, 15, -34]))
