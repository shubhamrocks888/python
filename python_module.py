##                      Python Modules

A module is a file containing Python definitions and statements. A module can define functions,
classes and variables. A module can also include runnable code. Grouping related code into a
module makes the code easier to understand and use.

Example:

# A simple module, calc.py 
def add(x, y): 
	return (x+y) 

def subtract(x, y): 
	return (x-y) 


                '''The import statement'''

We can use any Python source file as a module by executing an import statement in some other Python source file.
When interpreter encounters an import statement, it imports the module if the module is present in the search path.
A search path is a list of directories that the interpreter searches for importing a module. For example, to import
the module calc.py, we need to put the following command at the top of the script :

# importing module calc.py 
import calc 

print add(10, 2) 

##Output: 12


                '''The from import Statement'''

Python’s from statement lets you import specific attributes from a module. The from .. import .. has the following syntax :

# importing sqrt() and factorial from the 
# module math 
from math import sqrt, factorial 

# if we simply do "import math", then 
# math.sqrt(16) and math.factorial() 
# are required. 
print sqrt(16) 
print factorial(6) 

##Output: 12
4.0
720


                    '''The dir() function'''

The dir() built-in function returns a sorted list of strings containing the names defined by a module. The list contains the
names of all the modules, variables and functions that are defined in a module.

# Import built-in module random 
import random 
print dir(random) 

##Output:
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 
'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'WichmannHill', 
'_BuiltinMethodType', '_MethodType', '__all__', 
'__builtins__', '__doc__', '__file__', '__name__', 
'__package__', '_acos', '_ceil', '_cos', '_e', '_exp', 
'_hashlib', '_hexlify', '_inst', '_log', '_pi', '_random',
'_sin', '_sqrt', '_test', '_test_generator', '_urandom',
'_warn', 'betavariate', 'choice', 'division', 
'expovariate', 'gammavariate', 'gauss', 'getrandbits',
'getstate', 'jumpahead', 'lognormvariate', 'normalvariate',
'paretovariate', 'randint', 'random', 'randrange', 
'sample', 'seed', 'setstate', 'shuffle', 'triangular', 
'uniform', 'vonmisesvariate', 'weibullvariate']
