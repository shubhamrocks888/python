##global : This keyword is used to define a variable inside the function to be of a global scope.

a=5
def abc():
    global a
    a=10
abc()
print (a)           #Output: 10        

##non-local : 	This keyword works similar to the global, but rather than global, this keyword declares 
##		a variable to point to variable of outside enclosing function, in case of nested functions.

		 
def outer():
    a = 5
    def inner(): 
        nonlocal a  
        a = 10
    inner() 
    print (a)
outer()             #Output: 10

#######
def f():
    print (s)

    s = "me too"

    print (s)

s ="I love Geeksforgeeks"
f()
#Output:
'''Line 2: undefined: Error: local variable 's' referenced before assignment'''


#######
def f():
    

    global s = "me too"

    print (s)

s ="I love Geeksforgeeks"
f()
#Output:"me too"

