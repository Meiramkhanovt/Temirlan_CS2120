from cmath import sqrt
import math
a=int(input("Enter value of the leg (1) of the triangle 1: "))
b=int(input("Enter value of the leg (2) of the triangle 1: "))
c=int(input("Enter value of the leg (1) of the triangle 2: "))
d=int(input("Enter value of the leg (2) of the triangle 2: "))
def hyp(x, y, z, q):
    hyp1=math.sqrt(x**2+y**2)
    hyp2=math.sqrt(z**2+q**2)
    print("Hypotenuse 1:", hyp1)
    print("Hypotenuse 2:", hyp2)
    if hyp1>hyp2:
        print("Hypotenuse 1 is bigger than Hypotenuse 2")
    elif hyp1<hyp2:        
        print("Hypotenuse 2 is bigger than Hypotenuse 1")
    else: print("They are equal")
hyp(a,b,c,d)