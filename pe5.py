#! python3

import math

def compute():
	answer = 1

	for i in range(2, 20):
		answer = (answer * i) // math.gcd(answer, i)

	return str(answer)

print(compute())