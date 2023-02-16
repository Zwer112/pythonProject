# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (800, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
def kirpich(x, y, sh, wh):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x + sh, y)
    sd.line(start_point=start_point, end_point=end_point, width=3)
    start_point = sd.get_point(x + sh, y)
    end_point = sd.get_point(x + sh, y + wh)
    sd.line(start_point=start_point, end_point=end_point, width=3)
    start_point = sd.get_point(x + sh, y + wh)
    end_point = sd.get_point(x, y + wh)
    sd.line(start_point=start_point, end_point=end_point, width=3)
    start_point = sd.get_point(x, y + wh)
    end_point = sd.get_point(x, y)
    sd.line(start_point=start_point, end_point=end_point, width=3)

for x in range(0, 800, 60):
    for y in range(0, 600, 60):
        kirpich(x, y, 60, 30)
        kirpich(x + 30, y+30, 60, 30)

sd.pause()
