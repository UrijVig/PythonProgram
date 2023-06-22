# Напишите функцию same_by(func, objects)
# которая проверяет, все ли элементы в objects дают одинаковое значение характеристики func

# Аргументы:
# func - функция одного аргумента.
# objects - список или кортеж

# Возвращаемое значение:
# - Если objects пустой, вернуть None
# - Если все элементы в objects дают одинаковое значение func, вернуть True, иначе вернуть False

# Примеры/Тесты:
# same_by(lambda x: x % 2, [1, 2, 10, 12]) -> False
# same_by(lambda x: x % 2, [0, 2, 10, 12]) -> True
# same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]) -> True
# same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
# same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
# same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> True
# same_by(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> False
# same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]) -> True

def same_by(func, objects):
    if len(objects) == 0: return None
    for idx in range(len(objects)):
        if func(objects[idx]) != func(objects[idx - 1]): return False
    return True
print(same_by(lambda x: x % 2, [1, 2, 10, 12]))
print(same_by(lambda x: x % 2, [0, 2, 10, 12]))
print(same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]))
print(same_by(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]))
print(same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]))

# [*] Усложнение. Не используйте цикл в функции

def some_by_hard(func, objects):
    if len(objects) == 0: return None
    flag = func(objects[0])
    result = list(filter(lambda item: func(item) != flag, objects))
    if len(result) != 0: return False
    return True

print('\n',some_by_hard(lambda x: x % 2, [1, 2, 10, 12]))
print(some_by_hard(lambda x: x % 2, [0, 2, 10, 12]))
print(some_by_hard(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]))
print(some_by_hard(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]))
print(some_by_hard(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]))
print(some_by_hard(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]))
print(some_by_hard(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]))
print(some_by_hard(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]))





