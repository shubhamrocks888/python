##                          When to use yield instead of return in Python?

'''The yield statement suspends function’s execution and sends a value back to the caller,
but retains enough state to enable function to resume where it is left off. When resumed,
the function continues execution immediately after the last yield run. This allows its code
to produce a series of values over time, rather than computing them at once and sending them back like a list.'''

# A Simple Python program to demonstrate working 
# of yield 

# A generator function that yields 1 for the first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value) 

##Output:
##
##1
##2
##3

'''Return sends a specified value back to its caller whereas
Yield can produce a sequence of values. We should use yield
when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. A generator function is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield keyword rather than return.
If the body of a def contains yield, the function automatically becomes a generator function.'''



# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 

# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
	i = 1; 

	# An Infinite loop to generate squares 
	while True: 
		yield i*i				 
		i += 1 # Next execution resumes 
				# from this point	 

# Driver code to test above generator 
# function 
for num in nextSquare(): 
	if num > 100: 
		break	
	print(num)


##                                                Generator-Object : 
Generator functions return a generator object. Generator objects are used either by calling the
next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).

# A Python program to demonstrate use of 
# generator object with next() 

# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 
print(x.__next__()) # Or, next(x) 
print(x.__next__()) 
print(x.__next__()) 

