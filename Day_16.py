# Day_16 : Match Case Statements in Python

""" 
What is Match case statements?

To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

 """


#no need of breack in this


""" x = int(input("enter the num:"))

match x:

    case 0 :
        print("x is zero")

    case 4:
        print("case is 4")
    
    case _ if x != 90:
        print(x, "x is not 90")
            
    case _ if x != 90:
        print(x, "x is not 80")
            
    case _:
        print(x) """


day = "Monday"

match day:
    case "Monday":
        print("It's the start of the week!")
    case "Friday":
        print("It's almost the weekend!")
    case "Saturday", "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a regular day.")
