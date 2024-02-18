# mailing.py
from address import Address # Импортируем класс Address из файла address.py

class Mailing:
    """Класс, представляющий почтовое отправление"""

    def __init__(self, to_address, from_address, cost, track):
        """Конструктор, принимающий адрес получателя, адрес отправителя, стоимость и трек-номер"""
        self.to_address = to_address # Тип данных Address
        self.from_address = from_address # Тип данных Address
        self.cost = cost # Тип данных число
        self.track = track # Тип данных строка
