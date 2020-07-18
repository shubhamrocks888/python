'''                                      What is namespace                       '''

##A namespace is a system to have a unique name for each and every object in Python.
##An object might be a variable or a method. Python itself maintains a namespace in
##the form of a Python dictionary. 

'''                                     Types of namespaces :                     '''

##Some functions like print(), id() are always present, these are built in namespaces.
##The built-in namespace encompasses global namespace and global namespace encompasses local namespace.

'''                                     Lifetime of a namespace :                '''

##A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends,
##the lifetime of that namespace comes to an end. Hence, it is not possible to access inner
##namespace’s objects from an outer namespace.

'''Example:'''
# var1 is in the global namespace 
var1 = 5
def some_func(): 

	# var2 is in the local namespace 
	var2 = 6
	def some_inner_func(): 

		# var3 is in the nested local 
		# namespace 
		var3 = 7

'''                                   Scope of Objects in Python :              '''

##Scope refers to the coding region from which particular Python object is accessible.
##Hence one cannot access any particular object from anywhere from the code,the accessing
##has to be allowed by the scope of the object.
##
##Lets take an example to have details understanding of the same:

# Python program showing 
# a scope of object 

def some_func(): 
	print("Inside some_func") 
	def some_inner_func(): 
		var = 10
		print("Inside inner function, value of var:",var) 
	some_inner_func() 
	print("Try printing var from outer function: ",var) 
some_func() 

##Output:

'''Inside some_func
Inside inner function, value of var: 10

Traceback (most recent call last):
  File "/home/1eb47bb3eac2fa36d6bfe5d349dfcb84.py", line 8, in 
    some_func()
  File "/home/1eb47bb3eac2fa36d6bfe5d349dfcb84.py", line 7, in some_func
    print("Try printing var from outer function: ",var)
NameError: name 'var' is not defined'''
