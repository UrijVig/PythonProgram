list01 = []print("Пожалуйста заполните список, чтобы прекратить заполнение введите end")

while True:    
    data = input()
    if data == "end":      
        break
    else:       
        list01.append(int(data))
list02 = []

for i in list01:    count = 0
    for j in list02:
        if i == j:           
            count += 1
    if count < 1:        
        list02.append(i)

print(f"В списке {len(list02)} ")

list02 = []
for i in list01:   
    if i not in list02:
        list02.append(i)
        
print(f"В списке {len(list02)} ")

print(len(set(list01)))
