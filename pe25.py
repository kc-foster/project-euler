#! python3
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# Work in Progress

# my_max_integer_size's first in lists, remainder after
my_max_integer_size = 9000000000000000000

def generate_fib_seq(limit):
	
	fib = [[1]] * limit
	i = 0
	print(fib)
	while i < limit:

		# if less than my_max_integer_size
		if fib[i][0] < my_max_integer_size and fib[i+1][0] < my_max_integer_size:
			if fib[i][0] + fib[i+1][0] > my_max_integer_size:
				fib[i+2].append(my_max_integer_size)
				# one remander always for this case
				fib[i+2].append((fib[i][0] + fib[i+1][0]) % my_max_integer_size)
			else:
				fib[i+2].append(fib[i][0] + fib[i+1][0])

		# if greater than my_max_integer_size
		value1 = fib[i].pop(0)
		while value1 == my_max_integer_size:
			fib[i+2].append(my_max_integer_size)
			value1 = fib[i].pop(0)

		value2 = fib[i+1].pop(0)
		while value2 == my_max_integer_size:
			fib[i+2].append(my_max_integer_size)
			value2 = fib[i+1].pop(0)

		# if remainder exists
		remainder = (value1 % my_max_integer_size) + (value2 % my_max_integer_size)
		if remainder > my_max_integer_size:
			fib[i+2].append(my_max_integer_size)
			fib[i+2].append(remainder - my_max_integer_size)

		yield fib[i+2]
		i += 1


limit = 50
fibobj = generate_fib_seq(limit)

n = 0
for values_list in fibobj:

	print(f"{n}: {values_list}")
	n += 1




