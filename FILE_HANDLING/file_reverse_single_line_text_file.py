##  Python program to Reverse a single line of a text file


Input:
        This is a geek
        Welcome to GeeksforGeeks
        GeeksforGeeks is a computer science portal

    User choice = 0

Output:
        geek a is This
        Welcome to GeeksforGeeks
        GeeksforGeeks is a computer science portal


def user_choice(n):
    with open("demo3.txt",'r') as file:
        data = file.readlines()

    data[n] = data[n].split()
    data[n] = data[n][::-1]
    data[n] = " ".join(data[n])

    if data[n][-1]!='\n':
        data[n] = data[n] + '\n'

    with open("demo3.txt",'w') as file:
        file.writelines(data)

user_choice(0)
    
