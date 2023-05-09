#! python3

import math

def num_digits_fibonacci(n):

    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(n-2):
            a, b = b, a+b

        return math.log10(b) + 1



n = 1000
while num_digits_fibonacci(n) < 1000:
    n += 1

print(n)