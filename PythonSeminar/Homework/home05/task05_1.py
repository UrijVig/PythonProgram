# Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def extent_numbers(numbers,extent):
    if extent == 0:
        return 1
    return extent_numbers(numbers,extent - 1) * numbers

num = int(input("Введите число: "))
ex = int(input("Введите степень числа: "))

ex_num = extent_numbers(num,ex)

print(f"{num} в степени {ex} = {ex_num}")
