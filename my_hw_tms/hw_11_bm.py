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
            # date_time: datetime,
            history_opp: list[HistoryOpp]
    ) -> None:
        self.bank_acc = bank_acc
        self.balance = balance
        # self.date_time = datetime
        self.history_opp = list[HistoryOpp] = []  # как передать историю, не могу понять

    @property
    def check_balance(self):
        return f'Balance {self.bank_acc} = {self.balance}'

    def __repr__(self):
        return f'{self.bank_acc}, {OperationEnum}, {datetime},balance {self.balance}'

    def create_bank_acc(self, bank_acc: str, balance: float):
        self.bank_acc.append(bank_acc)
        self.balance = balance
        if bank_acc in self.bank_acc:
            return f'{self.bank_acc} is already exists'

    def income(self, amount: float):
        self.balance += amount
        date_time = datetime.now()
        print(f'{date_time}')
        self.history_opp.append(OperationEnum.PLUS, amount, date_time)
        # print(f'{self.bank_acc}, {OperationEnum}, {datetime},balance {self.balance}')

    def withdrawal(self, amount: float):
        if self.balance < amount:
            print('недостаточно средств')
            return
        self.balance -= amount
        date_time = datetime.now()
        print(f'{date_time}')
        self.history_opp.append(OperationEnum.MINUS, amount, datetime)
        # print(f'{self.bank_acc}, {OperationEnum}, {datetime},balance {self.balance}')


user1 = BankAcc('A', 1000)
print(user1)
# print(user1.check_balance)
# user1.income(200)
# print(user1.check_balance)


