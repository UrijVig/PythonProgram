# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

number = int(input("Пожалуйста, введите число: "))

count = 0

if number < 1: 
    print("введены некорректные данные! ")
else:
    while 2 ** count < number:
        degree = 2 ** count
        count += 1
        print(degree)


#Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print

string = ""
count = 0

while 2 ** count < number:
        degree = 2 ** count
        count += 1
        print(degree, end=',')
