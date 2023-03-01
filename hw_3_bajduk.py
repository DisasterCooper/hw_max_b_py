print('task_1')  # Имя и возраст пользователя, проверить, что возраст 18 лет и старше.
name_user = input('Введите имя: ')
age = int(input('Ваш возраст: '))
if age > 18:
    print(f'Привет, {name_user}! У вас есть доступ к взрослому контенту.')
elif age == 18:
    print(f'Привет, {name_user}! Поздравляю с совершеннолетием! У вас нет доступа к взрослому контенту.')
elif age < 18:
    print(f'Привет, {name_user}! У вас нет доступа к взрослому контенту.')

print('task_2')
# Пользователь вводит две строки. Нужно вывести True, если в обеих строках использовались одинаковые символы,
# и False иначе. Постараться решить, не используя циклы.
str_1 = set(input('Enter string 1:'))
str_2 = set(input('Enter string 2:'))
# print(str_1)
# print(str_2)
if str_1 == str_2:
    print('true')
elif str_1 != str_2:
    print('false')

print('task_3')  # Написать мини-игру Камень ножницы бумага с ботом.
rock = 1
scissors = 2
paper = 3
import random
user = int(input(f'user Выберите: 1 - rock or 2 - scissors or 3 - paper: '))
bot = random.randint(1, 3)
print(bot)
if bot == 1 and user == 2:
    print('bot выбрал rock, вы проиграли.')
elif bot == 1 and user == 3:
    print('bot выбрал rock, вы выиграли.')
elif bot == 2 and user == 1:
    print('bot выбрал scissors, вы выиграли.')
elif bot == 2 and user == 3:
    print('User2 выбрал scissors, вы проиграли.')
elif bot == 3 and user == 1:
    print('bot выбрал paper, вы проиграли.')
elif bot == 3 and user == 2:
    print('bot выбрал paper, вы выиграли.')
elif bot == user:
    print('Ничья.')
