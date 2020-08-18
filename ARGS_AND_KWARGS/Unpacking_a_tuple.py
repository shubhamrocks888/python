# Program to understand about 
# packing and unpacking in Python 

# this lines PACKS values 
# into variable a 
a = ("MNNIT Allahabad", 5000, "Engineering") 

# this lines UNPACKS values 
# of variable a 
(college, student, type_ofcollege) = a 

# print college name 
print(college)                          #Output: MNNIT Allahabad

# print no of student 
print(student)                          #Output: 5000

# print type of college 
print(type_ofcollege)                   #Output: Engineering

##NOTE : In unpacking of tuple number of variables on left hand side should be equal
##          to number of values in given tuple a.


'''Python uses a special syntax to pass optional arguments (*args) for tuple unpacking.
This means that there can be many number of arguments in place of (*args) in python.
All values will be assigned to every variable on left hand side and all remaining
values will be assigned to *args .For better understanding consider the following code.'''

# Python code to study about 
# unpacking python tuple using * 

# first and last will be assigned to x and z 
# remaining will be assined to y 
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50) 

# print details 
print(x)                                #Output: 10
print(y)                                #Output: ['Geeks',' for ', 'Geeks ']
print(z)                                #Output: 50 

# first and second will be assigned to x and y 
# remaining will be assined to z 
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50) 
print(x)                                #Output: 10
print(y)                                #Output: Geeks
print(z)                                #Output: ['for','Geeks',50]


# Python code to study about 
# unpacking python tuple using function 

# function takes normal arguments 
# and multiply them 
def result(x, y): 
	return x * y 
# function with normal variables 
print (result(10, 100))             #Output: 1000 

# A tuple is created 
z = (10, 100) 

# Tuple is passed 
# function unpacked them 

print (result(*z))                  #Output: 1000




