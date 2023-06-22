# Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО

# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич

# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович

# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием

# os.path и pathlib

import os.path as path1
# from os import getcwd 
# print(getcwd())

MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR,"data", "data1.txt")

list_data = list()

with open (file_name, "r", encoding="utf-8") as data:
    for line in data:
        # print(*line.strip().split("#"))
        last_name, first_name, parent = line.strip().split("#")
        print(last_name, first_name, parent)
        list_data.append([last_name, first_name, parent])


print(list_data)

