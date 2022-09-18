arr = input("Enter elements of the array: ")
list_new = list(map(int, arr.split()))
a = 0
b=1
for i in range(10):
    a=a+list_new[i]
    b=b*list_new[i]
print("Sum:",a)
print("Product:", b)