import json
import csv

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


# def add(a=0, b=0):
#     return a + b


# add()  # либо у функции нет аргументов, либо *args/**kwargs,
# либо у аргументов есть значения по умолчанию


# контекстный менеджер
with open('hello.txt') as file:  # то же самое -> 'hello.txt', 'rt'
    file_text = file.read()
    print(file_text)
    file.seek(0, 0)  # 1й - позиция курсора, позиция относительно начала файла

with open('hello.txt', 'rt') as file:
    pass

with open('hello2.txt', 'r') as file:  # a - append -- добавляет строку
    lines = file.readlines()

lines[0] = 'some new line\n'
with open('hello2.txt', 'w') as file:
    file.writelines(lines)

# # Json ##########################
# cтрока;
# число;
# логический (true или false);
# null;
# объект;
# массив

with open('example.json') as json_file:
    json_data = json.load(json_file)
    print(json_data)
    print(type(json_data))

with open('new_json.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)  # indent - отступы

# # csv ##########################

with open('example.csv') as file:
    csv_reader = csv.reader(file)
    data = []
    for index, line in enumerate(csv_reader):
        if index == 0:
            column_names = line
            continue
        data.append(line)

    print(column_names)
    print(data)


csv.register_dialect('my_delimiter', delimiter=';')


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


# 1
# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину.
some_text = """Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела"""""
#
with open('article.txt', 'w') as file:
    file.write(some_text)


def read(file_name: str) -> str | int | list:
    with open(file_name, 'r') as f:
        words = f.read().split()
        max_word_len = len(words[0])
        for word in words[1:]:
            if max_word_len < len(word):
                max_word_len = len(word)
        filter_result = (list(filter(lambda slovo: len(slovo) == max_word_len, words)))
        return filter_result


print(read('article.txt'))

# 2
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


def read_last(lines_number: int, file_name: str) -> None:
    if lines_number < 0:
        print('Неверный параметр')
        return
    file_ = open(file_name)
    lines = file_.readlines()
    for line_1 in lines[-lines_number:]:
        print(line_1)
    file.close()


read_last(3, 'article.txt')
