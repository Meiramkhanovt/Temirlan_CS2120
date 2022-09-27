for i in range(1, 1000):
    num = len(str(i))

    sum = 0

    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** num
        temp //= 10

    if i == sum:
        print(i)