import random

""" 1. Написать бесконечный итератор, который возвращает случайное число в заданном диапазоне.
Реализовать через класс-итератор и через функцию-генератор.
Протестировать обе реализации в цикле for.

Дополнительно (если есть время) добавить параметр стоп-число: 
как только генератор выдает стоп-число, он заканчивает генерировать новые.
"""
print('hw_13_task_1a')


class RandIterator:
    def __init__(self, first_num: int, end_num: int):
        self.first_num = first_num
        self.end_num = end_num

    def __next__(self):
        return random.randint(self.first_num, self.end_num)

    def __iter__(self):
        return self


rand_iterator = RandIterator(1, 15)
for num in rand_iterator:
    print(next(rand_iterator))
    if num == 15:
        break

print('hw_13_task_1b')


def rand_generator(first_num: int, end_num: int):
    while True:
        yield random.randint(first_num, end_num)


generator = rand_generator(1, 20)
for num in range(5):
    print(next(generator))

print('hw_13_task_1c')  # тут получился генератор для выборки stop_numb количества чисел


def rand_generator2(first_num: int, end_num: int, count_numb=None):
    while count_numb is None or first_num <= count_numb:
        first_num += 1
        yield random.randrange(first_num, end_num)


for num2 in rand_generator2(1, 100, count_numb=3):
    print(num2)


print('hw_13_task_1d')  # stop_numb


def rand_generator3(first_num: int, end_num: int, stop_numb=None):
    count = 0
    while count != stop_numb:
        count = random.randint(first_num, end_num)
        yield count


for num3 in rand_generator3(1, 10, stop_numb=2):
    print(num3)
