# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def entry_check(lst: list, left: int, right: int ) -> list:
    result = []
    for idx in range(len(lst)):
        if left <= lst[idx] <= right:
            result.append(idx)
    return result

print(" entry_check")
print(entry_check(lst1, 2, 10))
print(entry_check(lst1, 2, 9))
print(entry_check(lst1, 0, 6))

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
def entry_check_hard(lst: list, left: int, right: int ) -> list:
    return [idx for idx in range(len(lst)) if left <= lst[idx] <= right ]

print("\n entry_check_hard")
print(entry_check_hard(lst1, 2, 10))
print(entry_check_hard(lst1, 2, 9))
print(entry_check_hard(lst1, 0, 6))

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

def entry_check_very_hard(lst: list, left: int, right: int ) -> list:
    return [(idx,lst[idx]) for idx in range(len(lst)) if left <= lst[idx] <= right ]    

print("\n entry_check_very_hard")
print(entry_check_very_hard(lst1, 2, 10))
print(entry_check_very_hard(lst1, 2, 9))
print(entry_check_very_hard(lst1, 0, 6))