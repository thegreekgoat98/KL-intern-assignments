class Calculate:
    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num1/self.num2
    
def main():
   while(True):
       
       print("-----------------------------------------")
       print("0.Exit")
       print("1.Addition")
       print("2.Subtraction")
       print("3.Multiplication")
       print("4.Division")
       print("WHAT OPERATION YOU GONNA DO: ")
       op=int(input())
       if op==1:
           a=int(input("Enter the first number: "))
           b=int(input("Enter the second number: "))
           obj=Calculate(a,b)
           print("The sum is: ",obj.add())
       elif op==2:
           a=int(input("Enter the first number: "))
           b=int(input("Enter the second number: "))
           obj=Calculate(a,b)
           print("The difference is: ",obj.subtract())
       elif op==3:
           a=int(input("Enter the first number: "))
           b=int(input("Enter the second number: "))
           obj=Calculate(a,b)
           print("The product is: ",obj.multiply())
       elif op==4:
           a=int(input("Enter the first number: "))
           b=int(input("Enter the second number: "))
           obj=Calculate(a,b)
           print("The quotient is: ",obj.divide())
       else:
           print("Thankyou for using the calculator")
           break
       
main()
       

