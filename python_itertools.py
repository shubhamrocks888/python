Python’s Itertool is a module that provides various functions that work on
iterators to produce complex iterators. This module works as a fast, memory-
efficient tool that is used either by themselves or in combination to form
iterator algebra.

Different types of iterators provided by this module are:

##                        Infinite iterators
Iterator in Python is any Python type that can be used with a ‘for in loop’.
Python lists, tuples, dictionaries, and sets are all examples of inbuilt
iterators. But it is not necessary that an iterator object has to exhaust,
sometimes it can be infinite. Such type of iterators are known as Infinite iterators.

Python provides three types of infinite itertors:

1. '''count(start, step)''':
    This iterator starts printing from the “start” number and prints
    infinitely. If steps are mentioned, the numbers are skipped else step is 1 by default.
    See the below example for its use with for in loop.

Example:

import itertools

for i in itertools.count(5,5):
    print (i,end=" ")
##  Output: 5 10 15 20 25 30 35 40 45 50 ...........infinite output

for i in itertools.count(5,5):
    if i == 35:
        break
    else:
        print (i,end=" ")
##  Output: 5 10 15 20 25 30

2. '''cycle(iterable):'''
    This iterator prints all values in order from the passed container. It restarts
    printing from the beginning again when all elements are printed in a cyclic manner.

Example 1:

import itertools

count=0
for i in itertools.cycle('abcd'):
    if count==8:
        break
    else:
        print (i,end=" ")
        count+=1
##  Output: a b c d a b c d 


Example 2: Using next function.

import itertools 
l = ['a','b','c'] 
	
# defining iterator 
iterators = itertools.cycle(l) 
	
# for in loop 
for i in range(6): 
		
	# Using next function 
	print(next(iterators), end = " ") 
##  Output: a b c a b c

##if we dont define the iterator,then output will different
print(next(itertools.cycle(l)),end = " ")
##  Output: a a a a a a 

3. '''repeat(val,num)''':
    This iterator repeatedly prints the passed value infinite number of times.
    If the optional keyword num is mentioned, then it repeatedly prints num number of times.

import itertools 
	
# using repeat() to repeatedly print number 
print (list(itertools.repeat(25, 4)))
##  Output: [25, 25, 25, 25]
