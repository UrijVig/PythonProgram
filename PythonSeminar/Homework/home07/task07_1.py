# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# Примечание.
# Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.

def vowels_cont(data) -> int:
    vowels = {'а','у','е','ы','о','э','я','и','ю'}
    count = 0
    for el in data:
        if el in vowels: count += 1
    return count

def pryme_check(string) -> bool:
    data = list(string.split())
    for idx in range(len(data)):
        if vowels_cont(data[idx]) != vowels_cont(data[idx - 1]):
            return False
    return True

print("Основное решение: \n")
print(pryme_check("пара-ра-рам рам-пам-папам па-ра-па-дам"))
print(pryme_check("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
print(pryme_check("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
print(pryme_check("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
print(pryme_check("Пам-парам-пурум Пум-пурум-карам"))

# (*) Усложнение.
# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. Эта информация возвращается в виде списка словарей. 
# Каждый элемент списка(словарь) соответствует фразе.

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

def vowels_cont_hard(data) -> int:
    vowels = {'а','у','е','ы','о','э','я','и','ю'}
    count = 0
    for el in data:
        if el in vowels: count += 1
    return count

def counter_vowels(data) -> list:
    vowels = {'а','у','е','ы','о','э','я','и','ю'}
    vowels_in_data = list()
    for idx in range(len(data)):
        vowels_in_data.append([element for element in data[idx] if element in vowels])
    count_vowels = list()
    for item in vowels_in_data:
        set_vowels = set(item)
        count_list = list()
        for el in set_vowels:
            count_list.append(item.count(el))
        count_vowels.append(dict(zip(set_vowels, count_list)))
    return count_vowels
        
    
    
def pryme_check_hard(string, flag = True):    
    data = list(string.split())
    if flag:
        return f"({pryme_check_hard(string, False)}, {counter_vowels(data)})"
    else:        
        for idx in range(len(data)):
            if vowels_cont(data[idx]) != vowels_cont(data[idx - 1]):
                return False
        return True
print("\nРешение усложнённого задания: \n ")
print(pryme_check_hard("пара-ра-рам рам-пам-папам па-ра-па-дам", False))
print(pryme_check_hard("пара-ра-рам рам-пум-пупам па-ре-по-дам", True))
print(pryme_check_hard("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
print(pryme_check_hard("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
print(pryme_check_hard("Пам-парам-пурум Пум-пурум-карам"))