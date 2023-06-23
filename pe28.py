#! python3
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
# Finished

k = 1
total_rings = 500
current_skip = 2
sides = 4
skip_delta = 2

n = 1
result = 1
while k <= total_rings:
	for _ in range(sides):
		n += current_skip
		result += n
	current_skip += skip_delta
	k += 1

print(result)