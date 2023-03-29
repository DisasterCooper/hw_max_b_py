# dataclasses
from datetime import date
from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    phone: str


c = Contact('Ivan', '236236')
print(f"{c.name=}, {c.phone=}")
print(c)
print([c])

# classmethod
# применение - альтернативные инициализаторы
@dataclass
class User:
    name: str
    age: int

    @classmethod
    def from_year(cls, name: str, year_of_birth: int) -> "User":
        current_year = date.today().year
        age = current_year - year_of_birth
        return cls(name, age)


user = User('Joe', 30)
print(user)
user2 = User.from_year('Ann', 1990)
print(user2)
user3 = user.from_year('Jack', 1980)
print(user3)


# staticmethod
@dataclass
class User:
    name: str
    _age: int

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0
        self._age = value

    @staticmethod
    def say_hi() -> None:
        print("Hello world")


user = User('Joe', 30)
user.say_hi()
User.say_hi()


# property, свойство
@dataclass
class Contact:
    name: str
    code: int
    phone: int

    @property
    def full_phone_number(self):
        return f"+{self.code}{self.phone}"


contact = Contact('Egor', 375, 1111111)
print(contact.full_phone_number)


class BankAccount:
    def __init__(self):
        self._balance_usd = 0

    @property
    def balance_euro(self):
        return 1.2 * self._balance_usd

    @balance_euro.setter
    def balance_euro(self, value_euro):
        self._balance_usd = value_euro / 1.2

    @property
    def balance_blr(self):
        return self._balance_usd * 2.7

    @balance_blr.setter
    def balance_blr(self, value_blr):
        self._balance_usd = value_blr / 2.7


account = BankAccount()
# print(account.balance_usd)
print(account.balance_euro)
account.balance_euro = 100
print(account.balance_euro)
print(account.balance_blr)
account.balance_blr = 200
print(account.balance_euro)
print(account.balance_blr)


priority = "low"  # "high"/"medium"
@dataclass
class Priority:
    value: str


low = Priority("low")
foo = Priority("cat")

from enum import Enum, IntEnum


class PriorityEnum(IntEnum):
    HIGH = 0
    AVERAGE = 1
    LOW = 2


priority = PriorityEnum.HIGH
priority2 = PriorityEnum.AVERAGE
print(PriorityEnum.LOW == priority2)


print(PriorityEnum.(PriorityEnum.HIGH))

# решаем задачу
# Реализовать To Do список используя классы.
# В задаче хранить описание и приоритет (high, medium, low, по умолчанию low).
# Методы класса ToDoList:
# - добавить задачу
# - изменить описание задачи
# - изменить приоритет задачи
# - удалить задачу
# - вернуть список задач, отсортированный по приоритету (сначала высокий)
# - сохранить список в файл/загрузить из файла


# name mangling: __name (at least two leading underscores, at most one trailing underscore)
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# о каких magic methods важно знать
# __init__
# __str__
# __repr__
# __eq__, __ne__, __lt__(), __le__(), __gt__(), __ge__() - @total_ordering
# __hash__
# __call__


# hw



