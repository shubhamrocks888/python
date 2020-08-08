##          Ways to print escape characters in Python

Escape characters are characters that are generally used to
perform certain tasks and their usage in code directs the compiler
to take a suitable action mapped to that character.


Example :
'\n'  -->  Leaves a line
'\t'  -->  Leaves a space

# Python code to demonstrate escape character 
# string 

ch = "I\nLove\tGeeksforgeeks"

print ("The string after resolving escape character is : ") 
print (ch) 

##Output :
The string after resolving escape character is : 
I
Love    Geeksforgeeks


                            '''Using “r/R”'''
Adding “r” or “R” to the target string triggers a repr() to the string
internally and stops from the resolution of escape characters.

ch1 = r"I\nLove\tGeeksforgeeks"
ch2 = R"I\nLove\tGeeksforgeeks"

print (ch1)
print (ch2)

##Output :
I\nLove\tGeeksforgeeks
I\nLove\tGeeksforgeeks
