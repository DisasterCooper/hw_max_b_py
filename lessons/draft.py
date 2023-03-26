import json
print('hw_8_task_3')

dictionary = {'key': ('ключ', 'number')}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())

# dictionary['key'] = input('Введите id: ')
# print(dictionary)

simple_dict = {
    '130130': ('A', '11'),
    '123356': ('B', '12'),
    '123444': ('C', '13'),
    '141414': ('D', '14'),
    '141333': ('E', '22'),
}

with open('simple_dict.json', 'w') as file:
    json.dump(simple_dict, file)

# print('hw_8_task_3a')  # черновые мысли
#
# my_dict = {}
#
# number_elements = int(input('Введите количество элементов словаря: '))
#
# for i in range(number_elements):
#     key = input('Введите ключ (id): ')
#     value = input(str('Введите имя: '))
#     my_dict[key] = value
#
# print(my_dict)

print('hw_8_task_3_second version')
my_dict = {}

while True:
    key = int(input('Введите ключ (id из 6 символов): '))
    key_str = str(key)
    if len(key_str) != 6:
        print('Некорректная длина ключа. Попробуйте еще раз.')
        continue  # переход к следующей итерации цикла
    name = input('Введите имя: ')
    try:
        age = int(input('Введите возраст: '))
    except ValueError:
        print('Некорректный формат возраста. Попробуйте еще раз.')
        continue  # переход к следующей итерации цикла
    my_dict[key] = (name, age)
    print(f'Значение {my_dict[key]} успешно добавлено в словарь под ключом {key}.')
    if input('Продолжить? (y/n)').strip().lower() != 'y':
        break  # выход из цикла

print(my_dict)

with open('my_dict.json', 'w') as file:
    json.dump(my_dict, file)

print('hw_10_task_1')  # class auto с атрибутами


class Auto:

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birth(self):
        self.age += 1

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight


auto = Auto('Volvo', 5, 'Xc90', 'black', 2300)
auto.birth()
auto.move()
auto.stop()

print('hw_10_task_2')

