arr = input("Enter elements of the array: ")
list_new = list(map(int, arr.split()))
a=max(list_new)
b=min(list_new)
a_i=list_new.index(a)
b_i=list_new.index(b)
list_new.pop(a_i)
list_new.insert(a_i, b)
list_new.pop(b_i)
list_new.insert(b_i, a)
print(list_new)
