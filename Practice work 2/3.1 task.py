import math
x=int(input('Input the value of x: '))
y=int(input('Input the value of y: '))
print(math.pow(x, y*x)+math.pow(x, math.pow(x,y))-x**4)

#3/1