1.              '''Python File close() Method'''

The close() method closes an open file.
You should always close your files, in some cases, due to buffering,changes made to a file may not show until you close the file.

Syntax : file.close()

##Close a file after it has been opened:
f = open("demofile.txt", "r")
print(f.read())
f.close()


2.              '''Python File readable() Method'''

The readable() method returns True if the file is readable, False if not.

Syntax : file.readable()

#Python program
f = open('abc.txt','r')
print (f.readable())
#Output: True

f = open('abc.txt','w')
print (f.readable())
#Output: False


3.              '''Python File writable() Method'''

The writable() method returns True if the file is writable, False if not.
A file is writable if it is opened using "a" for append or "w" for write.

Syntax : file.writable()

#Python program
f = open('abc.txt','r')
print (f.writable())
#Output: False

f = open('abc.txt','w')
print (f.writable())
#Output: True

f = open('abc.txt','a')
print (f.writable())
#Output: True


4.                  '''Python File seek() Method'''

The seek() method sets the current file position in a file stream.
The seek() method also returns the new postion.

Syntax : file.seek(offset)

offset	Required. A number representing the position to set the current file stream position.

##abc.txt
'''Now the file has more content!
append operation has been done'''

#Python program
f = open('abc.txt','r')
f.seek(0)
print (f.read())

#Output:
Now the file has more content!
append operation has been done

#Python program
f = open('abc.txt','r')
f.seek(1)
print (f.read())

#Output:
ow the file has more content!
append operation has been done


5.              '''Python File tell() Method'''

The tell() method returns the current file position in a file stream.
Tip: You can change the current file position with the seek() method.

Syntax : file.tell()

#Python program
f = open('abc.txt','r')
print (f.tell())
#Output: 0

f = open('abc.txt','r')
f.read()
print (f.tell())
#Output: 62


6.          '''Python File writelines() Method'''

The writelines() method writes the items of a list to the file.
Where the texts will be inserted depends on the file mode and stream position.
"a":  The texts will be inserted at the current file stream position, default at the end of the file.
"w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.

Syntax : file.writelines(list)

list	The list of texts or byte objects that will be inserted.

#Python program
f = open("demofile.txt", "w")
f.writelines(["See you soon!", "Over and out."])
f.close()

f = open("demofile.txt",'a')
f.writelines(['Append has been done...'])
f.close()

f = open("demofile.txt",'r')
print (f.read())

#Output:
See you soon!Over and out.Append has been done...


7.          '''Python File name() Method'''

#Python program
f = open("demofile.txt",'r')
print (f.name)
#Output: demofile.txt


8.          '''Python File mode() Method'''

#Python program
f = open("demofile.txt",'r')
print (f.mode)
#Output: r


9.          '''Python File readlines() Method'''

The readlines() method returns a list containing each line in the file as a list item.
Use the hint parameter to limit the number of lines returned.
If the total number of bytes returned exceeds the specified number, no more lines are returned.

Syntax : file.readlines()

hint	Optional. If the number of bytes returned exceed the hint number, no more lines will be returned.
        Default value is  -1, which means all lines will be returned.


#Python program
f = open("demofile.txt",'r')
print (f.readlines())
#Output: ['fdlflsdf\n', 'slvsvlv\n', 'ddlslf\n', 'dmfdlslfsdfdl\n', ',dll\n']

print (f.readlines(-1))
#Output: ['fdlflsdf\n', 'slvsvlv\n', 'ddlslf\n', 'dmfdlslfsdfdl\n', ',dll\n']

print (f.readlines(0))
#Output: ['fdlflsdf\n', 'slvsvlv\n', 'ddlslf\n', 'dmfdlslfsdfdl\n', ',dll\n']

print (f.readlines(1))
#Output: ['fdlflsdf\n']


10.         '''Python File writelines() Method'''

The writelines() method writes the items of a list to the file.
Where the texts will be inserted depends on the file mode and stream position.
"a":  The texts will be inserted at the current file stream position, default at the end of the file.
"w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.

Syntax: file.writelines(list)

list	The list of texts or byte objects that will be inserted.

#Python program
f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

#Output:
See you soon!Over and out.

f.writelines(["See you soon!\n", "Over and out."])
print (f.read())
#Output:
See you soon!
Over and out.



