#! python3
# Find the sum of all the primes below two million.
# Finished

def seive(n):

	primelist = [True] * n
	primelist[0] = primelist[1] = False

	for i, isprime in enumerate(primelist):
		if isprime:
			yield i
			for notprime in range(i*i, n, i):	# i*i some kind of trick
				primelist[notprime] = False

summation = 0
obj = seive(2000000)

for i in obj:
	summation += i

print(summation)