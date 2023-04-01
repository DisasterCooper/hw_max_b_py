from dataclasses import dataclass, field


# про ПР
# про классы

# # name mangling, искажение имен: __name (at least two leading underscores,
# # at most one trailing underscore)
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

#
try:
    mapping = Mapping([1, 2, 3])
except ValueError:
    pass
# print(mapping._Mapping__update([4, 5, 6]))
# print(mapping.items_list)
#
#
# class MappingSubclass(Mapping):
#
#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)
#
#
# mapping_subclass = MappingSubclass([1, 2, 3])
# print(mapping_subclass.items_list)
# print(MappingSubclass.__mro__)
#
# # о каких magic methods важно знать
# # __init__
#
# # __str__ - человекочитаемый вид, на свое усмотрение
# # __repr__ - 'MappingSubclass([1, 2, 3])', для программистов
#
# # __eq__(==), __ne__(!=), __lt__(<), __le__(<=), __gt__(>), __ge__(>=) - @functools.total_ordering
# # __hash__
# # Если класс не определяет метод __eq__(), он также не должен определять операцию __hash__();
# # если он определяет __eq__(), но не __hash__(), его экземпляры нельзя будет использовать
# # в качестве элементов в хешируемых коллекциях (словарь и множество). Если класс определяет изменяемые объекты
# # и реализует метод __eq__(), он не должен реализовывать __hash__(),
# # так как реализация хешируемых коллекций требует, чтобы хеш-значение ключа было неизменным.
# # Пользовательские классы по умолчанию имеют методы __eq__() и __hash__();
# # с ними все объекты сравниваются как неравные (кроме самих себя),
# # и x.__hash__() возвращает соответствующее значение, такое что x == y подразумевает,
# # что x равно y и hash(x) == hash(y).
#
#
@dataclass
class User:
    name: str
    nums: list = field(default_factory=[])


user = User('Joe', [1, 2, 3])
user2 = User('Joe', [1, 2, 3])
user3 = user
print(id(user))
print(id(user2))
print(user == user2)
print(user == user3)
user.email = "joe@email.com"
print(user.email)
# user()
#
#
# # __slots__
# class Point:
#     __slots__ = ['x', 'y']
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(1, 1)
# print(p1.x, p1.y)
# # p1.z = 5
#
#
# # __call__
# class Magic:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print(f'we called our magic object {self.name}')
#
#
# magic = Magic('some name')
# magic()
# print(callable(magic))
# print(callable(user))


# Декоратор с помощью класса
from functools import wraps
from typing import Any, Callable


# def validate_one_int_arg(func: Callable) -> Callable:
#     @wraps(func)
#     def inner(number: int) -> Any:  # заменяет декорируемую функцию (в нашем случае это is_even)
#         if type(number) != int:
#             print('Ошибка! Введенные данные не являются числом')
#             return
#         return func(number)
#     return inner  # inner - это объект типа функция

from typing import Any


class validate_args:
    def __init__(self, validation_type):
        self.validation_type = validation_type

    def __call__(self, func):
        def new_func(number: Any):
            if type(number) != self.validation_type:
                print('Ошибка! Введенные данные не являются числом')
                return
            return func(number)
        return new_func


def validate_args(validation_type, some_str):
    def decorator(func):
        def new_func(number: Any):  # эта функция заменит наши is_even и do_smth
            if type(number) != validation_type:
                print('Ошибка! Введенные данные не являются числом')
                return
            print(f"валидация {some_str} прошла успешно!")
            return func(number)
        return new_func
    return decorator


@validate_args(int, "is_even validation")
def is_even(number: int) -> bool | None:
    return number % 2 == 0


@validate_args(float, "do_smth validation")
def do_smth(number: float) -> None:
    print(number)


# decorator = validate_args(int)
# is_even = decorator(is_even)  # вызываем у объекта decorator (класса validate_args) магический метод __call__


result = is_even(10)
print(result)
result2 = is_even('10')
do_smth(2.2)
do_smth('2.2')


# Metaclasses - classes for classes
# print(type(1))
# print(type(Mapping))
# print(type(type(Mapping)))
# type(<class_name>, <tuple_of_parent_classes>, <dict_with_attributes>)
# class User:
#     role = 'admin'

    # def __init__(self):
    #     self.


AdminUser = type("User", (), {'role': 'admin'})
print(AdminUser)
print(type(AdminUser))
admin = AdminUser()
print(admin.role)
admin.role = 'another'
print(admin.role)
print(AdminUser.role)
print(AdminUser.__class__)


class SingletonMeta(type):
    _instances = {}  # ключ - это объект-класс (SingletonClass), а значение - объект этого класса

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass


my_singl = SingletonClass()
my_singl2 = SingletonClass()
print(id(my_singl))
print(id(my_singl2))

#################### Exceptions ######################
num1 = 1
try:
    num2 = '0'  #int(input('Введите число: '))
    print(num1 / num2)
    print('деление окончено.')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except (ValueError, TypeError):
    print('Вы ввели не число')
finally:
    print("выполняется в любом случае")

try:
    file = open('hello.txt')
    # some code
finally:
    file.close()


with open('hello.txt') as file:
    file.read()
    raise ValueError




# ValueError
# TypeError
# NameError

