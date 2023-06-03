# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# Затем пользователь последовательно вводит температуру для каждого дня. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Необходимо вычислить длительность самой длинной оттепели

num = int(input('Введите число N: '))

maxStrik=0
currentStrik=0
currentTemp=0

for i in range(num):
    currentTemp = int(input('введите температуру:'))
    if currentTemp>0:
        currentStrik+=1
    else:
        currentStrik=0
    if currentStrik>maxStrik:
        maxStrik=currentStrik

print(maxStrik)
