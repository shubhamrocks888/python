##                      OS Module in Python with Examples

1.  The OS module in python provides functions for interacting with the operating system.
2.  OS, comes under Python’s standard utility modules.
3.  This module provides a portable way of using operating system dependent functionality.

    All functions in os module raise OSError in the case of invalid or inaccessible file names and paths,
    or other arguments that have the correct type, but are not accepted by the operating system.


                                    '''1. os.name:'''

    This function gives the name of the operating system dependent module imported. The
    following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’

import os 
print(os.name) 
#Output: nt


                                '''2. os.getcwd():'''

    Function os.getcwd(), returns the Current Working Directory(CWD) of the file used to
    execute the code, can vary from system to system.

import os
print (os.getcwd())
##Output:
C:\Users\dell\Desktop\python


                                '''3. os.chdir():'''

    Syntax: os.chdir(path)
    path: A complete path of directory to be changed to new directory path.
    Returns: Doesn’t return any value

import os
print (os.getcwd()) ##Output: C:\Users\dell\Desktop\python
print (os.chdir())  ##Output: TypeError: chdir() missing required argument 'path' (pos 1)

print (os.chdir("C:\Users\dell\Desktop"))
##Output: SynatxError unicode error (it cannot print \U bcoz it is escape characters)

os.chdir(r"C:\Users\dell\Desktop")
print (os.getcwd()) ##Output:   C:\Users\dell\Desktop 


                            '''4. os.listdir():'''

    Syntax          : os.listdir(path)

    Parameters:
    path (optional) : path of the directory

    Return Type     : This method returns the list of all files and directories in the
                      specified path. The return type of this method is list.

print (os.listdir())
## print Files and directories in  current working directory
['.rstudio-desktop', '.gnome'..............,'geeksforgeeks']

print (os.listdir("C:\Users\dell\Desktop"))
## print Files and directories in the path provided


                        '''5. os.mkdir():'''

    os.mkdir() method in Python is used to create a directory named path with the specified
    numeric mode. This method raise FileExistsError if the directory to be created already exists.

    Syntax   : os.mkdir(path, mode = 0o777, *, dir_fd = None)

    Return Type: This method does not return any value.

import os
os.chdir(r"C:\Users\dell\Desktop")
os.mkdir('mon')
# mon named folder is created in current directory

os.mkdir('mon/non')
##FileNotFoundError: [WinError 3] The system cannot find the path specified: 'mon/non'
(does not create folder inside folder)

os.mkdir(r"C:\Users\dell\Desktop\new")
# can create folder by providing a path
(new named folder created on desktop)



                        '''6. os.makedirs():'''

    os.makedirs() method in Python is used to create a directory recursively. That means while
    making leaf directory if any intermediate-level directory is missing, os.makedirs() method
    will create them all.

    Syntax: os.makedirs(path, mode = 0o777, exist_ok = False)

    Parameter:
    path                : A path-like object representing a file system path. A path-like object
                          is either a string or bytes object representing a path.
    mode (optional)     : A Integer value representing mode of the newly created directory..If this
                          parameter is omitted then the default value Oo777 is used.
    exist_ok (optional) : A default value False is used for this parameter. If the target directory
                          already exists an OSError is raised if its value is False otherwise not.

    Return Type: This method does not return any value.


import os
os.chdir(r"C:\Users\dell\Desktop")
os.makedirs(r'mon\non\onn')
    OR
os.makedirs(r"C:\Users\dell\Desktop\mon\non\onn")
    

#folder inside folder created inside current directory or provided directory


                            '''7. os.rmdir():'''

    os.rmdir() method in Python is used to remove or delete a empty directory.
    OSError will be raised if the specified path is not an empty directory.

    Syntax: os.rmdir(path, *, dir_fd = None)

    Parameter:
    path              : A path-like object representing a file path. A path-like
                        object is either a string or bytes object representing a path.
    dir_fd (optional) : A file descriptor referring to a directory.
                        The default value of this parameter is None.
                        If the specified path is absolute then dir_fd is ignored.

    Note: The ‘*’ in parameter list indicates that all following parameters (Here in our case ‘dir_fd’)
          are keyword-only parameters and they can be provided using their name, not as positional parameter.

    Return Type: This method does not return any value.

import os
os.chdir(r"C:\Users\dell\Desktop")

os.mkdir('mon')    '''OR''' os.mkdir(r"C:\Users\dell\Desktop\mon") 
# create folder named mon on desktop

