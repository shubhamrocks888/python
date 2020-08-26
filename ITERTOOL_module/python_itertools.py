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


##                      Combinatoric iterators

The recursive generators that are used to simplify combinatorial constructs such as permutations,
combinations, and Cartesian products are called combinatoric iterators.

In Python there are 4 combinatoric iterators:

1. '''Product()''':
    This tool computes the cartesian product of input iterables. To compute the product of an
    iterable with itself, we use the optional repeat keyword argument to specify the number of
    repetitions. The output of this function are tuples in sorted order.

Example:
from itertools import product 
	 
print(list(product([1, 2])))
##Output: [(1,), (2,)]        (default:repeat=1)

print(list(product([1, 2],repeat=0)))
##Output: [()]

print(list(product([1, 2],repeat=1)))
##Output: [(1,), (2,)] 

print(list(product([1, 2],repeat=2)))
##Output: [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(product(['geeks', 'for', 'geeks'], '2')))
##Output: [('geeks', '2'), ('for', '2'), ('geeks', '2')]

print(list(product('AB', [3, 4])))
##Output: [('A', 3), ('A', 4), ('B', 3), ('B', 4)]

2. '''Permutations()''':
    Permutations() as the name speaks for itself is used to generate all possible permutations
    of an iterable. All elements are treated as unique based on their position and not their
    values. This function takes an iterable and group_size, if the value of group_size is not
    specified or is equal to None then the value of group_size becomes length of the iterable.

Example:
from itertools import permutations 

print (list(permutations([1, 'geeks'],0)))
##Output: [()]

print (list(permutations([1, 'geeks'],1)))
##Output: [(1,), ('geeks',)]

print (list(permutations([1, 'geeks']))) 
##Output: [(1, 'geeks'), ('geeks', 1)]    (default length is equal to the length of iterable)

print (list(permutations([1, 'geeks'], 2))) 
##Output: [('A', 3), ('A', 4), ('B', 3), ('B', 4)]

print (list(permutations('AB'))) 
##Output: [('A', 'B'), ('B', 'A')] 
	
print(list(permutations(range(3), 2))) 
##Output: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

3. '''Combinations()''':
    This iterator prints all the possible combinations(without replacement) of the container
    passed in arguments in the specified group size in sorted order.

Example:

# import combinations from itertools module 
	
from itertools import combinations 
	
print(list(combinations(['A',2])))
##Output: TypeError: combinations() missing required argument 'r' (pos 2)

print(list(combinations('AB',2),1)) 
##Output: [('A',),(2,)]

print(list(combinations('AB',2),2)) 
##Output: [('A',2)]

print(list(combinations(range(2),1)))
##Output: [(0, ), (1, )]

4. '''Combinations_with_replacement()''':
    This function returns a subsequence of length n from the elements of the iterable where
    n is the argument that the function takes determining the length of the subsequences
    generated by the function. Individual elements may repeat itself in combinations_with_replacement function
	
from itertools import combinations_with_replacement 

print(list(combinations_with_replacement("AB", 2))) 
##Output: [('A', 'A'), ('A', 'B'), ('B', 'B')]

print(list(combinations_with_replacement([1, 2], 2))) 
##Output: [(1, 1), (1, 2), (2, 2)]

print(list(combinations_with_replacement(range(2), 1))) 
##Output: (0, ), (1, )]


##                              Terminating iterators
Terminating iterators are used to work on the short input sequences and produce the output
based on the functionality of the method used.

Different types of terminating iterators are:

1. '''accumulate(iter, func)''':
    This iterator takes two arguments, iterable target and the function which would be followed
    at each iteration of value in target. If no function is passed, addition takes place by default.
    If the input iterable is empty, the output iterable will also be empty.

Example:

import itertools 
import operator 

li1 = [1, 4, 5, 7] 
	
# prints the successive summation of elements 
print (list(itertools.accumulate(li1))) 
# Output: [1, 5, 10, 17]

# prints the successive summation of elements 
print (list(itertools.accumulate(li1,operator.add))) 
# Output: [1, 5, 10, 17]

# prints the successive multiplication of elements 
print (list(itertools.accumulate(li1, operator.mul))) 
# Output:  [1, 4, 20, 140]
	
2. '''chain(iter1, iter2..)''':
    This function is used to print all the values in iterable targets one after another mentioned
    in its arguments.

import itertools 

