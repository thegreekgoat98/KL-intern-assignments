#pylint --- 9.17/10.0
"""This program calculates Area, Perimeter of different shapes"""
import math
class Shape:
    """"This class calculates the Area and Perimeter of the shape"""
    area=0
    perimeter=0
    def __init__(self,args):
        """"This is the constructor"""
        self.args=args
        if len(args)==1:
            self.area=math.pi*args[0]*args[0]
            self.perimeter=2*math.pi*args[0]
        elif len(args)==2:
            self.area=args[0]*args[1]
            self.perimeter=2*(args[0]+args[1])
        elif len(args)==3:
            semi_pm=(args[0]+args[1]+args[2])/2
            value_before_sqroot=semi_pm*(semi_pm-args[0])*(semi_pm-args[1])-(semi_pm-args[2])
            self.area=math.sqrt(value_before_sqroot)
            self.perimeter=args[0]+args[1]+args[2]
    def print_values(self):
        """This function prints area and perimeter"""
        print("Area of the shape: ",self.area)
        print("Perimeter of the shape: ",self.perimeter)
dimensions = [int(dimensions) for dimensions in input("Enter the dimensions: ").split()]
obj=Shape(dimensions)
print("----------------------------------")
obj.print_values()
