#! python3

import math

def num_divisors(n):

	root = math.sqrt(n)
	flooredroot = math.floor(root)
	res = sum(2 for i in range(1, flooredroot + 1) if n % i == 0)

	return res

def compute():
	a = b = 0
	while True:
		b += 1
		a += b

		if num_divisors(a) >= 500:
			print(a)
			break

compute()