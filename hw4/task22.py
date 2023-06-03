'''Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами 
элементы множеств.'''

'''Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами 
элементы множеств.'''

import random
n = int(input('input number of elements in first set: '))
m = int(input('input number of elements in second set: '))

#быстрое решение

list1 = set()
list2 = set()
for i in range(n) :
    list1.add(random.randint(0, 20))
print(list1)
for i in range(n) :
    list2.add(random.randint(0, 20))
print(list2)

commonList = list1.intersection(list2)
print(*sorted(commonList))

# #полное решение


# list1 = []
# list2 = []
# commonList = []

# for i in range(n) :
#     list1.append(random.randint(0, 20))
# print(list1)
# for i in range(n) :
#     list2.append(random.randint(0, 20))
# print(list2)

# for i in list1 :
#     for j in list2 :
#         if i == j :
#             commonList.append(i)
# # print(*commonList)

# if len(commonList) > 1 :
#     resultList =[]
#     if commonList[1] > commonList[0] :
#         resultList.append(commonList[0])
#         resultList.append(commonList[1])
#     elif commonList[0] > commonList[1]:
#         resultList.insert(0, commonList[1])
#         resultList.append(commonList[0])

#     for number in commonList :
#         if number  < resultList[0] :
#             resultList.insert(0 , number)
#         if number > resultList[len(resultList) - 1]: 
#             resultList.insert(len(resultList), number)
#         for i in range(len(resultList) - 1) :
#             if number > resultList[i] and number < resultList[i + 1]:
#                     resultList.insert(i +1, number)
#     print(*resultList)
# elif len(commonList) != 0 :
#     print(*commonList)
# else :
#     print('no common elements')



