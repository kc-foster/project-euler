#! python3
# m > n, coprime, and both not odd

N = 500

import math

def mysort(coprimelist, i):	
	if coprimelist[i][0] > coprimelist[i][1]:
		return [coprimelist[i][0], coprimelist[i][1]]
	else:
		return None

coprimelist = []

for a in range(N):								# coprime list
	for b in range(N):
		if math.gcd(a, b) == 1:
			coprimelist.append([a, b])

sortedlist = [[0, 0]] * len(coprimelist)
counter = 0

for i in range(len(coprimelist)):				# m > n, sortedlist
	sortedlist[i] = mysort(coprimelist, i)
	if sortedlist[i] != None:
		counter += 1

del coprimelist									# free first list since its not being used

finallist = [[0, 0]] * counter
secondcounter = 0

for i in range(len(sortedlist)):				# both not odd, finallist
	if sortedlist[i] != None:
		if sortedlist[i][0] % 2 == 0 or sortedlist[i][1] % 2 == 0:
			finallist[secondcounter] = [sortedlist[i][0], sortedlist[i][1]]
			secondcounter += 1
		else:
			finallist[secondcounter] = None
			secondcounter += 1

del sortedlist									# free sortedlist because we have finallist

thirdcounter = 0

for i in range(len(finallist)):					# count how large lastlist needs to be
	if finallist[i] != None:
		thirdcounter += 1

lastlist = [[0, 0]] * thirdcounter
forthcounter = 0

for i in range(len(finallist)):
	if finallist[i] != None:
		lastlist[forthcounter] = [finallist[i][0], finallist[i][1]]
		forthcounter += 1

del finallist									# delete finallist not used

for i in range(len(lastlist)):
	m = lastlist[i][0]
	n = lastlist[i][1]
	for k in range(100):
		a = (k * (m**2 - n**2))
		b = (k * (2*m*n))
		c = (k * (m**2 + n**2))
		if (a + b + c == 1100):
			print(a, b, c, (a * b * c))
			break
		else:
			continue



