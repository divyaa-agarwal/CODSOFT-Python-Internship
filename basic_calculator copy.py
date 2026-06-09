#TAKE INPUT OF FIRST NUMBER
Operand1=int(input("ENTER YOUR FIRST NUMBER:"))
#TAKE INPUT OF SECOND NUMBER
Operand2=int(input("ENTER YOUR SECOND NUMBER:"))
#TAKE INPUT OF OPERATOR
Operator=input("ENTER YOUR OPERATOR:")

#CHECKING CONDITION ON THE BASIS OF OPERTORS
if Operator == "+":
    print("Result=",Operand1 + Operand2)
elif Operator == "-":
    print("Result=",Operand1 - Operand2)
elif Operator == "*":
    print("Result=",Operand1 * Operand2)
elif Operator == "/":
    print("Result=",Operand1 / Operand2)
else:
    print("INVALID INPUT")