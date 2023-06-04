#  Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.

# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.

# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

def rework_list(lst):
    for i in range(len(lst)):
        if lst[i] == 5:
            lst[i] = 1
    return lst
    
# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
    
def rework_list_app1(lst):
    flag = True
    for i in range(len(lst)):
        if lst[i] == 5:
            lst[i] = 1
            flag = False
    if flag:
        return None
    return lst

# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.

# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

def rework_list_app2(lst,key = 'enemy'):
    if key == "friend":
        for i in range(len(lst)):
            if lst[i] <= 2: 
                lst[i] = 5
        return lst
    else:
        for i in range(len(lst)):
            if lst[i] == 5: 
                lst[i] = 1
        return lst
    

list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
list_1 = rework_list(list_1)

print(list_1)

list_1 = [1, 3, 3, 3, 4, 2, 4, 3, 2]
list_1 = rework_list_app1(list_1)

print(list_1)

list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
list_1 = rework_list_app2(list_1,'friend')

print(list_1)

list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
list_1 = rework_list_app2(list_1)

print(list_1)
