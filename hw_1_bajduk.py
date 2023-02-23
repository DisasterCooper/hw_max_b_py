# получить сумму, разность, произведение, воспроизвести a в степень b,
# a поделить по модулю b и выполнить целочисленное деление a на b.
print('task_1')
a = 5
b = 3
print(a, b)
print('add =', a + b)
print('sub =', a - b)
print('mult =', a * b)
print('expon =', a ** b)
print('modul =', a % b)
print('floor_division =', a // b)

# расставить скобки, чтобы значение выражений не поменялось.
print('task_2')
x = 17 / 2 * 3 + 2
parentheses_x = (((17 / 2) * 3) + 2)
print(x)
print(parentheses_x)
x1 = 2 + 17 / 2 * 3
parentheses_x1 = (2 + ((17 / 2) * 3))
print(x1)
print(parentheses_x1)
x2 = 19 % 4 + 15 / 2 * 3
parentheses_x2 = ((19 % 4) + ((15 / 2) * 3))
print(x2)
print(parentheses_x2)
x3 = (15 + 6) - 10 * 4
parentheses_x3 = ((15 + 6) - (10 * 4))
print(x3)
print(parentheses_x3)
x4 = 17 / 2 % 2 * 3 ** 3
parentheses_x4 = (((17 / 2) % 2) * (3 ** 3))
print(x4)
print(parentheses_x4)

# даны действительные числа x и y.
print('task_3')
x = 3
y = -5
mod_x = abs(x)
mod_y = abs(y)
print(mod_x)
print(mod_y)
result = (mod_x - mod_y) / (1 + (mod_x * mod_y))
print(result)

# даны действительные числа x и y.
print("task_3a")
x = int(input('enter a first number:'))
y = int(input('enter a second number:'))
mod_x = abs(x)
mod_y = abs(y)
result = (mod_x - mod_y) / (1 + (mod_x * mod_y))
print(result)
