##          Function Decorators in Python | Set 1 (Introduction)

                        '''Background'''
Following are important facts about functions in Python that are useful to understand decorator functions.
In Python, we can define a function inside another function.
In Python, a function can be passed as parameter to another function (a function can also return another function).
filter_none

def messageWithWelcome(str): 

        def addWelcome():
                return "Welcome to "

        return addWelcome() + str


def site(site_name): 
	return site_name 

print (messageWithWelcome(site("GeeksforGeeks")))
## Output: Welcome to GeeksforGeeks

    
##                                Function Decorator
A decorator is a function that takes a function as its only parameter and returns a function. This is
helpful to “wrap” functionality with the same code over and over again. For example, above code can bere-written as following.
We use @func_name to specify a decorator to be applied on another function.

'''Example 1''':
def outer(fun):

        def inner():
                return "welcome to " + fun()

        return inner

@outer
def fun():
        return "club"

print (fun())
## Output: welcome to club


'''Example 2''':
def messagewithwelcome(site): 

        def addWelcome(site_name):
                return "Welcome to " + site(site_name)

        return addWelcome

@messagewithwelcome
def site(site_name): 
	return site_name

print (site("GeeksforGeeks")) 
## Output: Welcome to GeeksforGeeks

'''Example 3''':
# Adds a welcome message to the string 
# returned by fun(). Takes fun() as 
# parameter and returns welcome(). 
def decorate_message(fun): 

	# Nested function 
	def addWelcome(site_name): 
		return "Welcome to " + fun(site_name) 

	# Decorator returns a function 
	return addWelcome 

@decorate_message
def site(site_name): 
	return site_name; 

# Driver code 

# This call is equivalent to call to 
# decorate_message() with function 
# site("GeeksforGeeks") as parameter 
print (site("GeeksforGeeks")) 
## Output: Welcome to GeeksforGeeks


##              Decorators can also be useful to attach data (or add attribute) to functions.

# A Python example to demonstrate that 
# decorators can be useful attach data 

# A decorator function to attach 
# data to func 
def attach_data(func): 
	func.data = 3
	return func 

@attach_data
def add (x, y): 
	return x + y 

# Driver code 

# This call is equivalent to attach_data() 
# with add() as parameter 
print(add(2, 3)) 
print(add.data) 

## Output:
'''
5
3
'''
