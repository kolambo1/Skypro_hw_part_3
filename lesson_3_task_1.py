# lesson_3_task_1.py
from user import User # Импортируем класс User из файла user.py

my_user = User("Иван", "Иванов") # Создаем новый экземпляр User и сохраняем его в переменную my_user
my_user.print_first_name() # Вызываем метод, печатающий имя
my_user.print_last_name() # Вызываем метод, печатающий фамилию
my_user.print_full_name() # Вызываем метод, печатающий имя и фамилию