##                            File Handling in Python
1.  Python too supports file handling and allows users to handle files i.e., to read and write files,
    along with many other file handling options, to operate on files.
2.  Python treats file differently as text or binary and this is important.
3.  Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character.
    It ends the current line and tells the interpreter a new one has begun. Let’s start with Reading and Writing files.


1.                              ''' Working of open() function'''

    The key function for working with files in Python is the open() function.
    To return a file object we use open() function along with two arguments, that accepts file name and the mode, whether to read or write.

    SYNTAX : open(filename,mode)
    The open() function takes two parameters; filename, and mode.

    There are four different methods (modes) for opening a file:

    "r" -  Read   - Default value. Opens a file for reading, error if the file does not exist
    "a" -  Append - Opens a file for appending, creates the file if it does not exist
    "w" -  Write  - Opens a file for writing, creates the file if it does not exist
    "x" -  Create - Creates the specified file, returns an error if the file exists
    "r" -  for      both reading and writing

    In addition you can specify if the file should be handled as binary or text mode:
        "t" - Text - Default value. Text mode
        "b" - Binary - Binary mode (e.g. images)

##abc.txt file
'''fdlflsdf
slvsvlv
ddlslf
dmfdlslfsdfdl
ll'''

##    Example:
        To open a file for reading it is enough to specify the name of the file:
            f = open("demofile.txt")
        The code above is the same as:
            f = open("demofile.txt","rt")

        Because "r" for read, and "t" for text are the default values, you do not need to specify them.
        Note: Make sure the file exists, or else you will get an error.


# a file named "geek", will be opened with the reading mode. 
file = open('abc.txt','r')                                                        

# This will print every line one by one in the file 
for each in file:                                                   
	print (each)

##Output:
fdlflsdf

slvsvlv

ddlslf

dmfdlslfsdfdl

ll

##NOTE:Here,after the end of each line blank line is printed bcoz end default is "\n"
                            '''OR'''

for each in file:                                                   
	print (each,end="")

##Output:
fdlflsdf
slvsvlv
ddlslf
dmfdlslfsdfdl
ll


2.                      '''Working of read() mode'''

By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Python code to illustrate read() mode 
file = open("abc.text","r") 
print file.read() 

##Output:
fdlflsdf
slvsvlv
ddlslf
dmfdlslfsdfdl
ll


    '''Read Only Parts of the File'''
f = open('abc.txt')
print (f.read(5))

##Output:
fdlfl

    '''Read Line'''
You can return one line by using the readline() method:

f = open('abc.txt')
print (f.readline())

##Output:
fdlflsdf

f = open('abc.txt')
print (f.readline(1))

##Output:
f

print (f.readline(2))
##Output:
fd


f = open('abc.txt')
print (f.readline())
print (f.readline())

##Output:
fdlflsdf
slvsvlv

f = open('abc.txt')
lines_to_be_read = 3

for i in range(lines_to_be_read):
    print (f.readline(),end="")

##Output:
fdlflsdf
slvsvlv
ddlslf

    '''READ LINES'''

##abc.txt file
'''Now the file has more content!
append operation has been done'''

f = open('abc.txt')
print (f.readlines())

##Output:
['Now the file has more content!\n', 'append operation has been done']



3.                  '''Close Files'''

It is a good practice to always close the file when you are done with it.

f = open("demofile.txt", "r")
print(f.readline())
f.close()

##Note:
    You should always close your files, in some cases, due to buffering, changes made to a
    file may not show until you close the file.


4.                  '''Creating a file using write() mode'''

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

##Note: the "w" method will overwrite the entire file.

##abc.txt file
'''fdlflsdf
slvsvlv
ddlslf
dmfdlslfsdfdl
ll'''

# Python code to write a file 
f = open('abc.txt','w')
f.write("Now the file has more content!")
f.close()

f = open('abc.txt','r')
print (f.read())
f.close()
##Output:
Now the file has more content!


# Python code to write a file 
f = open('geek.txt','w')
f.write("Now the file has more content!")
f.write("This is the write command") 
f.write("It allows us to write in a particular file") 
f.close() 

f = open('geek.txt','r')
print (f.read())
f.close()

##Output:
Now the file has more content!This is the write commandIt allows us to write in a particular file



5.          '''Write to an Existing File'''

# Python code to illustrate append() mode 
f = open('abc.txt','a')
f.write("append operation has been done")
f.close()

f = open('abc.txt','r')
print (f.read())
f.close()

##Output:
Now the file has more content!append operation has been done


There are also various other commands in file handling that is used to handle various tasks like:
1.  rstrip(): This function strips each line of a file off spaces from the right-hand side.
2.  lstrip(): This function strips each line of a file off spaces from the left-hand side.



'''It is designed to provide much cleaner syntax and exceptions handling when you are working with code.
That explains why it’s good practice to use them with a statement where applicable. This is helpful
because using this method any files opened will be closed automatically after one is done, so auto-cleanup.'''
Example:

# Python code to illustrate with() 
with open("file.txt") as file: 
	data = file.read() 
# do something with data 


6.     '''Using write along with with() function'''

We can also use write function along with with() function:

# Python code to illustrate with() alongwith write() 
with open("file.txt", "w") as f: 
	f.write("Hello World!!!")



7.        '''split() using file handling'''

We can also split lines using file handling in Python. This splits the variable when space is encountered.
You can also split using any characters as we wish. Here is the code:

##abc.txt file
'''Now the file has more content!
append operation has been done'''


# Python code to illustrate split() function 

with open('abc.txt','r') as file:
    data = file.read()
    print (data.split())


##Output:
['Now', 'the', 'file', 'has', 'more', 'content!', 'append', 'operation', 'has', 'been', 'done']


8.   '''DELETE A FILE '''

To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("demofile.txt")

Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

  













    
