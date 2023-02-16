# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
sd.resolution = (800, 600)

for step in range(1, 36, 5):
    n = sd.get_point(50, 50+step)
    e = sd.get_point(750, 450+step)
    color = (rainbow_colors[step//5])
    sd.line(start_point=n, end_point=e, color=color, width=4)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
r = 100
for step in range(1, 106, 15):
    n = sd.get_point(400, 0)
    color = (rainbow_colors[step//15])
    sd.circle(center_position=n, radius = r+step, color=color, width=15)


sd.pause()
