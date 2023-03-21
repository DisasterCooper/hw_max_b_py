import json

list_ = []
dict_ = {}
set_ = set()

if not dict_ or not list_ or not set_:
    pass


def add(*args, **kwargs):
    print(args, type(args), end=' | ')
    print(kwargs, type(kwargs))


# add()
# add(2, 3)
# add(a=2, b=3)
# add(2, b=3)


def add(a=0, b=0):
    return a + b


# add()  # либо у функции нет аргументов, либо *args/**kwargs, либо у агрументов есть значения по умолчанию


##############################
# with open('hello.txt') as file:  #  то же самое, что и with open('hello.txt', 'rt') as file:
    # first_5_symbols = file.read(5)
    # print(first_5_symbols)
    # file.seek(6, 0)
    # line = file.readline()
    # print(line)
    # lines = file.readlines()
    # print(lines)
    # for line in file:
    #     print(line, end='')


# with open('some_folder2/new_hello.txt', 'w'):
#     pass


# string = 'привет'
# encoded_string = string.encode(encoding='utf-8')
# print(encoded_string)



# with open('hello3.txt') as file:
#     file_text = file.read()
#     print(file_text)
#
# cp1251_string = file_text.encode(encoding='cp1251')
#
# with open('not_utf.txt', 'wb') as file:
#     file.write(cp1251_string)


# В JSON значение может быть одним из шести типов данных:
# cтрока;
# число;
# логический (true или false);
# null;
# объект;
# массив


# import json
#
#
# with open('example.json') as json_file:
#     json_data = json.load(json_file)
#     print(json_data)
#     print(type(json_data))


# json_data_str = json.dumps(json_data)
# print(json_data_str)
# print(type(json_data_str))
#
# # dict_data = json.loads(json_data_str)
# data = json.loads('[1, 2, 3]')
# print(data)
# print(type(data))

# json_data["name"] = "Anna"
#
#
# with open('new_json.json', 'w') as json_file:
#     json.dump(json_data, json_file, indent=4)


import csv


csv.register_dialect('my_delimeter', delimiter=';')


with open('example.csv') as file:
    csv_reader = csv.reader(file)
    json_data = []
    for index, line in enumerate(csv_reader):
        # print(line)
        if index == 0:
            column_names = line
            continue

        # line_object = {}
        # for column_name, value in zip(column_names, line):
        #     line_object[column_name] = value

        line_object = {column_name: value for column_name, value in zip(column_names, line)}

        json_data.append(line_object)


print(json_data)
with open('csv_to_json.json', 'w') as json_file:
    json.dump(json_data, json_file)

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
with open('my_new_csv.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(list_2)
    csv_writer.writerow([1, 2, 3, 4])
    csv_writer.writerow(["hello"])
    csv_writer.writerows([list_2, list_1])


# list_1 = [1, 2, 3, 4, 5, 6, 7]
# list_2 = ['a', 'b', 'c', 'd']
#
# print(list(zip(list_1, list_2)))


def read(text: str) -> str:
    words = text.split()
    max_word = words[0]
    for word in words[1:]:
        if len(max_word) < len(word):
            max_word = word
    return max_word


words = "text text2 and you".split()
print(max(words, key=lambda word: len(word)))


# print(read("article.txt"))

