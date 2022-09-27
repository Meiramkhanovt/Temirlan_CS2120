a=int(input("Enter number 'a': "))
b=int(input("Enter number 'b': "))
c=int(input("Enter number 'c': "))
d=int(input("Enter number 'd': "))
x=a/b
y=c/d
for i in range(10):
    if (a%2==0 and d%2==0):
        a=a/2
        d=d/2
    if (a%3==0 and d%3==0):
        a=a/2
        d=d/2
    if (b%2==0 and c%2==0):
        b=b/2
        c=c/2
print()


