operand1=int(input("Enter the first number:" ))
operand2=int(input("Enter the second number:" ))
operator=input("What operation you wanna perform: ")

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
     return num1-num2

def multiply(num1,num2):
     return num1*num2

def divide(num1,num2):
     return num1/num2


def Calculate(num1,num2,op):
    if op=="+":
        print(add(num1,num2))
    elif op=="-":
        print(subtract(num1,num2))
    elif op=="*":
        print(multiply(num1,num2))
    else:
        print(divide(num1,num2))

    
Calculate(operand1,operand2,operator)






