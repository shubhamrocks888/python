##                        Operator Overloading in Python

Operator Overloading means giving extended meaning beyond their predefined operational meaning.
For example operator + is used to add two integers as well as join two strings and merge two lists.
It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed
that the same built-in operator or function shows different behavior for objects of different classes,
this is called Operator Overloading.

# Python program to show use of 
# + operator for different purposes. 

print(1 + 2)            # Output:  3

# concatenate two strings 
print("Geeks"+"For")    # Output: GeeksFor

# Product two numbers 
print(3 * 4)            # Output: 4

# Repeat the String 
print("Geeks"*4)        # Output: GeeksGeeksGeeksGeeks

##                    How to overload the operators in Python?

Consider that we have two objects which are a physical representation of a class (user-defined data type)
and we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how
to add two objects. So we define a method for an operator and that process is called operator overloading.
We can overload all existing operators but we can’t create a new operator. To perform operator overloading,
Python provides some special function or magic function that is automatically invoked when it is associated
with that particular operator. For example, when we use + operator, the magic method __add__ is automatically
invoked in which the operation for + operator is defined.

# Python Program illustrate how 
# to overload an binary + operator 

class A: 
	def __init__(self, a): 
		self.a = a 

	# adding two objects 
	def __add__(self, o): 
		return self.a + o.a 
ob1 = A(1) 
ob2 = A(2) 
ob3 = A("Geeks") 
ob4 = A("For") 

print(ob1 + ob2)        # Output:  3
print(ob3 + ob4)        # Output:  GeeeksFor

# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading. 

class complex: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	# adding two objects 
	def __add__(self, other): 
		return self.a + other.a, self.b + other.b 

	def __str__(self): 
		return self.a, self.b 

Ob1 = complex(1, 2) 
Ob2 = complex(2, 3) 
Ob3 = Ob1 + Ob2 
print(Ob3)              # Output: (3, 5)

# Python program to overload 
# a comparison operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __gt__(self, other): 
		if(self.a>other.a): 
			return True
		else: 
			return False
ob1 = A(2) 
ob2 = A(3) 
if(ob1>ob2): 
	print("ob1 is greater than ob2") 
else: 
	print("ob2 is greater than ob1") 

# Output:
ob2 is greater than ob1

# Python program to overload equality 
# and less than operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __lt__(self, other): 
		if(self.a<other.a): 
			return "ob1 is lessthan ob2"
		else: 
			return "ob2 is less than ob1"
	def __eq__(self, other): 
		if(self.a == other.a): 
			return "Both are equal"
		else: 
			return "Not equal"
				
ob1 = A(2) 
ob2 = A(3) 
print(ob1 < ob2)            # Output: ob1 is lessthan ob2

ob3 = A(4) 
ob4 = A(4) 
print(ob1 == ob2)           # Output: Not equal



