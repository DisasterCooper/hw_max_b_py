import datetime
from functools import wraps
from typing import Any, Callable

# # сигнатура функции - то что функция принимает, набор параметров


def validate_one_int_arg(func: Callable) -> Callable:
    print('Выполняем код функции validate_one_int_arg')
    @wraps(func)
    def inner(number: int) -> Any:  # заменяет декорируемую функцию (в нашем случае это is_even)
        if type(number) != int:
            print('Ошибка! Введенные данные не являются числом')
            return
        return func(number)
    return inner  # inner - это объект типа функция


@validate_one_int_arg(int)
def is_even(number: int) -> bool | None:
    return number % 2 == 0


# is_even_with_validation = validate_one_int_arg(is_even)


@validate_one_int_arg
def print_numbers(n: int) -> None:
    for num in range(1, n):
        if num % 7 == 0 and num % 4 == 0:
            return
        elif is_even(num):
            print(num ** 2)
        else:
            print(num)


# @validate_one_int_arg
# is_even = validate_one_int_arg(is_even)
print(type(is_even))

# print(is_even(2))
print(is_even(3))
print(is_even('12'))
print_numbers(5)
print_numbers('5')


# return
# return None    -> во всех 3-ех случаях вернется None


def print_func_call_time(func: Callable) -> Callable:
    print('Этот принт выполнится столько раз, сколько мы напишем @print_func_call_time')
    return func


@print_func_call_time  # код из print_func_call_time выполнится один раз, вот в этот момент, смысла такой декоратор особо не несет
def print_numbers():
    for num in range(10):
        print(num, end=' ')
    print()


# print_numbers()
# print_numbers()
# print_numbers()


def cache(func: Callable) -> Callable:
    print('Создаем пустой словарь...', end=' ')
    cached_data = {}  # вложенная для inner (или enclosing область видимости)
    print('Создали')
    @wraps(func)
    def inner(*args, **kwargs):
        # cached_data = {}  # локальная переменная, после выполнения функции уничтожается, и при каждом новом вызове создается новая
        # {(2, 3): 5, (3, 3): 6, ...}
        print(f'{cached_data=}')
        if args in cached_data:
           return cached_data[args]
        result = func(*args, **kwargs)
        cached_data[args] = result
        return result
    return inner


@cache
def add(a: int, b: int) -> int:
    print('Выполняем тело функции add')
    return a + b


@cache
def print_nums(n: int) -> None:
    print('Делаем что-то сложное, делаем долго..')
    return n
import datetime

print(add(2, b=3))  # здесь выполняем тело функции add
print(add(3, 3))  # здесь выполняем тело функции add
print(add(2, 3))  # здесь берем значение готовое из словаря

print_nums(1)
print_nums(1)
print_nums(1)


cached_data = {}
nums = [1, 2]  # unhashable
cached_data[nums] = 'список'
print(cached_data)

print(hash(1))
print(hash(2))
print(hash('s'))
print(hash([1, 2]))

s = set()
s.add(nums)


#############################################################################
############### Новая тема: Кодировки и файлы ###############################

# s = 'a'
# symbol_code = ord(s)
# print(symbol_code)
# print(chr(symbol_code))
# print(chr(12787))

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
with open('hello.txt') as file:
    file_text = file.read(5)
    print(file_text)

print('вышли из контекстного менеджера')
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
add()
