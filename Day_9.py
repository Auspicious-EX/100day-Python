#DAY 9 : Typecasting in Python


print(
""" 
Typecasting:\n
    - The conversion of one data type into the other data typeis knownas type casting in python or conversion in python.\n
    - There are two types of typecasting in python:\n
        1. Implicit Typecasting\n
        2. Explicit Typecasting\n
""" )


print(
"""
    - Implicit Typecasting:             \n
        - The typecasting which is done automatically by the compiler is known as implicit typecasting.\n
        - In this type of typecasting, the data type of the variable is automatically converted into another data type.\n
        - Exapmle:\n
        - a = 10
        - b = 20.5
""")
a = 10
print(type(a))
b = 20.5
print(type(b))
c = a + b
print(c)
print(type(c))

print(
"""
    - Explicit Typecasting:             \n
        - The typecasting which is done manually by the programmer is known as explicit typecasting.\n
        - In this type of typecasting, the data type of the variable is manually converted into another data type.\n
    
        - There are many types of explicit typecasting in python:\n
            1. int()\n
            2. float()\n
            3. str()\n
            4. bool()\n
            5. complex()\n
            6. list()\n
            7. tuple()\n
            8. set()\n
            9. dict()\n
            10. frozenset()\n
            11. bytes()\n
            12. bytearray()\n
            13. memoryview()\n
            
            
        - Exapmle:\n
        - a = 10
        - b = 20.5
""")
a = 10
print(type(a))
b = 20.5
print(type(b))
c = a + int(b)
print(c)
print(type(c))            