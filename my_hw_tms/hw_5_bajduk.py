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

print('task_2')


def where_numb(n: int) -> None:
    if type(n) != int:
        print('Ошибка! Введенные данные не являются числом')
    else:
        for num in range(0, n):
            if num % 7 == 0 and num % 4 == 0:
                return
            elif check(num):
                print(num ** 2)
            else:
                print(num)


where_numb(3)
