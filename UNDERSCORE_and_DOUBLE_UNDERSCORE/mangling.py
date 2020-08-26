##                            Name mangling in Python

In name mangling process any identifier with two leading underscore and one trailing underscore
is textually replaced with _classname__identifier where classname is the name of the current class.
It means that any identifier of the form __geek (at least two leading underscores or at most one
trailing underscore) is replaced with _classname__geek, where classname is the current class name
with leading underscore(s) stripped.

# Python program to demonstrate 
# name mangling 


class Student: 
	def __init__(self, name): 
		self.__name = name 

	def displayName(self): 
		print(self.__name) 

s1 = Student("Santhosh") 
s1.displayName()                # Output: Santosh

# Raises an error 
print(s1.__name)

# Output:
Traceback (most recent call last):
  File "/home/be691046ea08cd2db075d27186ea0493.py", line 14, in 
    print(s1.__name)
AttributeError: 'Student' object has no attribute '__name'

In the above example, the class variable __name is not accessible outside the class.
It can be accessed only within the class. Any modification of the class variable can be done
only inside the class.



                            ##Accessing Name Mangled variables
The name mangling process helps to access the class variables from outside the class. The class
variables can be accessed by adding _classname to it. The name mangling is closest to private not exactly private.

# Python program to demonstrate 
# name mangling 


class Student: 
	def __init__(self, name): 
		self.__name = name 

s1 = Student("Santhosh") 
print(s1._Student__name)        # Output: Santosh

