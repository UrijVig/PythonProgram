# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

num = int(input('Введите количество монет: '))

eagle = 0
tails = 0

for i in range(num):
    position = int(input('Введите положение монеты 0 - решка, 1 - орёл: '))
    if position == 0: 
        tails += 1
    if position == 1: 
        eagle += 1

if tails < eagle: 
    print(f"Нужно перевернуть {tails} монеток")
else: 
    print(f"Нужно перевернуть {eagle} монеток")
