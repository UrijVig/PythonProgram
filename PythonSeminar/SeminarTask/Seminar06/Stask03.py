# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.

# Напишите функцию
# Аргументы: список целых чисел
# Возвращает: кол-во пар

# Примеры/Тесты:
# <function_name>([1, 2, 3, 2, 3]) -> 2
# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

# def count_pairs(lst: list):
#     count = 0
#     for idx in range(len(lst)):
#         for j_idx in range(idx + 1, len(lst)):
#             if lst[idx] == lst[j_idx]:
#                 count += 1
#     return count

def count_pairs(lst: list):
    count = 0
    for idx in range(len(lst)):
        count += lst[idx +1:].count(lst[idx])
    return count

print(count_pairs([1, 2, 3, 2, 3, 3, 2, 4]))
print(count_pairs([1, 2, 3, 2, 3]))
