1.int(a,base): This function converts any data type to integer.
               'Base' specifies the base in which string is if data type is string.

The int() function converts the specified value into an integer number.
The int() function returns an integer object constructed from a number or string x, or return 0 if no arguments are given.

Syntax:
int(x=0)
int(x, base=10)

x	A number or string to be converted to integer object. Default argument is zero.	Required
base	Number format. Default value: 10.	                                        Optional


# initializing string                                       
s = "10010"
print (int(s,2))            #Output: 18
print (int(s,8))            #Output: 4104
print (int(s,10))           #Output: 10010
print (100)                 #Output: 100

2. float() : This function is used to convert any data type to a floating point number
print (float(s))            #Output: 10010.0

3. ord() : This function is used to convert a character to integer.
print (ord('0'))            #Output: 48
print (ord('a'))            #Output: 97
print (ord('A'))            #Output: 65

4. hex() : This function is to convert integer to hexadecimal string.
print (hex(16))             #Output: 0x10

5.oct() : This function is to convert integer to octal string.
print(oct(8))               #Output: 0o10

6. tuple() : This function is used to convert to a tuple.
s = 'geeks'
print (tuple(s))            #Output: ('g', 'e', 'e', 'k', 's')

7. set() : This function returns the type after converting to set.
s = 'geeks'
print (set(s))              #Output: {'g', 'k', 'e', 's'}

8. list() : This function is used to convert any data type to a list type.
s = 'geeks'
print (list(s))             #Output: ['g', 'e', 'e', 'k', 's']

9. dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
t = (('a',1),('b',2),('c',3))
l = [('a',1),('b',2),('c',3)]
s = {('a',1),('b',2),('c',3)}
print (dict(t))             #Output: {'a': 1, 'b': 2, 'c': 3}
print (dict(l))             #Output: {'a': 1, 'b': 2, 'c': 3}
print (dict(s))             #Output: {'a': 1, 'b': 2, 'c': 3}

10. str() : Used to convert integer into a string.

11. complex(real,imag) : : This function converts real numbers to complex(real,imag) number.
c = complex(1,2)
print (c)                   #Output: (1+2j)

12. chr(number) : : This function converts number to its corresponding ASCII character.
print (chr(75))             #Output: K
print (chr(76))             #Output: L






