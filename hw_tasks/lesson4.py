numbers = [1, 2, 5, 10]
# target_number = 2
# # print(target_number in numbers)

# итерируемся по элементам списка numbers
# for num in numbers:
#     print(f'итерация цикла, мы на элементе {num}')
#
# print('закончили')

# names = ['Artem', 'Anna', 'Joe', 'Artem', 'Anna', 'Joe', 'Artem', 'Anna', 'Joe', 'Artem', 'Anna', 'Joe']
# for name in names:
#     print(name)
#
# for number in numbers:
#     print(f'comparing to {number}')
#     if target_number == number:
#         print('We found number!')
#         break
# else:
#     print(f'{target_number} is not found:(')
#
# # print(number)
#
# for number in []:
#     print(number)

numbers = [1, 2, 5, 11, 3, 4, 22, 9]
# вывести из списка элементы с нечетными индексами
# (или вывести каждый второй элемент списка)

# print(numbers[1::2])

# # итерируемся по элементам списка numbers с индексами элементов
# for i, number in enumerate(numbers):
#     # print(f'index={i}, value={number}')
#     if i % 2 == 1:
#         print(number)

# tuple_ = (2, 5)
# print(tuple_[0])
# print(tuple_[1])
#
# for value in enumerate(numbers):
#     if value[0] % 2 == 1:
#         print(value[1])


# Дан список numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# Заменить каждый второй элемент на "hello"

# list_ = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# for i, num in enumerate(list_):
#     if i % 2 == 1:
#         list_[i] = "hello"
# # print(list_)
#
# indexes = list(range(5))
# print(indexes)
#
# for i in range(5):
#     print(i)
#
# n = len(list_)
# print(n)
# # итерируемся по индексам элементов списка list_
# for i in range(n):
#     if i % 2 == 1:
#         list_[i] = "hello"
# print(list_)

# 3 способа итерации:
# - только по элементам: for num in numbers:
# - только по индексам: for index in range(len(numbers)):
# - и по индексам и по элементам: for index, number in enumerate(numbers):

# ключевые слова:
# for, break, continue, else, while

# функции:
# range, enumerate

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
#
# for i, number in enumerate(numbers):
#     if number == 4:
#         break
#     # if i == 3:
#     #     continue
#     print(number)
# print(numbers)

# numbers = [5, 1, 2]  # len(numbers) = 3
# index = 0
# while index < len(numbers):  # проверяем условие, если True - выполняем код внутри цикла
#     print(numbers[index])  # выводим элемент списка по индексу index
#     index += 1  # увеличиваем индекс на 1
# print('finished')
# print(index)

# while True:
#     num1 = int(input('Число 1: '))
#     num2 = int(input('Число 2: '))
#     if num1 == 0 and num2 == 0:
#         print('Заканчиваем')
#         break
#     print(f'Сумма равна {num1 + num2}')

# string = "Hello world"
# for symbol in string:
#     if symbol != " ":
#         print(symbol)


# dictionary = {"dog": "собака", "cat": "кошка"}
# # print(list(dictionary))
# for key in dictionary:
#     print(key, dictionary[key])


# Пусть у нас есть массив чисел numbers = [3, 5, 2, 6, 8].
# Нужно вывести сумму первого и последнего элементов массива.
# numbers = [3, 5, 2, 6, 8]
# print(numbers[0] + numbers[-1])

# O - о-большое, верхняя оценка, в худшем случае

# O(1), за константное

# summ_ = 0
# for num in numbers:
#     summ_ += num
# print(summ_)

# O(n), линейное время выполнения

# O(1)
# O(log(n))
# O(n)
# O(n*log(n))
# O(n^2)
# O(n^3)
# O(2^n)

# numbers = [3, 5, 2, 6, 8]
# target_number = 8
#
# for num in numbers:
#     if num == target_number:
#         print('нашли!')
#         break
# else:
#     print('не нашли')
# print('закончили')

# numbers = [3, 5, 2, 6, 8]
# set_ = {2, 4, 5, 1}
# num = 3
#
# if num in numbers:  # O(n)
#     print('yes')
#
# if num in set_:  # O(1)
#     print('yes')
#
# dictionary = {'a': 1, 'b': 2}
# print('a' in dictionary)  # O(1)


# numbers1 = [1, 2, 3, 4, 5]  # n = len(numbers1)
# numbers2 = [3, 5, 2, 6, 8]  # m = len(numbers2)
# for num1 in numbers1:  # на 1-ой итерации num1 = 1 (перейдем на следующую итерацию только после того, как пройдемся по всем элементам списка numbers2
#     for num2 in numbers2:  # 3 -> 5 -> 2 -> 6 -> 8
#         print(num1 + num2)
# # O(n*m)

