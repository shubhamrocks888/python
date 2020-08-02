a=1,2,3
print (a)               #Output : (1, 2, 3)
print (type(a))         #Output : <class 'tuple'>


#Creating an empty Tuple 
Tuple1 = () 
print (Tuple1)                  #Output : ()

#Creatting a Tuple with the use of string
Tuple1 = ('Geeks', 'For') 
print(Tuple1)                   #Output : ('Geeks', 'For')

#Creating a Tuple  with the use of list 
list1 = [1, 2, 4, 5, 6] 
print(tuple(list1))             #Output : (1, 2, 4, 5, 6)

#Creating a Tuple with the use of built-in function 
Tuple1 = tuple('Geeks') 
print(Tuple1)                   #Output : ('G', 'e', 'e', 'k', 's')

#Creating a Tuple with single element
Tuple1 = ('Geeks',)
print(Tuple1)                   #Output : ('Geeks',)

# Reversing the Tuple  
Tuple1 = (1, 2, 4, 5, 6)
print(Tuple1[::-1])             #Output : (6,5,4,2,1)
