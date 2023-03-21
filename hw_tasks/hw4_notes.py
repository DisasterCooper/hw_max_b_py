"""
1. Если у вас условия взаимоисключающие, писать elif необязательно, можно просто else:
    for i, row in enumerate(str_):
        if i % 2 == 0:
            even_indexes.append(row)
        elif i % 2 != 0:  # здесь подходит просто else
            odd_indexes.append(row)

2. Одинаковые вещи пишем одинаково:
    for i, symbol in enumerate(str_):
        if i % 2 == 0:
            even_indexes.append(symbol)
        else:
            odd_indexes.append(str_[i])  # здесь лучше odd_indexes.append(symbol)

3. Там, где можно решить задачу циклом for, используем цикл for, а не while:
    sentence = "Hello World!"
    words = sentence.split()
    list_ = []
    index = 0
    while index < len(words):
        list_.append(words[index][::-1])
        index += 1
    print(" ".join(list_))

    # то же самое, но более pythonic:
    for word in words:
        list_.append(word[::-1])

4. Про конкатенацию строк в цикле (задание #2 и #4)
Лучше перед циклом определить переменную-список, в которую на каждой итерации добавлять результат,
а в конце, чтобы получить ответ, вызвать ''.join(some_list).
Дело в том, что так как строки неизменяемые, + и += возвращают новые объекты,
следовательно на каждой итерации будут пораждаться ненужные временные объекты.
    even_str = ''
    odd_str = ''
    for index, symbol in enumerate(str_):
        if index_ % 2 == 0:
            even_str += str_[index_]
        else:
            odd_str += str_[index_]

    # лучше так
    even_str_symbols = []
    odd_str_symbols = []
    for i, symbol in enumerate(str_):
        if i % 2 == 0:
            even_str_symbols.append(symbol)
        else:
            odd_str_symbols.append(symbol)
    print(''.join(even_str_symbols))
    print(''.join(odd_str_symbols))

5. Важно учиться гуглить и задавать вопросы по тому, что не получается:
Пример запроса в гугл: how to reverse string python
"""
