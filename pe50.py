#! python3
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# Finished

from libeuler import sieve_of_eratosthenes, is_prime

limit = 4000
primes = sieve_of_eratosthenes(limit)
primes_list_len = len(primes)

cached_prime_sum = prime_sum = max_chain_len = 0
output_dict = {}

for i in range(0, primes_list_len, 1):
	prime_sum = cached_prime_sum + primes[i]
	cached_prime_sum = prime_sum
	if i != 0:
		even_list = (i % 2 == 0)
		for k in range(0, i - 1, 1):
			if (i - k) < max_chain_len:
				break
			if (k > 0 and not even_list) or (k == 0 and even_list):
				if is_prime(prime_sum):
					if (i - k) > max_chain_len:
						max_chain_len = (i - k)
						output_dict.update({prime_sum: max_chain_len})
			prime_sum -= primes[k]
	else:
		continue

list_of_prime_sums = []

for key in output_dict.keys():
	if key < 1000000:
		list_of_prime_sums.append(key)

maximum_entry = 0
for entry in list_of_prime_sums:
	if output_dict[entry] > maximum_entry:
		maximum_entry = output_dict[entry]

reverse_dict = {v: k for k, v in output_dict.items()}

print(f"max prime sum: {reverse_dict[maximum_entry]} chain length: {maximum_entry}")
