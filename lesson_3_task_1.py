# lesson_3_task_2.py
from smartphone import Smartphone # Импортируем класс Smartphone из файла smartphone.py

catalog = [] # Создаем пустой список
# Добавляем пять разных экземпляров класса Smartphone в список
catalog.append(Smartphone("Samsung", "Galaxy S24U", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 15 5PRO MAX", "+79234567890"))
catalog.append(Smartphone("Huawei", "P60", "+79345678901"))
catalog.append(Smartphone("Xiaomi", "Mi 14 Ultra", "+79456789012"))
catalog.append(Smartphone("OnePlus", "12", "+79567890123"))

# Печатаем весь каталог в формате <марка> - <модель>. <номер телефона>
for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.number)