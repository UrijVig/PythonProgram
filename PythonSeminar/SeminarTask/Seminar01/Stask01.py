# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

m = int(input("Введите общее количество километров: "))
n = int(input("Введите максимальное расстояние в день: "))

# day = (m//n) + int(bool(m % n))
# day = (m + n - 1) // n 
day = -(-m//n)

print(f'Необходимо {day} дней')