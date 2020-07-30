1. AND Gate

# Python3 program to illustrate 
# working of AND gate 

def AND (a, b): 

	if a == 1 and b == 1: 
		return True
	else: 
		return False

# Driver code 
if __name__=='__main__': 
	print(AND(1, 1)) 

	print("+---------------+----------------+") 
	print(" | AND Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",AND(False,False)," | ") 
	print(" A = False, B = True | A AND B =",AND(False,True)," | ") 
	print(" A = True, B = False | A AND B =",AND(True,False)," | ") 
	print(" A = True, B = True | A AND B =",AND(True,True)," | ") 

##Output:
True
+---------------+----------------
 | AND Truth Table |    Result |
 A = False, B = False | A AND B = False  | 
 A = False, B = True  | A AND B = False  | 
 A = True, B = False  | A AND B = False  | 
 A = True, B = True   | A AND B = True   |

2.NAND Gate

def NAND(a,b):
    if a==1 and b==1:
        return False
    else:
        return True

3. OR Gate

def OR (a,b):
    if a==0 and b==0:
        return False
    else:
        return True

##   or

def OR(a, b): 
    if a == 1: 
        return True
    elif b == 1: 
        return True
    else: 
        return False

4. XOR Gate

def xor(a,b):
    if a!=b:
        return True
    else:
        return False

5. NOT Gate

def NOT(a):
    if a==1:
        return False
    else:
        return True

6.NOR Gate:

def  NOR(a,b):
    if a==1 and b==1:
        return False
    else:
        return True

7,XNOR Gate

def XNOR(a,b):
    if a!=b:
        return False
    else:
        return True
