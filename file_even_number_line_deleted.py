##Input:
This is a geek
Welcome to GeeksforGeeks
GeeksforGeeks is a computer science portal


##Output:
This is a geek
Welcome to GeeksforGeeks
GeeksforGeeks is a computer science portal


## Python Program to delete even no. of lines within same file

with open("demo3.txt",'r') as file:
    data = file.readlines()


with open("demo3.txt",'w') as f:
    for line in range(0,len(data),2):
        f.write(data[line])
