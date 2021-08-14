import array

numbers = array.array('i', (1, 2, 3))
print(numbers)
print(numbers[0])
numbers[0] = 99
print(numbers[0])
# will fail
# numbers[0] = 99.0


# Will fill, because it only accepts integers
# numbers = array.array('i', (1.0, 2, 3))
# print(numbers)


chars = array.array('u', ('h', 'e', 'y'))
print(chars)
