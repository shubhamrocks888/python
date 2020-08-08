##              OS Path module in Python

This module contains some useful functions on pathnames.
The path parameters are either strings or bytes .
These functions here are used for different purposes such as for merging, normalizing and retrieving path names in python .
All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the
same type, if a path or file name is returned. As there are different versions of operating system so there are several
versions of this module in the standard library.


                                '''1. os.path.basename(path)'''
It is used to return the basename of the file . This function basically return the file name from the path given.

import os
path = r"C:\Users\dell\Desktop\questions"
print (os.path.basename(path))
#Output: questions


                                '''2. os.path.dirname(path)'''
It is used to return the directory name from the path given. This function returns the name from the path except the path name.

import os
path = r"C:\Users\dell\Desktop\questions"
print (os.path.dirname(path))
#Output: C:\Users\dell\Desktop


                                '''3. os.path.isabs(path)'''
Basically,it tells you path is syntatically correct or not

It specifies whether the path is absolute or not.
In Unix system absolute path means path begins with the slash(‘/’) and in
Windows that it begins with a (back)slash after chopping off a potential drive letter.

import os
path = r"C:\Users\dell\Desktop\questions"
print (os.path.isabs(path))
#Output: True

                                '''4. os.path.exists(path)'''
It tells you whether the path exists or not

import os
path = r"C:\Users\dell\Desktop\questions"
print (os.path.exists(path))     #Output: True

path = r"C:\Users\dell\Desktop\questions\demo"
print (os.path.exists(path))     #Output: False

path = r"C:\Users\dell\Desktop\questions\demo.py"
print (os.path.exists(path))     #Output: True



                                '''5. os.path.isdir(path)'''
This function specifies whether the path is existing directory or not.

import os
path = r"C:\Users\dell\Desktop\questions"   #questions is a folder       
print (os.path.isdir(path))               #Output: True

path = r"C:\Users\dell\Desktop\questions\demo"  #demo is a file 
print (os.path.isdir(path))               #Output: False



                                '''6. os.path.isfile(path)'''
This function specifies whether the path is existing file or not.

import os
path = r"C:\Users\dell\Desktop\questions"   #questions is a folder       
print (os.path.isdir(path))               #Output: False

path = r"C:\Users\dell\Desktop\questions\demo.py"  #demo is a file 
print (os.path.isdir(path))               #Output: True



                                 '''7. os.path.join(path,filename)'''
import os
path = r"C:\Users\dell\Desktop\questions"   #questions is a folder       
print (os.path.join(path,'monty')) 
#Output: C:\Users\dell\Desktop\questions\monty
                                

                                '''8. os.path.split(path)'''
import os
path = r"C:\Users\dell\Desktop\questions\demo.py"   #questions is a folder       
print (os.path.split(path)) 
#Output: ('C:\\Users\\dell\\Desktop\\questions', 'demo.py')


                                 '''9. os.path.splitext(filename)'''
import os
print ( os.path.splitext('wallpaper2you_464171.jpg')) 
#Output: ('wallpaper2you_464171','.jpg')
                     