li1 = [1, 4, 5, 7] 
li2 = [1, 6, 5, 9] 
li3 = [8, 10, 5, 4] 

# using chain() to print all elements of lists 
print ("All values in mentioned chain are : ", end ="") 
print (list(itertools.chain(li1, li2, li3))) 
# Output: [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

3. '''chain.from_iterable()''':
    This function is implemented similarly as chain() but the argument here is a list of lists
    or any other iterable container.

import itertools 

li1 = [1, 4, 5, 7] 
li2 = [1, 6, 5, 9] 
li3 = [8, 10, 5, 4] 

li4 = [li1, li2, li3] 

# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ", end ="") 
print (list(itertools.chain.from_iterable(li4)))
# Output: [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

4. '''compress(iter, selector)''':
    This iterator selectively picks the values to print from the passed container according to the boolean
    list value passed as other arguments. The arguments corresponding to boolean true are printed else all are skipped.

import itertools 

# using compress() selectively print data values 
print ("The compressed values in string are : ", end ="") 
print (list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))) 
# Output: ['G', 'F', 'G']

print (list(itertools.compress('GEEKSFORGEEKS',(1,)))) 
#  Output: ['G']

5. '''dropwhile(func, seq)''':
    This iterator starts printing the characters only after the func. in argument returns false for the first time.

import itertools 
li = [2, 4, 5, 7, 8] 
	
# using dropwhile() to start displaying after condition is false 
print ("The values after condition returns false : ", end ="") 
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li))) 
#  Output: The values after condition returns false : [5, 7, 8]

6. '''filterfalse(func, seq)''':
    As the name suggests, this iterator prints only values that return false for the passed function.

import itertools 
li = [2, 4, 5, 7, 8] 

# using filterfalse() to print false values 
print ("The values that return false to function are : ", end ="") 
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li))) 
#  Output: The values that return false to function are : [5, 7]

7. '''islice(iterable, start, stop, step)''':
    This iterator selectively prints the values mentioned in its iterable container passed as argument.
    This iterator takes 4 arguments, iterable container, starting pos., ending position and step.

import itertools 
li = [2, 4, 5, 7, 8, 10, 20] 
	
# using islice() to slice the list acc. to need 
# starts printing from 2nd index till 6th skipping 2 
print ("The sliced list values are : ", end ="") 
print (list(itertools.islice(li, 1, 6, 2))) 
#  Output: The sliced list values are : [4, 7, 10]

8.'''starmap(func., tuple list)''':
    This iterator takes a function and tuple list as argument and returns the value according to the
    function from each tuple of list.

import itertools 
li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ] 
	
# using starmap() for selection value acc. to function 
# selects min of all tuple values 
print ("The values acc. to function are : ", end ="") 
print (list(itertools.starmap(min, li))) 
#  Output: The values acc. to function are : [1, 1, 4, 1]

9. '''takewhile(func, iterable)''':
    This iterator is opposite of dropwhile(), it prints the values till the function returns false for 1st time.

import itertools 
li = [2, 4, 6, 7, 8, 10, 20] 
	
# using takewhile() to print values till condition is false. 
print ("The list values till 1st false value are : ", end ="") 
print (list(itertools.takewhile(lambda x : x % 2 == 0, li ))) 
#  Output: The list values till 1st false value are : [2, 4, 6]

10. '''tee(iterator, count)''':-
    This iterator splits the container into a number of iterators mentioned in the argument.

import itertools 
li = [2, 4, 6, 7, 8, 10, 20]
iti = iter(li) 
	
# using tee() to make a list of iterators 
# makes list of 3 iterators having same values. 
it = itertools.tee(iti, 3) 
	
# printing the values of iterators 
print ("The iterators are : ") 
for i in range (0, 3): 
	print (list(it[i])) 
#  Output:
'''
[2, 4, 6, 7, 8, 10, 20]
[2, 4, 6, 7, 8, 10, 20]
[2, 4, 6, 7, 8, 10, 20]
'''

11. '''zip_longest( iterable1, iterable2, fillval)''':
    This iterator prints the values of iterables alternatively in sequence. If one of the iterables
    is printed fully, remaining values are filled by the values assigned to fillvalue.

import itertools 
	
# using zip_longest() to combine two iterables. 
print ("The combined values of iterables is : ") 
print (*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' ))) 

#  Output:
'''
The combined values of iterables is  : 
('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')'''
