#DAY 3 : Modules and pip

""" 
Module is like a code library which can be used to borrow code written by somebody else in our python program. 
                    There are two types of modules in python:

Built in Modules - These modules are ready to import and use and ships with the python interpreter. 
                    there is no need to install such modules explicitly.
                    example:
                    import math
                    
External Modules - These modules are imported from a third party file or can be installed using a 
                    package manager like pip or conda. Since this code is written by someone else, 
                    we can install different versions of a same module with time.
                    example:
                    import pandas as pd
                    import numpy as np
                    
Pip
Pip is a package manager in python which is used to install external modules in python.
                    example:
                    pip install pandas
                    pip install numpy


Using a module in Python (Usage):
We use the import syntax to import a module in Python. Here is an example code:

"""

import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file

""" 
Similarly we can install other modules and look into their documentations for usage instructions.
We will find ourselved doing this often in the later part of this course
"""
                    