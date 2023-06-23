#! python3 
# How many different ways can £2 be made using any number of coins?
# Work in Progress

import pdb

limit = 200

x_inc = 200
y_inc = 100
a_inc = 50
b_inc = 20
c_inc = 10
d_inc = 5
e_inc = 2
f_inc = 1

count = 0
for x_sum in range(0, limit + 1, x_inc):

	for y_sum in range(0, (limit - x_sum) + 1, y_inc):

		a_start = x_sum + y_sum

		for a_sum in range(0, (limit - a_start) + 1, a_inc):

			b_start = x_sum + y_sum + a_sum

			for b_sum in range(0, (limit - b_start) + 1, b_inc):

				c_start = x_sum + y_sum + a_sum + b_sum

				for c_sum in range(0, (limit - c_start) + 1, c_inc):

					d_start = x_sum + y_sum + a_sum + b_sum + c_sum

					for d_sum in range(0, (limit - d_start) + 1, d_inc):

						e_start = x_sum + y_sum + a_sum + b_sum + c_sum + d_sum

						for e_sum in range(0, (limit - e_start) + 1, e_inc):

							count += 1

print(count)


							#if (limit - (x_sum + y_sum + a_sum + b_sum + c_sum + d_sum + e_sum)):
								#f = (limit - (x_sum + y_sum + a_sum + b_sum + c_sum + d_sum + e_sum))