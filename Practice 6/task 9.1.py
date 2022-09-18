arr = input("enter the array: ")
list_new = list(map(int, arr.split()))
mini=1000000
for i in range(len(list_new)):
    if abs(list_new[i])<=mini:
        mini=abs(list_new[i])

print("result:",mini)
list_new.reverse()
print(list_new)