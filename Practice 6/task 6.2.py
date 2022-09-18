arr = input("Enter elements of the array: ")
list_new = list(map(int, arr.split()))
a = 0
for i in range(10):
    if list_new[i] > 5:
        a=a+list_new[i]
print("Sum:",a)