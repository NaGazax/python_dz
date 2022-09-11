# Задача №1

# number = input('Введи вещественное число: ')
# sum= 0
# for i in number:
#     if i != '.':
#         sum += int(i)

# print(f'Сумма цифр в числе: {sum}')

# Задача №2

# arr = []
# for i in range(1, int(input('Введи натуральное число: ')) + 1):
#     if i == 1:
#         arr.append(i)
#     else:
#         arr.append(arr[i - 2] * i)
# print(arr)

# Задача №3


# number = int(input('Введи натуральное число:  '))
# print ('{', end = '')
# for i in range(1, number + 1):
#     if i != number:
#         print(f'{i}: {round(((1 + 1/i) ** i), 2)},', end = ' ')
#     else:
#         print(f'{i}: {round(((1 + 1/i) ** i), 2)}' + '}')

# Задача №5

# import random

# list = ["1", "78", "166","900","172",]
# random.shuffle(list)

# print(list)

# Задача №4

# from random import randint

# element_numbers = int(input('Введите натуральное число: '))
# list = []
# for i in range(element_numbers):
#     list.append(randint(-element_numbers, element_numbers))
# print(list)
# f = open('file.txt', 'w', encoding='utf-8')
# for i in range(1, randint(1, element_numbers)):
#     f.write(str(randint(0, element_numbers - 1)) + '\n')
# f.close()

# f = open('file.txt', 'r', encoding='utf-8')
# miltiplication = 1
# for line in f:
#     miltiplication *= int(line)
# f.close()
# print(miltiplication)