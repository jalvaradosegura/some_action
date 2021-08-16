class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


# Infinite loop
# repeater = Repeater('Hello World')
# for item in repeater:
#    print(item)


class BoundedRepeater:
    def __init__(self, value, max_repeats: int):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


number_of_iterations = 5

print('Iterator with syntatic sugar')
repeater = BoundedRepeater('Hello World', number_of_iterations)
for item in repeater:
    print(item)


# Let's do the same thing but without the syntatic sugar
print('\nIterator without syntatic sugar')
repeater = BoundedRepeater('Hello World', number_of_iterations)
iterator = iter(repeater)
while True:
    try:
        next(iterator)
    except StopIteration:
        break
    print(item)


# Let's use generators to create our iterators
def repeater(value):
    while True:
        yield value


# Infinite loop
# for x in repeater('Hi'):
#    print(x)


def repeat_three_times(value):
    yield value
    yield value
    yield value


for x in repeat_three_times('3 times'):
    print(x)

iterator = repeat_three_times('3 times called by next')
next(iterator)
next(iterator)
next(iterator)
# Will raise StopIteration
# next(iterator)


def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value


for x in bounded_repeater('cool repeater', 2):
    print(x)


# Now let's use generator expressions
for x in ('Bom dia' for i in range(3)):
    print(x)


print(sum(x * 2 for x in range(10)))
iterator = ('generator expression' for x in range(3))
for x in iterator:
    print(x)


# Iterator chain
def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -1 * i


chain = negated(squared(integers()))
print(list(chain))


# another way of doing the chain
print('\n another way of doing the same')
integers = range(1, 9)
squared = (x * x for x in integers)
negated = (x * -1 for x in squared)
print(list(negated))
