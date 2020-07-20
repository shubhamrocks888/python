##                      One Liner If else

a = "hello" if 2>1 else "bye"
print (a)

##                      List Comprehension

# Python program showing 
# how to take multiple input 
# using List comprehension 


# taking three input at a time 
x, y, z = [int(x) for x in input("Enter three value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print("Third Number is: ", z) 
print() 

# taking two inputs at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First number is {} and second number is {}".format(x, y)) 
print() 

# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x) 

x = [i for i in range(4) if i%2==0]
print (x)
