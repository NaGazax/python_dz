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

from random import randint
from math import floor

first_arr = []
for i in range(0, randint(1, 10)):
    first_arr.append(randint(0, 20) + randint(0,100)/100)
print(first_arr)