arr= input("Enter the array: ")
list_new = list(map(int, arr.split()))
a=0
print(list_new)
for i in range(15):
    if list_new[i]<15:
        list_new[i]=0
    if list_new[i]>20:
        list_new[i]=1
print(list_new)