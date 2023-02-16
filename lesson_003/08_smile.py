# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (800, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile():
    point = sd.random_point()
    point_l = sd.get_point(point.x - 15, point.y + 10)
    point_r = sd.get_point(point.x + 15, point.y + 10)
    sd.circle(center_position=point, radius=50, width=5)
    sd.circle(center_position=point_l, radius=5, width=1)
    sd.circle(center_position=point_r, radius=5, width=1)
    sd.

for _ in range(10):
    smile()

# TODO здесь ваш код

sd.pause()
