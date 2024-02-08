# DAY 12 : Strings Slicing and Operations on Strings in Python

""" 
Lenght of String:
    len() function is used to find the length of the string.
    Syntax: len(string_name)
    

"""

name = "Shubham"
len_name = len(name)
print("Lenght of My name",name,"is",len_name)

""" 
String as an array:
    - A string is essentially a sequence of characters also called like an array. Thus we can access the elements of this array.
"""

name = "Shubham"
print(name[0])

""" 
Slicing in String:
    - Slicing is used to extract a part of a string.
    - Syntax: string_name[start_index:end_index:step]
    - start_index is inclusive and end_index is exclusive.
    - step is the number of characters to skip.
    - Type:
        - Positive Indexing: Starts from 0 and goes to n-1.
        - Negative Indexing: Starts from -1 and goes to -n.
        
"""

# Positive Slicing

name = "Shubham"
print(name[0:3]) 
print(name[2:5])
print(name[0:7:3])

# Nagetive Slicing

name = "Shubham"
print(name[-7:-4])
print(name[-5:-2])
print(name[-7:-1:3])
print(name[::-1])

""" 
Loop through a String:
    - We can loop through a string using for loop.
    
"""

name = "Shubham"
for i in name:
    print(i)
    
