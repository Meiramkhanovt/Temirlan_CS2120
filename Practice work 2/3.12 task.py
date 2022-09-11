import math
x=float(input('Input the value of x: '))
y=float(input('Input the value of y: '))
z=float(input('Input the value of z: '))
q=float(3/(x*y*z))
print((math.fabs(math.log1p(math.pow(x,3))+math.exp(2*x))/(x+3.4)-(math.pow(math.cos(q),3)/math.pow(math.sin(q), 3))))
#3.12