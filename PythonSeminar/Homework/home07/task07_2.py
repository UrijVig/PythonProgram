# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256

# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36

def print_operation_table(func, num_rows=6, num_columns=6):
    count = 10
    for rows in range(1,num_rows + 1):
        for columns in range(1,num_columns + 1):
            print("%3d" %func(rows,columns), end=' ')
        print()

print()
print("print_operation_table")
print_operation_table(lambda x,y: x**y,4,4)
print()
print_operation_table(lambda x,y: x*y)


# (*) Усложнение. Сформируйте форматированный вывод с номерами строк и столбцов

# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
#        1   2   3   4
#     ----------------
# 1 |    1   1   1   1
# 2 |    2   4   8  16
# 3 |    3   9  27  81
# 4 |    4  16  64 256

# print_operation_table(lambda x,y: x*y)
#        1   2   3   4   5   6
#     ------------------------
# 1 |    1   2   3   4   5   6
# 2 |    2   4   6   8  10  12
# 3 |    3   6   9  12  15  18
# 4 |    4   8  12  16  20  24
# 5 |    5  10  15  20  25  30
# 6 |    6  12  18  24  30  36

def print_operation_table_hard(func, num_rows=6, num_columns=6):
    one_string = "  "
    for columns in range(1,num_columns + 1):
        one_string += str(columns)
    for el in one_string:
        print("%3s" %el, end=' ')   
    print('\n','    '.ljust(len(one_string) * 4 -2,"-"))     
    for rows in range(1,num_rows + 1):
        print("{r:2d} |".format(r = rows),end = '\t')
        for columns in range(1,num_columns + 1):
            print("%3d" %func(rows,columns), end=' ')
        print()

print()
print("print_operation_table_hard")
print_operation_table_hard(lambda x,y: x**y,4,4)
print()
print_operation_table_hard(lambda x,y: x*y)