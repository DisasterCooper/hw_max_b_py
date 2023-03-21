# lambda_func = lambda number: "четное" if number % 2 == 0 else "нечетное"
# print(lambda_func(12))
# print(lambda_func(13))
# print(list(map(lambda number: "четное" if number % 2 == 0 else "нечетное", [2, 3, 4, 5])))
#
# numbers = [1, 2, 3, 4]
# print(numbers)
# print(list(map(lambda number: str(number), numbers)))
#
# strings = ('oko', 'hello', 'ervre', 'by')
# print(list(filter(lambda string: string == string[::-1], strings)))


# TDD - test driven development
test_cases = [
    '1', '-1', '0.1', '-0.1', '.1', '-.1', '0',
    'a', '', '1a', '--1', '1-', '1..1', '0.1a', '12 12', '-a12', '..1', '-...'
]


def analyze_str(num_str: str) -> int | float | None:
    if num_str.isdigit():
        print(f'положительное целое {num_str}')
        return int(num_str)
    cleaned_num_str = num_str.replace('-', '', 1).replace('.', '', 1)
    if not cleaned_num_str.isdigit() or ('-' in num_str and num_str[0] != '-'):
        print(f'некорректное число {num_str}')
        return None
    if '.' in num_str:
        num_type = 'дробное'
        num = float(num_str)
    else:
        num_type = 'целое'
        num = int(num_str)
    if num >= 0:
        num_sign = 'положительное'
    else:
        num_sign = 'отрицательное'
    print(f'{num_sign} {num_type} {num_str}')
    return num


def analyze_str2(num_str: str) -> int | float | None:
    if num_str.isdigit():
        print(f'положительное целое {num_str}')
        return int(num_str)
    cleaned_num_str = num_str.replace('-', '', 1).replace('.', '', 1)
    if not cleaned_num_str.isdigit() or ('-' in num_str and num_str[0] != '-'):
        print(f'некорректное число {num_str}')
        return None
    if '.' in num_str and num_str[0] == '-':
        print(f'отрицательное дробное {num_str}')
        return float(num_str)
    if num_str[0] == '-':
        print(f'отрицательное целое {num_str}')
        return int(num_str)
    print(f'положительное дробное {num_str}')
    return float(num_str)

# for num_str in test_cases:
#     print(analyze_str(num_str))


# print(list(map(analyze_str, test_cases)))

print([analyze_str2(num_str) for num_str in test_cases])


