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
#del fruits2

print(len(fruits))

print(fruits, type(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.


# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# add to set
fruits_set.add('Grape')

print(fruits_set)

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
# fruits_set.clear()
print(fruits_set)

# Delete
del fruits_set
