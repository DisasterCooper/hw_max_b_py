# str_ = "abc"
# for s in str_:
#     print(s)
#
# string = "abc"  # False
# # string = "abcba"  # True
#
# left_index = 0
# right_index = len(string) - 1
# while left_index != right_index:
#     if string[left_index] != string[right_index]:
#         print(False)
#         break
#     left_index += 1
#     right_index -= 1
# else:
#     print(True)


# def add(a, b):
#     return a + b


# print(add(2, 3))
# print(add(a=2, b=3))  # смысла для функции add с позиционными параметрами особо нет
# print(add(b=2, a=3))
# print(add(2, a=3))

# print(add())
# print(add(1))


# def add(a=0, b=0):
#     return a + b
#
#
# print(add())
# print(add(2))
# print(add(2, 3))
# print(add(a=2, b=3))
# print(c=2, d=4)
#
#
# def greet(name=None):  # name - опциональный аргумент
#     if name is None:
#         name = "stranger"
#     print('Greetings,', name)
#
#
# greet()
# greet('Joe')


# def get_list_with_1(a=[]):
#     a.append(1)  # добавляем в список число 1
#     return a


# print(get_list_with_1([3, 2]))
# print(get_list_with_1())
# print(get_list_with_1())
# print(get_list_with_1())


# def get_list_with_1(a=None):
#     if a is None:
#         a = []
#     a.append(1)  # добавляем в список число 1
#     return a
#
#
# print(get_list_with_1([3, 2]))
# print(get_list_with_1())
# print(get_list_with_1())
# print(get_list_with_1())


# def get_average(*args):
#     print(args)
#     print(type(args))
#     return sum(args) / len(args)


# print(get_average(2, 3))
# print(get_average(2, 3, 4))
# list_ = [2, 3, 4]
# d = {10: 'a', 'a': 10}
# print(list(d))
# print(get_average(*list_))

# def get_average(num1, *args):
#     return (sum(args) + num1) / (len(args) + 1)

#
# print(get_average(1))
# print(get_average(2, 3, 4))


# def print_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key in kwargs:
#         print(f'{key} is {kwargs[key]}')
#
#
# print_items(name='Joe', surname='Wood', age=30)
# print_items()
# # print_items(10)
# d = {
#     'name': 'Joe',
#     'age': 30,
# }
# print_items(**d)


# def foo(*args, **kwargs):
#     pass


# def add(a: str, b: int) -> int:
#     return a + b
#
#
# print(add(2, 3))
# result = add('a', 'b')


from typing import List, Dict, Optional, Set


# def get_sum(numbers: List[int], d: Optional[Dict[str, str]], s: Set[str]) -> int:
#     print(f'dict is {d}')
#     print(f'set is {s}')
#     return sum(numbers)
#
# def get_sum(numbers: list[int], d: dict[str, str] | None, s: set[str]) -> int:
#     print(f'dict is {d}')
#     print(f'set is {s}')
#     return sum(numbers)
#
#
# print(get_sum([1, 2, 3.5, 4, 5], {'a': 'aa'}, {'abc', 'd'}))
# print(get_sum([1, 2, 3.5, 4, 5], None, {'abc', 'd'}))


# def do_smth(a, *args, b=None, **kwargs):
#     print(a, type(a))
#     print(args, type(args))
#     print(b, type(b))
#     print(kwargs, type(kwargs))

# do_smth(1, 2, 3, [1, 2], 5, "abc")
# do_smth(1, 2, 3, [1, 2], b=5)
# do_smth(1, 2, 3, [1, 2], b=5, c=10, d=100)
# do_smth()
# do_smth(10)
# do_smth(2, 3, b=5)
# do_smth(2, 3, c=5)


# def do_smth(a, /):
#     print(a, type(a))
#
#
# do_smth(2)
#
#
# def do_smth(a, *, validator):
#     print(a, type(a))
#     print(validator, type(validator))
#
#
# do_smth(2, validator=3)




c = 1

#
# def add(a, b):
#     print(c)
#     return a + b + c
#
# print(add(2, 3))

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
# def add_3(a, b):
#     c += 2
#     return a + b + c


# def add_4(a, b):
#     print(c)
#     c = 10
#     return a + b + c
#
#
# print(add(2, 3))
# print(c)
# print(add_2(2, 3))
# print(c)
# print(add_3(2, 3))
# print(c)
# print(add_4(2, 3))

# LEGB
# L - local
# E - enclosed
# G - global
# B - built-in


b = 0


def add(a):
    b = 10
    def inner_add():
        c = 20
        return a + b + c

    return inner_add()


print(add(1))
