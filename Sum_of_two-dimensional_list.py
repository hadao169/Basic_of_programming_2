numbers = [[3,1,4,1,5], [9,2,6,5,3], [5,8,9,7,9], [3,2,3,8,4], [6,2,6,4,3]]

# approach 1
def sum_2D_list(my_list:list):
	sum = 0
	for row in my_list:
		for j in row:
			sum += j
	return sum

# approach 2: # Convert 2D array to a single list (flat array)
	flat_list = [i for sublist in my_list for i in sublist]

print(sum_2D_list(numbers))
