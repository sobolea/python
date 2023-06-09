'''Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко 
он их придумывает, Вам стоит написать программу. Винни-Пух считает, что 
ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
стихотворения одинаковое. Фраза может состоять из одного слова, если во 
фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг 
от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с 
клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
и “Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  '''

vowel = ['а', 'у', 'е', 'э', 'ю', 'и', 'я', 'ы', 'о']
def check(f, list):
    for i in range(len(list)):
        if not f(list[i]):
            return('Пам парам')
    return('Парам пам-пам')

phrases = list(input('input line: ').split())

kol = []

for i in range(len(phrases)):
    kol1 = 0
    for letter in phrases[i]:
        if letter in vowel:
            kol1 += 1
    kol.append(kol1)

print(check(lambda x: x == kol[0], kol))
