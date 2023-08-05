#! python3
# How many circular primes are there below one million?
# Finished

from libeuler import sieve_of_eratosthenes, circular_permutation

limit = 1000000
primes = sieve_of_eratosthenes(limit)
primes_save = sieve_of_eratosthenes(limit)
count = 4
prime_lists = [[]]
prime_lists.append([[[] for _ in range(2)] for _ in range(5)])

# any prime with a 2, 4, 5, 6, 8, or 0 will not be circular, because last digit cannot contain these numbers
# 3, 5, 7, 9, 11

invalid = {2, 4, 6, 8, 0, 5}
for i in range(len(primes)):
	for digit in str(primes[i]):
		if int(digit) in invalid:
			primes[i] = 0

print(f"check 1")

# sort all primes_save into smaller lists for checking
for prime in primes_save:

	prime_len = len(str(prime))
	first_digit = prime // 10 ** (prime_len - 1)

	if prime_len == 1:
		prime_lists[0].append(prime)
	elif prime_len == 2:
		if first_digit < 6:
			prime_lists[1][0][0].append(prime)
		else:
			prime_lists[1][0][1].append(prime)
	elif prime_len == 3:
		if first_digit < 6:
			prime_lists[1][1][0].append(prime)
		else:
			prime_lists[1][1][1].append(prime)
	elif prime_len == 4:
		if first_digit < 6:
			prime_lists[1][2][0].append(prime)
		else:
			prime_lists[1][2][1].append(prime)
	elif prime_len == 5:
		if first_digit < 6:
			prime_lists[1][3][0].append(prime)
		else:
			prime_lists[1][3][1].append(prime)
	elif prime_len == 6:
		if first_digit < 6:
			prime_lists[1][4][0].append(prime)
		else:
			prime_lists[1][4][1].append(prime)

print(f"check 2")

for prime in primes:	# primes contains possible circular primes

	if prime < 10:
		continue

	prime_perm = []

	circular_permutation(prime, prime_perm, 0)
	prime_perm.sort()

	check_perm_len = len(prime_perm)
	check_repeat_perm = 0
	counter = 0

	for perm in prime_perm:

		perm = int(perm)

		check_length = len(str(perm))
		check_value = perm // 10 ** (check_length - 1)

		if perm == prime:
			check_repeat_perm += 1
			continue

		if check_value < 6:
			if perm in prime_lists[1][check_length-2][0]:	# if perm is prime
				counter += 1
		else:
			if perm in prime_lists[1][check_length-2][1]:
				counter += 1

	if check_perm_len-1 == counter:
		#pdb.set_trace()
		for perm in prime_perm:		# zero the perm values in reduced prime list so each is not counted twice
			primes[primes.index(int(perm))] = 0
		count += check_perm_len
	elif check_repeat_perm > 1:
		#pdb.set_trace()
		primes[primes.index(int(perm))] = 0
		count += 1


print(count)