##          Difference between == and is operator in Python

The == operator compares the values of both the operands and checks for value equality.
Whereas is operator checks whether both the operands refer to the same object or not.

# python3 code to illustrate the difference between == and is operator 

list1 = [] 
list2 = [] 
list3=list1 

if (list1 == list2): 
	print("True") 
else: 
	print("False") 

##Output: True
'''Output of the first if condition is “True” as both list1 and list2 are empty lists.'''

if (list1 is list2): 
	print("True") 
else: 
	print("False") 

##Output: False
'''Second if condition shows “False” because two empty lists are at different memory locations.
Hence list1 and list2 refer to different objects. We can check it with id() function in python
which returns the “identity” of an object.'''

if (list1 is list3): 
	print("True") 
else:	 
	print("False") 

##Output: True
'''Output of the third if condition is “True” as both list1 and list3 are pointing to the same object.'''

list3 = list3 + list2 

if (list1 is list3): 
	print("True") 
else:	 
	print("False") 

##Output: False
'''Output of the fourth if condition is “False” because concatenation of two list is always produce a new list.'''


list1 = [] 
list2 = [] 

print(id(list1))            ##Output: 139877155242696
print(id(list2))            ##Output: 139877155253640
'''This shows list1 and list2 refers to different objects.'''


##                                              PYTHON is OPERATOR
1. Immutable data type : Integer ,string, tuple, bool
2. Mutable data type : List,Set,Dictionary

If x and y has mutable data type and both are representing same value,
then ---> x is y return True  

If x and y has immutable data type and both are representing same value,
then ---> x is y return False

Examples:
x = 5;y=5
print (x is y)                  ##Output: True

x= 'abc';y='abc'
print (x is y)                  ##Output: True

x= ('abc',2);y=('abc',2)
print (x is y)                  ##Output: True

x = 1>0;y = 5>0
print (x is y)                  ##Output: True

x = {1,2,3};y = {1,2,3}
print (x is y)                  ##Output:False

x = [1,2,3];y = [1,2,3]
print (x is y)                  ##Output: False

x = {'a':1,'b':2};y ={'a':1,'b':2}
print (x is y)                  ##Output: False
