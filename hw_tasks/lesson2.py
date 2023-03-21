# int_ = 1
# float_ = 0.
# bool_ = True
# string = "a"
# #
# a = 10 ** 1000
# print(a)
#
# b = 10.1 ** 1000
# print(b)
# # #
# print(2 + 1 == 3)
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2)
#
# from decimal import Decimal
#
# a = Decimal('0.1')
# b = Decimal('0.2')
# c = Decimal('0.3')
# print(a + b == c)
# print(Decimal(2.76))
#
# a = 1
# b = 1 + 1
# print(id(a))
# print(id(b))
# print(a is b)
#
# int_ = 1
# float_ = 0.
# bool_ = True

# string = "a"
# print(id(string))
# string += "b"  # string = string + "b"
# print(id(string))

# None

# ==, != - для чисел и строк

# some_variable = "sjdnv"
# some_variable = None
# print(some_variable is None)

# string = "a"
# string += "b"  # string = string + "b"

# num1 = 5.1
# numbers = [1, 2, 3, 1, -10, 100]  # list, список

# everything = ["a", 1, num1, True]
# print(everything)
# print(id(everything))
#
# everything.append("hello")
# # print(everything)
# print(everything[3], id(everything[3]))
# everything[3] = 2
# print(everything[3], id(everything[3]))

# print(everything[0])
# print(everything[-1])
# print(everything[0:2])
# print(everything[:2])
#
# everything[0] = 2
# print(everything)

# everything = ["a", 1, num1, True]

# everything.append("hello")
# print(everything)
#
# nums = [2, 3, 4]
# everything.append(nums)
# print(everything)
# print(len(everything))
#
# everything.extend(nums)
# print(everything)

# everything.insert(1, "hello")
# print(everything)
# everything.insert(10, "hello")
# print(everything)

#
# print(len(everything))
#
# everything.remove(4)
# print(everything, ". длина:", len(everything))
# everything.remove(nums)
# print(everything, ". длина:", len(everything))
#
# del everything[0]
# print(everything)
#
# del everything[2]
# print(everything)
#
# del everything[1:3]
# print(everything)

# first_item = everything.pop(0)
# print(everything)
# print(first_item)

# everything.remove(True)
# everything.remove(True)


# matrix = [[1, 2], [3, 4]]
# print(matrix)

# string = "hello world, I write code"
# words = string.split()
# print(words)
#
# variable_name = "some_many_words_name"
# not_working = variable_name.split()
# print(not_working)
# words = variable_name.split("_")
# print(words)
#
# str_ = ""
# print(len(str_))
#
# result = " ".join(words)
# print(result)
# print(type(result))
#
# result2 = ", ".join(words)
# print(result2)
#
# string = "   hello     "
#
# cleaned_name = string.strip()
# print(cleaned_name)
#
# cleaned_name_r = string.rstrip()
# print(cleaned_name_r)
#
# cleaned_name_l = string.lstrip()
# print(cleaned_name_l)

# numbers = (1, 2, 10)  # tuple, кортеж
# print(numbers)
# print(type(numbers))
#
# numbers2 = (1, 2, 10)
# print(id(numbers))
# print(id(numbers2))

# numbers = 1, 2, 10
# print(numbers)
# print(type(numbers))

# a, b = input(), input()
# a, b = 2, 3  # 2, 3 - это кортеж, тут происходит распаковка
# print(a)
# print(b)

# a, *b, c = (1, 2, 3, 5, 3, "hello", None)
# print(a)
# print(b)
# print(c)
# print('------------------------')
#
# a, b, *c = 1, 2, 3, 5, 3, "hello"
# print(a)
# print(b)
# print(c)
# print('------------------------')
#
# *a, b, c = 1, 2, 3, 5, 3, "hello"
# print(a)
# print(b)
# print(c)
#
# a, _, *c = 1, 2, 3, 5, 3, "hello"
# print(a)
# print(c)

# a = 2
# b = 3
# a, b = b, a
# print(a, b)

# a = (1, )
# print(a)
# print(type(a))
# b = (1)
# print(b)
# print(type(b))

# Чем отличается список от множества:
# 1. В множестве все элементы уникальны, в списке могут повторяться
# 2. В множестве порядок НЕ сохраняется, в списке сохраняется
# 3. Нельзя обращаться по индексу
# 4. Методы по добавлению: для списка append, для множества add
# 5. Проверка выхождения элемента в множества (например, 10 in set_) работает быстрее
#    чем для списка

# names = {"name1", 1, None, False, False}  # set, множество
# print(names)
# print(type(names))
#
# names.add("name2")
# print(names)
#
# names.add("name2")
# print(names)
#
# print(len(names))
#
# names.remove(None)
# print(names)

# names.remove(None)
# print(names)

# print(names[0])  # так нельзя

# list, tuple, set
# list_ = [1, 2, 3]
# tuple_ = (1, 2, 3)
# set_ = {1, 2, 3}
#
# print(1 in list_)
# print(10 in list_)
#
# print(1 in tuple_)
# print(10 in tuple_)
#
# print(1 in set_)
# print(10 in set_)




dictionary = {'name': 1}
# 'name' - ключ, key
# 1 - значение, value

dictionary = {'key': 'ключ', 'number': 'число', 'cat': 'кот', 'dog': 'собака'}
# print(dictionary['cat'])
#
# print(dictionary.keys())
# print(dictionary.values())
#
# dictionary['print'] = 'напечатать'
# print(dictionary)
#
# dictionary['print'] = 'распечатать'
# print(dictionary)

# dict2 = {'dict': 'словарь', 'list': 'список'}
# dictionary.update(dict2)
# print(dictionary)
#
# del dictionary['dict']
# print(dictionary)

# deleted_value = dictionary.pop('print')
# print(dictionary)
# print(deleted_value)

# print(dictionary)
# # print(dictionary['print'])
# print(dictionary.get('print'))
# print(dictionary.get('key'))
# print(dictionary.get('wrong', 'ключа нет в словаре'))
# print(dictionary.get('number', 'ключа нет в словаре'))
