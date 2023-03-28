from dataclasses import dataclass


# staticmethod
@dataclass
class User:
    name: str
    age: int

    @staticmethod
    def say_hi() -> None:
        print("Hello world")


user = User('Joe', 30)
user.say_hi()
User.say_hi()


# property
@dataclass
class Contact:
    name: str
    code: int
    phone: int

    @property
    def full_phone_number(self):
        return f"+{self.code}{self.phone}"


contact = Contact('Egor', 375, 111111)
print(contact.full_phone_number)


@dataclass
class BankAccount:
    balance_usd: int

    @property  # свойство, дает возможность только прочитать
    def balance_euro(self):
        return 1.2 * self.balance_usd

    @balance_euro.setter  # дает возможность записать
    def balance_euro(self, value_euro):
        self.balance_usd = value_euro / 1.2

    @property
    def balance_blr(self):
        return self.balance_usd * 2.7


account = BankAccount(100)
print(account.balance_usd)
print(account.balance_euro)
account.balance_euro = 100
print(account.balance_usd)
print(account.balance_blr)


@dataclass
class Priority:
    value: str


low = Priority('low')


from enum import Enum, IntEnum
import csv

class PriorityEnum(Enum):  # можно использовать и IntEnum
    LOW = 'low'
    HIGH = 'high'
    MEDIUM = 'medium'


priority = PriorityEnum.HIGH
priority2 = PriorityEnum.LOW
print(PriorityEnum.LOW == priority2)


# Реализовать To Do список используя классы.
# В задаче хранить описание и приоритет (high, medium, low, по умолчанию low).
# Методы класса ToDoList:
# - добавить задачу
# - изменить описание задачи
# - изменить приоритет задачи
# - удалить задачу
# - вернуть список задач, отсортированный по приоритету (сначала высокий)
# - сохранить список в файл/загрузить из файла


class PriorityEnum(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Task:
    def __init__(self, name_task: str, task: str, priority_task: PriorityEnum):
        self.name_task = name_task
        self.task = task
        self.priority = priority_task

    def __repr__(self):
        return f'{self.name_task}, {self.task}, {self.priority}'


class TodoList:
    def __init__(self):
        self.to_do_list: list[Task] = []

    def add_list(self, task: Task):
        self.to_do_list.append(task)

    def edit_task(self, task: Task, new_task: str):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].task = new_task

    def edit_priority(self, task: Task, new_priority: PriorityEnum):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].priority = new_priority

    def del_task(self, task: Task):
        if task in self.to_do_list:
            self.to_do_list.remove(task)

    def get_list(self) -> list[Task]:
        return sorted(self.to_do_list, key=lambda task: task.priority, reverse=True)

    def save_file(self):
        file_name = 'task.csv'
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name_task', 'task', 'priority'])
            result = [[element.name_task, element.task, element.priority] for element in self.to_do_list]
            writer.writerow(result)


task = Task('first', 'first task', PriorityEnum.LOW)
task2 = Task('first2', 'first task', PriorityEnum.MEDIUM)
task3 = Task('first3', 'first task', PriorityEnum.HIGH)
task4 = Task('first4', 'first task', PriorityEnum.LOW)

to_do_list = TodoList()
to_do_list.get_list()
to_do_list.add_list(task)
to_do_list.add_list(task2)
to_do_list.add_list(task3)
to_do_list.add_list(task4)

print(to_do_list.get_list())
print(to_do_list.to_do_list)

to_do_list.edit_task(task3, 'edit task')
print(to_do_list.get_list())

to_do_list.del_task(task2)
print(to_do_list.get_list())

to_do_list.edit_task(task, PriorityEnum.HIGH)
print(to_do_list.get_list())


to_do_list.save_file()


