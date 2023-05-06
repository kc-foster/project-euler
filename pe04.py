#! python3
# Find the largest palindrome made from the product of two 3-digit numbers.
# Finished

import math

palindrome_list = []
for i in range (100, 1000):
	for j in range (100, 1000):
		k = i * j
		if str(k) == str(k)[ : : -1]:	# reversed word
			palindrome_list.append(k)

print(str(max(palindrome_list)))




