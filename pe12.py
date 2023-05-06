#! python3
# What is the value of the first triangle number to have over five hundred divisors?
# Finished

import math

def num_divisors(n):

	root = math.sqrt(n)
	flooredroot = math.floor(root)
	res = sum(2 for i in range(1, flooredroot + 1) if n % i == 0)

	return res

n = 25
while num_divisors(n*(n+1)//2) < 501:
	n += 25

print(f"{n}: {n*(n+1)//2}")