os.rmdir('mon')     '''OR''' os.rmkdir(r"C:\Users\dell\Desktop\mon") 
#delete folder named mon on desktop

    
##cannot delete folder inside a folder
os.makedirs(r'mon\non')
os.rmdir(r'mon')
##OSError: [WinError 145] The directory is not empty: 'mon'


                            '''8. os.removedirs():'''

    Syntax      : os.removedirs(path)
    Paramete    :
    path        : A path-like object representing a file path. A path-like object is either a string
                  or bytes object representing a path.

    Return Type : This method does not return any value.
                          
import os
os.chdir(r"C:\Users\dell\Desktop")
os.makedirs(r"mon\non")
os.removedirs(r"mon\non")
#whole folder of mon is deleted including non

#Note: Be careful about using below function
os.removedirs('/home/User/Documents/foo/bar/baz')

In above path, os.removedirs() method will try to remove the leaf directory first i.e ‘baz’. If the leaf
directory ‘baz’ is successfully removed then method will try to remove ‘/home/User/Documents/foo/bar’
then ‘/home/User/Documents/foo/’ then ‘/home/User/Documents’ until an error is raised. The directory to
be deleted should be empty.

All parent directory 
# of 'baz' will be also 
# removed if they are empty 


                            '''9. os.remove():'''
To delete a file, you must import the OS module, and run its os.remove() function:

##Delete a File
import os
os.remove("demofile.txt")

##Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

  
                            '''10. os.rename():'''
os.rename() method in Python is used to rename a file or directory.
This method renames a source file/ directory to specified destination file/directory.

Syntax: os.rename(source, destination, *, src_dir_fd = None, dst_dir_fd = None)

Parameters:
source: A path-like object representing the file system path. This is the source file path which is to renamed.
destination: A path-like object representing the file system path.
src_dir_fd (optional): A file descriptor referring to a directory.
dst_dir_fd (optional): A file descriptor referring to a directory.

Return Type: This method does not return any value.

import os
os.chdir(r"C:\Users\dell\Desktop")
os.mkdir('mon')

os.rename('mon','non') or os.rename(r"C:\Users\dell\Desktop\mon",r"C:\Users\dell\Desktop\non")



                        '''11. os.stat():'''
os.stat() method in Python performs stat() system call on the specified path.
This method is used to get status of the specified path.


Syntax          : os.stat(path)

Parameter       :
path            : A string or bytes object representing a valid path

Return Type     : This method returns a ‘stat_result’ object of class ‘os.stat_result’ which represents the
                  status of specified path. The returned ‘stat-result’ object has following attributes:


st_mode    : It represents file type and file mode bits (permissions).
st_ino     : It represents the inode number on Unix and the file index on Windows platform.
st_dev     : It represents the identifier of the device on which this file resides.
st_nlink   : It represents the number of hard links.
st_uid     : It represents the user identifier of the file owner.
st_gid     : It represents the group identifier of the file owner.
st_size    : It represents the size of the file in bytes.
st_atime   : It represents the time of most recent access. It is expressed in seconds.
st_mtime   : It represents the time of most recent content modification. It is expressed in seconds.
st_ctime   : It represents the time of most recent metadata change on Unix and creation time on Windows. It is expressed in seconds.
st_atime_ns: It is same as st_atime but the time is expressed in nanoseconds as an integer.
st_mtime_ns: It is same as st_mtime but the time is expressed in nanoseconds as an integer.
st_ctime_ns: It is same as st_ctime but the time is expressed in nanoseconds as an integer.
st_blocks  : It represents the number of 512-byte blocks allocated for file.
st_rdev    : It represents the type of device, if an inode device.
st_flags   : It represents the user defined flags for file.

Note: Some attributes are platform dependent and are subject to availability.


import os
path = os.getcwd()
print (os.stat(path))

#Output:
os.stat_result(st_mode=16895, st_ino=2251799814575688, st_dev=1257321393, st_nlink=1, st_uid=0, st_gid=0, st_size=20480,
               st_atime=1596888418, st_mtime=1596883463, st_ctime=1594638727)

print (os.stat(path).st_size)       #Output:20480



                                '''12. os.walk():'''
OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up.
For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

dirpath : Prints out directories only from what you specified.         <class 'str'>
dirnames : Prints out sub-directories from root.                        <class 'list'>
filenames : Prints out all files from root and directories.             <class 'list'>


return a generator object i.e, <generator object walk at 0x104c287c8> actually return a tuple (currentpath,directories,files)

path = os.getcwd()
for i,j,k in os.walk(path):
    print (i,j,k)

