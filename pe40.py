#! python3
# Champernowne's Constant problem #40  https://projecteuler.net/problem=40
# Finished

from math import log10, floor

# number of numbers for each singles, doubles, ... etc.
nn1 = 9
nn2 = (nn1 ** 2) + nn1	
nn3 = (1000 - 1) - (nn1 + nn2)	
nn4 = (10000 - 1) - (nn1 + nn2 + nn3)
nn5 = (100000 - 1) - (nn1 + nn2 + nn3 + nn4)
nn6 = (1_000_000 - 1) - (nn1 + nn2 + nn3 + nn4 + nn5)

len_dict = {0: nn1, 1: nn2, 2: nn3, 3: nn4, 4: nn5, 5: nn6}
index_list = [10, 100, 1000, 10000, 100000, 1_000_000]
start_values = [1, 10, 100, 1000, 10000, 100000, 1_000_000]
# for each of the start_values, define divider values for below
bases = [50, 33, 25, 20, 16, 14]

product = 1
# for each of the indexes (excluding index 1 which just equals number 1)
for current_index in index_list:
	remaining_digits_save = 0
	# ...  select nn#'s 0-5
	for len_dict_index in range(0, 6):
		# ... if this is not the first pass of loop
		if len_dict_index > 0:
			# ... update remaining_digits with remaining_digits minus this pass's set of number of TOTAL DIGITS
			remaining_digits = (remaining_digits - (len_dict[len_dict_index] * int(log10(index_list[len_dict_index]))))
		else:
			# ... if first pass of loop, set remaining_digits with the current index into Champernowne's constant minus this pass's set of number of TOTAL DIGITS
			remaining_digits = (current_index - (len_dict[len_dict_index] * int(log10(index_list[len_dict_index]))))
		# check if we passed the special number at index current_index
		if remaining_digits < 0:
			# ... break and go to while loop below
			break
		# save remaining digit count to use the previous remaining digit count for loop below to find how far we are from the special number
		remaining_digits_save = remaining_digits
	# found an area of numbers where index is at, divide remaining_digits_save by the length of the singles, doubles, triples etc numbers
	distance_float = (remaining_digits_save / int(log10(start_values[len_dict_index + 1])))
	if current_index == 10:
		distance_float = 0
	distance_remainder_float = distance_float % 1
	distance = int(distance_float - distance_remainder_float)
	distance_remainder_as_a_2_digit_int = floor(distance_remainder_float * 10)
	if current_index != 10 and len(str(distance_remainder_as_a_2_digit_int)) == 1:
		distance_remainder_as_a_2_digit_int = int(str(distance_remainder_as_a_2_digit_int) + '0')
	# dont need to consider when index into number is 0, because that means it divides evenly, distance will pick up the value
	index_into_number = distance_remainder_as_a_2_digit_int // bases[len_dict_index - 1]
	special_number = start_values[len_dict_index] + distance
	special_number_str = list(str(special_number))
	product = product * int(special_number_str[index_into_number])
	print(f"special digit: {int(special_number_str[index_into_number])}, special number: {special_number}, index into special number: {index_into_number}")

print(f"product: {product}")
