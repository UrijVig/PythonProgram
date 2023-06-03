# Пользователь вводит одно число N – количество арбузов.
# Затем пользователь последовательно вводит массы соответсвующих арбузов
# Необходимо вывести на экран массы самого тяжелого и самого легкого арбузов

num = int(input('Введите количество арбузов: '))

max_kg=0
min_kg=999999

for i in range(num):
    watermelonMass = int(input('Введите массу арбуза:'))
    if watermelonMass
        max_kg:
        max_kg=watermelonMass
    if watermelonMass<min_kg:
       min_kg=watermelonMass
    
print(f"Массы арбузов: min={min_kg}, max={max_kg}") 
