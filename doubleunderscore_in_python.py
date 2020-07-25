                            '''Double Underscore(__)'''

##          __leading_double_underscore

Leading double underscore tell python interpreter to rewrite name in order to avoid conflict in subclass.
Interpreter changes variable name with class extension and that feature known as the Mangling.

testFile.py
class Myclass(): 
	def __init__(self): 
		self.__variable = 10


Calling from Interpreter

>>> import testFile 
>>> obj = testFile.Myclass() 
>>> obj.__variable 
Traceback (most recent call last): 
File "", line 1, in
AttributeError: Myclass instance has no attribute '__variable'
nce has no attribute 'Myclass'
>>> obj._Myclass__variable 
10


In Mangling python interpreter modify variable name with ___. So Multiple time It use as the Private member
because another class can not access that variable directly.
Main purpose for __ is to use variable/method in class only If you want to use it outside of the class you
can make public api

class Myclass(): 
	def __init__(self): 
		self.__variable = 10
	def func(self) 
		print self.__variable 

Calling from Interpreter:

>>> import testFile 
>>> obj = testFile.Myclass() 
>>> obj.func() 
10


##                      __BEFORE_AFTER__
Name with start with __ and ends with same considers special methods in Python. Python provide this methods
to use it as the operator overloading depending on the user.
Python provides this convention to differentiate between the user defined function with the module’s function

class Myclass(): 
    def __add__(self,a,b): 
        print a*b 

Calling from Interpreter
>>> import testFile 
>>> obj = testFile.Myclass() 
>>> obj.__add__(1,2) 
2
>>> obj.__add__(5,2) 
10

