'''Note – A set cannot have mutable elements like a list, set or dictionary, as its elements.'''


##                              Creating a Set
set1 = set()
print (set1)            ##Output: set()

set1 = set("geeksforgeeks")
print (set1)            ##Output: {'g', 'o', 'e', 'f', 'r', 'k', 's'}

set1 = set(["Geeks", "For", "Geeks"])
print (set1)            ##Output: {'Geeks', 'For'}


##                      Python Set add() Method
'''If the element already exists, the add() method does not add the element.

Syntax : set.add(elmnt)   ----> It returns None
elmnt	Required. The element to add to the set'''

s ={'a','b','c'}
s.add('d')
print (s)               ##Output: {'d','b','a','c'}
s.add('d')
print (s)               ##Output: {'d','b','a','c'}


##                      Python Set clear() Method
'''The clear() method removes all elements in a set.

Syntax : set.clear()   ----> It returns None
'''
s ={'a','b','c'}
s.clear()
print (s)               ##Output: set()


##                      Python Set copy() Method
'''The copy() method copies the set.

Syntax : set.copy()   ----> It returns the copy of set
'''

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)                ##Output: {"apple", "banana", "cherry"}


##                      Python Set difference() Method
'''The difference() method returns a set that contains the difference between two sets. 

Syntax :        set.difference(set)   ----> It returns set contains items that exist only
                                            in the first set, and not in both sets.
set    :	Required. The set to check for differences in'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print (x.difference(y))             ##Output: {'cherry', 'banana'}
print (y.difference(x))             ##Output: {'microsoft', 'google'}


##                      Python Set difference_update() Method
'''The difference_update() method removes the items that exist in both sets.

The difference_update() method is different from the difference() method,
because the difference() method returns a new set, without the unwanted
items, and the difference_update() method removes the unwanted items from
the original set.

Syntax :        set1.difference_update(set2) ---> It returns a None
'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)                        ##Output: {'banana', 'cherry'}


##                      Python Set intersection Method
'''The intersection() method returns a set that contains the similarity between two or more sets.

Meaning: The returned set contains only items that exist in both sets, or in all sets
         if the comparison is done with more than two sets.

Syntax :  set.intersection(set1, set2 ... etc)

set1	Required. The set to search for equal items in
set2	Optional. The other set to search for equal items in.
        You can compare as many sets you like.
        Separate the sets with a comma'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)                        ##Output: {'apple'}


##                      Python Set intersection_update() Method
'''The intersection_update() method removes the items that is not present in both sets
(or in all sets if the comparison is done between more than two sets).

The intersection_update() method is different from the intersection() method,
because the intersection() method returns a new set, without the unwanted items,
and the intersection_update() method removes the unwanted items from the original set.

Syntax :  set.intersection_update(set1, set2 ... etc    ----> It returns None'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)                        ##Output: {'apple'}


##                      Python Set symmetric_difference() Method
'''The symmetric_difference() method returns a set that contains all items from both set,
   but not the items that are present in both sets.

Meaning: The returned set contains a mix of items that are not present in both sets.

Syntax :    set.symmetric_difference(set)
set	    Required. The set to check for matches in'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)                        ##Output: {'microsoft','cherry','banana','google'}


##                      Python Set symmetric_difference_update() Method
'''The symmetric_difference_update() method updates the original set by removing items
that are present in both sets, and inserting the other items.

Syntax :    set.symmetric_difference_update(set) ------> It returns None
'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)                        ##Output: {'banana', 'google', 'microsoft', 'cherry'}


##                      Python Set union() Method
'''The union() method returns a set that contains all items from the original set,
and all items from the specified sets.
You can specify as many sets you want, separated by commas.
If an item is present in more than one set, the result will contain only one appearance of this item.

Syntax  :   set.union(set1, set2...)
set1	    Required. The set to unify with
set2	    Optional. The other set to unify with.
            You can compare as many sets as you like.
            Separate each set with a comma'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)                        ##Output: {'banana', 'cherry', 'apple', 'microsoft', 'google'}


##                      Python Set update() Method
'''The update() method updates the current set, by adding items from another set.
If an item is present in both sets, only one appearance of this item will be present in the updated set.

Syntax  :   set.update(set)              ----> It returns None
set	    Required. The set insert into the current set'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x)                        ##Output: {'microsoft', 'apple', 'google', 'cherry', 'banana'}


##                     Python Set discard() Method
'''The discard() method removes the specified item from the set.

Syntax  :   set.discard(value)
value	    Required. The item to search for, and remove'''

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)                   ##Output: {'apple','cherry'}

##NOTE : This method is different from the remove() method, because the remove()
##       method will raise an error if the specified item does not exist, and the
##       discard() method will not.


##                     Python Set pop() Method
'''The pop() method removes a random item from the set.

Syntax  :   set.pop()   ----->  This method returns the removed item.'''

fruits = {"apple", "banana", "cherry"}
print(fruits.pop())              ##Output: apple


##                     Python Set isdisjoint() Method
'''The isdisjoint() method returns True if none of the items are present in both sets,
otherwise it returns False.

Syntax  :   set.isdisjoint(set)    -----> returns True or False
set	    Required. The set to search for equal items in'''

##Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
print(x.isdisjoint(y))          ##Output:True


##                     Python Set issubset() Method
'''The issubset() method returns True if all items in the set exists in the specified set,
otherwise it retuns False.

Syntax  :   set.issubset(set)    -----> returns True or False'''

##Return True if all items set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y))            ##Output:True
print(y.issubset(x))            ##Output:False


##                     Python Set issuperset() Method
'''The issuperset() method returns True if all items in the specified set exists in the original set,
otherwise it retuns False.

Syntax  :   set.issuperset(set)    -----> returns True or False'''

##Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
print(x.issuperset(y))          ##Output:True












