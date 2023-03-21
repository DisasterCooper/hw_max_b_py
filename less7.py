import datetime
from functools import wraps
from typing import Any, Callable

# TDD - test driven development
my_test_examples = [
    '1', '-1', '0.1', '-0.1', '.1', '-.1', '0',
    '', 'a', '1aa', '--1', '1-', '1..1', '0.1a', '22 11', '-a11', '..1',
]


def accept_str(some_str: str) -> int | float | None:
    if some_str.isdigit():  # целое
        print(f'Вы ввели положительное целое число {some_str}')
        return int(some_str)
    void_str = some_str.replace('-', '', 1).replace('.', '', 1)  # 1 - кол-во раз, сколько удалить символ
    if not void_str.isdigit() or ('-' in some_str and some_str[0] != '-'):
        print(f'Ошибка!Вы ввели некорректное число {some_str}')
        return None
    if '.' in some_str:
        num_format = 'дробное число'
        num = float(some_str)
    else:
        num_format = 'целое число'
        num = int(some_str)
    if num >= 0:
        num_sign = 'положительное'
    else:
        num_sign = 'отрицательное'
    print(f'{num_format} {num_sign} {some_str}')
    return num


# for some_str in my_test_examples:
#     print(accept_str(some_str))

print(list(map(accept_str, my_test_examples)))
#
# print([accept_str(string) for string in my_test_examples])


# Кодировка
# s = 'a'
# print(ord(s))
# print(chr(124124))

# контекстный менеджер
with open('hello.txt') as file:  # предпочитаем его, он закрывает сам file
    file_text = file.read()
    print(file_text)

print('вышли из контекстного менеджера')

########################################################
# Новая тема: Кодировки и файлы

s = 'a'
symbol_code = ord(s)
print(symbol_code)
print(chr(symbol_code))
print(chr(12787))

# /home/vika/Documents/python_lessons/hello.txt - это абсолютный путь
# hello.txt - а это относительный
# file = open('hello.txt')
# file_text = file.read()
# print(file_text)

# file_text = file.read(5) # прочитать 5 символов из файла
# print(file_text)

# for row in file:
#     print(f'прочитали строку: {row}')

# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.close()

# контекстный менеджер
# with open('hello.txt') as file:
#     file_text = file.read(5)
#     print(file_text)
#
# print('вышли из контекстного менеджера')
# file.read(5)

def log_info(func):
    def inner(*args, **kwargs):
        time = datetime.datetime.now()
        result = func(*args, **kwargs)
        log_message = f'Функция add вызвана в {time}'
        additional_info = []
        if args:
            additional_info.append(f'с позиционными параметрами {args}')
        if kwargs:
            additional_info.append(f'с именнованными параметрами {kwargs}')
        if additional_info:
            log_message += ' ' + ' и '.join(additional_info)
        else:
            log_message += ' без параметров'
        print(log_message)
        return result
    return inner


@log_info
def add(a=0, b=0):
    return a + b

add(1, 2)
add(a=1, b=2)
add(1, b=2)
add()  # у ф-ции нет аргументов, или *args, **kwargs, или у аргумента значение по умолчанию

