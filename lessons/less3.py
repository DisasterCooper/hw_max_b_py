# num = int(input())
# print(num)
# print(type(num))
#
# print(bool(1))  # bool проверяет, не пустой ли объект
# print(bool(0.5))
# print(bool(0))
# print(bool('123'))
# print(bool(''))
# print(bool(' '))
# print(bool([]))
# print(bool([0]))
#
# print(bool({'a': 1}))
# print(bool({}))
# num1 = 1
# num2 = 2
# print(str(num1) + str(num2))
# print(str(num1 + num2))
# print(str([1, 2, 3]))

list_ = list('abc')
print(id(list_))
list_2 = list(list_)
print(id(list_2))
# удобно делать копию, с разным id, и потом работать с ним.

tuple_ = tuple('123')
d = {1: 'a', 2: 'b'}
print(d.keys())
# tuple_ = tuple(d)
list_ = list(d)
print(tuple_)
print(list_)


# Есть массив чисел numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]. Нужно поменять местами первый и последний элементы.
# (двумя способами указать последний элемент).

numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
print(numbers)
print(numbers[0], numbers[-1])
# numbers[0], numbers[-1] = numbers[-1], numbers[0]
# print(numbers)
# tmp = numbers[0]
# numbers[0] = numbers[-1]
# numbers[-1] = tmp
# print(numbers)

print(numbers[len(numbers)-1])

a, b, c, d = 'spam'
print(a, b, c, d)
spam = ham = 'lunch'
print(spam)
print(ham)


list_ = [1, 2, [1]]
list_ += [4, 5, 6]
print(list_ + list_)
list_ *= 2
print(list_)

list_3 = [1, 2, [2]]
list_4 = list_3 * 2
print(list_3)
print(list_4)
list_[2].append(5)
print(list_)

# from copy import deepcopy  # копирование объекта со всей вложенностью
list_ = [1, 2, [1]]
list_3 = list_[:]
list_4 = list(list_)
# list_2 = list_ = deepcopy(list_)
list_ += [4, 5, 6]
print(list_ + list_)
list_ *= 2
print(list_)
print('initial', list_)

list_ = [1, 2, 3]
print(sum(list_))
print(max(list_))
print(min(list_))

list_ = ['a', 'b', 'c']
print(''.join(list_))  # join существует только как метод строки
print('-'.join(list_))

list_ = [1.3, 2.7, 3]
print(list_)

# Форматирование строк

list_ = ['a', 'b', 'c']
result = ('-'.join(list_))

template = 'My joint string is {}'
print(f'My joint string is {result}')  # f-string
print(f'My joint string is {str(10) + str(10)}')
print(template.format(result))  # метод format
print(template.format('hello'))

# Операторы ветвления

# if, elif, else
num1 = int(input('num1: '))
num2 = int(input('num2: '))
# is_bigger = num1 > num2
# print(is_bigger)

if num1 > num2:
    print(f'{num1} is bigger than {num2}')
    if num1 > 0:
        print(f'num1 is bigger than 0')
elif num1 < num2:
    print(f'{num1} is smaller than {num2}')
else:
    print(f'{num1} = {num2}')

if num1 + num2 == 5:
    print(f'{num1} + {num2} = 5')

# and or
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# True or False = True
# False or True = True
# False or False = False

num1 = int(input('num1: '))
num2 = int(input('num2: '))
if num1 > num2 or num1 < 0 or num2 > 0:  # False or False or True = True (3 and 3)
    print(f'{num1} is bigger than {num2}')
elif num1 < num2:
    print(f'{num1} is smaller than {num2}')
else:
    print(f'{num1} = {num2}')

if num1 + num2 == 5:
    print(f'{num1} + {num2} = 5')

num = 10
result_str = str(num) if num else 'empty'  # тернарный оператор
# это упрощенное чем ниже
# if num:
#     result_str = str(num)
# else
#     result_str = 'empty'

print(result_str)
print(type(result_str))

list_ = [5]
result_str = str(list_) if list_ else 'empty'
print(result_str)
print(type(result_str))

# 2 (на if else)
# Напишите программу, которая запрашивает у пользователя два числа (x и y) и выводит на экран результат их сравнения.
#
# Если x больше y, то программа должна вывести сообщение "x больше y".
# Если x меньше y, то программа должна вывести сообщение "x меньше y".
# Если x равно y, то программа должна вывести сообщение "x равно y".
# Однако, если x и y кратны 2, то программа должна вывести дополнительное сообщение "Оба числа кратны 2".
x = int(input('Введите число x:'))
y = int(input('Введите число  y:'))
if x % 2 == 0 and y % 2 == 0:
    print('Оба числа кратны 2')
elif x % 2 != 0 and y % 2 != 0:
    print('оба числа не кратны 2')
if x > y:
    print(f'x больше y')
elif x < y:
    print(f'x меньше y')
elif x == y:
    print(f'x равно y')
