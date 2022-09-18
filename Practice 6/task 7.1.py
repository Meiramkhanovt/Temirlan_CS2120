arr = input("Enter elements of the array: ")
list_new = list(map(int, arr.split()))
a = 1
b=0
for i in range(len(list_new)):
    if list_new[i]%2!=0:
        a=a*list_new[i]
    else:
        b=b+list_new[i]
print("Sum:",b)
print("Product:", a)