# DAY 49 : File IO in Python

""" 
Opening a File
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:
 """
f = open('myfile.txt', 'r')

""" 
By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.
 """

""" 
Modes in file
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).

 """

# Reading a file
""" 
Once we have a file object, we can use various methods to read from the file.

The read() method reads the entire contents of the file and returns it as a string.
 """

# f = open("Day_49.txt", 'r')
# # f = open("Day_49.txt",) # 'r' modeis defol


# text = f.read()
# print(text)
# f.close()

#Writting
""" 
To write to a file, we first need to open it in write mode.
We can then use the write() method to write to the file. 
 """

# f = open("Day_49.txt", 'w')
# f.write("kabhi khushi kabhi gam") # overrites
# f.close()

#Appending
""" 
Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.
 """

# f = open("Day_49.txt", 'a')
# f.write("Hello I am shubhm aks Auspicious-EX") # overrites
# f.close()

#using with
""" 
The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it.
 """

with open("Day_49.txt", 'a') as f :
    f.write(" Auspicious-EX")




