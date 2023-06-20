'''Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с 
клавиатуры. Формула для получения n-го члена прогрессии: 
an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

n1 = int(input('input first elememt: '))
step = int(input('intput step: '))
kol = int(input('input number of elements: '))
my_list = []

for i in range(1, kol +1) :
    my_list.append(n1 + (i-1) * step)
    print(my_list[i - 1])