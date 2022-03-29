class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()
William = Person()
William.age = 12
# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.age)
print(William.age)

# Calling object's greet() method
# Output: Hello
harry.greet()