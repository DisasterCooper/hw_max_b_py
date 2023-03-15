import datetime
from functools import wraps
from typing import Callable

print('hw_7_task_1')


def console_input(func: Callable) -> Callable:
    print('Выводим в консоль имя функции, время вызова и  параметры')

    @wraps(func)
    def inner(*args, **kwargs):
        time = datetime.datetime.now()
        result = func(*args, **kwargs)
        console_mess = f'Функция {func.__name__} вызвана в {time}'
        inf_func = []
        if args:
            inf_func.append(f' c позиционными параметрами {args}')
        if kwargs:
            inf_func.append(f' c именованными параметрами {kwargs}')
        if inf_func:
            console_mess += '' + ' и' .join(inf_func)
        else:
            console_mess += ' без параметров'
        print(console_mess)
        return result
    return inner


@console_input
def add(a=1, b=2):
    return a + b


add(1, 2)
add(a=1, b=2)
add(1, b=2)
add()
