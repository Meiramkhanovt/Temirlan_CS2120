arr = input("enter the array: ")
list_new = list(map(int, arr.split()))

mean = sum(list_new)/len(list_new)

for i in list_new:
    if list_new[i] %10 == 0:
        list_new[i] = mean

print("result:",list_new)