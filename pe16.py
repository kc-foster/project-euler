#! python3

def compute():
	
	a = 2
	n = 1000
	mylist = []

	while n > 2:
		if n % 2 == 0:
			n = n//2
			a = a**2
		else:
			mylist.append(a)
			n = n//2
			a = a**2

	product = a**n
	for x in mylist:
		product *= x

	result = 0
	for num in str(product):
		result += int(num)

	print(result)

compute()
quit()

# 16**125
# 256** **62