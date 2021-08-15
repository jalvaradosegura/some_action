lst = [x for x in range(0, 10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 0 1  2  3  4  5  6  7  8  9  10
print(lst)
print(lst[::3])
print(lst[3:10])
print(lst[3:10:2])
print(lst[3:10:3])
print(lst[3:10:4])
print('reverse')
# reverse a list
print(lst[::-1])
# copied list (shallow copy: 1 lvl deep)
print('make shallow copies')
lst.append(['h', 'hi'])
copied_list = lst[:]
print(copied_list is lst)
print(copied_list == lst)
lst[-1][0] = 999
print(copied_list)
# clear a list
print('clear a list')
del lst[:]
print(lst)
