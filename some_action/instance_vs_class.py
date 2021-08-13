class Dog:
    num_legs = 4

    def __init__(self, name):
        self.name = name


john = Dog('john')
kat = Dog('kat')
print(john.num_legs, kat.num_legs)
print(Dog.num_legs)

# error the class can't access an instance variable
# print(Dog.name)

print('==============================')

Dog.num_legs = 6
print(john.num_legs, kat.num_legs)
print(Dog.num_legs)

print()

Dog.num_legs = 4
john.num_legs = 6
print(john.num_legs, kat.num_legs)
print(Dog.num_legs)

print('buuut')
print(john.num_legs, john.__class__.num_legs)


print()
print('new class incoming')


class CounterObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


print(CounterObject().num_instances)
print(CounterObject().num_instances)
print(CounterObject().num_instances)


print()
print('now same class but with a bug')


class CounterObject2:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1


print(CounterObject2().num_instances)
print(CounterObject2().num_instances)
print(CounterObject2().num_instances)

print()
print('now same class but with a bug version 2')


class CounterObject3:
    num_instances = 2

    def __init__(self, x):
        self.num_instances *= x


print(CounterObject3(2).num_instances)
print(CounterObject3(3).num_instances)
print(CounterObject3(4).num_instances)
