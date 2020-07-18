##                  Python String split() Method

'''The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
Note: When maxsplit is specified, the list will contain the specified number of elements plus one.'''

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
