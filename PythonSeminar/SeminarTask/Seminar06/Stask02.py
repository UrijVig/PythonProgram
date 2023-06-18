# Дан список, целых чисел.
# Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Функция
# Аргументы: список целых чисел
# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 5]) -> [5]
# <function_name>([1, 5, 1, 6, 1]) -> [5,6]
# <function_name>([7, 5, 1, 6, 8]) -> [8]
# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

def  neibors (lst: list) -> list:
    result_list = []
    for idx in range(len(lst)-1):
        if lst[idx-1] < lst[idx] and lst[idx + 1] < lst[idx]:
            result_list.append(lst[idx])
    idx = len(lst) - 1
    if lst[0] < lst[idx] and lst[idx - 1] < lst[idx]:
        result_list.append(lst[idx])
    return result_list

print(neibors([1, 3, 3, 3, 5]))
print(neibors([1, 5, 1, 6, 1]))
print(neibors([7, 5, 1, 6, 8]))
print(neibors([8, 1, 5, 4, 5]))
