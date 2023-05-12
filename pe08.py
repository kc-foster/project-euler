#! python3
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
# 
import math

n0 = "73167176531330624919225119674426574742355349194934"
n1 = "96983520312774506326239578318016984801869478851843"
n2 = "85861560789112949495459501737958331952853208805511"
n3 = "12540698747158523863050715693290963295227443043557"
n4 = "66896648950445244523161731856403098711121722383113"
n5 = "62229893423380308135336276614282806444486645238749"
n6 = "30358907296290491560440772390713810515859307960866"
n7 = "70172427121883998797908792274921901699720888093776"
n8 = "65727333001053367881220235421809751254540594752243"
n9 = "52584907711670556013604839586446706324415722155397"
n10 = "53697817977846174064955149290862569321978468622482"
n11 = "83972241375657056057490261407972968652414535100474"
n12 = "82166370484403199890008895243450658541227588666881"
n13 = "16427171479924442928230863465674813919123162824586"
n14 = "17866458359124566529476545682848912883142607690042"
n15 = "24219022671055626321111109370544217506941658960408"
n16 = "07198403850962455444362981230987879927244284909188"
n17 = "84580156166097919133875499200524063689912560717606"
n18 = "05886116467109405077541002256983155200055935729725"
n19 = "71636269561882670428252483600823257530420752963450"

n_list = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19]

# first, get a list of numbers from these strings
numlist = []
for numstring in n_list:
	numlist = numlist + list(numstring)

integerlist = []
for strinteger in numlist:
	integerlist.append(int(strinteger))

# then, add each 13 numbers, printing max result
pos = 0
result = []
while (pos + 13) < len(integerlist):
	result.append(math.prod(integerlist[pos:pos+13]))
	pos += 1

print(max(result))


