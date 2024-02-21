# DAY 50 : read(), readlines() and other methods


f = open('Day_50.txt', 'r')
i = 0

""" 
readlines() method
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

The readlines() method reads all the lines of the file and returns them as a list of strings.
 """

f = open('Day_50.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Example
while True:
    i = i+1
    line = f.readline()
    if not line:
    # print(line , type(line))
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks A: {m1}")
    print(f"Marks B: {m2}")
    print(f"Marks C: {m3}")

    print(line)


""" 
writelines() method
The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:

This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:
 """
f = open('Day_50.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

f = open('Day_50.txt', 'a')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()