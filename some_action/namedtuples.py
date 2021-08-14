from collections import namedtuple
from typing import NamedTuple

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

print()
# from typing import NamedTuple


class Dog(NamedTuple):
    name: str
    breed: str
    age: int


# I love him
zendo = Dog('Zendo', 'Pembroke Corgi', 7)
print(zendo)
# Will fail, NamedTuple's are inmutable
# zendo.legs = 4
