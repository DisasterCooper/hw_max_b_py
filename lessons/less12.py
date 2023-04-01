from dataclasses import dataclass


# Magic methods

# name mangling, искажение имен

# __update - можно вызвать только через <class>__update
# если не хотим, чтобы что-то сломали -> при наследовании


# @dataclass # будет сравнивать все, что в init
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

# decorator = validate_args(int)
# is_even = decorator(is_even)  # то же самое что is_even = validate_args(int)(is_even)

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
        print(f'Время вывода функции: {t2-t1}')
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
    num2 = '0'    # int(input('Введите число: '))
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

