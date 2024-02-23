# DAY 57: Classes and Objects in Python 

""" 
Python Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.
 """

""" 
Creating a Class:
Let us now create a class using the class keyword.
 """

class Person:
    name = "Harry"
    occupation = "Software Engineer"
    networth = "10"
    def info(self):
        print(f"{self.name} is a {self.occupation}")


""" 
Creating an Object:
Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
 """
a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()


""" 
self parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.
 """