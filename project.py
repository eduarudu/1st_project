from receiptsbase import Phone, Notebook, TV
from receiptsbase import all_receipts

p1 = Phone("LG", 'android', 'сломан экран')
p1.name = 'Щуревич Виктория Геннадьевна'

p2 = Phone("Lenovo", 'android', 'сломано гнездо для зарядки')
p2.name = 'Мурашко Юлия Сергеевна'

p3 = Phone("Xiaomi", 'android', 'не работает камера')
p3.name = 'Рачинский Павел Игоревич'

n1 = Notebook('Aser', 'Windows', '1994', 'ремонт кулера в ноутбуке')
n1.name = 'Аттас Елена-Мария Андреевна'

n2 = Notebook('Lenovo', 'Windows', '2015', 'ремонт материнской платы')
n2.name = 'Былино Константин Сергеевич'

n3 = Notebook('Apple', 'Mac OS', '2020', 'замена северного моста')
n3.name = 'name'

t1 = TV('LG', '33', 'линия битых пикселей на матрице')
t1.name = 'Аттас Елена-Мария Андреевна'

t2 = TV('Sony', '33', 'нет звука')
t2.name = 'Картуль Виолетта Викторовна'

t3 = TV('Panasonic', '33', 'не включается')
t3.name = 'Микуло Александр Сергеевич'

for i in all_receipts:
    print(i)

while True:
    options = input("Напишите '1', если вы хотите сдать технику в ремонт или '2', если вы хотите просмотреть информацию: ")
    if options == "1":


        name = input("Введите своё ФИО: ")
        a = input("Введите номер сответствующий вашей техники для ремонта. 1 - телефон, 2 - ноутбук, 3 - телевизор: ")


        if a == "1":
            phone1 = Phone(input("Введите марку телефона: "), input("Укажите операционную систему: "), input('Опишите поломку: '))
            phone1.name = name
            print(f'номер квитанции: {phone1.receipt_number}', f'тип изделия: {phone1.technique_type}', f'дата приемки: '
                  f'{phone1.accepted}', f'дата выполнения ремонта: {phone1.issued}', f'ФИО заказчика: {phone1.name}',
                  phone1.stat(), f'статус: {phone1.status} ', sep="\n")
            print("--------------------------------------------------------------------------------------------")


        if a == "2":
            note1 = Notebook(input("Введите марку ноутбука: "), input("Укажите операционную систему: "),
                             input('Укажите год выпуска: '), input('Опишите поломку: '))
            note1.name = name
            print(f'номер квитанции: {note1.receipt_number}', f'тип изделия: {note1.technique_type}', f'дата приемки: '
                  f'{note1.accepted}', f'дата выполнения ремонта: {note1.issued}', f'ФИО заказчика: {note1.name}',
                  note1.stat(), f'статус: {note1.status} ', sep="\n")
            print("--------------------------------------------------------------------------------------------")


        if a == "3":
            tv1 = TV(input("Введите марку телевизора: "), input("Укажите диагональ экрана: "), input('Опишите поломку: '))
            tv1.name = name
            print(f'номер квитанции: {tv1.receipt_number}', f'тип изделия: {tv1.technique_type}', f'дата приемки: '
                  f'{tv1.accepted}', f'дата выполнения ремонта: {tv1.issued}', f'ФИО заказчика: {tv1.name}',
                  tv1.stat(), f'статус: {tv1.status} ', sep="\n")
            print("--------------------------------------------------------------------------------------------")

        else:
            pass

        a = input("a=")
        if a == "1":
            print(all_receipts)
        else:
            pass


    elif options == "2":
        pass








