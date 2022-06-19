from receiptsbase import Phone, Notebook, TV
from receiptsbase import all_receipts

p1 = Phone('Щуревич Виктория Геннадьевна', "LG", 'android', 'сломан экран')
p1.status = "repaired"

p2 = Phone('Мурашко Юлия Сергеевна', "Lenovo", 'android', 'сломано гнездо для зарядки')
p2.status = "issued"

p3 = Phone('Рачинский Павел Игоревич', "Xiaomi", 'android', 'не работает камера')
p3.status = "ready"

n1 = Notebook('Аттас Елена-Мария Андреевна', 'Aser', 'Windows', '1994', 'ремонт кулера в ноутбуке')
n1.status = "issued"

n2 = Notebook('Былино Константин Сергеевич', 'Lenovo', 'Windows', '2015', 'ремонт материнской платы')
n2.status = "ready"

n3 = Notebook('Картуль Виолетта Викторовна', 'Apple', 'Mac OS', '2020', 'замена северного моста')
n3.status = "repaired"

t1 = TV('Аттас Елена-Мария Андреевна', 'LG', '33', 'линия битых пикселей на матрице')
t1.status = "issued"

t2 = TV('Картуль Виолетта Викторовна', 'Sony', '33', 'нет звука')
t2.status = "ready"

t3 = TV('Микуло Александр Сергеевич', 'Panasonic', '33', 'не включается')
t3.status = "repaired"



a = input("a=")
if a == "0":
    for i in all_receipts:
        print(i)
else:
    pass

while True:
    options = input("Напишите '1', если вы хотите сдать технику в ремонт или '2', если вы хотите просмотреть информацию: ")
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
        a = input("Введите номер квитанции или ФИО: ")
        for i in all_receipts:
            for key, value in i.items():
                for p in i.values():
                    if p == a:
                        print(key, ":", value)

    # elif options == "2":
    #     a = input("Введите номер квитанции или ФИО: ")
    #     for i in all_receipts:
    #         for key, value in i.items():
    #             for p in i.values():
    #                 if p == a:
    #                     n = i["ФИО заказчика"]
    #                     if p == n:
    #                         print(key, ":", value)












