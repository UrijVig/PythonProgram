explorer - открыть проводник
shutdown -r -t 0 - перезагрузка компа
dpiscaling - параметры экрана

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Примеры/Тесты:
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Input: a b c d a a a a a a a
# Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7
# Строку не обязательно вводить с клавиатуры

string = "aaabcaadcdd"
new_string = ""

for i in string:
    count = 0
    if i not in new_string:
        new_string += (i + " ")
    else:
        for j in new_string:
            if i == j:
                count+= 1
        new_string +=  (f"{i}_{count} ")

print(new_string)

####################################################

new_string = ""
for idx, val in enumerate(string):
    n = string[0:idx].count(val)
    if n > 0 :
        new_string +=  (f"{val}_{n} ")
    else:
        new_string += (val + " ")
        
print(new_string)

####################################################

new_list = []
for idx, val in enumerate(string):
    n = string[0:idx].count(val)
    new_list.append(f"{val}_{n}" if n > 0 else val)
    
print(" ".join(new_list))

####################################################

new_list.clear()
new_dict = dict()
for idx, val in enumerate(string):
    if val in new_dict.keys():
        new_dict[val] += 1
        new_list.append(f"{val}_{new_dict[val]}")
    else:
        new_dict[val] = 0
        new_list.append(val)

print(" ".join(new_list))









