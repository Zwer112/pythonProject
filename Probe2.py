import random

import simple_draw as sd

def buble (point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius)


sd.resolution = (800, 600)
point = sd.get_point(100, 100)
radius1 = 50
for _ in range(3):
    radius1 += 5
    sd.circle(center_position=point, radius=radius1, width=3, color=(255, 0 ,0))
point = sd.get_point(200, 500)
buble(point=point, step=10)

for i in range(10):
    point = sd.get_point(300+i*40, 100)
    buble(point, 20)
    #sd.circle(center_position=point, radius=20, width=3, color=(255, 0, 0))

for j in range(100, 400, 100):
    for i in range(10):
        point = sd.get_point(300 + i * 40, 100+j)
        buble(point, 20)

for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    buble(point, step)

sd.pause()


