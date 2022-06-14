import datetime
from datetime import timedelta
import random

all_receipts = []

class Receipt():
    global all_receipts
    count_receipts = 0

    def __init__(self):
        self.receipt_number = Receipt.count_receipts
        self.accepted = datetime.date.today()
        self.issued = self.accepted + timedelta(random.randint(1,5))

class Phone(Receipt):
    def __init__(self, brand, operating_system, breakdown, receipt_number, accepted, issued):
        super().__init__(self, receipt_number, accepted, issued)
        self.brand = brand
        self.operating_system = operating_system
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        all_receipts.append(Phone)

    def stat(self):
        st = input("Введите номер сответствующий статусу ремонта. 1 - ремонтируется, 2 - готово, 3 - выдано клиенту: ")
        if st == "1":
            self.status = "repaired"
        if st == "2":
            self.status = "ready"
        if st == "3":
            self.status = "issued"


class Notebook(Receipt):
    def __init__(self, receipt_number, accepted, issued, brand, operating_system, year, breakdown):
        super().__init__(self, receipt_number, accepted, issued)
        self.brand = brand
        self.operating_system = operating_system
        self.year = year
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        Receipt.all_receipts.append(Notebook)

    def stat(self):
        st = input("Введите номер сответствующий статусу ремонта. 1 - ремонтируется, 2 - готово, 3 - выдано клиенту: ")
        if st == "1":
            self.status = "repaired"
        if st == "2":
            self.status = "ready"
        if st == "3":
            self.status = "issued"


class TV(Receipt):
    def __init__(self,  receipt_number, accepted, issued, brand, screen_diagonal, breakdown,):
        super().__init__(self, receipt_number, accepted, issued)
        self.brand = brand
        self.screen_diagonal = screen_diagonal
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        Receipt.all_receipts.append(TV)

    def stat(self):
        st = input("Введите номер сответствующий статусу ремонта. 1 - ремонтируется, 2 - готово, 3 - выдано клиенту: ")
        if st == "1":
            self.status = "repaired"
        if st == "2":
            self.status = "ready"
        if st == "3":
            self.status = "issued"


while True:
    name = input("Введите своё ФИО: ")
    a = input("Введите номер сответствующий вашей техники для ремонта. 1 - телефон, 2 - ноутбук, 3 - телевизор: ")

    if a == "1":
        phone1 = Phone(input("Введите марку телефона: "), input("Укажите операционную систему: "), input('Опишите поломку: '))
        # phone1 = ("LG", "microsoft", "сломан экран")
        product_type = "Phone"
        print(f'номер квитанции: {Phone(Receipt).receipt_number}', f'тип изделия: {product_type}', f'дата приемки: '
              f'{Phone(Receipt).accepted}', f'дата выполнения ремонта: {Phone(Receipt).issued}', f'ФИО заказчика: {name}',
              Phone(Receipt).stat(), f'статус: {Phone(Receipt).status} ', sep="\n")

    if a == "2":
        note1 = Notebook(input("Введите марку ноутбука: "), input("Укажите операционную систему: "),
                         input('Укажите год выпуска: '), input('Опишите поломку: '))
        product_type = "Notebook"
        print(f'номер квитанции: {Notebook(Receipt).receipt_number}', f'тип изделия: {product_type}', f'дата приемки: '
              f'{Notebook(Receipt).accepted}', f'дата выполнения ремонта: {Notebook(Receipt).issued}', f'ФИО заказчика: {name}',
              Notebook(Receipt).stat(), f'статус: {Notebook(Receipt).status} ', sep="\n")


    if a == "3":
        tv1 = TV(input("Введите марку телевизора: "), input("Укажите диагональ экрана: "), input('Опишите поломку: '))
        product_type = "TV"
        print(f'номер квитанции: {TV(Receipt).receipt_number}', f'тип изделия: {product_type}', f'дата приемки: '
              f'{TV(Receipt).accepted}', f'дата выполнения ремонта: {TV(Receipt).issued}', f'ФИО заказчика: {name}',
              TV(Receipt).stat(), f'статус: {TV(Receipt).status} ', sep="\n")

    # else:
    #     print("выбрана несуществующая опция")
    #     a = input("Введите номер сответствующий вашей техники для ремонта. 1 - телефон, 2 - ноутбук, 3 - телевизор: ")


print()