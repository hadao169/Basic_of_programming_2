sum = 0
for x in range(1,8):
	tem = int(input(f"Enter the temperature of day {x}: "))
	sum += tem
print(f"The average temperature for the week is {round(sum/7, 2)} °C")
	