"""Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
 Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
хранить операцию (снятие или пополнение), сумму, дату и время операции.
Создать экземпляр банковского аккаунта и проверить его работу."""
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

print('hw_11_task1')


class OperationEnum(Enum):
    PLUS = 'пополнение'
    MINUS = 'снятие'


@dataclass
class BankAcc:
    name: str
    balance: float

    # history: list | None

    @property
    def check_balance(self):
        return f'Balance {self.name} = {self.balance}'


@dataclass
class History:
    operation: OperationEnum
    amount: float
    date_time: datetime


class Operation_with_acc:

    def income(self, amount: float):
        self.balance += amount
        self.history.append('income', datetime.now())


user1 = BankAcc('A', 1000)
print(user1.check_balance)

