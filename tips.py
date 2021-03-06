x = 08
print (x)
#Output:
SyntaxError : leading zeros in decimal integer literals are not permitted

#                       is used for single line comment in Python

""" this is a comment """ is used for multi line comments

'''Declared using Continuation Character (\):'''
##s = 1 + 2 + 3 + \
##    4 + 5 + 6 + \
##    7 + 8 + 9

'''Declared using parentheses () : '''
##n = (1 * 2 * 3 + 7 + 8 + 9)

'''Declared using square brackets [] :'''
##footballer = ['MESSI',
##          'NEYMAR',
##          'SUAREZ']

'''Declared using braces {} :'''
##x = {1 + 2 + 3 + 4 + 5 + 6 +
##     7 + 8 + 9}

'''Declared using semicolons(;) :'''
##flag = 2; ropes = 3; pole = 4
######

##2.                Print without newline in Python 3.x

'''Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

Parameters:
value(s) : Any value, and as many as you like. Will be converted to string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

Returns: It returns output to the screen.'''

print('G','F','G')              returns G F G
print('G','F','G',sep='')       returns GFG


 
for i in range(1, 5): 
	for j in range(i): 
		print(i, end=' ') 
	print()

##Output:
1 
2 2 
3 3 3 
4 4 4 4

for i in range(1, 5): 
	for j in range(i): 
		print(i, end=' ') 
	print('\n')

##Output:
1 

2 2 

3 3 3 

4 4 4 4 

for i in range(1, 5): 
	for j in range(i): 
		print(i, end=' ') 
	print(end='\n')

##Output:
1 
2 2 
3 3 3 
4 4 4 4

NOTE: print () and print (end='\n') both are same 


##3.                Reversing the string and list

x = "hello"
y = [1,2,3,4]
print (x[::-1])
print (y[::-1])


##4.            Floor division directly

print (5/2)                 returns 2.5
print (5//2)                returns 2


##5.    Print The File Path Of Imported Modules.

import os 
import socket 

print(os) 
print(socket) 

#Output:
<module 'os' from 'C:\\Python\\lib\\os.py'>
<module 'socket' from 'C:\\Python\\lib\\socket.py'>


##6.     Use Of Enums In Python.

x,y,z = range(3)
print (x,y,z)                  
#Output:0 1 2

##7.    Find The Most Frequent Value In A List.

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count))
#Output: 4


##8.Check The Memory Usage Of An Object.

import sys 
x = 1
print(sys.getsizeof(x)) 
#Output: 14


##9. Print string N times.
n = 2
a = "GeeksforGeeks"
print(a * n)
#Output: GeeksforGeeksGeeksforGeeks


##10.   Checking if two words are anagrams

from collections import Counter 
def is_anagram(str1, str2): 
	return Counter(str1) == Counter(str2) 

# or without having to import anything 
def is_anagram(str1, str2): 
	return sorted(str1) == sorted(str2) 

print(is_anagram('geek', 'eegk')) 
print(is_anagram('geek', 'peek'))


##11.   Transposing a Matrix

l = [[1,2,3],[4,5,6],[7,8,9]]
print (list(zip(*l)))
#Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


##12.   Store all three values of the list in 3 new variables
l = [1,2,3]
x,y,z = l
print (x,y,z)
#Output: 1 2 3


##13.     Create a single string from all the elements in list above.
a = ["Code", "mentor", "Python", "Developer"]
print ("".join(a))
#Output: CodementorPythonDeveloper


##14
l1 = ['a', 'b', 'c', 'd']
l2 = ['p', 'q', 'r', 's']
Write a Python code to print
ap
bq
cr
ds

for i in zip(l1,l2):
    print(i[0],i[1],sep="")
'''OR'''
for i,j in zip(l1,l2):
        print (i,j,sep="")


##15.   Print "codecodecodecode mentormentormentormentormentor" without using loops
print ("code"*4 + " " + "mentor"*5)  
##                '''OR'''
print ("code"*4,"mentor"*5)  


##16.
a = [[1, 2], [3, 4], [5, 6]]
Convert it to a single list without using any loops.
Output:- [1, 2, 3, 4, 5, 6]

import itertools 
list(itertools.chain.from_iterable(a))



