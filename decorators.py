##                              Decorators in Python
In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
Functions can be defined inside another function and can also be passed as argument to another function.
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function
or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without
permanently modifying it.

In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

Syntax for Decorator:

@gfg_decorator
def hello_decorator(): 
	print("Gfg") 

## Output: NameError: name 'gfg_decorator' is not defined


'''Above code is equivalent to - 

def hello_decorator(): 
	print("Gfg") 
	
hello_decorator = gfg_decorator(hello_decorator)'''

In the above code, gfg_decorator is a callable function, will add some code on the top of some another callable function,
hello_decorator function and return the wrapper function.


# defining a decorator 
def hello_decorator(func): 

	# inner1 is a Wrapper function in 
	# which the argument is called 
	
	# inner function can access the outer local 
	# functions like in this case "func" 
	def inner1(): 
		print("Hello, this is before function execution") 

		# calling the actual function now 
		# inside the wrapper function. 
		func() 

		print("This is after function execution") 
		
	return inner1 


# defining a function, to be called inside wrapper 
def function_to_be_used(): 
	print("This is inside the function !!") 


# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 


# calling the function
function_to_be_used() 

## Output:
'''
Hello, this is before function execution
This is inside the function !!
This is after function execution
'''


##                      What if a function returns something –

def hello_decorator(func): 
	def inner1(*args, **kwargs): 
		
		print("before Execution") 
		
		# getting the returned value 
		returned_value = func(*args, **kwargs) 
		print("after Execution") 
		
		# returning the value to the original frame 
		return returned_value 
		
	return inner1 


# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
	print("Inside the function") 
	return a + b 

a, b = 1, 2

# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b)) 

## Output:
'''
before Execution
Inside the function
after Execution
Sum = 3
'''
