# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1


# Extend class
class Customer(User):
  # Construcotr
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance
    

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init customer object
janet = Customer('Janet Johnson', 'janet@gmail.om', 26)

janet.set_balance(500)
print(janet.greeting())




# Init user object
Cami = User('Cami B', 'cami@gmail.com', 17)

print(type(Cami))
print(Cami.name)

Cami.has_birthday()
print(Cami.greeting())