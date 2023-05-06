#! python3
# Problem 1: Find the sum of all the multiples of 3 or 5 below 1000
# Finished
	
total = 0
for i in range(1, 1000, 1):
	if (i % 3 == 0) or (i % 5 == 0):
		print(i)
		total += i
print(total)