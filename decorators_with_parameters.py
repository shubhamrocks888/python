##              Decorators with parameters in Python

Syntax for decorators with parameters –

@decorator(params)
def func_name():
    ''' Function implementation'''

The above code is equivalent to

def func_name():
    ''' Function implementation'''

func_name = (decorator(params))(func_name)


# Python code to illustrate 
# Decorators with parameters in Python 

def decorator(*args, **kwargs): 
	print("Inside decorator") 
	
	def inner(func): 
		
		# code functionality here 
		print("Inside inner function") 
		print("I like", kwargs['like']) 
		
		func() 
		
	# reurning inner function	 
	return inner 

@decorator(like = "geeksforgeeks") 
def my_func(): 
	print("Inside actual function") 

# Output:
Inside decorator
Inside inner function
I like geeksforgeeks
Inside actual function




# Python code to illustrate 
# Decorators with parameters in Python 

def decorator_func(x, y): 

	def Inner(func): 

		def wrapper(*args, **kwargs): 
			print("I like Geeksforgeeks") 
			print("Summation of values - {}".format(x+y) ) 

			func(*args, **kwargs) 
			
		return wrapper 
	return Inner 


# Not using decorator 
def my_fun(*args): 
	for ele in args: 
		print(ele) 

# another way of using dacorators 
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks') 

# Output:
I like Geeksforgeeks
Summation of values - 27
Geeks
for
Geeks
