#! python3
# Problem 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Finished

new = 0
total = 0
fib = [1, 1]
while new < 4000000:
	xpos = len(fib) - 1
	ypos = len(fib) - 2
	new = fib[ypos] + fib[xpos]
	fib.append(new)
	if new % 2 == 0:
		total += new
		
print(total)