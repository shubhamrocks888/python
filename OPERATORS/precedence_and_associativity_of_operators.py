##          Operator Precedence and Associativity

Operator precedence determines which operator is performed first in an expression
with more than one operators with different precedence.

Example: 10 + 20 * 30 is calculated as 10 + (20 * 30)
         and not as (10 + 20) * 30

Operators Associativity is used when two operators of same precedence appear in an
expression. Associativity can be either Left to Right or Right to Left.

For example: ‘*’ and ‘/’ have same precedence and their associativity is Left to Right,
                so the expression “100 / 10 * 10” is treated as “(100 / 10) * 10”.


OPERATOR            DESCRIPTION	                                        ASSOCIATIVITY

( )         Parentheses (function call) (see Note 1)                    left-to-right
[ ]         Brackets (array subscript)
.           Member selection via object name
->          Member selection via pointer
++ —	    Postfix increment/decrement (see Note 2)



	
++          Prefix increment/decrement                                  right-to-left
+           Unary plus/minus
! ~         Logical negation/bitwise complement
(type)      Cast (convert value to temporary value of type)
*           Dereference
&           Address (of operand)
sizeof      Determine size in bytes on this implementation




* / %	    Multiplication/division/modulus	                        left-to-right
+  –	    Addition/subtraction	                                left-to-right
<<  >>	    Bitwise shift left, 	                                left-to-right
<  <=       Relational less than/less than or equal to                  left-to-right     
>  >=	    Relational greater than/greater  than or equal to           left-to-right
	
== !=	    Relational is equal to/is not equal to	                left-to-right
&	    Bitwise AND	                                                left-to-right


^	    Bitwise exclusive OR	                                left-to-right
|	    Bitwise inclusive OR	                                left-to-right
&&	    Logical AND	                                                left-to-right
| |	    Logical OR	                                                left-to-right


? :	    Ternary conditional	                                        right-to-left

=           Assignment                                                  right-to-left
+= -=       Addition/subtraction assignment
*= /=       Multiplication/division assignment
%= &=       Modulus/bitwise AND assignment
^= |=       Bitwise exclusive/inclusive OR assignment
<<= >>=     Bitwise shift left/right assignment

,           Comma (separate expressions)	                        left-to-right
