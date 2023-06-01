# # Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = input("Введите номер билета: ")

right = int(number[3::])
left = int(number[:3:])

results = 0
numbers = right
while numbers > 0: 
    x = numbers % 10
    results = results + x
    numbers = numbers // 10

right = results

results = 0
numbers = left
while numbers > 0: 
    x = numbers % 10
    results = results + x
    numbers = numbers // 10

left = results

if right == left:
    print("Ваш билет счастливый!")
else:
    print("Ваш билет не счасливый")

#Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор

res = "Yes " if right == left else "No"
print(res)
