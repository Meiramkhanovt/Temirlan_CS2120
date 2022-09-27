import math
x=5
y=6
a=2
b=3
R=4
def inSide(X,Y,A,B,r):
    qwe=math.pow((X-A),2)
    rty=math.pow((Y-B),2)
    if ((qwe+rty)==(r*r)):
        print("Inside")
    else: print("Outside")
inSide(x,y,a,b,R)