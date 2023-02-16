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
    point_l = sd.get_point(point.x - 20, point.y + 10)
    point_r = sd.get_point(point.x + 20, point.y + 10)
    point_ll = sd.get_point(point.x - 30, point.y - 30)
    point_rr = sd.get_point(point.x + 30, point.y - 20)
    sd.circle(center_position=point, radius=50, width=0)
    sd.circle(center_position=point_l, radius=15, color=(0, 0, 0), width=0)
    sd.circle(center_position=point_r, radius=15, color=(0, 0, 0), width=0)
    sd.rectangle(left_bottom=point_ll, right_top=point_rr, color=(0, 0, 0), width=0)


for _ in range(10):
    smile()

# TODO здесь ваш код

sd.pause()
