n = 3
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

p = 0
s = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            s += a[i][j]
            p += 1

print("number of positives:", p)
print("sum:", s)