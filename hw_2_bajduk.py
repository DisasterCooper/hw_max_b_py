string_1 = 'task_1'  # создать 3 переменные с одинаковыми данными и одинаковыми id.
some_a = 13
some_b = 13
some_c = 13
print(string_1)
print(id(some_a))
print(id(some_b))
print(id(some_b))

string_2 = 'task_2'  # создать 2 переменные с одинаковыми данными и разными id.
num_1 = [2]
num_2 = [2]
print(string_2)
print(id(num_1))
print(id(num_2))
cat_1 = ['Matilda']
cat_2 = ['Matilda']
print(id(cat_1))
print(id(cat_2))

string_3 = 'task_3'  # используя распаковку кортежа, поменять местами значения переменных a и b, а потом b и c.
print(string_3)
a, b, c = (1, 2, 3)
print(a, b, c)
a = 2
b = 1
print(a, b, c)
b = 3
c = 1
print(a, b, c)

string_4 = 'task_4'  # вывести на экран, используя словарь, столицу Польши, а на следующей строке столицу Беларуси.
countries_capitals = {'Belarus': 'Minsk', 'Poland': 'Warsaw', 'Great Britain': 'London'}
print(string_4)
print(countries_capitals)
print(countries_capitals['Poland'])
print(countries_capitals['Belarus'])

string_5 = 'task_5'
print(string_5)
all_food = ['котлета', 'пюре', 'драники', 'пицца', 'мороженое']
and_ = 'и'
my_favorite_food = 'Из предложенного я больше всего люблю: '
print(my_favorite_food, all_food[2], and_, all_food[4])

string_6 = 'task_6'
print(string_6)
friends = {'Egor', 'Liza', 'Vanya', 'Yana'}
print(type(friends))
name = input('Please enter a name:')
if name in list(friends):
    print('I have a friend ', name)
else:
    print(name, 'isn`t my friend')
#  Предпочтителен тип set - уникальность элементов и скорость выхождения.
#  Однако, множество не подойдет, если несколько друзей с одинаковыми именами.
