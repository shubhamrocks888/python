Consider below programs that use Logical Not (or !) operator on boolean.

# A Python program that uses Logical Not or ! on boolean 
a = not True
b = not False
print (a) 
print (b) 
# Output:
False
True

The outputs of above programs are as expected, but the outputs following
programs may not be as expected if we have not used Bitwise Not (or ~) operator before.
# A Python program that uses Bitwise Not or ~ on boolean 
a = True
b = False
print (~a) 
print (~b)
Output:
-2
-1

Reason: The bitwise not operator ~ returns the complement of a number i.e., it switches each
        1 to 0 and each 0 to 1. Booleans True and False have values 1 and 0 respectively.

Bitwise not operator: Returns one’s compliement of the number.

Example:

a = 10 = 1010 (Binary)

~a = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11 (Decimal)
