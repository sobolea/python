'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
'''

my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
result = []
n1= int(input('input right border: '))
n2= int(input('input left border: '))
for i in range (len(my_list)) :
  if my_list[i]<n2 and my_list[i]>n1:
      result.append(i)
      
print(*result)

