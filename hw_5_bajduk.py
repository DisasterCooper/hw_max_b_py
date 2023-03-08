print('task_1')  # def проверки, является ли целое число четным


def check(number: int) -> bool:
    if type(number) != int:
        print('Ошибка! Введенные данные не являются числом')
        return False
    elif number % 2 == 0:
        return True
    else:
        return False


print(check('Hello'))
print(check(2))
print(check(3))
