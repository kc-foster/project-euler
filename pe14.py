#! python3
'''
https://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def compute():

	N = 1000000
	cache = dict()
	current_longest_n = -1
	for n in range(2, N, 1):
		working_element = n
		current_length = 0
		while working_element != 1:
			if working_element in cache:
				current_length += cache[working_element]
				cache.update({n: current_length})
				break
			else:
				working_element = seq(working_element)
				current_length += 1
				cache.update({n: current_length})
		if current_longest_n == -1:
			current_longest_n = n
		elif cache[current_longest_n] < cache[n]:
			current_longest_n = n

	print(current_longest_n)

def seq(n):
	a = n
	if a % 2 == 0:
		a = a // 2
		return a	
	else:
		a = ((3*a) + 1)
		return a	


compute()