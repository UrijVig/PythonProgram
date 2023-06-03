# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summa = int(input("Пожалуйста введите сумму задуманых чисел: "))
product = int(input("Пожалуйста введите произведение задуманых чисел: "))

x = 0
y = 0

discriminant = summa ** 2 - 4 * product

if discriminant < 0: 
    print("Упс, что-то пошло не так :)...")
elif discriminant == 0:
    x = summa / 2
    y = product / x
    print (f"X = {x}, Y = {y}")
else:
    x = (summa + discriminant ** 0.5) / 2 # При поиске обоих иксов нужно было искать так же два игрика, и ответы зеркалили друг друга, согласно чему я принял решение, что можно обойтись поиском одного икса
    y = product / x
    print (f"X = {round(x,2)}, Y = {round(y,2)}") 

for i in range(summa):
    for j in range(i,summa):
        if i + j == summa and i * j == product: 
            print (f"X = {i}, Y = {j}")

#Усложнение. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.
import math

if discriminant < 0: 
    print("Упс, что-то пошло не так :)...")
elif discriminant == 0:
    x = summa / 2
    y = product / x
    print (f"X = {x}, Y = {y}")
else:
    x = (summa + math.sqrt(discriminant)) / 2 
    y = product / x
    print (f"X = {round(x,2)}, Y = {round(y,2)}") 
