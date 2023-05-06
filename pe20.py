#! python3

# n - (sum(base-x expansion of n)) / (base-x used) - 1
# base-x is the prime used

def base_conv(num, radix):

	digits = []
	digit = 0
	while num > 0:
		if num == 1:
			digits.append(num)
			break
		digit = num % radix		# 1 = 1 % 2
		num = num // radix 		# 1 = 3 // 2 110
		digits.append(digit)

	return digits

def seive(n):

	field = []
	for i in range(2, n, 1):
		field.append(i)

	for hop in field:
		if hop != 0:
			for zeroed in range((hop ** 2), n, hop):
				field[zeroed - 2] = 0

	for num in field:
		if num != 0:
			yield num

def compute():

	n = 100
	exponent = 0
	total = 1
	solution = 0
	seiveobj = seive(n)

	for x in seiveobj:
		expansion_sum = 0
		for converted in base_conv(n, x):
			expansion_sum += converted
		exponent = int((n - expansion_sum) / (x - 1))
		total *= x ** exponent

	for i in str(total):
		solution += int(i)

	print(solution)

compute()
quit()
