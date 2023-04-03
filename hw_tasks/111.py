import random
from datetime import datetime

print('hw_12_task_1')
"""Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
 имя функции, время вызова, и с какими параметрами она вызвана"""


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        curr_time = datetime.now()
        general_in_str = ''
        if args:
            general_in_str += f' позиционными параметрами {self.func(*args)};'
        if kwargs:
            general_in_str += f' именованными параметрами {self.func(**kwargs)};'
        elif args and kwargs:  # пока не придумал для args и kwargs более корректный способ
            general_in_str += f'  позиционными параметрами {self.func(*args)}, и с именованными параметрами {self.func(**kwargs)};'
        print(f'Функция {self.func.__name__} вызвана в {curr_time} c {general_in_str}')
        return self.func(*args, **kwargs)


@Timer
def check_args(*args):
    return args


@Timer
def check_kwargs(**kwargs):
    return kwargs


@Timer
def check_mix(*args, **kwargs):
    return args, kwargs


check_args(1, 2)
check_kwargs(a=3, b=4)
check_mix(10, b=15)

print('hw_12_task_2')
"""Камень ножницы бумага с ботом - обработка исключений"""

rock = 1
scissors = 2
paper = 3

while True:
    # try:
    #     user = int(input(f'Выберите: 1 - rock or 2 - scissors or 3 - paper: '))
    #     if user not in [1, 2, 3]:
    #         raise ValueError('Ошибка! Введите число от 1 до 3')
    #     else:
    #         print(f'Вы выбрали {user}')
    # finally:
    #     print('Попробуем снова?')

    try:
        user = int(input(f'Выберите: 1 - rock or 2 - scissors or 3 - paper: '))
        print(f'Вы выбрали {user}')
    except ValueError:
        print('Ошибка! Введите число от 1 до 3')
    finally:
        print('Попробуем снова?')

    bot = random.randint(1, 3)
    print(f'Бот выбрал {bot}')

    if bot == 1 and user == 2:
        print('bot выбрал rock, вы проиграли.')
    elif bot == 1 and user == 3:
        print('bot выбрал rock, вы выиграли.')
    elif bot == 2 and user == 1:
        print('bot выбрал scissors, вы выиграли.')
    elif bot == 2 and user == 3:
        print('User2 выбрал scissors, вы проиграли.')
    elif bot == 3 and user == 1:
        print('bot выбрал paper, вы проиграли.')
    elif bot == 3 and user == 2:
        print('bot выбрал paper, вы выиграли.')
    elif bot == user:
        print('Ничья.')
