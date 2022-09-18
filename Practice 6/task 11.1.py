n=int(input("Enter number of elements: "))
arr= input("Enter the array: ")
list_new = list(map(int, arr.split()))
print(list_new)
for i in range(n):
    if list_new[i]%2!=0:
        list_new.pop(i) 
print(list_new)
print(max(list_new))
