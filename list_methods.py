##                      Python List sort() Method
'''The sort() method sorts the list ascending by default.
You can also make a function to decide the sorting criteria(s).

Syntax : list.sort(reverse=True|False, key=myFunc)  -----> returns None

reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
key	Optional. A function to specify the sorting criteria(s)'''

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print (cars)        ##Output : ['BMW', 'Ford', 'Volvo']
cars.sort(reverse=True)
print (cars)        ##Output : ['Volvo', 'Ford', 'BMW']
cars.sort(key=lambda i :len(i))
print (cars)        ##Output : ['BMW', 'Ford', 'Volvo']


def func(z):
    return len(z)
cars.sort(key=func)
print(cars)         ##Output : ['BMW', 'Ford', 'Volvo']


##                      Python List reverse() Method
'''The reverse() method reverses the sorting order of the elements.
Syntax : list.reverse()   ----> IT RETURNS the None'''

fruits = ['apple', 'banana', 'cherry']
print(fruits.reverse())
print (fruits)
##Output : ['cherry', 'banana', 'apple']


##                      Python List append() Method
'''The append() method appends an element to the end of the list.
Syntax : list.append(elmnt)   ----> IT RETURNS NONE

elmnt	Required. An element of any type (string, number, object etc.)
'''
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")


##                      Python List clear() Method
'''The clear() method removes all the elements from a list.
Syntax : list.clear()   ----> IT RETURNS NONE'''

fruits = ['apple', 'banana', 'cherry']
fruits.clear()


##                      Python List copy() Method
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print (x)
##Output : ['apple', 'banana', 'cherry', 'orange']


##                      Python List extend() Method
'''The extend() method adds the specified list elements (or any iterable) to the end of the current list.
Syntax : list.extend(iterable))   ----> IT RETURNS NONE

iterable	Required. Any iterable (list, set, tuple,string etc.)
'''
fruits = ['apple','orange']
fruits.extend(('1','2','3'))
print (fruits)
##Output : ['apple', 'orange', '1', '2', '3']

fruits = ['apple','orange']
fruits.extend(['1','2','3'])
print (fruits)
##Output : ['apple', 'orange', '1', '2', '3']

fruits = ['apple','orange']
fruits.extend('abc')
print (fruits)
##Output : ['apple', 'orange', 'a', 'b', 'c']


##                      Python List index() Method
'''The index() method returns the position at the first occurrence of the specified value.
Syntax : list.index(elmnt)

elmnt	Required. Any type (string, number, list, etc.). The element to search for'''

fruits = [4, 55, 64, 32, 16, 32]
print (fruits.index(32))
##Output : 3


##                      Python List insert() Method
'''Syntax : list.insert(pos,elmnt)   ----> IT RETURNS NONE   '''
fruits = [1,2,3,4]
fruits.insert(5,5)
print (fruits)
##Output : [1,2,3,4,5]

fruits = [1,2,3,4]
fruits.insert(90,5)
print (fruits)
##Output : [1,2,3,4,5]


##                      Python List pop() Method
'''Note: The pop() method returns removed value(default value is -1).

The pop() method removes the element at the specified position.
Syntax : list.pop(pos)   ----> IT RETURNS the last value if pos not mentioned

pos	Optional. A number specifying the position of the element you want to remove,
        default value is -1, which returns the last item  '''


##                      Python List remove() Method
'''Note: The remove() method returns the None.

The remove() method removes the first occurrence of the element with the specified value.
Syntax : list.remove(elmnt)   ----> IT RETURNS the last value if pos not mentioned
elmnt	Required. Any type (string, number, list etc.) The element you want to remove'''

fruits = ['apple', 'banana', 'cherry']
print(fruits.remove("banana"))
##Output : None











