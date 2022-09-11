import math
a=float(input('Input the value of a: '))
b=float(input('Input the value of b: '))
c=float(input('Input the value of c: '))
D=float(b**2-4*a*c)
if(D==0):{
    print('This quadratic equation has only 1 root')
}
elif(D>0):{
print('This quadratic equation has 2 roots')
}
else:{
    print("This quadratic equation has no roots")
}
#3. Find the roots of a quadratic equation