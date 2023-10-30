#! python3
# What is the first 10 digits of the series 1 ** 1 + 2 ** 2 ...
# work in progress

result = 0
for i in range(1000, 0, -1):
	a = i
	mylist = []
	while i > 2:
		if not i % 2:
			i = i // 2
			a = a ** 2
		else:
			mylist.append(a)
			i = i // 2
			a = a ** 2

	c = 1
	for factor in mylist:
		c *= factor

	result += int(str(c * (a ** i))[-10:])

print(int(str(result)[-10:]))