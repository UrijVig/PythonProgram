# Даны два списка чисел. Требуется вывести те элементы первого списка , которых нет во втором списке.
# Создайте функцию.
# Аргументы: два списка целых чисел
# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

list_1 = [3, 4, 1, 5, 1, 3, 10, 4, 9, 5]
list_2 = [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]

def defference_list(lst1: list, lst2: list) -> list:
    set_lst1 = set(lst1)
    set_lst2 = set(lst2)
    return list (set_lst1.difference(set_lst2))
    
print(defference_list(list_1, list_2))

# [*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений
# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]

def defference_list_hard(lst1: list, lst2: list) -> list:
    set_lst2 = set(lst2)
    result_list = []
    for item in lst1:
        if item not in set_lst2:
            result_list.append(item)
    return result_list;

print(defference_list_hard(list_1, list_2))
