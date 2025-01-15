def max_value():
	myList = []
	for i in range(5):
		x = int(input("Type in a number: "))
		myList.append(x)

	max = myList[0]
	for i in myList:
		if i > max:
			max = i
	return max

print(max_value())