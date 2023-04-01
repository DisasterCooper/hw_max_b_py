from dataclasses import dataclass


# Magic methods

# name mangling, искажение имен:  __name (at least two leading underscores,
# # # at most one trailing underscore)


# __update - можно вызвать только через <class>__update
# если не хотим, чтобы что-то сломали -> при наследовании

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


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
# # в качестве элементов в хешируемых коллекциях (словарь и множество).
# Если класс определяет изменяемые объекты и реализует метод __eq__(),
# он не должен реализовывать __hash__(), так как реализация хешируемых коллекций требует,
# чтобы хеш-значение ключа было неизменным.
# # Пользовательские классы по умолчанию имеют методы __eq__() и __hash__();
# # с ними все объекты сравниваются как неравные (кроме самих себя),
# # и x.__hash__() возвращает соответствующее значение, такое что x == y подразумевает,
# # что x равно y и hash(x) == hash(y).


@dataclass  # будет сравнивать все, что в init
class User:
    # name: str
    def __init__(self, name):
        self.name = name


user = User('Joe')
user2 = User('Joe')
user3 = user
print(id(user))
print(id(user2))
print(user == user2)  # если dataclass - магический метод сделает True
print(user == user3)


# __eq__ (==), __ne__(!=), ... - @functools.total_ordering


# __slots__  # не дает добавить классу никакие другие атрибуты
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 1)
print(p1.x, p1.y)


# p1.z = 5  # выдаст ошибку


# __call__
class Magic:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f' we called our magic object {self.name}')


magic = Magic('some name')
magic()  # метод call дает вызвать такой экземпляр (+ позволяет вызвать объект класса)
print(callable(magic))  # проверяет метод на "магичность =)"

# декоратор класса
from functools import wraps
from typing import Any, Callable


def validate_one_int_arg(func: Callable) -> Callable:
    @wraps(func)
    def inner(number: int) -> Any:  # заменяет декорируемую функцию (в нашем случае это is_even)
        if type(number) != int:
            print('Ошибка! Введенные данные не являются числом')
            return
        return func(number)
    return inner  # inner - это объект типа функция


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
# is_even = decorator(is_even)  # то же самое что is_even = validate_args(int)(is_even)

result = is_even(10)
print(result)
result2 = is_even('10')
do_smth(2.2)
do_smth('2.2')


print('________Task________')
import time


def foo():
    print('Hello world')


class process_time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.func(*args, **kwargs)
        t2 = time.time()
        print(f'Время вывода функции: {t2 - t1}')
        return result


@process_time
def foo():
    time.sleep(1)
    print('Hello world')


foo = process_time(foo)  # это так выглядит декоратор
foo()

# Metaclasses - classes for classes
print(type(1))
# type - конструктор классов для классов
AdminUser = type('User', (), {'role': 'admin'})
print(AdminUser)
print(type(AdminUser))
admin = AdminUser()
print(admin.role)
admin.role = 'another'
print(admin.role)
print(AdminUser.role)
print(AdminUser.__class__)


class SingletonMeta(type):  # type - для наследования к метаклассу
    _instances = {}  # ключ - это объект-класс (SingletonClass), а значение - объект этого класса

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)  # здесь в super можно ничего не передавать
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass


my_singleclass = SingletonClass()
my_singleclass2 = SingletonClass()
print(id(my_singleclass))
print(id(my_singleclass2))

####### exception #######
num1 = 1
num2 = 0
try:
    print(num1 / num2)
    print('деление окончено')
except ZeroDivisionError:
    print('На ноль делить нельзя')

# ValueError
# TypeError
# NameError

num1 = 1
try:
    num2 = '0'  # int(input('Введите число: '))
    print(num1 / num2)
    print('деление окончено')
except ZeroDivisionError:
    print('На ноль делить нельзя')
except (ValueError, TypeError):
    print('Вы ввели не число')
finally:
    print('Выполняется в любом случае')

# ValueError
# TypeError
# NameError
