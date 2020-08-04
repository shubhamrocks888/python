##          Precision Handling in Python

Python in its definition allows to handle precision of floating point numbers in several
ways using different functions. Most of them are defined under the “math” module. Some
of the most used operations are discussed in this article.

1. trunc() :- This function is used to eliminate all decimal part of the floating point number and return the integer without the decimal part.

2. ceil() :- This function is used to print the least integer greater than the given number.

3. floor() :- This function is used to print the greatest integer smaller than the given integer.

# Python code to demonstrate ceil(), trunc() 
# and floor() 

# importing "math" for precision function 
import math 

# initializing value 
a = 3.4536

# using trunc() to print integer after truncating 
print ("The integral value of number is : ",end="") 
print (math.trunc(a)) 

# using ceil() to print number after ceiling 
print ("The smallest integer greater than number is : ",end="") 
print (math.ceil(a)) 

# using floor() to print number after flooring 
print ("The greatest integer smaller than number is : ",end="") 
print (math.floor(a)) 

# Output:
The integral value of number is : 3
The smallest integer greater than number is : 4
The greatest integer smaller than number is : 3
