#! python3
'''
https://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def seq(n):
	a = n
	yield a
	while a > 1:
		if a % 2 == 0:
			a = a // 2
			yield a
		else:
			a = ((3*a) + 1)
			yield a

def checkcache(element, cache):

	i = 0
	subseq_length = 0
	cache_len = len(cache)
	for cache_element in cache:
		if cache_element == element:
			subseq_length = (cache_len - cache.index(element))
			return subseq_length
		elif cache_len > i:
			continue
		i += 1
	return 0						# nothing found for this cache

def compute():

	N = 100
	cache = [[] for _ in range(N)]
	save_n_seq = [0 for _ in range(N)]
	seq_length_save = 0


	for n in range(1, N, 1):

		length = 0
		seqobj = seq(n)

		for working_element in seqobj:

			# put working element in correct cache first (cache n)
			# then check previous caches for element 	 (cache 0 to n-1)
			# if found record length of cache length - element index
			# else add one to length

			cache[n].append(working_element)
			result = 0

			for j in range(0, n - 1, 1):

				result = checkcache(working_element, cache[j])
				if result == 0:
					continue
				else:
					length += result
					break

			if result == 0:
				length += 1

		save_n_seq[n] = length
		seq_length_save = max(length, seq_length_save)

	for i, seq in enumerate(save_n_seq):
		if seq_length_save == seq:
			print(i)

	print(seq_length_save)

# 6789 for N = 100 this sounds super wrong

compute()