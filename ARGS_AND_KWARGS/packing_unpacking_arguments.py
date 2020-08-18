'''We use two operators * (for tuples) and ** (for dictionaries).'''

# A Python program to demonstrate need 
# of packing and unpacking 

# A sample function that takes 4 arguments 
# and prints them. 
def fun(a, b, c, d): 
	print(a, b, c, d) 

# Driver Code 
my_list = [1, 2, 3, 4] 

# This doesn't work 
fun(my_list) 

##Output : TypeError: fun() takes exactly 4 arguments (1 given)


##                                    * Unpacking for tuple
''' We can use * to unpack the list so that all elements of it can
    be passed as different parameters.                         '''

# A sample function that takes 4 arguments 
# and prints the, 
def fun(a, b, c, d): 
	print(a, b, c, d) 

# Driver Code 
l = [1, 2, 3, 4]

##NOTE: l can be {1,2,3,4}

# Unpacking list into four arguments 
fun(*l)

##Output :  (1,2,3,4)

##                                    * Packing for tuple
'''When we don’t know how many arguments need to be passed to a python
function, we can use Packing to pack all arguments in a tuple.'''

def mySum(*args):           # here args has become a tuple
    sum = 0
    for i in args:
        sum = sum+i
    print (sum)
    print (type(args))
    print (args[0],args[1])

# Driver code 
mySum(1, 2, 3, 4, 5)

##Output :
##15
##<class 'tuple'>
##1 2

'''The above function mySum() does ‘packing’ to pack all the arguments that
this method call receives into one single variable. Once we have this ‘packed’
variable, we can do things with it that we would with a normal tuple. args[0]
and args[1] would give you the first and second argument, respectively. Since
our tuples are immutable, you can convert the args tuple to a list so you can
also modify, delete and re-arrange items in i.'''



##                                          ** for dictionary

##                                    ** Unpacking for dictionary
def f(a,b,c):
    print (a,b,c)

d ={'a':1,'b':2,'c':3}
f(**d)

##Output : 1 2 3

##                                    ** Packing for dictionary

def f(**args):                  # here args has become a dictionary
    for i in args:
        print (i,args[i])
    print (type(args))

f(a=1,b=2,c=3)

##Output :
'''
a 1
b 2
c 3
<class 'dict'>
'''





    



