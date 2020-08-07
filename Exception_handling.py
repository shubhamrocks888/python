'''Error in Python can be of two types i.e. Syntax errors and Exceptions.
Errors are the problems in a program due to which the program will stop the execution.
On the other hand, exceptions are raised when some internal events occur which changes
the normal flow of the program.'''

##                                        The difference between Syntax Error and Exceptions

##'''-->Syntax Error:'''

amount = 10000
 if(amount>2999) 
	print("You are eligible to purchase Dsa Self Paced")

'''O/P---->Syntax Error: invalid syntax'''

##'''Exceptions: Exceptions are raised when the program is syntactically correct but the
##code resulted in an error.This error does not stop the execution of the program, however,
##it changes the normal flow of the program.


marks = 10000

# perform division with 0 
a = marks / 0
print(a) 

'''O/P--->ZeroDivisionError : division by zero'''

##                                        Try and Except in Exception Handling

marks=1000
try:
    marks/0
    print ("Divided successully")
except ZeroDivisionError:
    print ("division not happpened")

##              OR

marks=1000
try:
    if marks/0:                                                             
        print ("Divided successully")
except ZeroDivisionError:
    print ("division not happpened")

'''O/P---->division not happpened'''
##--->    Same goes for IndexError

##Handle multiple exceptions: except(NameError,ZeroDivisionError):

# Program to handle multiple errors with one except statement 
try :  
    a = 3
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print ("Value of b = ", b) 
  
# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
    print ("\nError Occurred and Handled")

'''Output:
Error Occurred and Handled

If you change the value of ‘a’ to greater than or equal to 4, the output will be

Value of b =  
Error Occurred and Handled
The output above is so because as soon as python tries to access the value of b, NameError occurs.'''


##                                               Else Clause


'''In python, you can also use else clause on the try-except block which must be present after
all the except clauses. The code enters the else block only if the try clause does not raise an exception.'''

# Program to depict else clause with try-except 

# Function which returns a/b 
def AbyB(a , b): 
	try: 
		c = ((a+b) / (a-b)) 
	except ZeroDivisionError: 
		print ("a/b result in 0")
	else: 
		print (c) 

# Driver program to test above function 
AbyB(2.0, 3.0) 
AbyB(3.0, 3.0) 

##The output for above program will be :
'''-5.0
a/b result in 0'''


##                                               Finally Keyword in Python


'''Python provides a keyword finally, which is always executed after try and except blocks.
The finally block always executes after normal termination of try block or after try block
terminates due to some exception.'''

##Syntax:
##try:
##       # Some Code.... 
##
##except:
##       # optional block
##       # Handling of exception (if required)
##
##else:
##       # execute if no exception
##
##finally:
##      # Some code .....(always executed)
##


# Python program to demonstrate finally 
	
# No exception Exception raised in try block 
try: 
	k = 5//0 # raises divide by zero exception. 
	print(k) 
	
# handles zerodivision exception	 
except ZeroDivisionError:	 
	print("Can't divide by zero") 
		
finally: 
	# this block is always executed 
	# regardless of exception generation. 
	print('This is always executed')

##Output:
'''Can't divide by zero
This is always executed'''

##Example:
try:
    print("yes")
finally:
    print ("no")

##Output:
'''yes
no'''

##Example:
try:
       print("yes")
else:
       print("no")

##Output:
'''raises an error'''

       
       




##                                                       Raising Exception


'''The raise statement allows the programmer to force a specific exception to occur.
The sole argument in raise indicates the exception to be raised. This must be either
an exception instance or an exception class (a class that derives from Exception).'''

# Program to depict Raising Exception 

try: 
	raise NameError("Hi there") # Raise Error 
except NameError: 
	print "An exception"
	raise # To determine whether the exception was raised or not 

'''The output of the above code will simply line printed as “An exception” but a Runtime error
will also occur in the last due to raise statement in the last line. So, the output on your
command line will look like:'''

##Traceback (most recent call last):
##  File "003dff3d748c75816b7f849be98b91b8.py", line 4, in 
##    raise NameError("Hi there") # Raise Error
##NameError: Hi there

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

##Output:
'''Traceback (most recent call last):
  File "C:\Users\dell\Desktop\python\demo.py", line 39, in <module>
    raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero'''

##Example:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

##Output:
'''Traceback (most recent call last):
  File "C:\Users\dell\Desktop\python\demo.py", line 39, in <module>
    raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed'''
