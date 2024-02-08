#DAY 11 : Strings in Python

""" 
String:
    - In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
    - Strings are immutable, which means that once you create a string, you cannot change it. You can, however, create new strings from the original one.
    - Strings are objects in Python, so you can use built-in methods to create new strings.
    - Strings are sequences of characters, so you can access individual characters and substrings using indexing and slicing.
    - Strings are iterable, so you can use them in loops.
    - Strings are compared using comparison operators.
    - Strings are ordered, so you can sort them.
    - Strings are collections, so you can check for membership using the in operator.

- It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
- Sometimes, the user might need to put quotation marks in between the strings.
    
"""

name = "Shubham"
print("Hello",name)

chat = 'He say ,"Hello Shubham"'
print(chat)


""" 
Multiline String:

- In Python, you can use triple quotes to create multiline strings. You can use single or double quotes for multiline strings.
- Multiline strings are used when you want to print a string on multiple lines.
- Multiline strings are also used for docstrings, which are used to document functions, classes, and modules.
- Multiline strings are also used for comments that span multiple lines.
- To define multiline strings with triple quotes ("" "), use three double or single quote characters at the beginning of each line."" "

"""

chat = """
Shubham : Hello Viny
Viny : Hello Shubham
Shubham : How are you?
Viny : I am fine

"""

print(chat)




# Accessing Characters of a String \ Indexing
""" 

- You can access individual characters of a string using indexing. Indexing starts from 0.
- You can also use negative indexing to access characters from the end of the string. The last character has an index of -1.
- You can also use slicing to access substrings. Slicing is done by specifying the start and end index, separated by a colon (:). The start index is included, but the end index is not included.
- If you omit the start index, the substring starts from the beginning of the string. If you omit the end index, the substring ends at the end of the string.
- You can also use negative indexing for slicing. The last character has an index of -1.
- You can also specify a step value for slicing. The step value specifies the number of characters to skip. The default step value is 1.
- You can also use negative step values for slicing. The last character has an index of -1.
- You can also use slicing to reverse a string.
- You can also use the in operator to check if a string contains a substring.
"""

#Positive Indexing
name = "Shubham"
print(name[0])
print(name[1])
print(name[2])

#Negative Indexing
name = "Shubham"
print(name[-1])
print(name[-2])
print(name[-3])
