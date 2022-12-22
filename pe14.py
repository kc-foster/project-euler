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

def compute():

	cachelist = [[] for _ in range(1000)]
	currentseq = 0

	for n in range(1, 1000, 1):
		seqobj = seq(n)
		if currentseq == 0:	# cache is empty
			for i, element in enumerate(seqobj):
				cachelist[currentseq][i] = element
		else:
			i = 0
			cachelen = 0
			index = 0
			for working_element in seqobj:			# for each element in current sequence, look into the cachelist and pull cache_elements for matches
				for cache in cachelist:
					for cache_element in cache:
						if cache_element == working_element		# get the first element that matches
							cachelen = len(cachelist[i])
							index = cachelist[i].index(cache_element)

		currentseq += 1

def seq(n):	# yield collatz sequence values for each number given to it one at a time, so that i can choose to check them against sequences in cache either one at a time or in intervals
	a = n
	while a > 1:
		if a % 2 == 0:
			a = a // 2
			yield a
		else:
			a = ((3*a) + 1)
			yield a

compute()