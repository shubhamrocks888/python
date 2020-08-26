##          Python | Difference between iterable and iterator

Iterable is an object, which one can iterate over. It generates an Iterator
when passed to iter() method. Iterator is an object, which is used to iterate
over an iterable object using __next__() method. Iterators have __next__() method,
which returns the next item of the object.

Note that every iterator is also an iterable, but not every iterable is an iterator.
For example, a list is iterable but a list is not an iterator. An iterator can be created
from an iterable by using the function iter(). To make this possible, the class of an object
needs either a method __iter__, which returns an iterator, or a __getitem__ method with
sequential indexes starting with 0.

for city in ["Berlin", "Vienna", "Zurich"]: 
    print(city)

When a for loop is executed, for statement calls iter() on the object, which it is supposed to
loop over. If this call is successful, the iter call will return an iterator object that defines
the method __next__(), which accesses elements of the object one at a time. The __next__() method
will raise a StopIteration exception, if there are no further elements available. The for loop will
terminate as soon as it catches a StopIteration exception.

# list of cities 
cities = ["Berlin", "Vienna", "Zurich"] 

# initialize the object 
iterator_obj = iter(cities) 

print(next(iterator_obj)) 
print(next(iterator_obj)) 
print(next(iterator_obj))
print(next(iterator_obj))

#Output:
Berlin
Vienna
Zurich
Traceback (most recent call last):
  File "C:\Users\dell\Desktop\python\demo.py", line 7, in <module>
    print (next(iterator))
StopIteration



Code #3 : Check object is iterable or not
# Function to check object 
# is iterable or not 
def iterable(obj): 
	try: 
		iter(obj) 
		return True
		
	except TypeError: 
		return False

# Driver Code	 
for element in [34, [4, 5], (4, 5), 
			{"a":4}, "dfsdf", 4.5]: 
				
	print(element, " is iterable : ", iterable(element)) 

#Output:
34  is iterable :  False
[4, 5]  is iterable :  True
(4, 5)  is iterable :  True
{'a': 4}  is iterable :  True
dfsdf  is iterable :  True
4.5  is iterable :  False
