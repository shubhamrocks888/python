##                      Deleting/Updating from a String

'''In Python, Updation or deletion of characters from a String is not allowed.
This will cause an error because item assignment or item deletion from a String
is not supported. Although deletion of entire String is possible with the use of
a built-in del keyword. This is because Strings are immutable, hence elements of
a String cannot be changed once it has been assigned. Only new strings can be
reassigned to the same name.''''

# Python Program to Update 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a character 
# of the String 
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ") 
print(String1) 

##Error:
'''Traceback (most recent call last):
File “/home/360bb1830c83a918fc78aa8979195653.py”, line 10, in
String1[2] = ‘p’
TypeError: ‘str’ object does not support item assignment'''

##                  Escape Sequencing in Python

# Python Program for 
# Escape Sequencing 
# of String 

# Initial String 
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 

# Escaping Single Quote 
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ") 
print(String1) 

# Escaping Doule Quotes 
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ") 
print(String1) 

# Printing Paths with the 
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1) 

##Output:
'''Initial String with use of Triple Quotes: 
I'm a "Geek"

Escaping Single Quote: 
I'm a "Geek"

Escaping Double Quotes: 
I'm a "Geek"

Escaping Backslashes: 
C:\Python\Geeks\'''
