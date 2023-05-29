'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
величине элемент к заданному числу X. Пользователь в первой строке 
вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка 
содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5'''

n = int(input('input number of elements: '))
array = []
for i in range(n) :
    array.append(int(input('input element of array: ')))
x = int(input('input number: '))

diff = abs(array[0] - x)
number = array[0]
for item in array :
    if abs(item - x) < diff :
        diff = abs(item - x) 
        number = item
print(number)