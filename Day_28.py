# DAY_28: f-strings in Python

"""
f-strings in Python:
f-strings, also known as formatted string literals, allow us to embed expressions inside string literals, using curly braces {}. They provide a concise and readable way to format strings.

Usage:
f-strings are prefixed with the letter 'f' or 'F' before the opening quotation mark. Inside the string, expressions are written within curly braces {}, which are replaced by their values during runtime.

Syntax:
f"string {expression}"

Benefits:
1. Readability: f-strings improve code readability by allowing variable interpolation directly within string literals.
2. Simplicity: They provide a simple and straightforward way to format strings compared to older methods like format() or % formatting.

"""

# Example: Using f-strings with .format() method
letter = "Hello i am {} and i am from {}"
country = "India"
name = "Shubham"
print(letter.format(name, country))

# Example: Using f-strings directly
print(f"Hello i am {name} and i am from {country}")

# Example: Using f-strings with formatted numbers
txt = "For only {prize:.2f} dollars"
print(txt.format(prize=49.099999))

prize = 49.099999
txt = f"For only {prize:.2f} dollars"
print(txt)

# Example: Using f-strings with expressions
print(f"{2 * 30}")

# Example: Escaping braces in f-strings
print(f"Hello using {{prize}}")
