##          Python range() does not return an iterator

range() :

Python range function generates a list of numbers which are generally used
in many situation for iteration as in for loop or in many other cases. In python range
objects are not iterators. range is a class of a list of immutable objects. The iteration
behavior of range is similar to iteration behavior of list in list and range we can not
directly call next function. We can call next if we get an iterator using iter.


# Python program to understand range 
demo = range(6) 

print(demo) 
# it will generate error 
print(next(demo)) 

#Output:
range(0, 6)
Traceback (most recent call last):
  File "C:\Users\dell\Desktop\python\demo.py", line 5, in <module>
    print(next(demo))
TypeError: 'range' object is not an iterator


'''Note : Above runtime error clearly indicates that python range is not a iterator.'''

Because range is iterable so we can get a iterator with the help of them but we can not
directly call next in next. Below example explains it clearly


# Python program to understand range 

# creates an iterator 
demo = iter(range(6)) 

# print iterator 
print(demo) 

# use next 
print(next(demo)) 


#Output:
<listiterator object at 0x7f3f32a46450 >
0


# Python program to understand range 

# creates a demo range 
demo = range(1, 31, 2) 

# print the range 
print(demo) 

# print the start of range 
print(demo.start) 

# print step of range 
print(demo.step) 

# print the index of element 23 
print(demo.index(23)) 

# since 30 is not present it will give error 
print(demo.index(30)) 


#Output:
range(1, 31, 2)
1
2
11

 Traceback (most recent call last):
  File "/home/cddaae6552d1d9288d7c5ab503c54642.py", line 19, in 
    print(demo.index(30))
ValueError: 30 is not in range



