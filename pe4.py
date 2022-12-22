#! python3

import math

def compute():
	palindrome_list = []
	for i in range (100, 1000):
		for j in range (100, 1000):
			k = i * j
			if str(k) == str(k)[ : : -1]:	# reversed word
				palindrome_list.append(k) 
	return str(max(palindrome_list))

print(compute())


