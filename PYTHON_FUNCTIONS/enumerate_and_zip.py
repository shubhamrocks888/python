##                          Python enumerate() Function

Enumerate is built-in python function that takes input as iterator, list etc and returns a
tuple containing index and data at that index in the iterator sequence.

The enumerate() function adds a counter as the key of the enumerate object.

Syntax: enumerate(iterable, start)

iterable  An iterable object
start	  A Number. Defining the start number of the enumerate object. Default 0

##Example
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print (y)                   ##Output: <enumerate object at 0x03818CA8>
print (list(y))             ##Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars):
    print (x[0],x[1])

##Output:
0 Aston
1 Audi
2 McLaren 

for x in enumerate(cars,6):
    print (x[0],x[1])
##Output:
6 Aston
7 Audi
8 McLaren


##                          Python zip() Function
This function is helpful to combine similar type iterators(list-list or dict- dict etc,)
data items at ith position. It uses the shortest length of these input iterators. Other
items of larger length iterators are skipped. In case of empty iterators, it returns No output

If the passed iterators have different lengths, the iterator with the least items decides the
length of the new iterator.

Syntax: zip(iterator1, iterator2, iterator3 ...)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

print (zip(a,b))                ##Output: <zip object at 0x0341FF68>
print (list(zip(a,b)))          ##Output: [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
print (tuple(zip(a,b)))         ##Output: (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS", "Car Repair Kit","Dolby sound kit"]

for i in zip(cars,accessories):
    print (i)

##Output:
('Aston', 'GPS')
('Audi', 'Car Repair Kit')
('McLaren', 'Dolby sound kit')


##                          Unzip
The reverse of these iterators from zip function is known as unzipping using “*” operator.

# Python program to demonstrate unzip (reverse 
# of zip)using * with zip function 

# Unzip lists 
l1,l2 = zip(*[('Aston', 'GPS'),('Audi', 'Car Repair'),('McLaren', 'Dolby sound kit')]) 

# Printing unzipped lists	 
print(l1)                   ##Output:('Aston', 'Audi', 'McLaren')
print(l2)                   ##Output:('GPS', 'Car Repair', 'Dolby sound kit')

  

