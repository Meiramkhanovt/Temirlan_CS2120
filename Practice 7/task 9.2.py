import statistics

def mult(ugway):

	result = 1
	for x in ugway:
		result = result * x
	return result


list1 = [2, 2, 1]
list2 = [4, 4, 0]
list3 = [1, 6, 3]

print("The product of the elements in the 1st list =", mult(list1))
print("The product of the elements in the 2nd list =", mult(list2))
print("The product of the elements in the 3rd list =", mult(list3))

print("The arithmetic mean of the 1st list =", statistics.mean(list1))
print("The arithmetic mean of the 2nd list =", statistics.mean(list2))
print("The arithmetic mean of the 3rd list =", statistics.mean(list3))