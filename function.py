##                Pass by Reference or pass by value?

One important thing to note is, in Python every variable name is a reference.
When we pass a variable to a function, a new reference to the object is created.
Parameter passing in Python is same as reference passing in Java.


# Here x is a new reference to same list lst 
def myFun(x): 
x[0] = 20

# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15] 
myFun(lst); 
print(lst)                       ##Output:[10,2,3,4] 


When we pass a reference and change the received reference to something else, the
connection between passed and received parameter is broken. For example, consider below program.

def myFun(x): 

# After below line link of x with previous 
# object gets broken. A new object is assigned 
# to x. 
x = [20, 30, 40] 

# Driver Code (Note that lst is not modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15] 
myFun(lst); 
print(lst)                      ##Output:[10, 11, 12, 13, 14, 15]



##                      Variable Length Arguments

def myFun(*argv): 
	for arg in argv: 
		print (arg,end=" ") 
	
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
##Output: Hello Welcome to GeeksforGeeks

def fun(**kwargs):
    for i  in kwargs.items():
        print (i,end=" ")

fun(x='1',y='2',z='3')
##Output: ('x', '1') ('y', '2') ('z', '3') 

