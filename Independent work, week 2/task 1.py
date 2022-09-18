arr = input("Enter elements of the array: ")
list_new = list(map(int, arr.split()))
list_new.reverse()
print(list_new)