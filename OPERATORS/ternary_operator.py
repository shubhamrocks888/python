##                                              Ternary Operator in Python

Ternary operators also known as conditional expressions are operators that evaluate
something based on a condition being true or false.

It simply allows to test a condition in a single line replacing the multiline
if-else making the code compact.

Syntax : [on_true] if [expression] else [on_false]

##1.    Simple Method to use ternary operator:
a, b = 10, 20
min = a if a < b else b 
print(min) 
Output: 10

##2.    Direct Method by using tuples, Dictionary and lambda

# Python program to demonstrate ternary operator 
a, b = 10, 20

# Use tuple for selecting an item 
# (if_test_false,if_test_true)[test] 
print( (b, a) [a < b] ) 

# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 

# lamda is more efficient than above two methods 
# because in lambda we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]()) 

Output:
10
10
10

##3.    Ternary operator can be written as nested if-else:

# Python program to demonstrate nested ternary operator 
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a") 

Above approach can be written as:

# Python program to demonstrate nested ternary operator 
a, b = 10, 20

if a != b: 
	if a > b: 
		print("a is greater than b") 
	else: 
		print("b is greater than a") 
else: 
	print("Both a and b are equal") 

Output: b is greater than a
