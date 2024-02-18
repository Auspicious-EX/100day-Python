#DAY 32 : Set Methods in Python

S = { 1,2,3,4}
S2 = {5,6,7}
print(S.union(S2))


""" 
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.
 """
 #another Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

S.update(S2)
print(S , S2)

""" 
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
 """

S.intersection(S2)
print(S , S2)

#Another Exaple
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)


#symmetric_difference
""" 
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#symmetric_difference_updat
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#IV. difference() and difference_update():
""" 
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#isdisjoint():
""" 
The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#issuperset():
""" 
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))



#issubset():
""" 
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

#add()
""" 
If you want to add a single item to the set use the add() method.
 """
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Ahmedabad")
print(cities)

#update()
""" 
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#remove()/discard()
""" 
We can use remove() and discard() methods to remove items form list.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

""" 
The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

 """

#pop()
""" 
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


#del
""" 
del is not a method, rather it is a keyword which deletes the set entirely.
 """

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

#clear():
""" 
This method clears all items in the set and prints an empty set.
 """
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

""" 
Check if item exists
You can also check if an item exists in the set or not.
 """