#! python3
# What is the largest prime factor of the number 600851475143?
# Finished

num = 600851475143

def seive(n):

	primelist = [True] * n
	primelist[0] = primelist[1] = False

	for i, isprime in enumerate(primelist):
		if isprime:
			yield i
			for notprime in range(i*i, n, i):
				primelist[notprime] = False

mylist = [i for i in seive(int(num ** .5)) if num % i == 0]
print(max(mylist))