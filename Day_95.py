# DAY 95 : Regular Expressions in Python 

# https://regexr.com/

""" 
Regular Expressions in Python
Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.
 """

import re

"""  
Metacharacters in regular expressions
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs

Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

Importing re Package
In Python, regular expressions are supported by the re module. The basic syntax for working with regular expressions in Python is as follows:

import re

Searching for a pattern in re using re.search() Method
re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. We can use re.search method like this to search for a pattern in regular expression:
"""

pattern = r"[A-Z]+yclone"

text = '''
Kabhie Kabhie Cyclone(translation: Sometimes) is a 1976 Indian Hindi-language musical romantic drama film written by Pamela Chopra and directed and produced by Yash Chopra under the production banner of Yash Raj Films. Released on 27 cyclone February 1976, the film stars an ensemble cast of Waheeda Rehman, Shashi Kapoor, Dyclone Amitabh Bachchan, Rakhee Gulzar, Rishi Kapoor and Neetu Singh. This was Yash Chopra's second directorial film with Bachchan and Shashi Kapoor in the lead roles after Deewaar (1975) and was particularly noted for its soundtrack compositions by Khayyam. The film received widespread critical acclaim upon release, with high praise directed towards its story, screenplay, direction, dialogues, soundtrack, and performances of the ensemble cast, and is regarded as a cult film over the years.
'''

match = re.search(pattern, text)
print(match)


""" 
Searching for a pattern in re using re.findall() Method
You can also use the re.findall function to find all occurrences of the pattern in a string:
 """

matches = re.finditer(pattern, text)

for match in matches:
  print(match.span()) 
  print(text[match.span()[0]: match.span()[1]])

  """ 
   Conclusion
Regular expressions are a powerful tool for working with strings and text data in Python. Whether you're matching patterns, replacing text, or extracting information, regular expressions make it easy to perform complex string operations with just a few lines of code. With a little bit of practice, you'll be able to use regular expressions to solve all sorts of string-related problems in Python.
     """