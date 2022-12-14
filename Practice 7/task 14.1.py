def countdividors(a):
    res = []
    i = 1
    while i * i < a + 1:
        if a % i == 0:
            res.append(i)
            if i != a // i:
                res.append(a // i)
        i += 1
    return sorted(res)


def fun(m, n):
    div = []
    for num in range(m, n + 1):
        frac = countdividors(num)
        div.append((len(frac), -num, frac[-2:]))
    div.sort()
    print(-div[-1][1], 'consist', div[-1][0], 'divisors')


fun(394441, 394505)