#! python3
# What is the 10 001st prime number?
# FInished

def sieve(limit):

    primes = [True] * (limit+1)
    iter = 0

    while iter < limit**0.5 :
        if iter < 2:
            primes[iter]= False

        elif primes[iter]:
            for i in range(iter*2, limit+1, iter):
                primes[i] = False

        iter+=1

    return [x for x in range(limit+1) if primes[x]]


# just try different maximums
primes = sieve(150000)

print(primes[10001])