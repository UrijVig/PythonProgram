import os.path as path1

def input_data() -> list:
    user = []
    user.append(input("Введите фамилию: "))
    user.append(input("Введите имя: "))
    user.append(input("Введите номер телефона: "))
    user.append(input("Введите описание: "))
    return user

def create(phone_dir_local: dict, idc: int, user: list) -> dict:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = path1.abspath(path1.dirname(__file__))
    fule_name = path1.join(MAIN_DIR, file_name + ".txt")
    with open(fule_name, mode='w', encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f"{user[0]} {user[1]} {user[2]} {user[3]} {idc}\n")

def search_user(phone_dir: dict, searching: str) ->int:
    for idc, user in phone_dir.items():        
        if user[0].startswith(searching):
            return idc
        
def print_phone_dir(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}: {user[0]} {user[1]} {user[2]} {user[3]}")

def update(phone_dir_local: dict,idc: int) -> dict:
    print("Введите отредактированное поле (без запятых, через пробелы)")
    user = [el for el in input().split()]
    phone_dir_local[idc] = user
    return phone_dir_local

def delete(phone_dir_local: dict,key_count_local: int, idc: int) -> dict:    
    for idx in phone_dir_local.keys():        
        if idx < key_count_local and idx >= idc:
            phone_dir_local[idx] = phone_dir_local[idx + 1]
    phone_dir_local.pop(key_count_local)
    key_count_local -= 1
    return phone_dir_local, key_count_local

def import_phone_dir(phone_dir_local: dict,key_count_local: int, file_name: str, sym: str):
    MAIN_DIR = path1.abspath(path1.dirname(__file__))
    fule_name = path1.join(MAIN_DIR, file_name + ".txt")
    with open(fule_name, mode='r+', encoding='utf-8') as file:
        for line in file:
            user = line.strip().split(sym)
            phone_dir_local, key_count_local = create(phone_dir_local, key_count_local,user)
    return phone_dir_local, key_count_local
