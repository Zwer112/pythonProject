# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
# def triangle(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v1.draw(width=3)
#     engpoint = v1.end_point
#     v2 = sd.get_vector(engpoint, angle+120, length)
#     v2.draw(width=3)
#     engpoint = v2.end_point
#     v3 = sd.get_vector(engpoint, angle + 240, length)
#     v3.draw(width=3)
#
# def square(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v1.draw(width=3)
#     engpoint = v1.end_point
#     v2 = sd.get_vector(engpoint, angle+90, length)
#     v2.draw(width=3)
#     engpoint = v2.end_point
#     v3 = sd.get_vector(engpoint, angle + 180, length)
#     v3.draw(width=3)
#     engpoint = v3.end_point
#     v4 = sd.get_vector(engpoint, angle + 270, length)
#     v4.draw(width=3)
#
# def fvsquare(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v1.draw(width=3)
#     engpoint = v1.end_point
#     v2 = sd.get_vector(engpoint, angle+360/5, length)
#     v2.draw(width=3)
#     engpoint = v2.end_point
#     v3 = sd.get_vector(engpoint, angle + 360/5*2, length)
#     v3.draw(width=3)
#     engpoint = v3.end_point
#     v4 = sd.get_vector(engpoint, angle + 360/5*3, length)
#     v4.draw(width=3)
#     engpoint = v4.end_point
#     v5 = sd.get_vector(engpoint, angle + 360/5*4, length)
#     v5.draw(width=3)
#
# def sxsquare(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v1.draw(width=3)
#     engpoint = v1.end_point
#     v2 = sd.get_vector(engpoint, angle+360/6, length)
#     v2.draw(width=3)
#     engpoint = v2.end_point
#     v3 = sd.get_vector(engpoint, angle + 360/6*2, length)
#     v3.draw(width=3)
#     engpoint = v3.end_point
#     v4 = sd.get_vector(engpoint, angle + 360/6*3, length)
#     v4.draw(width=3)
#     engpoint = v4.end_point
#     v5 = sd.get_vector(engpoint, angle + 360/6*4, length)
#     v5.draw(width=3)
#     engpoint = v5.end_point
#     v6 = sd.get_vector(engpoint, angle + 360 / 6 * 5, length)
#     v6.draw(width=3)

def drwmain(point, angle, length, st, width):
    for i in range(1, st+1):
        v = sd.get_vector(point, angle+360/st*i, length)
        point = v.end_point
        v.draw(width=width)


point_0 = sd.get_point(300, 300)
points = ((100, 100), (400, 100), (100, 400), (400, 400))
#drwmain(point_0, 30, 200, 3, 2)
drwmain(sd.get_point(150, 100), 30, 100, 3, 2)
drwmain(sd.get_point(400, 100), 30, 100, 4, 2)
drwmain(sd.get_point(150, 400), 30, 100, 5, 2)
drwmain(sd.get_point(400, 400), 30, 100, 6, 2)

# triangle(sd.get_point(200, 200), 30, 100)
# square(point_1, 20, 200)
# fvsquare(point_2, 0, 150)
# sxsquare(point_3, -90, 50)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
