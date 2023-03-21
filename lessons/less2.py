# для работы с float импорт файлов
# from decimal import Decimal  # когда нужно строгое равенство
# a = Decimal('0.1')
# b = Decimal('0.2')
# c = Decimal('0.3')
# print(a + b == c)
# print(Decimal(2.76))
#
# a = 1000
# b = 1001
# print(id(a))
# print(id(b))
# # # is - сравнивает результаты id
# print(a is b)
# # # - 5, 255 - py сразу создает объекты в памяти
# #
# string = "a"
# print(str)
# string += "b" #то же самое, что string = string + "b"
#
# # None - если не знаем, что за переменная -- тип для пустоты
# some_variable = "none"
# print(some_variable is None)

# # COLLECTION
# списки, list (еще один изменяемый вид, можно хранить что угодно)
#  но можно изменить через срез
# numbers = [1, 2, 3, -10, 100]
# everything = ["a", 1, ]
# # # numbers.append()  # добавить элемент в список
# print(numbers)
# print((type(numbers)))
# print(everything[:2])

# everything = ["a", 1, ]
# print(everything)
# everything.append("hello")
# nums = [2, 3, 4]
# print(nums)
# everything.extend(nums)  # делает из списка "плоский" список
# print(everything)
# print(len(everything))
# everything.remove(1)
# print(everything)
# everything.insert(1, "hello")  # добавить элемент в список
# print(everything)
# del everything[1]
# print(everything)
# first_item = everything.pop(0)
# print(everything)

# matrix = [[1, 2], [3, 4]]
# print(matrix)


# string = "hello world, i write code"
# print(string)
# words = string.split()
# print(words)
#
# # variable_name = "some_many_words_name"
# # not_working = variable_name.split()  #вернется не строка, а список
# # print(not_working)
# # words = variable_name.split("_")
# # print(words)
# #
# # # склеить в одну строку
# str_ = ""
# print(len(str_))
# #
# result = " "
# print(result)
# result = ", ".join("words")
# print(result)
#
# string = "    hello   "
# print(string)
# cleaned_name = string.strip()  # почистить пробелы, rstrip, lstrip
# print(cleaned_name)

# numbers = (1, 2, 10)   # кортеж tuple
# print(numbers)
# print(type(numbers))
# print(id(numbers))
# a, b = 2, 3     # 2, 3 - кортеж. тут происходит распаковка
# print(a)
# print(b)
#
# a, b, *c = 1, 2, 3, 5, 555
# print(a)
# print(b)
# print(c)
# print('------------')
# a, b, *c = (1, 2, 3, 5, 555, "hello")
# print(a)
# print(b)
# print(c)

# a = (1,)  # кортеж для 1 элемента
# b = (1)
# print(a)
# print(type(a))
# print(b)
# print(type(b))

# names = {'name1', 1, None, False, False}  # сет, множество
# print(names)
# print(type(names))
# #
# names.add("name2")
# print(names)
# print(len(names))
#
# names.remove(None)
# print(names)
# # print(names[0]) # так нельзя

list_ = [1, 2, 3]
tuple_ = (1, 2, 3)
set_ = {1, 2, 3}
print(1 in list_)
print(1 in list_)
print(10 in list_)

print(1 in tuple_)
print(10 in tuple_)

print(1 in set_)
print(10 in set_)


# Чем отличается список от множества:
# 1. В множестве все элементы уникальны, в списке могут повторяться
# 2. В множестве порядок НЕ сохраняется, в списке сохраняется
# 3. Нельзя обращаться по индексу
# 4. Методы по добавлению: для списка append, для множества add
# 5. Проверка выхождения элемента в множества (например, 10 in set_) работает быстрее чем для списка

dictionary = {'name': 1}
# 'name' - key
# 1 - value
print(dictionary.get)
dictionary = {'key': 'ключ', 'number': 'число', 'cat': 'кот', 'dog': 'собака'}
print(dictionary['cat'])
print(dictionary.keys())
print(dictionary.values())

dictionary['print'] = 'напечатать'
print(dictionary)

dictionary['print'] = 'распечатать'
print(dictionary)

dict2 = {'dict': 'словарь', 'list': 'список'}
dictionary.update(dict2)
print(dictionary)

del dictionary['dict']
print(dictionary)

deleted_value = dictionary.pop('print')
print(dictionary)
print(deleted_value)

print(dictionary)
# print(dictionary['print'])
print(dictionary.get('print'))
print(dictionary.get('key'))
print(dictionary.get('wrong', 'ключа нет в словаре'))
print(dictionary.get('number', 'ключа нет в словаре'))


string_1 = 'Пусть у нас есть массив чисел numbers = [3, 5, 2, 6, 8]'
string_2 = 'Нужно вывести сумму первого и последнего элементов массива.'
numbers = [3, 5, 2, 6, 8]
print(numbers)
a = numbers[0]
b = numbers[4]
print(a + b)
c = numbers[-1]
d = numbers[-5]
print(d + c)

# Пусть у нас есть массив слов pets = ["cat", "dog", "fish", "hamster", "parrot"].
# Нужно вывести в консоль второе и четвертое слово через запятую.
pets = ["cat", "dog", "fish", "hamster", "parrot"]
print(pets[1], ",", pets[4])

# создать 3 переменные с одинаковыми данными и одинаковыми id
a = 1
b = 1
c = 1
print(id(a))
print(id(b))
print(id(c))

# создать 2 переменные с одинаковыми данными и разными id
arr1 = [0, 1, 2]
arr2 = [0, 1, 2]
print(id(arr1))
print(id(arr2))
