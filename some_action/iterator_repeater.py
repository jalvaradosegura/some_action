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
