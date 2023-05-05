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
def take_input():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the first number: "))
    return [num1,num2]


    
def main():
   
   
       print("-----------------------------------------")
       print("0.Exit")
       print("1.Addition")
       print("2.Subtraction")
       print("3.Multiplication")
       print("4.Division")
       print("WHAT OPERATION YOU GONNA DO: ")
       op=int(input())
       user_input=take_input()
       obj=Calculate(user_input[0], 
       user_input[1])
       if op==1:
           print("The sum is: ",obj.add())
       elif op==2:         
           print("The difference is: ",obj.subtract())
       elif op==3:
           print("The product is: ",obj.multiply())
       elif op==4:
           print("The quotient is: ",obj.divide())

       
main()
       

