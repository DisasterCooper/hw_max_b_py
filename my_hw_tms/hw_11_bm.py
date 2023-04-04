"""Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
 Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
хранить операцию (снятие или пополнение), сумму, дату и время операции.
Создать экземпляр банковского аккаунта и проверить его работу."""
from datetime import datetime
from enum import Enum

print('hw_11_task1')


class OperationEnum(Enum):
    PLUS = 'incoming'
    MINUS = 'withdrawal'


class NotMoneyError(Exception):
    pass


class HistoryOpp:
    def __init__(
            self,
            operation_enum: OperationEnum,
            amount: float,
            date_time: datetime,
    ) -> None:
        self.operation_enum = operation_enum
        self.amount = amount
        self.date_time = date_time

    def __repr__(self):
        return f'{self.operation_enum}, {self.amount}, {self.date_time}'


class BankAcc:

    def __init__(
            self,
            bank_acc: str,
            balance: float,
    ) -> None:
        self.bank_acc = bank_acc
        self.balance = balance
        self.date_time = datetime
        self.history_opp: list[HistoryOpp] = []  # как передать историю, не могу понять

    @property
    def check_balance(self):
        return f'Balance {self.bank_acc} = {self.balance}'

    def __repr__(self):
        return f'{self.bank_acc},balance {self.balance}'

    def income(self, amount: float):
        self.balance += amount
        self.history_opp.append(HistoryOpp(OperationEnum.PLUS, amount, datetime.now()))

    def withdrawal(self, amount: float):
        if self.balance < amount:
            raise NotMoneyError
        self.balance -= amount
        self.history_opp.append(HistoryOpp(OperationEnum.MINUS, amount, datetime.now()))


user1 = BankAcc('A', 1000)
print(user1.check_balance)
user1.income(200)
print(user1.check_balance)
user1.withdrawal(1000)
print(user1.check_balance)
try:
    user1.withdrawal(1000)
except NotMoneyError:
    print('недостаточно средств')
finally:
    print(user1.check_balance)
