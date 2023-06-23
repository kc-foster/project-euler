#! python3 
# How many different ways can £2 be made using any number of coins?
# Work in Progress

import pdb
from array import array

unique_seqs = [[]]
limit = 200

x_inc = 200
y_inc = 100
a_inc = 50
b_inc = 20
c_inc = 10
d_inc = 5
e_inc = 2
f_inc = 1

x = y = a = b = c = d = e = f = 0

for x_sum in range(0, limit, x_inc):

	y = 0

	for y_sum in range(0, limit - x_sum, y_inc):

		a = 0

		a_start = x_sum + y_sum

		for a_sum in range(0, limit - a_start, a_inc):

			b = 0

			b_start = x_sum + y_sum + a_sum

			for b_sum in range(0, limit - b_start, b_inc):

				c = 0

				c_start = x_sum + y_sum + a_sum + b_sum

				for c_sum in range(0, limit - c_start, c_inc):

					d = 0

					d_start = x_sum + y_sum + a_sum + b_sum + c_sum

					for d_sum in range(0, limit - d_start, d_inc):

						e = 0

						e_start = x_sum + y_sum + a_sum + b_sum + c_sum + d_sum

						for e_sum in range(0, limit - e_start, e_inc):

							if (limit - (x_sum + y_sum + a_sum + b_sum + c_sum + d_sum + e_sum)):
								f = (limit - (x_sum + y_sum + a_sum + b_sum + c_sum + d_sum + e_sum))

							temp_seqs = array('B', [x, y, a, b, c, d, e, f])
							unique_seqs.append(temp_seqs)

							f = 0

							e += 1

						d += 1

					c += 1

				b += 1

			a += 1

		y += 1

	x += 1

unique_seqs.pop(0)
print(len(unique_seqs))


