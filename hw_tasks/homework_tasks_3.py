# 1
# Написать программу, которая получает имя и возраст пользователя, проверяет, что возраст 18 лет и старше
# и выдает приветсвенное сообщение в зависимости от возраста. Примеры работы:
# Имя Иван, возраст 34 -> "Приветсвую, Иван! У вас есть доступ к взрослому контенту."
# Имя Лиза, возраст 15 -> "Приветсвую, Лиза! У вас нет доступа к взрослому контенту."
# Имя Артем, возраст 18 -> "Приветсвую, Артем! Поздравляю с совершеннолетием! У вас нет доступа к взрослому контенту."

# name_user = input('Введите имя: ')
# age = int(input('Ваш возраст: '))
# if age > 18:
#     print(f'Привет, {name_user}! У вас есть доступ к взрослому контенту.')
# elif age == 18:
#     print(f'Привет, {name_user}! Поздравляю с совершеннолетием! У вас нет доступа к взрослому контенту.')
# elif age < 18:
#     print(f'Привет, {name_user}! У вас нет доступа к взрослому контенту.')


# 2*
# Пользователь вводит две строки. Нужно вывести True, если в обеих строках использовались одинаковые символы,
# и False иначе. Постараться решить, не используя циклы.
# Примеры работы:
# "abc" и "bca" -> True
# "aabc" и "abc" -> True
# "Abc" и "abc" -> False
# "abc" и "aaa" -> False

# str_1 = set(input('Enter string 1:'))
# str_2 = set(input('Enter string 2:'))
# print(str_1)
# print(str_2)
# # print(type(str_1))
# # print(type(str_2))
# if str_1 == str_2:
#     print('true')
# elif str_1 != str_2:
#     print('false')

# 3*
# Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
# либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
# Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
# Бот выбрал ножницы, вы проиграли!
# Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами
game = {'rock': '1', 'scissors': '2', 'paper': '3'}
rock = 1
scissors = 2
paper = 3
# import random
user = int(input(f'user Выберите: 1 - rock or 2 - scissors or 3 - paper: '))
user2 = int(input('Выберите: 1 - rock or 2 - scissors or 3 - paper: '))
# bot = [1, 2, 3]
# bot = random.randint(1, 3)
# print(bot)
# print(game)
# print(type(bot))
# print(type(user))

if user2 == 1 and user == 2:
    print('User2 выбрал rock, вы проиграли.')
elif user2 == 1 and user == 3:
    print('User2 выбрал rock, вы выиграли.')
elif user2 == 2 and user == 1:
    print('User2 выбрал scissors, вы выиграли.')
elif user2 == 2 and user == 3:
    print('User2 выбрал scissors, вы проиграли.')
elif user2 == 3 and user == 1:
    print('User2 выбрал paper, вы проиграли.')
elif user2 == 3 and user == 2:
    print('User2 выбрал paper, вы выиграли.')
elif user == user2:
    print('Ничья.')
#
# if user > bot:
#     print(f'bot выбрал Выиграл')
# elif user < bot:
#     print(f'{user} проиграл')
# elif user == bot:
#     print('Ничья.')
