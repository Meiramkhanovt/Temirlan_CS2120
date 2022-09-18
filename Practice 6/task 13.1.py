n=int(input("Enter number of elements in the array: "))
arr = input("Enter the array: ")
list_new = list(map(int, arr.split()))
a=0
for i in range(n):
    for j in range (i+1, n):
        if list_new[i]==list_new[j]:
            print("The same number is:", list_new[j])
            print("indices:", i, j)
