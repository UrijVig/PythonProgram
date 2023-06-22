# Напишите программу, генерирующую элементы арифметической прогрессии# Программа принимает от пользователя три числа :
# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# Примеры/Тесты:# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map
input_list = [int(el) for el in input().split()]
start, step, quantity = input_list

def subsequence(start: int, step: int, quantity: int) -> list:
    lst = []    
    for item in range(quantity):
        lst.append(start + step * item)        
    return lst

print(subsequence(7,2,5))
print(subsequence(2,3,12))
print(subsequence(start,step,quantity))

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

def subsequence_hard(start: int, step: int, quantity: int) -> list:
    return [ start + step * item for item in range(quantity)]    

print(subsequence_hard(7,2,5))
print(subsequence_hard(2,3,12))
print(subsequence_hard(start,step,quantity))