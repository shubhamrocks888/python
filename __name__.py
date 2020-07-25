##                      __name__ (A Special variable) in Python

Since there is no main() function in Python, when the command to run a python program
is given to the interpreter, the code that is at level 0 indentation is to be executed. 

__name__ is a built-in variable which evaluates to the name of the current module.
Thus it can be used to check whether the current script is being run on its own or
being imported somewhere else by combining it with if statement, as shown below.

# File1.py 

print "File1 __name__ = %s" %__name__ 

if __name__ == "__main__": 
	print "File1 is being run directly"
else: 
	print "File1 is being imported"

Output :
File1 __name__ = __main__File1 is being run directly

# File2.py 

import File1 

print "File2 __name__ = %s" %__name__ 

if __name__ == "__main__": 
	print "File2 is being run directly"
else: 
	print "File2 is being imported"

Output :
File1 __name__ = File1
File1 is being imported
File2 __name__ = __main__
File2 is being run directly



