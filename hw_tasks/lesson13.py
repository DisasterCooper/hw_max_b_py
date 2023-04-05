# Pull Requests:
# - В одном PR одно дз
# - В имени PR должен быть номер дз
# - Если вам нужно что-то добавить на гит хаб, не относящееся к дз,
#   все равно создаете новую ветку и новый PR, только уже не нужно меня в reviewers
#   добавлять, мержите сами
# - В main/master не коммитить и не пушить напрямую!
# - Когда я оставляю в комментариях просьбу что-то поправить, вы делаете коммиты в эту же ветку
#   и пушите эту же ветку на гитхаб. НЕ ЗАКРЫВАЙТЕ ПУЛ РЕКВЕСТЫ, иначе и вы и я теряете историю того,
#   что было изначально и что я просила исправить


test_cases = [
    '1', '-1', '0.1', '-0.1', '.1', '-.1', '0',
    'a', '', '1a', '--1', '1-', '1..1', '0.1a', '12 12', '-a12', '..1', '-...'
]


def analyze_str(num_str: str) -> int | float | None:
    try:
        number = float(num_str)
    except ValueError:
        print(f'некорректное число {num_str}')
        return
    num_info = []
    if number > 0:
        num_info.append("положительное")
    else:
        num_info.append("отрицательное")
    if number == int(number):
        number = int(number)
        num_info.append("целое")
    else:
        num_info.append("дробное")

    print(f'{num_info[0]} {num_info[1]} {num_str}')
    return number


# print([analyze_str(num_str) for num_str in test_cases])


# Итераторы и итерируемые объекты

# Итератор - объект, который реализует метод __next__, который возвращает следующий элемент
# или выбрасывает исключение StopIteration. В Python итераторы также реализуют __iter__
# (возвращает self), поэтому они также iterable.

# Iterable (итерируемый объект) - объект, при передаче которого встроенной функции
# iter() возвращается итератор.

# iter(...) и next(...)

# Как работает iter:
# - если есть __iter__, вызывает его
# - если нет __iter__, но есть __getitem__, то питон создает итератор, который пытается
#   извлекать элементы по-прядку, начиная с индекса 0
# - иначе возбуждается исключение


# nums = [1, 2, 3]  # в nums лежит iterable
# nums_iterator = iter(nums)  # __iter__, в nums_iterator лежит итератор
# item1 = next(nums_iterator)  # __next__
# print(item1)
# item2 = next(nums_iterator)
# print(item2)
# item3 = next(nums_iterator)
# print(item3)
# try:
#     item4 = next(nums_iterator)
# except StopIteration:
#     print('элементы закончились')
# else:
#     print(item4)


class Iterable:
    def __init__(self, num: int):
        self._nums = [num] * 10

    def __getitem__(self, index: int):
        return self._nums[index]


# iterable_object = Iterable(1)
# my_iterator = iter(iterable_object)
# item1 = next(my_iterator)
# print(item1)
# for item in my_iterator:  # в цикле for мы можем пользоваться iterable объектами
#     print(item, end=' ')
# print()
# for item in my_iterator:
#     print(item, end=' ')
# item2 = next(my_iterator)


# MyInt из 10 урока
class MyInt(int):
    def __len__(self):
        return len(str(self))

    def __getitem__(self, index):  # list_[1]
        # if index >= len(self):
        #     print('error')
        #     return
        return str(self)[index]


# num = MyInt(123)
# # num[10]
# for digit in num:
#     print(digit)


class EndlessIterator:  # одновременно и iterable (есть метод __iter__) и итератор (потому что есть __next__)
    def __init__(self, start_num: int, end_num: int = None):
        self.current_num = start_num
        self.end_num = end_num

    def __next__(self):
        if self.end_num is not None and self.current_num >= self.end_num:
            raise StopIteration
        result = self.current_num
        self.current_num += 1
        return result

    def __iter__(self):
        return self


# endless_iterator = EndlessIterator(5, 20)
# for num in endless_iterator:
#     print(num)
#     # if num == 25:
#     #     break
#
#
# endless_iterator = iter(EndlessIterator(5, 20))
# while True:
#     try:
#         num = next(endless_iterator)
#     except StopIteration:
#         break
#     print(num)


# Генераторы
def endless_generator(num: int, end_num: int = None):
    while True:
        if end_num is not None and num >= end_num:
            break
        yield num
        num += 1


endless_iterator = endless_generator(5)
print(next(endless_iterator))
print(next(endless_iterator))
print(next(endless_iterator))

# import random
#
# n = 10
# my_list = [random.randint(1, 5) for _ in range(n)]
# for num in my_list:
#     print(num)
#
# print('end')
#
# for num in (random.randint(1, 5) for _ in range(n)):
#     print(num)

for num in endless_iterator:
    print(num)
    if num == 25:
        break


endless_iterator = endless_generator(5, 7)
print(next(endless_iterator))
print(next(endless_iterator))
try:
    print(next(endless_iterator))
except StopIteration:
    print("end")



# 2. Реализовать генератор, который работает как enumerate

# reverse, zip, range

# Контекстный менеджер
# timeit(label="")

# Регулярные выражения
# задача с числами

