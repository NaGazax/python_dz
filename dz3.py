# Задача №1

# myList = [10, 32, 12, 78, 5, 94, 7, 112, 0]
# print("Cписок:")
# print(myList)
# list_length=len(myList)
# sumOfElements=0
# for i in range(1,list_length,2):
#     sumOfElements=sumOfElements+myList[i]

# print("Сумма элементов на нечетной позиции:", sumOfElements)

# Задача №2 

# from random import randint
# from math import ceil

# arr = []
# for i in range (0, randint(1, 8)):
#     arr.append(randint(0, 35))
# print(arr)

# arr2 = []
# for i in range(0, ceil(len(arr)/2)):
#     arr2.append(arr[i] * arr[- 1 - i])
# print(arr2)

# Задача №3 

# from random import randint

# first_arr = []
# for i in range(0, randint(1, 10)):
#     first_arr.append(randint(0, 20) + randint(0,100)/100)
# print(first_arr)

# def dif(first_arr):
#     max_min =[]
#     for i in range(len(first_arr)):
#         max_min.append(first_arr[i]%1)
#     return max(max_min) - min(max_min)
# print(first_arr, ' -> ', round(dif(first_arr),2))

# # Задача №4


# a = int(input("Введите число: "))
# num = bin(a) 
# print(num[2:]) 

# Задача №5

# k = int(input('Введите число k: '))
# fib_list = [0]*(k*2+1)
# fib_list[k] = 0
# fib_list[k+1] = 1
# for i in range(k+2, len(fib_list)):
#     fib_list[i] = fib_list[i-2] + fib_list[i-1]

# for i in range(k, -1, -1):
#     fib_list[i] = fib_list[i+2] - fib_list[i+1]
# print(fib_list)