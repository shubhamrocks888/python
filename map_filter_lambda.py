'''1.lambda    :   Python provides the ability to create a simple (no statements allowed internally) anonymous
                inline function called lambda function. Using lambda and map you can have two for loops in one line.
                                                    OR
                A lambda function is a small anonymous function.
                A lambda function can take any number of arguments, but can only have one expression.'''

x = lambda a:a+2
print (x(5))

y = lambda a,b:a*b
print (y(2,3))

z = lambda a,b,c:a+b+c
print(z(1,2,3))

##                                      Why Use Lambda Functions?
'''The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:'''

def myfunc(n):
    return lambda a:a*n

mydoubler = myfunc(5)
print(mydoubler(2))

##                                      MAP FUNCTION?

'''2.map   :   The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.

Syntax  :  map(function, iterables)

Parameter Values:

Parameter     Description

function      Required. The function to execute for each item
iterable      Required. A sequence, collection or an iterator object. You can send as many iterables as you like,
              just make sure the function has one parameter for each iterable.'''

def my_func(n):
    return len(n)

x = map(my_func,('apple','banana','orange'))
print(list(x))

def my_funcc(a, b):
  return a + b

x = map(my_funcc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

##                                      FILTER Function?

ages = [5, 12, 17, 18, 24, 32]

def age(x):
    if x>18:
        return x
z = list(filter(age,ages))
print (z)

        
    

    
