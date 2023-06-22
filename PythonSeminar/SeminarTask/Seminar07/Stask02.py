# Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.

# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.

# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И

# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?

import os.path as path1

MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR,"data", "data1.txt")

list_data = list()

with open (file_name, "r", encoding="utf-8") as data:
    for line in data:
        # last_name, first_name, parent = line.strip().split("#")
        list_data.append(line.strip().split("#"))

# print(list_data)

file_name_two = path1.join(MAIN_DIR, "results", "Names.txt")

with open(file_name_two, mode = "wt", encoding="utf-8") as resul_file:
    for last_name, first_name, parent in list_data:    
        string = f"{last_name} {first_name[0]}.{parent[0]}."
        resul_file.write(string + "\n")

def name_file() -> str:
    return input("Введите желаемое имя файла (без расширения): ") + ".txt"

file_name_two = path1.join(MAIN_DIR, "results", name_file())
with open(file_name_two, mode = "wt", encoding="utf-8") as resul_file:
    space = str(input("Введите разделитель между фамилией и инициалами: "))
    point = str(input("Введите разделительмежду инициалами: "))
    end_symvol = str(input("Введите символ, закрывающий строку: "))
    for last_name, first_name, parent in list_data:
        string = f"{last_name}{space}{first_name[0]}{point}{parent[0]}{end_symvol}"
        resul_file.write(string + "\n")