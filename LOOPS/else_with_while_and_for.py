##Using else statement with while loops:

The else clause is only executed when your while condition becomes false.
If you break out of the loop, or if an exception is raised, it won’t be executed.

#Python program to illustrate 
# combining else with while 
count = 0
while (count < 3):	 
	count = count + 1
	print("Hello Geek") 
else: 
	print("In Else Block") 

##Output:
'''Hello Geek
Hello Geek
Hello Geek
In Else Block'''

##Single statement while block:

count = 0
while (count == 0): print("Hello Geek") 

'''Note: It is suggested not to use this type of loops as it is a never ending infinite
loop where the condition is always true and you have to forcefully terminate the compiler.'''


##Using else statement with for loops:

# Python program to illustrate 
# combining else with for 

list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
	print list[index] 
else: 
	print "Inside Else Block"

##Output:
'''geeks
for
geeks
Inside Else Block'''
