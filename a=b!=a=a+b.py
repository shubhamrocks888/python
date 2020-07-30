In python a += b doesn’t always behave the same way as a = a + b,
same operands may give the different results under different conditions.

##Example 1
list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 += [1, 2, 3, 4] 

print(list1)        ##Output: [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list2)        ##Output: [5, 4, 3, 2, 1, 1, 2, 3, 4]

##Example 2
list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 = list1 + [1, 2, 3, 4] 

# Contents of list1 are same as above 
# program, but contents of list2 are 
# different. 
print(list1)        ##Output: [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list2)        ##Output: [5, 4, 3, 2, 1]


expression list1 += [1, 2, 3, 4] modifies the list in-place, means it
extends the list such that “list1” and “list2” still have the reference to the same list.

expression list1 = list1 + [1, 2, 3, 4] creates a new list and changes “list1”
reference to that new list and “list2” still refer to the old list.
