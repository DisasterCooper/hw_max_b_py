import json
import csv
import random

print('hw_8_task_4')
# прочитать сохраненный json-файл и записать данные на диск в csv-файл;
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"

# по 4 заданию, ты пока прочитал json-файл,
# открыл csv на запись, и записал названия колонок
# сейчас можно итерироваться по объектам из json_data
# и записывать по строчке данные в csv,
# при этом в конце добавляя номер телефона (можешь генерить рандомное число)

simple_dict = {
    130130: ('A', 11),
    123356: ('B', 12),
    123444: ('C', 13),
    141414: ('D', 14),
    141333: ('E', 22),
}

with open('simple_dict.json', 'w') as file:
    json.dump(simple_dict, file)

with open('simple_dict.json') as f:
    json_data = json.load(f)
    print(json_data)
    # print(type(json_data))

with open('my_dict.csv', 'w') as f:
    writer_csv = csv.writer(f)
    writer_csv.writerow(['id', 'name', 'age', 'phone'])
    for item_key in json_data:
        writer_csv.writerow([item_key, json_data[item_key][0], json_data[item_key][1], random.randint(1, 10)])
        writer_csv.writerow([simple_dict])


# json_data[item_key][0] -- можно через *json_data[item_key] (сделать распаковку)
