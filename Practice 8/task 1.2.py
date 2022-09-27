a = []
for i in range(3):
    a.append(list(map(int, input().split())))

def min_elts(a):
    return list(map(min, a))