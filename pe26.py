#! python3 
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# Finished

import math, pdb
limit = 2000

cycles_list = []
for denominator in range(2, 1001):
    save_denominator = denominator
    quotient_list = []
    remainder = 1
    counter = 0

    while (counter == 0) or (remainder != 0) and (quotient_list[0:int((counter)//2)] != quotient_list[int((counter)//2):counter]) and (counter != limit):

        y = int(math.log10(denominator) + 1)
        while (((remainder * (10 ** (int(math.log10(denominator)) + y)))) // denominator) > 9:
            y -= 1

        nominator = remainder * (10 ** (int(math.log10(denominator)) + y))
        quotient = int(nominator // denominator)

        if remainder == 1:
            for x in range(int(math.log10(nominator)), 1, -1):
                if x == 1:
                    break
                quotient_list.append(0)
                counter += 1
                if denominator % 10 == 0:
                    quotient //= 10

        quotient_list.append(quotient)
        remainder = nominator % denominator

        counter += 1

    #print(f"denominator: {save_denominator} quotient_list: {quotient_list}")

    if limit == counter:
        # check for offset cycles
        offset = 1
        while (offset < (limit - 2)):
            positionk = 1
            while (quotient_list[(offset):(offset + positionk)]) != (quotient_list[(offset + positionk):(offset + (positionk * 2))]):
                if ((offset + (positionk * 2)) >= limit):
                    break
                positionk += 1
            if (quotient_list[(offset):(offset + positionk)]) == (quotient_list[(offset + positionk):(offset + (positionk * 2))]):
                break
            offset += 1

        #print(f"cycle length for {save_denominator}: {positionk}")
        cycles_list.append(positionk)
    elif (quotient_list[0:int((counter)//2)] == quotient_list[int((counter)//2):counter]):
        #print(f"cycle length for {save_denominator}: {(counter)//2}")
        cycles_list.append(counter//2)
    else:
        #print(f"cycle length for {save_denominator}: 0")
        cycles_list.append(0)

# add two to index because the loop starts at 2
#print(cycles_list)
result = max(cycles_list)
print(f"maximum cycle length: {result} index: {cycles_list.index(result) + 2}")
