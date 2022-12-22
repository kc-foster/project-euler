#! python3

num = 600851475143

def seive(n):

	primelist = [True] * n
	primelist[0] = primelist[1] = False

	for i, isprime in enumerate(primelist):
		if isprime:
			yield i
			for notprime in range(i*i, n, i):	# i*i some kind of trick
				primelist[notprime] = False

mylist = [i for i in seive(10000) if num % i == 0]



		

