import math
print('Pick up a number depending on what area you want to find')
what=int(input('1(Rectangle), 2(Triangle), 3(Circle): '))

if what==1:
    a=float(input('Type length of the rectangle: '))
    b=float(input('Type width of the rectangle: '))
    area=float(a*b)
    print('Area of the rectangle is ' + format(area))
elif (what==2):
    a=float(input('Type length of the side of the triangle: '))
    b=float(input('Type length of the side of the triangle: '))
    c=float(input('Type length of the side of the triangle: '))
    P=float((a+b+c)/2)
    area=float(math.sqrt(P*(P-a)*(P-b)*(P-c)))
    print('Area of the triangle is ' + format(area))

elif(what==3):
    a=float(input('Type radius of the circle: '))
    area=float(math.pi*a*a)
    print('Area of the circle is ' + format(area))

else:{
print('Something went wrong')
}


#4 Area