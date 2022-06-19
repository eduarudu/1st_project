import datetime
from datetime import timedelta
from receiptsbase import Phone, Notebook, TV, Admin
from receiptsbase import all_receipts, all_admins

p1 = Phone('Щуревич Виктория Геннадьевна', "LG", 'android', 'сломан экран')
p2 = Phone('Мурашко Юлия Сергеевна', "Lenovo", 'android', 'сломано гнездо для зарядки')
p3 = Phone('Рачинский Павел Игоревич', "Xiaomi", 'android', 'не работает камера')
n1 = Notebook('Аттас Елена-Мария Андреевна', 'Aser', 'Windows', '1994', 'ремонт кулера в ноутбуке')
n2 = Notebook('Былино Константин Сергеевич', 'Lenovo', 'Windows', '2015', 'ремонт материнской платы')
n3 = Notebook('Картуль Виолетта Викторовна', 'Apple', 'Mac OS', '2020', 'замена северного моста')
t1 = TV('Аттас Елена-Мария Андреевна', 'LG', '33', 'линия битых пикселей на матрице')
t2 = TV('Картуль Виолетта Викторовна', 'Sony', '33', 'нет звука')
t3 = TV('Микуло Александр Сергеевич', 'Panasonic', '33', 'не включается')

admn1 = Admin('GuruCo', 'Splash459', 'Синицкий Павел Константинович')
admn2 = Admin('elena_gudzima', 'operamyall_94', 'Аттас Елена-Мария Андреевна')
admn3 = Admin('nyashmyash', 'Pepe1010', 'Былино Константин Сергеевич')
admn4 = Admin('TeaCup', 'cocoaCUP', 'Картуль Виолетта Викторовна')
admn5 = Admin('wetItalian', 'bringmeaPIE', 'Микуло Александр Сергеевич')
admn6 = Admin('0', '0', '0')

def show_receipts():
    a = input("Введите номер квитанции или ФИО: \n")
    for i in all_receipts:
        for key, value in i.items():
            for p in i.values():
                if p == a:
                    print(key, ":", value)

    # a = input("Введите номер квитанции или ФИО: ")
    # for i in all_receipts:
    #     for key, value in i.items():
    #         if  i["номер квитанции"] == a:
    #             a = i["ФИО заказчика"]
    #             for p in i.values():
    #                 if p == a:
    #                     print(key, ":", value)

def show_admins():
    print('Список всех адмиистраторов:\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯')
    for i in all_admins:
        for key, value in i.items():
            if key == "ФИО":
                print(value)

def del_admin():
    n = input("Введите ФИО администратора для удаления: ")
    for i in all_admins:
        if i["ФИО"] == n:
            del i
            print("администратор удалён")
    print(" ")
    show_admins()

# a = input("a=")
# if a == "0":
#     for i in all_receipts:
#         print(i)
# else:
#     pass
#
# for i in all_admins:
#     print(i)

while True:
    options = input("Напишите:\n'1', если вы хотите сдать технику в ремонт\n'2', если вы хотите просмотреть информацию\n"
                    "'3', чтобы зайти в администраторскую панель\n---------------------------------------------\n")
    if options == "1":


        name = input("Введите своё ФИО: ")
        a = input("Введите номер сответствующий вашей техники для ремонта. 1 - телефон, 2 - ноутбук, 3 - телевизор: ")


        if a == "1":
            phone1 = Phone(name, input("Введите марку телефона: "), input("Укажите операционную систему: "), input('Опишите поломку: '))
            print(f'номер квитанции: {phone1.receipt_number}', f'тип изделия: {phone1.technique_type}', f'дата приемки: '
                  f'{phone1.accepted}', f'дата выполнения ремонта: {phone1.issued}', f'ФИО заказчика: {phone1.name}',
                  phone1.stat(), f'статус: {phone1.status} ', sep="\n")
            print("--------------------------------------------------------------------------------------------")


        if a == "2":
            note1 = Notebook(name, input("Введите марку ноутбука: "), input("Укажите операционную систему: "),
                             input('Укажите год выпуска: '), input('Опишите поломку: '))
            print(f'номер квитанции: {note1.receipt_number}', f'тип изделия: {note1.technique_type}', f'дата приемки: '
                  f'{note1.accepted}', f'дата выполнения ремонта: {note1.issued}', f'ФИО заказчика: {note1.name}',
                  note1.stat(), f'статус: {note1.status} ', sep="\n")
            print("--------------------------------------------------------------------------------------------")


        if a == "3":
            tv1 = TV(name, input("Введите марку телевизора: "), input("Укажите диагональ экрана: "), input('Опишите поломку: '))
            print(f'номер квитанции: {tv1.receipt_number}', f'тип изделия: {tv1.technique_type}', f'дата приемки: '
                  f'{tv1.accepted}', f'дата выполнения ремонта: {tv1.issued}', f'ФИО заказчика: {tv1.name}',
                  tv1.stat(), f'статус: {tv1.status} ', sep="\n")
            print("--------------------------------------------------------------------------------------------")

        else:
            pass


    elif options == "2":

        show_receipts()
        print(" ")


    elif options == "3":
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        for i in all_admins:
            if i['логин'] == login and i['пароль'] == password:
                print(" ")
                action = input("Выберите действие:\n'1' - Действия с админами\n'2' - Действия с квитанциями"
                               "\n---------------------------------------------\n")

                if action == "1":
                    action_1 = input("Следующее действие:\n'1' - отобразить список всех админов\n'2' - удалить админа из списка"
                                     "\n'3' - добавить нового админа\n---------------------------------------------\n")

                    if action_1 == "1":
                        show_admins()
                        print(" ")

                    if action_1 == "2":
                        del_admin()
                        print(" ")

                    if action_1 == "3":
                        admin = Admin(input('Придумайте свой логин: '), input('Придумайте свой пароль: '), input('Укажите своё ФИО: '))
                        print('⌢⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢  новый администратор создан  ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ \n')

                if action == "2":
                    action_2 = input("Следующее действие:\n'1' - изменить статус ремонта\n'2' - изменить дату выполнения ремонта"
                                     "\n'3' - посмотреть информацию о квитанции\n---------------------------------------------\n")

                    if action_2 == "1":
                        number = input('Введите номер квитанции: ')
                        for i in all_receipts:
                            if i["номер квитанции"] == number:
                                st = input(
                                    "Введите номер сответствующий статусу ремонта. 1 - ремонтируется, 2 - готово, 3 - выдано клиенту: ")
                                if st == "1":
                                    i["статус"] = "ремонтируется"
                                if st == "2":
                                    i["статус"] = "готово"
                                if st == "3":
                                    i["статус"] = "выдано клиенту"
                                print('⌢⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢  статус изменён  ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ \n')

                    if action_2 == "2":
                        number = input('Введите номер квитанции: ')
                        for i in all_receipts:
                            if i["номер квитанции"] == number:
                                print('дата приёмки: ', i['дата приёмки'])
                                print('установленная дата выполнения ремонта: ', i['дата выполнения ремонта'])
                                i["дата выполнения ремонта"] = datetime.date.today() + timedelta(days = int(input("введите "
                                    "количетво дней, через которое заказ будет выполнен, начиная с сегодня = ")))
                                print(f'⌢⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢  дата изменена  ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ ⌣⌢ \nНовая дата выполнения ремонта = {i["дата выполнения ремонта"]}\n')

                    if action_2 == "3":
                        show_receipts()
                        print(" ")
            # else:
            #     print('░░░░░░░ неверный логин или пароль ░░░░░░░ \n')
            #     break