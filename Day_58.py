# DAY 58 : Constructors in Python

""" 
Constructors
A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
 
 
Syntax of Python Constructor
def __init__(self):
	# initializations

init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.

Types of Constructors in Python
Parameterized Constructor
Default Constructor
Parameterized Constructor in Python
When the constructor accepts arguments along with self, it is known as parameterized constructor.

These arguments can be used inside the class to assign the values to the data members.

Example: 

"""
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")


""" 
Default Constructor in Python
When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
 """
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()



# PRACTICE

class Person:


    def __init__(self,n,o):
        print("Hello i am person")
        self.name = n
        self.occ  = o


    def info(self):
        print(f"{self.name} is {self.occ}")

a = Person( 'Herry',"Dev")
b = Person("Shubhm","editor")

# a.name = "Divya"
# a.occupation = "HR"
a.info()
b.info()
# c = Person(1,2,3)