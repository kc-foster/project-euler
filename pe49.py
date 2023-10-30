#! python3
# What 4-digit sequence where each term increases by 3330 are all prime and permutations of the first term?
# work in progress

from libeuler import sieve_of_eratosthenes, is_prime

PRIMES_MAX = 3339

primes_list = sieve_of_eratosthenes(PRIMES_MAX)
editted_prime_list = []
for n in primes_list:
	length_check = len(str(n)) == 4
	if length_check:
		editted_prime_list.append(n)

for first_term in editted_prime_list:
	second_term = first_term + 3330
	third_term = second_term + 3330

	permute_count_second_term = permute_count_third_term = 0
	for digit in str(first_term):
		permute_check_second_term = digit in str(second_term)
		if permute_check_second_term:
			permute_count_second_term += 1

		permute_check_third_term = digit in str(third_term)
		if permute_check_third_term:
			permute_count_third_term += 1

	sequence_check = (permute_count_second_term == 4 and permute_count_third_term == 4)
	if sequence_check:
		if is_prime(second_term) and is_prime(third_term):
			print(first_term, second_term, third_term)
