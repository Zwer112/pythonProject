# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


col = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
col_p = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purpule']
# TODO здесь ваш код
def drwmain(point, angle, length, st, width, color):
    for i in range(1, st+1):
        v = sd.get_vector(point, angle+360/st*i, length)
        point = v.end_point
        v.draw(color=color, width=width)


point_0 = sd.get_point(200, 200)
print('Выберите цвет 1-7 ')
for i in col_p:
    print(i)
color = int(input('Выберите цвет 1-7  '))
vc = col[color-1]

drwmain(point_0, 0, 80, 5, 3, vc)


sd.pause()
