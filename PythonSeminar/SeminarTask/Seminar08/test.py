import general_task as gen

def test():
    phone_dir = {1: ["Иванов","Иван","+7(xxx)xxx-xx-xx","desription_Иванов"],
            2: ["Петров","Петр","+7(---)xxx-xx-xx","desription_Петров"],
            3: ["Соколов","Илья","+7(---)---------","desription_Соколов"],
            4: ["Павельев","Андрей","+7(***)***-**-**","desription_Павельев"],
            5: ["Пешехов","Антон","+7++++++++++","desription_Пешехов"],
            6: ["Сааков","Илья","+7(+++)+++-++-++","desription_Сааков"]}
    key_count = 6
    print(phone_dir)

    print("\n Проверка ввода пользователя с клавиатуры: ")
    user = gen.input_data()
    phone_dir, key_count = gen.create(phone_dir,key_count, user)

    print("\n Проверка вывода справочника на экран: ")
    gen.print_phone_dir(phone_dir)

    print("\n Проверка экспортирования файда: ")
    file_name = input("выберите имя файла: ")
    gen.export_phone_dir(phone_dir,file_name)

    print("\n Проверка поиска: ")
    searching = input("Введите фамилию или часть фамилии:")
    print("Искомый вами объект хранится под ключом: ", gen.search_user(phone_dir, searching))
    print(phone_dir[gen.search_user(phone_dir, searching)])

    print("\n Проверка функции Update: ")
    searching = input("Введите фамилию или часть фамилии:")
    idc = gen.search_user(phone_dir, searching)
    print(phone_dir[idc])
    gen.update(phone_dir,idc)
    print(phone_dir[idc])

    print("\n Проверка работы, функции удаления поля: ")
    gen.print_phone_dir(phone_dir)
    idc = int(input("Введите номер элемента, который хотите удалить: "))
    phone_dir, key_count = gen.delete(phone_dir, key_count, idc)
    gen.print_phone_dir(phone_dir)

    print("\n Проверка работы, импорта файлов: ")
    gen.print_phone_dir(phone_dir)
    file_name = input("выберите имя файла: ")
    symbol = input("Введите тип разделителя, например # . , или пробел ")
    phone_dir, key_count = gen.import_phone_dir(phone_dir,key_count,file_name, symbol)
    gen.print_phone_dir(phone_dir)