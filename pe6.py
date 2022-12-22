
#! python3

import math

d = math.pow((50 * 101), 2)
s = 0
for i in range(1, 101):
	s += i * i

answer = d - s
print(str(answer))