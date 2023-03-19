import json
import csv

print('hw_8_task_2')
line_1 = "Monday\n"
line_2 = "Tuesday\n"
line_3 = "Wednesday\n"
line_4 = "Thursday\n"
with open('days.txt', 'w') as file:
    file.write(line_1)
    file.write(line_2)
with open('days.txt', 'a') as file:
    file.write(line_3)
    file.write(line_4)

print('hw_8_task_3')
simple_dict = {
    '130130': ('A', '11'),
    '123356': ('B', '12'),
    '123444': ('C', '13'),
    '141414': ('D', '14'),
    '141333': ('E', '22'),
}

with open('simple_dict.json', 'w') as file:
    json.dump(simple_dict, file)

print('hw_8_task_3_second version')
my_dict = {}

while True:
    key = int(input('Введите ключ (id из 6 символов): '))
    key_str = str(key)
    if len(key_str) != 6:
        print('Некорректная длина ключа. Попробуйте еще раз.')
        continue
    name = input('Введите имя: ')
    try:
        age = int(input('Введите возраст: '))
    except ValueError:
        print('Некорректный формат возраста. Попробуйте еще раз.')
        continue
    my_dict[key] = (name, age)
    print(f'Значение {my_dict[key]} успешно добавлено в словарь под ключом {key}.')
    if input('Продолжить? (y/n)').strip().lower() != 'y':
        break

print(my_dict)

with open('my_dict.json', 'w') as file:
    json.dump(my_dict, file)

print('hw_8_task_4')
with open('my_dict.json', 'r') as f:
    json_data = json.load(f)
    print(json_data)

csv_row_names = [['id', 'name', 'age', 'phone']]

# for row in my_dict:
    # csv_row_names.append([row['id'], row['name'], row['age'], row.get('phone', '')])  # get?

with open('my_dict.csv', 'w', newline='', encoding='utf-8') as f:
    wr_csv = csv.writer(f)
    wr_csv.writerows(csv_row_names)
