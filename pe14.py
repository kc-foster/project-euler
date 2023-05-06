#! python3
# Problem 14: Which starting number, under one million, produces the longest chain of Collatz sequence?
# Finished

def seq(n):
	seq = []
	while n != 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = (((n << 1) + n + 1) // 2)
		seq.append(n)
	return seq

seq_lengths = {}
for n in range(1000000, 1, -1):

	sequence = seq(n)
	seq_len = len(sequence)
	seq_lengths.update({n: seq_len})


max_length = max(seq_lengths.values())
print(list(seq_lengths.keys())[list(seq_lengths.values()).index(max_length)])