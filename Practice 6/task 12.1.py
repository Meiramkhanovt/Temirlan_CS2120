arr = input("Enter the array: ")
list_new = list(map(int, arr.split()))
list_new.sort()
for i in list_new:
    if i%2 != 0:
        print(i)
        break