# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является.
# Т.е. выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

num = int(input('Введите число: '))

first_num = 0
second_num = 1
third_num = first_num + second_num

count = 3

while num > third_num:
    first_num = second_num
    second_num = third_num
    third_num = first_num + second_num
    count += 1

if third_num != num:
    count = -1

print(count)
