#DAY_23 : List Methods in Python 

l = [1,2,8,3,4,5]
print(l)

""" 
add eliment is list using append
 """

# l.append(7)
# print(l)

""" 
list.sort()
This method sorts the list in ascending order. The original list is updated
 """

# l.sort()
# print(l)

""" 
reverse()
This method reverses the order of the list.
 """

# l.reverse()
# print(l)

""" 
index()
This method returns the index of the first occurrence of the list item.
 """
# print(l.index(1))
""" 
count()
Returns the count of the number of items with the given value.
 """
# print(l.count(1))

""" 
copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
 """
# m = l.copy()
# m[0] = 0
# print(l)


""" 
insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method
 """
# l.insert(1,345)
# print(l)


""" 
extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
 """
# m = [900,1000,1100]
# l.extend(m)
# print(l)

""" 
Concatenating two lists:
You can simply concatenate two lists to join two lists.
 """
# k = l + m
# print(k)

