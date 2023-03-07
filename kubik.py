from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        for _ in range(10):
            x = randint(1, self.sides)
            print(x, end =' ')
        print('')

cub10 = Die(20)
cub10.roll_die()
cub5 = Die(4)
cub5.roll_die()

cub61 = Die()
cub61.roll_die()