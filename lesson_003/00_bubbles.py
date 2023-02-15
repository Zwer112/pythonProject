# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

for i in range(3):
    point = sd.get_point(100, 100)
    sd.circle(point, 50+i*20)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    for i in range(4):
        sd.circle(point, radius = step*i)

point = sd.get_point(200, 200)
bubble(point, 50)


# Нарисовать 10 пузырьков в ряд

for x in range(11):
    if x == 0:
        continue
    point = sd.get_point(x*50, 200)
    bubble(point, 50)


# Нарисовать три ряда по 10 пузырьков
for y in range(200, 500, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point, 50)



# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.clear_screen()
for _ in range(101):
    point = sd.random_point()
    step = random.randint(5, 8)
    bubble(point, step)

sd.pause()


