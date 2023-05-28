'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) '''

number = int(input('Введите число: '))

sum = 0
str_sum = ''
while number < 9:
    sum += number % 10
    str_sum += str(number % 10) + '+'
    number //= 10
sum += number % 10
str_sum += str(number % 10) 

print(sum, '(', str_sum, ')')