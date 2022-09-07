import math
x=int(input('Input value of x: '))
t=int(input('Input value of t: '))
z=(9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t)))*math.pow(math.e,x)
print(z)
