# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Create dict
person = {
    'first_name': 'Cami',
    'last_name': 'Balo',
    'age': 17
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))


# print(person2, type(person2))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item
del(person)['age']
person.pop('phone')

# Clear
person.clear()

# Get lengeth
print(len(person2))


print(person)

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[1]['name'])
