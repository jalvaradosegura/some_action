import math
from enum import Enum, unique


@unique
class PizzaSizes(Enum):
    SMALL = 1
    MEDIUM = 3
    BIG = 5
    # will raise an error because the value is duplicated
    # XL = 5


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        # Example of !r or repr(<string>) (they're the same)
        # name = 'Jorge'
        # print(f'Hello {repr(name)}')
        # print(f'Hello {name!r}')
        return f'Pizza({self.radius!r}, {self.ingredients!r})'

    @classmethod
    def margaritha(cls):
        return cls(PizzaSizes.MEDIUM.value, ['cheese', 'tomatoes'])

    @classmethod
    def hawaiian(cls):
        return cls(PizzaSizes.MEDIUM.value, ['cheese', 'ham', 'pineaple'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


print('kinds of pizza')
print(Pizza(2, ['cheese', 'tomatoe', 'peperonni']))
print(Pizza.margaritha())
print(Pizza.hawaiian())
print('default pizza size')
hawaiian = Pizza.hawaiian()
margaritha = Pizza.margaritha()
print(hawaiian.area())
print(margaritha.area())
