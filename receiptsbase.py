import datetime
from datetime import timedelta
import random
all_receipts = []
all_admins = []

class Receipt():

    count_receipts = 100

    def __init__(self, name):
        self.name = name
        self.receipt_number = str(Receipt.count_receipts)
        self.accepted = datetime.date.today()
        self.issued = self.accepted + timedelta(random.randint(1, 5))
        self.status = 'не определён'

    def stat(self):
        st = input("Введите номер сответствующий статусу ремонта. 1 - ремонтируется, 2 - готово, 3 - выдано клиенту: ")
        if st == "1":
            self.status = "ремонтируется"
        if st == "2":
            self.status = "готово"
        if st == "3":
            self.status = "выдано клиенту"


class Phone(Receipt):
    def __init__(self, name, brand, operating_system, breakdown):
        super().__init__(name)
        self.brand = brand
        self.technique_type = "Phone"
        self.operating_system = operating_system
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        phone_dict = {'номер квитанции': self.receipt_number, 'тип изделия': self.technique_type,
                   'дата приёмки': self.accepted, 'дата выполнения ремонта': self.issued, 'ФИО заказчика': self.name,
                   'статус': self.status}
        all_receipts.append(phone_dict)


class Notebook(Receipt):
    def __init__(self, name, brand, operating_system, year, breakdown):
        super().__init__(name)
        self.brand = brand
        self.technique_type = "Notebook"
        self.operating_system = operating_system
        self.year = year
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        notebook_dict = {'номер квитанции': self.receipt_number, 'тип изделия': self.technique_type,
                      'дата приёмки': self.accepted, 'дата выполнения ремонта': self.issued, 'ФИО заказчика': self.name,
                      'статус': self.status}
        all_receipts.append(notebook_dict)


class TV(Receipt):
    def __init__(self, name, brand, screen_diagonal, breakdown):
        super().__init__(name)
        self.brand = brand
        self.technique_type = "TV"
        self.screen_diagonal = screen_diagonal
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        tv_dict = {'номер квитанции': self.receipt_number, 'тип изделия': self.technique_type,
                         'дата приёмки': self.accepted, 'дата выполнения ремонта': self.issued,
                         'ФИО заказчика': self.name, 'статус': self.status}
        all_receipts.append(tv_dict)


class Admin():
    def __init__(self, login, password, name):
        self.login = login
        self.password = password
        self.name = name
        admin_dict = {'логин': self.login, 'пароль': self.password, 'ФИО': self.name}
        all_admins.append(admin_dict)