class Address:
    """Класс, представляющий адрес"""

    def __init__(self, index, city, street, house, apartment):
        """Конструктор, принимающий индекс, город, улицу, дом и квартиру"""
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
