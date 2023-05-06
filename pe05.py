#! python3
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Finished

import math

answer = 1

for i in range(2, 20):
	answer = (answer * i) // math.gcd(answer, i)

print(answer)