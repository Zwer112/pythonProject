class Car:
    def __init__(self, name, model, year, tank):
        self.name_car = name
        self.model_car = model
        self.year_car = year
        self.tank_car = tank
    def get_full_info(self):
        full_infa = (str(self.name_car).title()+' '+str(self.model_car).title()+' '+str(self.year_car))
        return full_infa
    def old_year(self):
        old_y = 2023-int(self.year_car)
        return old_y

class ElCar(Car):
    def __int__(self, name, model, year, tank):
        super().__init__(name, model, year, tank)
        self.bat = 100
        self.col = 'Red'

        self.battaty = 0
    def el_full_info(self):
        efull = (str(self.bat)+' '+str(self.col))
        return efull
    def old_year(self):
        old_y = 2023
        return old_y


my_car = Car('audi', 'a4', 2005, 50)
print(my_car.get_full_info())
print(my_car.old_year())

my_ecar = ElCar('Tesla', 'Mosel K', 2021, 0)
my_ecar.col = 'Red'
my_ecar.bat = 90000
print(my_ecar.get_full_info()+" "+my_ecar.el_full_info())
print(my_ecar.old_year())
my_ecar1 = ElCar('Tesla1', 'Mosel K1', 2022, 10000)
print(my_ecar1.get_full_info()+" "+my_ecar1.el_full_info())