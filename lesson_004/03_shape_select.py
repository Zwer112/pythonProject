# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

col = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
col_p = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purpule']
fig = ['tri', 'kva', 'penta', 'sixta']

# TODO здесь ваш код
def drwmain(point, angle, length, st, width, color):
    for i in range(1, st+1):
        v = sd.get_vector(point, angle+360/st*i, length)
        point = v.end_point
        v.draw(color=color, width=width)


point_0 = sd.get_point(200, 200)

print('Выберите фигуру 1-4 ')
for i in fig:
    print(i)
nam = int(input('выбор'))


print('Выберите цвет 1-7 ')
for i in col_p:
    print(i)
color = int(input('выбор'))
vc = col[color-1]

drwmain(point_0, 0, 80, nam+2, 3, vc)


sd.pause()
