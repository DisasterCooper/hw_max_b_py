import json
import csv
import random

print('hw_8_task_4')
# прочитать сохраненный json-файл и записать данные на диск в csv-файл;
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"

# my_dict = {
#     '130130': ('A', '11'),
#     '123356': ('B', '12'),
#     '123444': ('C', '13'),
#     '141414': ('D', '14'),
#     '141333': ('E', '22'),
# }
#
# with open('my_dict.json', 'w') as file:
#     json.dump(my_dict, file)

# по 4 заданию, ты пока прочитал json-файл,
# открыл csv на запись, и записал названия колонок
# сейчас можно итерироваться по объектам из json_data
# и записывать по строчке данные в csv,
# при этом в конце добавляя номер телефона (можешь генерить рандомное число)
# with open('my_dict.json', 'r') as file:
#     json_data = json.load(file)
#     print(json_data)
#
# json_data_str = json.dumps(json_data)
# print(type(json_data_str))
# with open('my_dict.csv', 'w', newline='', encoding='utf-8') as f:
#     writer_csv = csv.writer(f)
#     csv_row_names = ['id', 'name', 'age', 'phone']
#     writer_csv.writerow(csv_row_names)
#     for row in my_dict:
#         add_phone = ['111-11-11', '111-11-22', '111-22-22', '222-22-22', '333-33-33']
#         with open('my_dict.csv', 'a') as file:
#             writer_csv = csv.writer(file)
#             writer_csv.writerow(json_data)

################################
# итог решение

simple_dict = {
    130130: ('A', 11),
    123356: ('B', 12),
    123444: ('C', 13),
    141414: ('D', 14),
    141333: ('E', 22),
}

with open('simple_dict.json') as f:
    json_data = json.load(f)

with open('simple_dict.csv', 'w') as f:
    writer_csv = csv.writer(f)
    writer_csv.writerow(['id', 'name', 'age', 'phone'])
    for item_key in json_data:
        writer_csv.writerow([item_key, json_data[item_key][0], json_data[item_key][1], random.randint(100000, 200000)])
