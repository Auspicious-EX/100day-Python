#DAY 5 : Comments, Escape Sequences & Print Statement 

print("\nComments:")
""" 
Comments:
- Single line comments are written using the hash symbol (#) at the beginning of a single line comment.
- Multi-line comments are written using three double quotes ("" ") at the beginning and end of a multi-line comment.
- Comments are used to explain code when the basic code is not clear.
- Comments are used to make the code more readable.
- Comments are used to prevent execution when testing code.
- Comments can be added anywhere in your Python program.
- The first character after the opening quotation mark must be a letter or an underscore (_). 
    Subsequent characters may include letters, digits, and underscores.
   
Example:    
"""

# This is single line statement for comment
print("\nHow to write comments in python...\n")
""" 
This is multi line statement for comment
"""



print("\nEscape Sequences:")
""" 
Escape Sequences:
- Escape sequences are used in strings to display characters that are otherwise difficult to type out or would cause errors by being interpreted incorrectly.
- An escape sequence starts with a backslash (\), followed by the character you want to insert.
- Escape sequences allow you to include special characters in strings.
- To insert characters that are illegal in a string, use an escape character.

Which are the escape sequences ?
- \'	Single Quote
- \"	Double Quote
- \\	Backslash
- \n	New Line
- \r	Carriage Return
- \t	Tab
- \b	Backspace
- \f	Form Feed
- \ooo	Octal value

Example:
"""

print("\nHello sir ? are your name is \"Shubham\" ? ") # \"	Double Quote
print("\nSir , I can ask some quation...\nare you live in Mehsana?") # \n New Line




print("\nPrint Statement:")
""" 
Print Statement:
- The print() function prints the specified message to the screen, or other standard output device.
- The message can be a string, or any other object, the object will be converted into a string before written to the screen.
- The end parameter is used to specify the line end character.
- The sep parameter is used to specify the separator between the arguments to print() function.

Some more on print statements:
- The print() function prints the given object to the standard output device (screen) or to the text stream file.
- The print() function accepts the following parameters:
    - object - object to the printed. * indicates that there may be more than one object
    - sep - objects are separated by sep. Default value: ' '
    - end - end is printed at last
    - file - must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
- The print() function basically uses file object sys.stdout (screen) to write output.
- The print() function returns None.

Example:

"""

print("\nHello World!")
print("Hello","World","!", sep="_")
print("Hello","World","!", sep="_", end="All")
