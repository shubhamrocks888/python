##              Python sorted() Function
The sorted() function returns a sorted list of the specified iterable object.

You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

Note: You cannot sort a list that contains BOTH string values AND numeric values.

Syntax: sorted(iterable, key=key, reverse=reverse)

iterable	Required. The sequence to sort, list, dictionary, tuple etc.
key	Optional. A Function to execute to decide the order. Default is None
reverse	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

a = ("b", "g", "a", "d", "f", "c", "h", "e")
print (sorted(a))                           #Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print (sorted(a,reverse=True))              #Output: ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

x = ('cat','tiger','lion')
print (sorted(x,key=lambda i :len(i)))      #Output: ['cat', 'lion', 'tiger']

z = ('cat','tiger','lion')

def myfunc(z):
    return len(z)
print (sorted(z,key=myfunc))                #Output: ['cat', 'lion', 'tiger']


##              Python reversed() Function
The reversed() function returns a reversed iterator object.

Syntax: reversed(sequence)

sequence	Required. Any iterable object

NOTE:   The list.reverse() method reverses a List.

alph = ["a", "b", "c", "d"]
print (reversed(alph))              #Output: <list_reverseiterator object at 0x03BD5610>
print (list(reversed(alph)))        #Output: ['d', 'c', 'b', 'a']
print (tuple(reversed(alph)))       #Output: ('d', 'c', 'b', 'a')

for i in reversed(alph):
    print (i,end=" ")               #Output: d c b a  


##              Python round() Function
The round() function returns a floating point number that is a rounded version of the specified number,
with the specified number of decimals.

The default number of decimals is 0, meaning that the function will return the nearest integer.

Syntax: round(number, digits)

number	Required. The number to be rounded
digits	Optional. The number of decimals to use when rounding the number. Default is 0

print (round(5.76543))              #Output:6
print (round(5.46543))              #Output:5
print (round(5.76543,2))            #Output:5.77


##              Python range() Function
This returns a range object (a type of iterable).
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1
(by default), and stops before a specified number.

Syntax: round(number, digits)

start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

print (range(5))                    #Output:range(0, 5)
print (list(range(5)))              #Output:[0,1,2,3,4]
for i in range(5):
    print (i,end=" ")               #Output:0 1 2 3 4

for i in range(3,10,2):
    print(i,end=" ")                #Output:3 5 7 9


##              Python abs() Function
The abs() function returns the absolute value of the specified number.
NOTE: It acts like a moduloud i.e, like |x|

Syntax: abs(n)

n	Required. A number

print (abs(7.25))                   #Output:7.25
print (abs(-7.25))                  #Output:7.25
print  (abs(3+5j))                  #Output:5.830951894845301
