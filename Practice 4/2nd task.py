array = [1, 2, 3, 4, 5, 0]
sum=int(0)
number = int(0)
while array[number] != 0:
    sum += array[number]
    number += 1
print('the sum of numbers in array', sum)
print('number of elemets is', number + 1)