print('task_1')  # Завернуть код из первой задачи прошлого домашнего задания в вечный цикл.
while True:
    name_user = input('Введите имя: ')
    age = int(input('Ваш возраст: '))
    if age > 18:
        print(f'Привет, {name_user}! У вас есть доступ к взрослому контенту.')
    elif age == 18:
        print(f'Привет, {name_user}! Поздравляю с совершеннолетием! У вас нет доступа к взрослому контенту.')
    elif age < 18:
        print(f'Привет, {name_user}! У вас нет доступа к взрослому контенту.')
        if age == 0:
            print(f'Закончили')
            break

print('task_2a - через слайсы')
string_1 = input('Введите произвольную строку 1: ')
str_even_slays = string_1[1::2]
print(f'Введена четная строка: {str_even_slays}')
str_odd_slays = string_1[::2]
print(f'Введена нечетная строка: {str_odd_slays}')
print('\n\n', str_even_slays, '     ', str_odd_slays, '\n !!!')

print('task_2b - через цикл')
string_2 = input('Введите произвольную строку 2: ')
str_even_cycle = ''
str_odd_cycle = ''
for i in range(len(string_2)):
    if i % 2 == 1:
        str_even_cycle += string_2[i]
    else:
        str_odd_cycle += string_2[i]
print(f'Введена четная строка: {str_even_cycle}')
print(f'Введена четная строка: {str_odd_cycle}')
print('\n\n', str_even_cycle, '     ', str_odd_cycle, '\n !!!')

print('task_3')  # Сделать программу, в которой нужно будет угадывать число.
import random

min_num = 1
max_num = 20
bot = random.randint(min_num, max_num)

while True:
    user = int(input(f'Введите число, которое загадал бот, от {min_num} до {max_num}: '))
    if user == bot:
        print('Да, это оно!')
        break
    elif user != bot:
        print(f'Не угадали.. Пожалуйста, попробуйте еще.')

print('task_4')  # Для введенной строки изменить порядок символов в каждом слове в предложении
string_4 = "Hello World!"
print(string_4)
words = string_4.split()  # разбиваем строку на слова
new_sentence = []  # для измененных слов
for word in words:
    new_word = word[::-1]  # изменяем порядок символов в слове
    new_sentence.append(new_word)
result = ' '.join(new_sentence)  # объединяем новую строку с пробелами
print(result)
