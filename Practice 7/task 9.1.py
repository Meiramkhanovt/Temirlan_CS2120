x=str(input("Enter a number: "))
def sum(n):
    riko=0
    for i in n:
        riko+=int(i)
    return riko
def how_many(n, y):
    count=0
    n=int(n)
    while(n>=y):
        n-=y
        count+=1
    print(count)
bla=sum(x)
how_many(x, bla)