import math
print("Please choose geometric shape")
x=int(input("If it is circle - enter 1, if it is rectangle - enter 2, if it is triangle - enter 3: "))
def shape (n):
    if(n==1):
        radius=int(input("Enter length of the radius: "))
        print("Area of the circle is:", math.pi*(radius**2))
    elif(n==2):
        length=int(input("Enter length of the rectangle: "))
        width=int(input("Enter width of the rectangle: "))
        print("Area of the rectangle is:", length*width)
    else:
        height=int(input("Enter height of the triangle: "))
        base=int(input("Enter value of the base of the triangle: "))
        print("Area of the triangle is:", (height*base)/2)
shape(x)