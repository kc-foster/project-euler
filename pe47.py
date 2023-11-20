#! python3
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
# work in progess

from libeuler import factor, sieve_of_eratosthenes
#import pdb

START = 1000
LIMIT = 100000
primes = sieve_of_eratosthenes(LIMIT)
base = START

check_list = [0 for _ in range(LIMIT - START + 3)]
while base < LIMIT:

	print(base)

	# test 4 nums
	if base == START or prime_hit:

		prime_hit = False

		factors0 = factor(base)
		factors1 = factor(base+1)
		factors2 = factor(base+2)
		factors3 = factor(base+3)

		if len(factors0) == 1 or len(factors1) == 1 or len(factors2) == 1 or len(factors3) == 1:
			prime_hit = True
			base += 4
			continue

		is_valid_row = [0 for _ in range(4)]
		is_valid_row_index = 0
		factors_dictionary = {0: factors0, 1: factors1, 2: factors2, 3: factors3}			

		# for each number
		for num in range(4):
			output_factors = []
			save = None
			# for each prime factor pick out the unique ones
			for prime_factor_index in range(len(factors_dictionary[num])):
				if factors_dictionary[num][prime_factor_index] != save:
					output_factors.append(factors_dictionary[num][prime_factor_index])
				save = factors_dictionary[num][prime_factor_index]


			# output_factors now contains unique factors, test if it is length 4
			if len(output_factors) == 4:
				is_valid_row[is_valid_row_index] = 1
			else:
				is_valid_row[is_valid_row_index] = 0
			is_valid_row_index += 1

		if sum(is_valid_row) == 4:
			print(base, factors_dictionary[0], factors_dictionary[1], factors_dictionary[2], factors_dictionary[3])
			break


	# test 1 num
	else:
		# shift is_valid_row left 1, set is_valid_row_index to 3
		prime_hit = False

		factors0 = factors1
		factors1 = factors2
		factors2 = factors3
		factors3 = factor(base+3)

		if len(factors3) == 1:
			prime_hit = True
			base += 4
			continue

		is_valid_row = is_valid_row[1:]
		factors_dictionary = {0: factors0, 1: factors1, 2: factors2, 3: factors3}

		output_factors = []
		save = None
		# for each prime factor in factors3 pick out the unique ones
		for prime_factor_index in range(len(factors_dictionary[3])):
			if factors_dictionary[num][prime_factor_index] != save:
				output_factors.append(factors_dictionary[num][prime_factor_index])
			save = factors_dictionary[num][prime_factor_index]

		# output_factors now contains unique factors, test if it is length 4
		if len(output_factors) == 4:
			is_valid_row.append(1)
		else:
			is_valid_row.append(0)

		if sum(is_valid_row) == 4:
			print(base, factors_dictionary[0], factors_dictionary[1], factors_dictionary[2], factors_dictionary[3])
			break

	
	base += 1