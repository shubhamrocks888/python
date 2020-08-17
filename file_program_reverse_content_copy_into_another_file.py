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
