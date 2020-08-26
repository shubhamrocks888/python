##                                        Single Underscore

1.                            `             In Interpreter:

_ returns the value of last executed expression value in Python Prompt/Interpreter.

>>> a = 10
>>> b = 10
>>> _ 
Traceback (most recent call last): 
File "<stdin>", line 1, in <module> 
NameError: name '_' is not defined 
>>> a+b 
20
>>> _ 
20
>>> _ * 2
40
>>> _ 
40
>>> _ / 2
20


2.                                      For Ignoring Values

Multiple time we do not want return values at that time assign those values to Underscore.
It used as throwaway variable.

# Ignore a value of specific location/index 
for _ in range(10) 
	print "Test"

# Ignore a value when unpacking 
a,b,_,_ = (1,2,3,4)


3.                                      After a name

Python has their by default keywords which we can not use as the variable name.
To avoid such conflict between python keyword and variable we use underscore after name

>>> class MyClass(): 
...	 def __init__(self): 
...			 print "OWK"

>>> def my_defination(var1 = 1, class_ = MyClass): 
...	 print var1 
...	 print class_

>>> my_defination() 
1
__main__.MyClass 
>>> 


4.                                      Before a name

Leading Underscore before variable/function/method name indicates to programmer that It is
for internal use only, that can be modified whenever class want.
Here name prefix by underscore is treated as non-public. If specify from Import * all the
name starts with _ will not import. Python does not specify truly private so this ones can
be call directly from other modules if it is specified in __all__, We also call it weak Private

class Prefix: 
...	 def __init__(self): 
...			 self.public = 10
...			 self._private = 12
>>> test = Prefix() 
>>> test.public 
10
>>> test._private 
12

Python class_file.py
def public_api(): 
	print "public api"

def _private_api(): 
	print "private api"

Calling file from Prompt
>>> from class_file import *
>>> public_api() 
public api 

>>> _private_api() 
Traceback (most recent call last): 
File "<stdin>", line 1, in <module> 
NameError: name '_private_api' is not defined 

>>> import class_file 
>>> class_file.public_api() 
public api 
>>> class_file._private_api() 
private api 





