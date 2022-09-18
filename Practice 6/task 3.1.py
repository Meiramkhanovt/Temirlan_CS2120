n = [1, 2, 3, 4, 5, 6, 7]
siu=0
for i in range(len(n)):
    if i%2!=0:
        siu+=n[i]
        print(n[i])
    else : continue
print(n)
print(siu)