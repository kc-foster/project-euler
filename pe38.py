#! python3
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, 3 ,..., n) where n > 1?
# Work in Progress



# Its larger than the obvious pandigital 918273645
# no matter the integers p, q, prduct will be at most int(log10(p))+1 + int(log10(q))+1
# large p for low q, and vice versa
# for p = 1 digit ... 2 digit, then max q is 5
#  


n = 987654321       # largest possible pandigital
limit = 918273645 # smallest 

# pandigital_list = number_combinations(n, start)
ranges = [[1, 2], [1, 2, 3], [1, 2, 3, 4]]

p_upper_bound = [9999, 333, 33]
p_lower_bound = [5000, 100, 25]
current_largest = int(limit)

for k in range(3):
    for p in range(p_lower_bound[k], p_upper_bound[k]+1, 1):
        string = ''
        for j in range(len(ranges[k])):
            string += str(p * ranges[k][j])
        nine_digit_num = int(string)
        interesting_num = (nine_digit_num > limit)
        if interesting_num:
            digit_list = [int(digit) for digit in str(nine_digit_num)]
            if 0 in digit_list:
                continue
            pandigital = len(set(digit_list)) == 9
            if pandigital:
                larger = (nine_digit_num > current_largest)
                if larger:
                    current_largest = nine_digit_num
        nine_digit_num = 0


print(current_largest)