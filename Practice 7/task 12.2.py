import math

def median(a, b, c):
    median = 0.5*math.sqrt(2 * (b**2 + c**2) - a**2)
    return median


print("Enter lengths of each side:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if abs(a - b) >= c | a + b <= c:
    print("impossible triangle")
print("medians of the original triangle:")
ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)
print(ma, mb, mc)
print("drawn medians of the triangle:")
mma = median(ma, mb, mc)
mmb = median(mb, ma, mc)
mmc = median(mc, ma, mb)
print(mma, mmb, mmc)