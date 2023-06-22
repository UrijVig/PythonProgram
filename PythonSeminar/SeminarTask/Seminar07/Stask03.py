# Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# преобразовать его в списки вида
# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]

# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П

import os.path as path1

MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR,"data", "data1.txt")

list_data = list()

with open (file_name, "r", encoding="utf-8") as data:
    for line in data:
        # last_name, first_name, parent = line.strip().split("#")
        list_data.append(line.strip().split("#"))

# list_data_1 = [f"{last_name} {first_name[0]}.{parent[0]}." for last_name, first_name, parent in list_data]
# print(list_data_1)
# list_data_2 = [f"{last_name}-{first_name[0]}-{parent[0]}" for last_name, first_name, parent in list_data]
# print(list_data_2)

# def rework(lst: list,space = ' ',point = '.',end_symvol = '.') -> str:
#     last_name, first_name, parent = lst
#     return f"{last_name}{space}{first_name[0]}{point}{parent[0]}{end_symvol}"

# list_data_1 = [rework(item) for item in list_data]
# print(list_data_1)
# list_data_2 = [rework(item,"-", "-","") for item in list_data]
# print(list_data_2)

list_data_1 = list(map(lambda item: f"{item[0]} {item[1][0]}.{item[2][0]}.", list_data))
print(list_data_1)
list_data_2 = list(map(lambda item: f"{item[0]}-{item[1][0]}-{item[2][0]}", list_data))
print(list_data_2)

list_data_1 = [f"{last_name} {first_name[0]}.{parent[0]}." for last_name, first_name, parent in list_data if last_name[0] == "П" or first_name[0]  == "П" or parent[0] == "П" ]
print(list_data_1)
