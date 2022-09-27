x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y=[2, 2, 3, 5, 5, 9, 7, 8, 9, 23, 1, 1, 10, 41, 50]
z=[0, 1, 2, 1, 14, 15, 32, 30, 54, 26, 25, 24, 24, 2, 9]
def sum_mean(a, b, c):
    sum1, sum2, sum3 = 0, 0, 0
    for i in a:
        sum1+=i
    print("Sum of the numbers in the first array is:", sum1)
    print("Arithmetic mean is:", sum1/15)
    for j in b:
        sum2+=j
    print("Sum of the numbers in the second array is:", sum2)
    print("Arithmetic mean of the second array is:", sum2/15)
    for h in c:
        sum3+=h
    print("Sum of the numbers in the third array is:", sum3)
    print("Arithmetic mean of the third array is:", sum3/15)
sum_mean(x, y, z)
