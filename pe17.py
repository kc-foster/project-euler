#! python3

eng_odd_digits_3 = {0: 0, 1: 3, 2: 6, 3: 6, 4: 8, 5: 7} # odd spelling for 10 11 12 13 15.
eng_digit_4 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4} # singles, but also qualifies hundreds
eng_digit_3 = {0: 0, 1: 4, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6} # tens
eng_digit_2 = {0: 0, 1: 7} # hundred
eng_digit_1 = {0: 0, 1: 8} # thousand

# nine hundred and ninty nine 23
total = 0
xtotal = 0
running_total = 0
for x in range(1, 1001, 1):
	digit1 = 0
	digit2 = 0
	digit3 = 0
	digit4 = 0
	digit1 = x // 1000						# thousands
	if digit1:
		total += eng_digit_4[1] + eng_digit_1[1]
		print(f"total: {total}")
		break
	else:
		digit2 = x // 100 									# hundreds
		digit3 = ((x - (digit2 * 100)) // 10) 				# tens
		digit4 = (((x - (digit2 * 100)) - (digit3 * 10)))	# singles

		if digit2 and not digit3 and not digit4:
			total += eng_digit_2[1] + eng_digit_4[digit2]
		elif digit2 and (digit3 or digit4):
			total += eng_digit_2[1] + eng_digit_4[digit2] + 3

		if (digit3 == 1) and (digit4 == 0):
			total += eng_odd_digits_3[1]		# +17 nine hundred and ten
			continue
		elif (digit3 == 1) and (digit4 == 1):
			total += eng_odd_digits_3[2]
			continue
		elif (digit3 == 1) and (digit4 == 2):
			total += eng_odd_digits_3[3]
			continue
		elif (digit3 == 1) and (digit4 == 3):
			total += eng_odd_digits_3[4]
			continue
		elif (digit3 == 1) and (digit4 == 5):
			total += eng_odd_digits_3[5]
			continue
		elif digit3:
			total += eng_digit_3[digit3]

		if digit4:
			total += eng_digit_4[digit4]
	#xtotal = eng_digit_1[digit1] + eng_digit_4[digit2] + eng_digit_2[1] + eng_digit_3[digit3] + eng_digit_4[digit4] + 3
	#running_total += xtotal
	#print(f"x: {x} running total: {running_total}, total: {total}")

exit()