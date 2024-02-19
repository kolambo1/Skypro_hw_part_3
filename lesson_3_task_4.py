# lesson_3_task_4.py
import turtle # Импортируем модуль turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

# Нарисовать квадрат
def draw_rect(t):
    for x in range(0, 4):
        t.right(90)
        t.forward(100)

# Рисует квадраты в цикле
for x in range(0, 360):
    draw_rect(my_turtle)
    my_turtle.right(1)

# Нарисовать голову животного
def draw_head(t):
    t.penup()
    t.goto(-200, 200) # Перемещаемся в левый верхний угол
    t.pendown()
    t.setheading(0) # Сбрасываем угол поворота
    t.fillcolor("brown") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.circle(100) # Рисуем круг радиуса 100
    t.end_fill() # Заканчиваем заливку

# Нарисовать глаза животного
def draw_eyes(t):
    t.penup()
    t.goto(-230, 230) # Перемещаемся в левый глаз
    t.pendown()
    t.fillcolor("white") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.circle(20) # Рисуем круг радиуса 20
    t.end_fill() # Заканчиваем заливку
    t.penup()
    t.goto(-170, 230) # Перемещаемся в правый глаз
    t.pendown()
    t.fillcolor("white") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.circle(20) # Рисуем круг радиуса 20
    t.end_fill() # Заканчиваем заливку
    t.penup()
    t.goto(-230, 230) # Перемещаемся в левый глаз
    t.pendown()
    t.fillcolor("black") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.circle(10) # Рисуем круг радиуса 10
    t.end_fill() # Заканчиваем заливку
    t.penup()
    t.goto(-170, 230) # Перемещаемся в правый глаз
    t.pendown()
    t.fillcolor("black") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.circle(10) # Рисуем круг радиуса 10
    t.end_fill() # Заканчиваем заливку

# Нарисовать нос животного
def draw_nose(t):
    t.penup()
    t.goto(-200, 200) # Перемещаемся в центр головы
    t.pendown()
    t.fillcolor("black") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.right(60) # Поворачиваемся на 60 градусов вправо
    t.forward(50) # Идем вперед на 50
    t.left(120) # Поворачиваемся на 120 градусов влево
    t.forward(50) # Идем вперед на 50
    t.left(120) # Поворачиваемся на 120 градусов влево
    t.forward(50) # Идем вперед на 50
    t.end_fill() # Заканчиваем заливку

# Нарисовать уши животного
def draw_ears(t):
    t.penup()
    t.goto(-300, 250) # Перемещаемся в левое ухо
    t.pendown()
    t.fillcolor("brown") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.left(30) # Поворачиваемся на 30 градусов влево
    t.forward(100) # Идем вперед на 100
    t.right(120) # Поворачиваемся на 120 градусов вправо
    t.forward(100) # Идем вперед на 100
    t.right(120) # Поворачиваемся на 120 градусов вправо
    t.forward(100) # Идем вперед на 100
    t.end_fill() # Заканчиваем заливку
    t.penup()
    t.goto(-100, 250) # Перемещаемся в правое ухо
    t.pendown()
    t.fillcolor("brown") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.left(120) # Поворачиваемся на 120 градусов влево
    t.forward(100) # Идем вперед на 100
    t.right(120) # Поворачиваемся на 120 градусов вправо
    t.forward(100) # Идем вперед на 100
    t.right(120) # Поворачиваемся на 120 градусов вправо
    t.forward(100) # Идем вперед на 100
    t.end_fill() # Заканчиваем заливку

# Нарисовать тело животного
def draw_body(t):
    t.penup()
    t.goto(-200, 100) # Перемещаемся в начало тела
    t.pendown()
    t.fillcolor("brown") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.right(90) # Поворачиваемся на 90 градусов вправо
    t.forward(200) # Идем вперед на 200
    t.left(90) # Поворачиваемся на 90 градусов влево
    t.forward(400) # Идем вперед на 400
    t.left(90) # Поворачиваемся на 90 градусов влево
    t.forward(200) # Идем вперед на 200
    t.left(90) # Поворачиваемся на 90 градусов влево
    t.forward(400) # Идем вперед на 400
    t.end_fill() # Заканчиваем заливку

# Нарисовать хвост животного
def draw_tail(t):
    t.penup()
    t.goto(200, -100) # Перемещаемся в конец тела
    t.pendown()
    t.fillcolor("brown") # Задаем цвет заливки
    t.begin_fill() # Начинаем заливку
    t.right(45) # Поворачиваемся на 45 градусов вправо
    t.forward(100) # Идем вперед на 100
    t.left(90) # Поворачиваемся на 90 градусов влево
    t.forward(50) # Идем вперед на 50
    t.left(90) # Поворачиваемся на 90 градусов влево
    t.forward(100) # Идем вперед на 100
    t.end_fill() # Заканчиваем заливку

# Вызвать функцию для рисования хвоста
draw_tail(my_turtle)

# Вызвать функции в правильном порядке
draw_head(my_turtle)
draw_eyes(my_turtle)
draw_nose(my_turtle)
draw_ears(my_turtle)
draw_body(my_turtle)
draw_legs(my_turtle)
