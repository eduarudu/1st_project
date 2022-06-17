import datetime
from datetime import timedelta
import random
all_receipts = []

class Receipt():
    global all_receipts
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

telev1 = TV('LG', '33', 'линия битых пикселей на матрице')
telev1.name = 'Аттас Елена-Мария Андреевна'

telev2 = TV('Sony', '33', 'нет звука')
telev2.name = 'Картуль Виолетта Викторовна'

telev3 = TV('Panasonic', '33', 'не включается')
telev3.name = 'Микуло Александр Сергеевич'

