from collections import Counter

# Go-to set
print('\nset')
my_set = {1, 2, 3, 3}
print(my_set)
my_set.add(5)
print(my_set)
vowels = {'a', 'e', 'i', 'o', 'u'}
name = set('alice')
print(name)
print(name.intersection(vowels))
print(vowels.intersection(set('murcielago')))
print(vowels.intersection(set('perro')))

print('\nFrozenset')
# frozen set: inmuttable
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# this will fail
# vowels.add('p')
some_dict = {vowels: 'super cool'}
print(some_dict)
print(some_dict[vowels])

print('\nCounter')
# from collections import Counter

inventory = Counter()
inventory.update({'fire-sword': 1, 'boh': 1, 'ham': 3})
loot = {'ham': 6, 'draggy-ham': 2, 'sov': 1}
inventory.update(loot)
print(inventory)
print(len(inventory))
print(sum(inventory.values()))
