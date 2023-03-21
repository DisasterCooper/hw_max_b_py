a = 2
b = 2
c = a + b
d = ","
# print(c)
# print(a - b)
string = "a ** с"
print(a ** c, d, string)

print(a // b)
str = "hello"
str1 = "world"
# f string - форматирование строк
print(f"{str} {str1}")

x = (17 / 2) * 3 + 2
print(x)

x2 = ((17 / 2) % 2) * (3 ** 3)
print(x2)


num1 = 1
num2 = 2
if num1 > num2:
    # pass ничего не делает, но убирает ошибку
    pass
    print("num1 is bigger than num2")
# pass ничего не делает, но убирает ошибку
else:
    print("num1 is smaller or equal to num2")

num1 = 3
num2 = 3
print(num1 > num2)
if num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is bigger than num2")
else:
    print("num1 is smaller or equal to num2")

# пример сложнее
num1 = 4
num2 = 3
print(num1 > num2)
if num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal to num2")

# пример еще сложнее
num1 = 4
num2 = 3
print(num1 > num2)
if num1 == num2:
    print("num1 is equal to num2")
if num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal to num2")
