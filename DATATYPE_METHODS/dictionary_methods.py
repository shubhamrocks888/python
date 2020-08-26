'''Note –   Dictionary keys are case sensitive, same name but different cases of
            Key will be treated distinctly.'''

# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')])
print (Dict)            #Output : {1: 'Geeks', 2: 'For'}


##          Adding elements to a Dictionary
# Creating an empty Dictionary 
Dict = {} 
print(Dict)                      #Output : {}

# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict)                     #Output : {0: 'Geeks', 2: 'For', 3: 1}

# Adding set of values 
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print(Dict)                      #Output : {0: 'Geeks', 2: 'For', 3: 1, 'Value_set': (2, 3, 4)}

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print(Dict)                     #Output : {0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4)}

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print(Dict)                     #Output : {0: 'Geeks', 2: 'Welcome', 3: 1, 5: {'Nested': {'1': 'Life', '2': 'Geeks'}}, 'Value_set': (2, 3, 4)}



##                      Python Dictionary clear() Method
'''The clear() method removes all the elements from a dictionary.
Syntax : dictionary.clear()      -----> It returns None'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)                  #Output : {}

##                      Python Dictionary copy() Method
'''The copy() method returns a copy of the specified dictionary.
Syntax : dictionary.copy()      -----> It returns None'''


##                      Python Dictionary fromkeys() Method
'''The fromkeys() method returns a dictionary with the specified keys and the specified value.
Syntax : dict.fromkeys(keys, value)     ----> It returns a dictionary with default value None 

keys	Required. An iterable specifying the keys of the new dictionary
value	Optional. The value for all keys. Default value is None'''

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)             #Output : {'key1': None, 'key2': None, 'key3': None}
print (dict.fromkeys(x,1))  #Output : {'key1': 1, 'key2': 1, 'key3': 1}


##                      Python Dictionary get() Method
'''The get() method returns the value of the item with the specified key.
Syntax : dictionary.get(keyname, value)      -----> It returns None

keyname	Required. The keyname of the item you want to return the value from
value	Optional. A value to return if the specified key does not exist. Default value None

NOTE : It does not update the dictionary'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))                 #Output : Mustang
print(car.get("models"))                #Output : None
print(car.get("models",'ferrari'))      #Output : ferrari  


##                      Python Dictionary items() Method
'''The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
Syntax : dictionary.items(keyname, value)'''

car = {"brand": "Ford",
  "model": "Mustang",
  "year": '1964'}
x = car.items()
print(x)                            #Output : dict_items([('brand','Ford'),('model','Mustang'),('year','1964')])
print (x[0])
#Output :
##Traceback (most recent call last):
##  File "C:\Users\dell\Desktop\python\dictionary_methods.py", line 92, in <module>
##    print (x[0])
##TypeError: 'dict_items' object is not subscriptable
for i in x:
    print (i,end=" ")               #Output : ('brand', 'Ford') ('model', 'Mustang') ('year', '1964') 


##                      Python Dictionary keys() Method
'''The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
Syntax : dictionary.keys()'''

print (car.keys())      #Output : dict_keys(['brand', 'model', 'year'])


##                      Python Dictionary values() Method
'''The values() method returns a view object. The view object contains the values of the dictionary, as a list
Syntax : dictionary.values()'''


##                      Python Dictionary pop() Method
'''The pop() method removes the specified item from the dictionary.
Syntax : dictionary.pop(keyname, defaultvalue)

keyname	        Required. The keyname of the item you want to remove
defaultvalue	Optional. A value to return if the specified key do not exist.

If this parameter is not specified, and the no item with the specified key is found, an error is raised'''

print (car.pop("model"))        #Output : Mustang


##                      Python Dictionary popitem() Method
'''The popitem() method removes the item that was last inserted into the dictionary.
The removed item is the return value of the popitem() method, as a tuple, see example below.

Syntax : dictionary.popitem()'''
car = {"brand": "Ford","model": "Mustang","year": 1964}
print (car.popitem())           #Output :   ('year', 1964)


##                      Python Dictionary setdefault() Method
'''The setdefault() method returns the value of the item with the specified key.
If the key does not exist, insert the key, with the specified value, see example below

Syntax :        dictionary.setdefault(keyname, value)
keyname	        Required. The keyname of the item you want to return the value from
value	        Optional.If the key exist, this parameter has no effect.
                If the key does not exist, this value becomes the key's value,Default value None'''

car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.setdefault("color", "white")
print(x)                    #Output : White
print (car)                 #Output : {'model': 'Mustang', 'brand': 'Ford', 'year': 1964, 'color': 'White'}


##                      Python Dictionary update() Method
'''The update() method inserts the specified items to the dictionary.

Syntax :        dictionary.update(iterable)    -----> returns None
iterable	A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary'''

car = {"brand": "Ford","model": "Mustang","year": 1964}

car.update({"color": "White"})
print(car)              #Output : {'model': 'Mustang', 'brand': 'Ford', 'year': 1964, 'color': 'White'}














