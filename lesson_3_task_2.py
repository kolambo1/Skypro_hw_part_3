# lesson_3_task_2.py
from smartphone import Smartphone # Импортируем класс Smartphone из файла smartphone.py

catalog = [] # Создаем пустой список
# Добавляем пять разных экземпляров класса Smartphone в список
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 12", "+79234567890"))
catalog.append(Smartphone("Huawei", "P40", "+79345678901"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79456789012"))
catalog.append(Smartphone("OnePlus", "9", "+79567890123"))

# Печатаем весь каталог в формате <марка> - <модель>. <номер телефона>
for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.number)
