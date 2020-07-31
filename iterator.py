##                  Iterators in Python

Iterator in python is any python type that can be used with a ‘for in loop’.
Python lists, tuples, dicts and sets are all examples of inbuilt iterators.
These types are iterators because they implement following methods. In fact,
any object that wants to be an iterator must implement following methods.

__iter__ method that is called on initialization of an iterator. This should
return an object that has a next or __next__ (in Python 3) method.
next ( __next__ in Python 3) The iterator next method should return the next
value for the iterable. When an iterator is used with a ‘for in’ loop, the for
loop implicitly calls next() on the iterator object. This method should raise
a StopIteration to signal the end of the iteration.

# Here is an example of a python inbuilt iterator 
# value can be anything which can be iterate 
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value) 

while True: 
	try: 

		# Iterate by calling next 
		item = next(iterable_obj) 
		print(item) 
	except StopIteration: 

		# exception will happen when iteration will over 
		break

# Output:
G                                                                                                                                                                            
e                                                                                                                                                                            
e                                                                                                                                                                            
k                                                                                                                                                                            
s

# A simple Python program to demonstrate 
# working of iterators using an example type 
# that iterates from 0 to given value 

# An iterable user defined type 
class Test:
    def __init__(self,end):
        self.start = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start<=self.end:
            self.start+=1
            return self.start-1
        if self.start>self.end:
            raise StopIteration

# Prints numbers from 0 to 10
for i in Test(10): 
	print(i) 

# Output:
0
1
2
3
4
5
6
7
8
9
10

# A simple Python program to demonstrate 
# working of iterators using an example type 
# that iterates from 10 to given value 

# An iterable user defined type 
class Test: 

	# Cosntructor 
	def __init__(self, limit): 
		self.limit = limit 

	# Called when iteration is initialized 
	def __iter__(self): 
		self.x = 10
		return self

	# To move to next element. In Python 3, 
	# we should replace next with __next__ 
	def __next__(self): 

		# Store current value ofx 
		x = self.x 

		# Stop iteration if limit is reached 
		if x > self.limit: 
			raise StopIteration 

		# Else increment and return old value 
		self.x = x + 1; 
		return x 

# Prints numbers from 10 to 15 
for i in Test(15): 
	print(i) 

# Output:
10
11
12
13
14
15
