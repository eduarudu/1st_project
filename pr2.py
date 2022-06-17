import datetime
from datetime import timedelta
import random
import receiptsbase

while True:
    options = input("Напишите '1', если вы хотите сдать технику в ремонт или '2', если вы хотите просмотреть информацию: ")
    if options == "1":


        class Receipt():
            count_receipts = 100

            def __init__(self):
                self.name = name
                self.receipt_number = Receipt.count_receipts
                self.accepted = datetime.date.today()
                self.issued = self.accepted + timedelta(random.randint(1,5))

            def stat(self):
                st = input("Введите номер сответствующий статусу ремонта. 1 - ремонтируется, 2 - готово, 3 - выдано клиенту: ")
                if st == "1":
                    self.status = "repaired"
                if st == "2":
                    self.status = "ready"
                if st == "3":
                    self.status = "issued"


        class Phone(Receipt):
            def __init__(self, brand, operating_system, breakdown):
                super().__init__()
                self.brand = brand
                self.technique_type = "Phone"
                self.operating_system = operating_system
                self.breakdown = breakdown
                Receipt.count_receipts += 1
                receiptsbase.all_receipts.append(Phone)


        class Notebook(Receipt):
            def __init__(self, brand, operating_system, year, breakdown):
                super().__init__()
                self.brand = brand
                self.technique_type = "Notebook"
                self.operating_system = operating_system
                self.year = year
                self.breakdown = breakdown
                Receipt.count_receipts += 1
                receiptsbase.all_receipts.append(Notebook)


        class TV(Receipt):
            def __init__(self, brand, screen_diagonal, breakdown):
                super().__init__()
                self.brand = brand
                self.technique_type = "TV"
                self.screen_diagonal = screen_diagonal
                self.breakdown = breakdown
                Receipt.count_receipts += 1
                receiptsbase.all_receipts.append(TV)


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
            print(receiptsbase.all_receipts)
        else:
            pass


    elif options == "2":
        for i in receiptsbase.all_receipts:
            print(Phone.__dict__)
        else:
            print("---")

            ооо







