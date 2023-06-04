# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

input_list1 = [2, 4, 8, 10, 10, 8, 6, 4, 2]
input_list2 = [3, 9, 12, 15, 18]

set_1 = set(input_list1) 
set_2 = set(input_list2)

output_set = set(set_2.intersection(set_1))
outpu_list = list(output_set)

outpu_list.sort()
if outpu_list == []:
    print("Повторяющихся чисел нет!")
else:
    for i in outpu_list:
        print(i, end=' ')