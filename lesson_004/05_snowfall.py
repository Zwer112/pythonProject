# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
y = 555
N = 20
t_x = []
t_y = []
ligth = []
factor_a = [] #- место ответвления лучиков
factor_b = [] #- длина лучиков
factor_c = [] # - угол отклонения лучиков
for x in range(0, N):
    t_x.append(sd.randint(0, 1200))
    t_y.append(y)
    ligth.append(sd.randint(5, 30))
    factor_a.append(sd.randint(1, 100) / 100)
    factor_b.append(sd.randint(1, 100) / 100)
    factor_c.append(sd.randint(1, 180))

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# TODO здесь ваш код
sd.clear_screen()

while True:
    sd.start_drawing()

    for i in range(0, N):


        point = sd.get_point(t_x[i], t_y[i])

        sd.snowflake(point, length=ligth[i], color=sd.background_color, factor_a=factor_a[i], factor_b=factor_b[i],
                 factor_c=factor_c[i])

        t_x[i] = t_x[i] + sd.random_number(0, 15)
        t_y[i] = t_y[i] - sd.random_number(0, 50)

        n_point = sd.get_point(t_x[i], t_y[i])

        sd.snowflake(n_point, length=ligth[i], factor_a=factor_a[i], factor_b=factor_b[i], factor_c=factor_c[i])

        if t_y[i] < 20:
            t_x[i] = sd.random_number(0, sd.resolution[0])
            t_y[i] = y

    sd.sleep(0.1)

    sd.finish_drawing()



    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


