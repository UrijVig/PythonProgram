# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.

# list1 = []
# print("Пожалуйста заполните список, чтобы прекратить заполнение введите end")

# while True:    #Цикл ввода списка с клавиатуры.
#     data = input()
#     if data == "end":       
#         break
#     else:       
#         list1.append(int(data))

list1 = [10, 7, 3, 3, 2, 7, 3, 8]

print(list1)

k = int(input("Пожалуйста, введите искомое число: "))

list2 = [i - k for i in list1]

for i in range(len(list2)): 
    if list2[i] < 0: list2[i] *= -1
    
print(f"Самое близкое число к {k} это {list1[list2.index(min(list2))]}")

res = {list1[i] for i in range(len(list1)) if min(list2) == list2[i]}

        
print(f"Самые близкие числа к искомому: {res}")
