# lesson_3_task_3.py
from mailing import Mailing # Импортируем класс Mailing из файла mailing.py
from address import Address # Импортируем класс Address из файла address.py

# Создаем экземпляр класса Mailing и заполняем его поля
my_mailing = Mailing(
    to_address = Address("123456", "Moscow", "Lenina", "10", "5"), # Адрес получателя
    from_address = Address("654321", "St.Petersburg", "Nevsky", "20", "15"), # Адрес отправителя
    cost = 100, # Стоимость
    track = "RU1234567890" # Трек-номер
)

# Распечатываем в консоль отправление в формате: Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
print(f"Отправление {my_mailing.track} из {my_mailing.from_address.index}, {my_mailing.from_address.city}, {my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} в {my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.street}, {my_mailing.to_address.house} - {my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей.")
