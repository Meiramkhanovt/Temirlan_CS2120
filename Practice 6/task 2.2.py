n = [1, 2, -3, -4, 5, 6, -7]
a = []
b = []
for i in n:
    if i>=0:
        a.insert(0, i)
    else:
        b.insert(0, i)
print(a)
print(b)