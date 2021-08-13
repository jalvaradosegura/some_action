import copy

x = [1, 2, 3]
y = x

print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)
x.append(4)
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)

print()

# Shallow copy, it actually copy 1 lvl deep
print('shallow copy')
x = [1, 2, 3]
y = list(x)
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)
x[0] = 3
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)

print()

# Won't work for second level deep
print('shallow copy')
x = [[1, 2, 3], [4, 5], [6, 7]]
y = list(x)
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)
x.append(['hi'])
x[0][1] = 'x'
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)

print()

# Deepcopy
print('deep copy')
x = [[1, 2, 3], [4, 5], [6, 7]]
y = copy.deepcopy(x)
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)
x.append(['hi'])
x[0][1] = 'x'
print(x)
print(y)
print('x == y', x == y)
print('x is y', x is y)
