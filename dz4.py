# Задача №1
# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# Задача №2
# n = int(input("Введи число: "))
# list = []
# d = 2
# while d * d <= n:
#         if n % d == 0:
#             list.append(d)
#             n //= d
#         else:
#             d += 1
#             if n > 1:
#                  list.append(n)
# print(list)

# # Задача №3

# import random
# list_1 = [random.randint(0,100) for i in range (10)]
# print('Исходный список ', list_1)
# new_list =[]
# [new_list.append(i) for i in list_1 if i not in new_list ]
# print('Список без повторных элементов ', new_list)

# Задача 4 

# import random

# k = int(input('Введите коэффициент: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))

# if a != 0:
#     first = (str(a) + "x^" + str(k) + " + ")
# else:
#     first = (str())

# if b != 0:
#     second = (str(b) + "x" + " + ")
# else:
#     second = (str())

# if c != 0:
#     third = (str(c) + " = 0")
# else:
#     third = (str())

# print(f'{first}{second}{third}')