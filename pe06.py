#! python3
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Finished

d = (50 * 101) ** 2
s = 0
for i in range(1, 101):
	s += i * i

answer = d - s
print(str(answer))