import general_task as gen

def menu ():
    key_count = 0
    phone_dir = dict()
    print("Введите 0 если хотите завершить программу!")
    print("Введите 1 если хотите ввести нового пользователя. ")
    print("Введите 2 если хотите распечатать справочник. ")
    print("Введите 3 если хотите экспортировать файл. ")
    print("Введите 4 для поиска. ")
    print("Введите 5 для редактирования записи. ")
    print("Введите 6 для удаления записи. ")
    print("Введите 7 для импорта файла. ")
    while (True):
        number = int(input("Введите операцию "))
        if number == 0: break
        if number == 1:
            user = gen.input_data()
            phone_dir, key_count = gen.create(phone_dir,key_count, user)
        if number == 2:
            gen.print_phone_dir(phone_dir)
        if number == 3:
            file_name = input("выберите имя файла: ")
            gen.export_phone_dir(phone_dir,file_name)
        if number == 4:
            searching = input("Введите фамилию или часть фамилии:")
            print("Искомый вами объект хранится под ключом: ", gen.search_user(phone_dir, searching))
        if number == 5:
            searching = input("Введите фамилию или часть фамилии:")
            idc = gen.search_user(searching)
            print(phone_dir[idc])
            gen.update(phone_dir,idc)
        if number == 6:
            idc = int(input("Введите номер элемента, который хотите удалить: "))
            phone_dir, key_count = gen.delete(phone_dir, key_count, idc)
        if number == 7:
            file_name = input("выберите имя файла: ")
            symbol = input("Введите тип разделителя, например # . , или пробел ")
            phone_dir, key_count = gen.import_phone_dir(phone_dir,key_count,file_name, symbol)