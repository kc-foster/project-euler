#! python3

import math

def seive(n):	
	primelist = [True] * n
	primelist[0] = primelist[1] = False

	for i, isprime in enumerate(primelist):
		if isprime:
			yield i
			for notprime in range(i*i, n, i):	
				primelist[notprime] = False

i=0
obj = seive(500000)
while i < 10001:
	try:
		k = next(obj)
		i += 1
		continue
	except StopIteration:
		print(f"seive higher, last prime found was number: " + str(i))
		break

print(str(k))
print(str(i))
