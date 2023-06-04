# Дана строка, состоящая из слов. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Слово не зависит от регистра написания букв.
# Определите, сколько различных слов содержится в этом тексте.

# Примеры/Тесты:

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. 
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 14

# Input: Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
# Curabitur a tellus ut arcu gravida porta eget a lacus. Curabitur ornare varius turpis, ultricies mollis sem convallis in. 
# Nunc scelerisque lacinia risus sit amet aliquam.
# Output: 31

input_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

dict1 = set(input_string.upper().split()) 
dict2 = set(input_string.split()) 

print(f"Без учёта регистра: {len(dict1)}")
print(f"С учётом регистра: {len(dict2)}")
