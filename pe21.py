#! python3
# Problem 21: Evaluate the sum of all the amicable numbers under 10000.
# Finished

import math

# you can append two divisors at a time
def divisors(n):

	divisorslist = [1]

	for i in range(2, int(math.sqrt(n) + 1), 1):
		if n % i == 0:
			divisorslist.append(n // i)
			divisorslist.append(i)

	return divisorslist

nsum = 0
check = 0
amicable = []
MAX = 10000

myrange = []
for x in range(1, MAX, 1):
	myrange.append(x)

for n in myrange:
	if n == 0:
		continue
	nsum = sum(divisors(n))
	check = sum(divisors(nsum))
	if check == n and nsum != n:
		amicable.append(n)
		amicable.append(nsum)
		myrange[n - 1] = 0
		myrange[nsum - 1] = 0
	# ignore perfect nums	
	elif check == n and nsum == n:
		continue

total = 0
for num in amicable:
	total += num

print(amicable)
print(total)

# test amicable list
for a in amicable:
	sum_a = sum(divisors(a))
	sum_b = sum(divisors(sum_a))
	if a == sum_b:
		continue
	else:
		print(f"fail at {a}: sum a: {sum_a}, sum b: {sum_b}")
