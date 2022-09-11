import math
y=int(input('Input value of y: '))
x=int(input('Input value of x: '))
H=(math.sqrt(math.cos(2*y)+math.sin(4*y)+math.sqrt(math.pow(math.e, x)+math.pow(math.e,-x))))/(math.pow((math.pow(math.e, -x)+(math.pow(math.e, x)), 3)*((math.sin(4*y)+math.pow(math.cos(2*y),-2))),2))
print(H)
#2