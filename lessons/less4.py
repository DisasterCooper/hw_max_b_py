# циклы
# numbers = [1, 2, 5, 10]
# target_number = 2
# # # print(target_number in numbers)
# #
# # # итерируемся по элементам списка numbers:
# #
# # for number in numbers:
# #     print(f'итерация цикла, мы на элементе {number}')
# #
# # print('finish')
#
# names = ['Artem', 'Anna', 'Joe']
# for name in names:
#     print(name)
#
# #
# for number in numbers:
#     print(f'comparing to {number}')
#     if target_number == number:
#        print('we found number!')
#        break
# else:
#     print(f'{target_number} is not found:(')
#
# print(number)
# for number in []:
#     print(number)
#
# numbers = [1, 2, 5, 11, 3, 4, 22, 9]
# # print(numbers)
# # print(numbers[1::2])
# # # задача - вывести из списка элементы с нечетными индексами
# # # (или вывести каждый второй элемент списка)
# #
# # # итерируемся по элементам списка numbers с индексами циклов:
# # # используем распаковку ниже:
# for i, number in enumerate(numbers):  # enumerate возвращает tuple
#         # print(f'index={i}, value={number}')
#     if i % 2 == 1:
#         print(number)
#
#
# typle_ = (2, 5)
# print(typle_[0])
# print(typle_[1])
#
# for value in enumerate(numbers):
#     if value[0] % 2 == 1:
#         print(value[1])


# Дан список numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# Заменить каждый второй элемент на 0.

# list_ = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# print(list_)
# for i, num in enumerate(list_):
#     if i %2 == 1:  # проверка на нечетность
#         list_[i] = 0
# print(list_)
# for i, num in enumerate(numbers):
#     if i %3 == 2:
#         list_[i] = 'hello'
# print(list_)
#
# # итерируемся по индексам списка numbers, вариант решения через range.
# n = len(list_)
# print(n)
# for i in range(n):
#     if i %2 == 1:  # проверка на нечетность
#         list_[i] = 'hello'
# print(list_)
#
# indexes = list(range(5))
# print(indexes)
#
# for i in range(5):
#     print(i)

# 3 способа итерации:
# - только по элементам: for num in numbers:
# - только по индексам: for index in range(len(numbers)):
# - и по индексам, и по элементам: for index, number in enumerate(numbers):

# ключевые слова:
# for, break, continue, else, while

# функции:
# range, enumerate
#
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
#
# for i, number in enumerate(numbers):
#     if number == 4:
#         continue
#     if i == 3:
#         continue
#     print(number)
# print(numbers)


# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# # - написать все элементы, кроме 4
# for i, number in enumerate(numbers):
#     if number != 4:
#         print(number)

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]  # len(numbers) = 9
# index = 0
# while index < len(numbers):  # проверяем условие, если True - выполняем код внутри цикла
#     print(numbers[index])  # выводим элемент списка по индексу index
#     index += 1  # увеличиваем индекс на 1
# print('finished')
# print(index)


# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]  # len(numbers) = 9
# index = 0
# while index < len(numbers):
#     print(f'val = {numbers[index]}')
#     index += 1
#     print(f'index = {index}')
# print('finished')

# # while True - вечный цикл
# while True:
#     num1 = int(input('number 1: '))
#     num2 = int(input('number 2: '))
#     if num1 == 0 and num2 == 0:
#         print('finish')
#         break
#     print(f'сумма равна {num1 + num2}')

# string = 'hello world'
# for symbol in string:
#     print(symbol)

# Дан список numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# Посчитать сумму элементов списка, не использую встроенную функцию sum
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# a = 0
# for number in numbers:
#     a += number
# print(a)
# print(sum(numbers))
#
# # Дан словарь:
# # Для каждого элемента словаря вывести на экран: "У друга <имя> номер телефона <номер>"
#
# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,}
# for name in friends_phone_numbers:
#     print(f'у друга {name} номер телефона {friends_phone_numbers[name]}')
#
# # Пользователь вводит число. Проверить, если пользователь ввел какие-либо символы
# # кроме цифр, вывести сообщение 'Вы ввели невалидное число", иначе вывести на экран сумму цифр числа.
# # Сделать двумя способами (с циклом и без)
#
# num_str = input('введите число: ')
# sum_ = 0
# if num_str.isdigit():
#     for symbol in num_str:
#         sum_ += int(symbol)
#     print(sum_)
# else:
#     print(f'Вы ввели невалидное число')


# dictionary = {'dog': 'собака', 'cat': 'кошка'}
# print(list(dictionary))
# for key in dictionary:
# print(key, dictionary[key])

# numbers = [3, 5, 3, 6, 8]
# print(numbers[0] + numbers[-1])
#
# # 0(1) , за константное
#
# summ_ = 0
# for num in numbers:
#     summ_ += num
# print(summ_)
# 0(n) , линейное время выполнения

#  0 - O большое, верхняя оценка, в худшем случае

# 0(1)
# 0(log(n))
# 0(n)
# 0(n*log(n))
# 0(n^2)
# 0(n^3)
# 0(2^n)

# numbers = [3, 5, 3, 6, 8]
# target_number = 3
#
# for num in numbers:
#     if num == target_number:
#         print('нашли')
#         break
# else:
#     print('не нашли')

# numbers = [3, 5, 3, 6, 8]
# set_ = {2, 4, 5, 1}
# num = 3
# if num in numbers:  # 0(n)
#     print('yes')
#
# if num in set_:  # 0(1)
#     print('yes')
#
# dictionary = {'a': 1, 'b': 2}
# print('a' in dictionary)  # 0(1)
#

# numbers1 = [1, 2, 3, 4, 5]  # n = len(numbers1)
# numbers2 = [3, 5, 2, 6, 8]  # m = len(numbers2)
# for num1 in numbers1:
#     for num2 in numbers2:  # 1 из num1 для 3 - 5 - 2 - 6 - 8, и только потом на 2 из первого цикла
#         print(num1 + num2)
# # 0(n*m)

# Пользователь вводит строку. Нужно посчитать сколько раз встречается каждый из символов строки
# string = input()  # 0(n^2)
# set_ = set(string)
# for str in set_:
#     kol = 0
#     for str1 in string:
#         if str == str1:
#             kol += 1
#     print(kol)

# string = input()
# dict_ = dict()  # в словаре храним: ключ - символ, а значение - сколько раз встретим
#
# for str in string:  # линейное
#     if str in dict_:
#         dict_[str] += 1
#     else:
#         dict_[str] = 1
# print(dict_)
