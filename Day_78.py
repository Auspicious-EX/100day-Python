# DAY 78 : Single Inheritance in Python


""" 
Single Inheritance in Python
Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

Syntax
The syntax for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses, like this:

class ChildClass(ParentClass):
    # class body
 """

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species='Dog')
        self.breed = breed

    def make_sound(self):
        print("Bark")

d = Dog("Dog","Dogerman")
d.make_sound()


a = Animal("dog","Dog")
a.make_sound()

""" 
The Dog class inherits all the attributes and behaviors of the Animal class, including the __init__ method and the make_sound method. Additionally, the Dog class has its own __init__ method that adds a new attribute for the breed of the dog, and it also overrides the make_sound method to specify the sound that a dog makes.

Single inheritance is a powerful tool in Python that allows you to create new classes based on existing classes. It allows you to reuse code, extend it to fit your needs, and make it easier to manage complex systems. Understanding single inheritance is an important step in becoming proficient in object-oriented programming in Python.
 """



class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")
    
    def purr(self):
        print("Purring...")
    
    def chase_mouse(self):
        print("Chasing mouse...")

c = Cat("Whiskers", "Tabby")
c.make_sound()  
c.purr()        
c.chase_mouse() 
