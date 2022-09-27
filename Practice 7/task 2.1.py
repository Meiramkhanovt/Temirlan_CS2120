import math
def hex_area(n):
    return(((3*math.pow(3, 0.5))/2)*math.pow(n,2))
x=int(input("Enter the length of one side of the regular hexagon: "))
print('Area of the hexagon is:', hex_area(x))