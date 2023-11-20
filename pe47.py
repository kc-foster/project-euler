#! python3
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
# Finished


from libeuler import sieve_of_eratosthenes, factor

LIMIT = 1_000_000

primes = sieve_of_eratosthenes(int((LIMIT) / (2 * 3 * 5)))

factors = [0 for _ in range(LIMIT)]
for prime in primes:
	for n in range(1, len(factors) // prime):
		factors[prime * n] += 1

for n in range(len(factors)):
	if factors[n] == 4 and factors[n+1] == 4 and factors[n+2] == 4 and factors[n+3] == 4:
		print(n)
		break
