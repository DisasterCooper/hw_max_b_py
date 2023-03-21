# print("Hello World")

# name = input("Enter your name ")
# print("Hello,", "hello", name)

# number = 1
# print(type(number))
#
# float_number = 1.0
# print(type(float_number))
#
# string = "Hello"
# print(type(string))
#
# is_smth = True  # False
# print(type(is_smth))

string = "Hello World"
# print(len(string))
#
# print(string[0])
# print(string[-1])
# print(string[-2])
#
# print(string[0:6])
# print(string[6:11])
# print(string[::2])
# print(string[-5:0:1])

# print(string.lower())
# print(string.upper())
# print("hello-world".title())

# print(string.isdigit())
# print(string.isalpha())

# print(string.find("l"))
# print(string.rfind("l"))
# print(string.find("m"))

string = "Hello World"
string2 = "!!!"
# new_string = string.replace("World", "Joe")
# # print(new_string)
# print(string.replace("World", "Joe").replace("Hello", "Hi"))

num1 = 10
num2 = 2

# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)  # float
# print(num1 // num2)
# print(11 / 2)
# print(11 // 2)
# print(round(11 / 2))
# print(11 % 2)
# print(num1 ** num2)

num1 = 10
num2 = 2

# print(num1 == num2)
# print(num1 != num2)
# print(num1 > num2)
# print(num1 < num2)
# print(5 >= 5)
# print(5 <= 5)

# print("True" == "true")
# print("abc" < "bcd")
# print(ord("a"))
# print(ord("b"))

# print(2 + 2 * 3)
# print((2 + 2) * 3)
# print(2 + (2 * 3))
# print(5 - 2 - 1)
# print(2 ** 3 ** 2)
# print((2 ** 3) ** 2)

str1 = "Hello"
str2 = "World"

# print("{str1} {str2}")
# print(str1, str2)
# print(f"{str1}, {str2}, and everybody!")
# print("{0}, {1}, and everybody!".format(str1, str2))
# print("{0}, {1}, and everybody!".format("man1", "man2"))
# print("{str1}, {str2}, and everybody!".format(str1=str1, str2=str2))


num1 = 4
num2 = 3
# print(num1 > num2)
if num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal to num2")


# пример сложнее
num1 = 4
num2 = 3
# print(num1 > num2)
if num1 - 1 > num2:
    print("num1 - 1 is bigger than num2")
elif num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal to num2")


num1 = 3
num2 = 3
# еще пример, еще сложнее
if num1 == num2:
    print("num1 is equal to num2")
if num1 - 1 > num2:
    print("num1 - 1 is bigger than num2")
elif num1 > num2:
    print("num1 is bigger than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal to num2")
