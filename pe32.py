#! python3
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# Finished

import math

limit = 10000

list_of_pandigitals = []

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(1, (limit // 2) + 1):

	for y in range(1, limit + 1):

		z = x * y

		total_digit_length = int(math.log10(z) + 1) + int(math.log10(x) + 1) + int(math.log10(y) + 1)

		if total_digit_length < 9:

			continue

		elif total_digit_length > 9:

			break

		elif total_digit_length == 9: # 9 digits total, no zeros

			test_list = []

			val_list = [z, x, y]

			for i in range(3):

				test_list.extend([int(digit) for digit in str(val_list[i])])

			test_list.sort()

			if test_list == num_list:

				list_of_pandigitals.append(z)

print(sum(set(list_of_pandigitals)))