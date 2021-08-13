from collections import namedtuple

Car = namedtuple('Car', ['color', 'mileage'])

# this one also works
# Car = namedtuple('Car', 'color mileage')

print(dir(Car))

my_car = Car('red', 12)
print(my_car)
print(my_car.color)
# you can change the value of an atribute
# my_car.color = 'blue'


ElitricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
print(ElitricCar('blue', 12, 99))
