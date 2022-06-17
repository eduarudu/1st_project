import datetime
from datetime import timedelta
import random
all_receipts = []


class Receipt():
    count_receipts = 100

    def __init__(self):
        self.name = "name"
        self.receipt_number = Receipt.count_receipts
        self.accepted = datetime.date.today()
        self.issued = self.accepted + timedelta(random.randint(1, 5))

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
        all_receipts.append(Phone)


class Notebook(Receipt):
    def __init__(self, brand, operating_system, year, breakdown):
        super().__init__()
        self.brand = brand
        self.technique_type = "Notebook"
        self.operating_system = operating_system
        self.year = year
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        all_receipts.append(Notebook)


class TV(Receipt):
    def __init__(self, brand, screen_diagonal, breakdown):
        super().__init__()
        self.brand = brand
        self.technique_type = "TV"
        self.screen_diagonal = screen_diagonal
        self.breakdown = breakdown
        Receipt.count_receipts += 1
        all_receipts.append(TV)