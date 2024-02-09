# DAY-13 : String Methods in Python

# len(): Returns the length of the string.
a = "Shubham"
print("len:", len(a))

# upper(): Converts all characters in the string to uppercase.
print("upper:", a.upper())

# lower(): Converts all characters in the string to lowercase.
print("lower:", a.lower())

# rstrip(): Removes trailing characters from the right end of the string.
print("rstrip:", a.rstrip("!"))

# replace(): Replaces occurrences of a specified string with another string.
print("replace:", a.replace("Shubham", "Viny"))

# split(): Splits the string into a list using a specified separator.
print("split:", a.split(" "))

# capitalize(): Converts the first character to uppercase and the rest to lowercase.
blogHeading = "introduction to pytHon"
print("capitalize:", blogHeading.capitalize())

# center(): Returns a centered string of specified width.
str1 = "Welcome to the Console!!!"
print("center:", str1.center(50))

# count(): Returns the number of occurrences of a specified value in the string.
print("count:", a.count("Shubham"))

# endswith(): Checks if the string ends with a specified suffix.
print("endswith (!):", str1.endswith("!!!"))
print("endswith (to):", str1.endswith("to", 4, 10))

# find(): Searches the string for a specified value and returns the position of where it was found.
a = "I am shubham, hello"
print("find (hello):", a.find("hello"))

# index(): Searches the string for a specified value and returns the position of where it was found.
print("index (hello):", a.index("hello"))

# isalnum(): Returns True if all characters in the string are alphanumeric.
str = "WelcomeToTheConsole"
print("isalnum:", str.isalnum())

# isalpha(): Returns True if all characters in the string are alphabetic.
print("isalpha:", str.isalpha())

# islower(): Returns True if all characters in the string are lowercase.
print("islower:", str.islower())

# isprintable(): Returns True if all characters in the string are printable.
print("isprintable:", str.isprintable())

# isspace(): Returns True if all characters in the string are whitespace.
str1 = "         "
print("isspace:", str1.isspace())

# istitle(): Returns True if the string follows the rules of a title.
s = "Hello Man"
print("istitle:", s.istitle())

# startswith(): Checks if the string starts with a specified value.
print("startswith (Hello):", s.startswith("Hello"))

# swapcase(): Swaps cases, lower case becomes upper case and vice versa.
print("swapcase:", s.swapcase())

# title(): Converts the first character of each word to upper case.
a ="his name is shrey"
print("title:", a.title())