# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Cretae tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs a trailing comma
fruits2 = ('Apples',)

# Get a value
print(fruits[1])

# Can't chage value
#fruits[0] = 'Pears'

# Delelte tuple
del fruits2

print(len(fruits))

print(fruits, type(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.
