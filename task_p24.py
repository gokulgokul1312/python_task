import math

def triangle():
    a=int(input("enter the number a: "))
    b=int(input("enter the number b: "))
    c=int(input("enter the number c: "))
    s=(a+b+c)/2
    area_triangle=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of Triangle: {}".format(area_triangle)) 
triangle()
print("\n")
print("********************************************\n")

def square():
    a=int(input("enter the number a: "))
    area_square=a*a
    print("Area of Square: {}".format(area_square))
square()
print("\n")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

def rectangle():    
    l=int(input("enter the number l: "))
    b=int(input("enter the number b: "))
    area_rectangle=l*b
    print("Area of rectangle: {}".format(area_rectangle))
rectangle()
print("\n")
print("+++++++++++++++++++++++++++++++++++++++++++++\n")

def circle():
    r=int(input("enter the number r: "))
    area_circle=math.pi*r*r
    print("Area of Circle: {}".format(area_circle))
circle()
print("\n")
print("---------------------------------------------\n")

def trapezium():
    b1=int(input("enter the number b1: "))
    b2=int(input("enter the number b2: "))
    h=int(input("enter the number h: "))
    area_trapezium=((b1+b2)/2)*h
    print("Area of Trapezium: {}".format(area_trapezium))
trapezium()

