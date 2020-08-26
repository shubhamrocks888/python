##                  Python String split() Method

'''The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax :  string.split(separator, maxsplit)
separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"'''

txt = "i am a boy"
z = txt.split()
print (z)
##Output:
##['i', 'am', 'a', 'boy']

txt = "i am a boy"
z = txt.split(" ",1)
print (z)
##Output:
##['i', 'am a boy']


# Python program showing how to 
# multiple input using split 

# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 

# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split() 
print("Total number of students: ", x) 
print("Number of boys is : ", y) 
print("Number of girls is : ", z) 
print() 

# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 

# taking multiple inputs at a time 
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x)

##                  Python String rsplit() Method
'''The rsplit() method splits a string into a list, starting from the right.
If no "max" is specified, this method will return the same as the split() method.
Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax :  string.rsplit(separator, maxsplit)

separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"'''

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
##Output : ['apple', 'banana', 'cherry']




##                  Python String join() Method
'''The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.

Syntax :  string.join(iterable)

iterable	Required. Any iterable object where all the returned values are strings'''

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
##Output : John#Peter#Vicky

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
##Output : nameTESTcountry

x = "hello"
print (".".join(x))
##Output : h.e.l.l.o

##                  Python String count() Method

'''The count() method returns the number of times a specified value appears in the string.

Syntax :  string.count(value, start, end)

value	Required. A String. The string to value to search for
start	Optional. An Integer. The position to start the search. Default is 0
end	Optional. An Integer. The position to end the search. Default is the end of the string'''


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
##Output: 2

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
##Output: 1

##                  Python String endswith() Method

'''The endswith() method returns True if the string ends with the specified value, otherwise False.

Syntax :  string.count(value, start, end)

value	Required. The value to check if the string ends with
start	Optional. An Integer specifying at which position to start the search
end	Optional. An Integer specifying at which position to end the search'''

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
##Output: True

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)
##Output: False

##                  Python String startswith() Method
The startswith() method returns True if the string starts with the specified value, otherwise False.
Syntax :  string.startswith(value, start, end)


##                  Python String find() Method
'''The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only
difference is that the index() method raises an exception if the value is not found. (See example below)

Syntax :  string.count(value, start, end)

value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string'''

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
##Output: 1

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
##Output: 8

txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))
##Output:
'''-1
Traceback (most recent call last):
  File "demo_ref_string_find_vs_index.py", line 4 in <module>
    print(txt.index("q"))
ValueError: substring not found'''

##                  Python String rfind() Method
The rfind() method finds the last occurrence of the specified value.
The rfind() method returns -1 if the value is not found.
The rfind() method is almost the same as the rindex() method. See example below.


##                  Python String replace() Method
'''The replace() method replaces a specified phrase with another specified phrase.
Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

Syntax : string.replace(oldvalue, newvalue, count)

oldvalue	Required. The string to search for
newvalue	Required. The string to replace the old value with
count	        Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences'''

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
##Output: three three was a race horse, two two was three too.

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)
##Output: three three was a race horse, two two was one too.

##                  Python String strip() Method
'''The strip() method removes any leading (spaces at the beginning) and
trailing (spaces at the end) characters (space is the default leading character to remove)

Syntax : string.strip(characters)

characters	Optional. A set of characters to remove as leading/trailing characters'''

txt = "     banana     "
x = txt.strip()
print(x)
##Output: banana

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
##Output: banana

##                  Python String rstrip() Method
'''The rstrip() method removes any trailing characters (characters at the end a string),
space is the default trailing character to remove.

Syntax:string.rstrip(characters)

characters	Optional. A set of characters to remove as trailing characters'''

txt = "banana,,,,,ssaaww....."
x = txt.rstrip(",.asw")
print(x)
##Output: banana













