#! python3 
# How many different ways can £2 be made using any number of coins?
# Work in Progress

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

for x_sum in range(0, limit + 1, x_inc):

	y = 0

	for y_sum in range(x_sum, limit + 1, y_inc):

		a = 0

		for a_sum in range(x_sum + y_sum, limit + 1, a_inc):

			b = 0

			for b_sum in range(x_sum + y_sum + a_sum, limit + 1, b_inc):

				c = 0

				for c_sum in range(x_sum + y_sum + a_sum + b_sum, limit + 1, c_inc):

					d = 0

					for d_sum in range(x_sum + y_sum + a_sum + b_sum + c_sum, limit + 1, d_inc):

						e = 0

						for e_sum in range(x_sum + y_sum + a_sum + b_sum + c_sum + d_sum, limit + 1, e_inc):

							if (limit - (x_sum + y_sum + a_sum + b_sum + c_sum + d_sum + e_sum)) > 0:
								f = (limit - (x_sum + y_sum + a_sum + b_sum + c_sum + d_sum + e_sum))

							temp_seqs = [x, y, a, b, c, d, e, f]
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
print(unique_seqs)
print("\n")

