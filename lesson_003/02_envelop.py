# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7

def inconv(paper_x, paper_y):
    if paper_x < envelop_x and paper_y < envelop_y:
        print(paper_x, paper_y, 'В конверте')
    else: print(paper_x, paper_y, 'Не помещается')


# проверить для

paper_x, paper_y = 9, 8
inconv(paper_x, paper_y)
paper_x, paper_y = 6, 8
inconv(paper_x, paper_y)
paper_x, paper_y = 8, 6
inconv(paper_x, paper_y)
paper_x, paper_y = 3, 4
inconv(paper_x, paper_y)
paper_x, paper_y = 11, 9
inconv(paper_x, paper_y)
paper_x, paper_y = 9, 11
inconv(paper_x, paper_y)

# (просто раскоментировать нужную строку и проверить свой код)


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
def incert(x, y, z):
    if hole_x > x and hole_y > y:
        print('Пройдет по xy')
    elif hole_x > y and hole_y > z:
        print('Пройдет по yz')
    elif hole_x > x and hole_y > z:
        print('Пройдет по zx')
    else:
        print ('Не пройдет')


brick_x, brick_y, brick_z = 11, 10, 2
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 2, 10
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 11, 2
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 10, 2, 11
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 10, 11
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 2, 11, 10
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 5, 6
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 5
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 5
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 5, 3
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 6, 3
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 5, 3, 6
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 3, 6
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 11, 6, 3
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 11, 3
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 6, 3, 11
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 6, 11
incert(brick_x, brick_y, brick_z)
brick_x, brick_y, brick_z = 3, 11, 6
incert(brick_x, brick_y, brick_z)
# (просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код
