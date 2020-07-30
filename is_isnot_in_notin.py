##  Python Membership and Identity Operators | in, not in, is, is not

1. in           : The ‘in’ operator is used to check if a value exists in a sequence or not.
                 Evaluates to true if it finds a variable in the specified sequence and false otherwise.

# Python program to illustrate 
# Finding common member in list 
# using 'in' operator 
list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
for item in list1: 
	if item in list2: 
		print("overlapping")	 
else: 
	print("not overlapping") 
# Output: not overlapping

2. ‘not in’    : Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

# Python program to illustrate 
# not 'in' operator 
x = 24
y = 20
list = [10, 20, 30, 40, 50 ]; 

if ( x not in list ): 
print("x is NOT present in given list") 
else: 
print("x is present in given list") 

if ( y in list ): 
print("y is present in given list") 
else: 
print("y is NOT present in given list") 

##                        Identity operators

In Python are used to determine whether a value is of a certain class or type. They are usually used to determine
the type of data a certain variable contains.
There are different identity operators such as

1.‘is’      : Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.

# Python program to illustrate the use 
# of 'is' identity operator 
x = 5
if (type(x) is int): 
	print("true") 
else: 
	print("false")
# Output: True

2.‘is not’  :Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.

# Python program to illustrate the 
# use of 'is not' identity operator 
x = 5.2
if (type(x) is not int): 
	print("true") 
else: 
	print("false") 
# Output: True

