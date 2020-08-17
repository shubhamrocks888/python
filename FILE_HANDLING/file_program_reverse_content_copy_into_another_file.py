##  Python program to reverse the content of a file and store it in another file
Given a text file. The task is to reverse as well as stores the content from an input file to an output file.

This reversing can be performed in two types.

Full reversing        : In this type of reversing all the content get reversed.
Word to word reversing: In this kind of reversing the last word comes first and the first word goes to the last position.

Example 1: Full Reversing

Input: 
        Hello Geeks
        for geeks!

Output:
        !skeeg rof
        skeeG olleH


##  Python program

'''abc.txt
This is a first line...
And this is a second file..
'''
        
with open('abc.txt','r') as file:
    data = file.read()

with open('demo.txt','w') as f:
    f.write(data[::-1])

with open('demo.txt','r') as x:
    print (x.read())

#Output:
..elif dnoces a si siht dnA
...enil tsrif a si sihT


##Example 2: Word to word reversing

Input: 
        Hello Geeks
        for geeks!

Output:
         geeks! for
         Geeks Hello


# Open the file in write mode 
f2 = open("output2.txt", "w") 


# Open the input file again and get 
# the content as list to a variable data 
with open("file.txt", "r") as myfile: 
	data = myfile.readlines()

        #if last line of data doesnot end with '\n'
	if data[-1][len(data[-1])-1]!='\n':
            data[-1] = data[-1] + '\n'


# We will just reverse the 
# array using following code 
data_2 = data[::-1] 

# Now we will write the fully reverse 
# list in the output2 file using 
# following command 
f2.writelines(data_2) 

f2.close() 
