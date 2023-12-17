#! python3
# Coded Triangle Numbers problem #42  https://projecteuler.net/problem=42
# Finished

alpha_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,}

with open('0042_words.txt', 'r') as file:
	file_content = file.read()
	words = [word.strip('"') for word in file_content.split('","')]
	maxlen = 0
	for word in words:
		wordlen = len(word)
		if wordlen > maxlen:
			maxlen = wordlen

	max_word_value = maxlen * alpha_values['Z']
	tri = 1
	x = 2
	list_of_tri_nums = []
	while tri < max_word_value:
		list_of_tri_nums.append(tri)
		tri += x
		x += 1

	special_words = []
	for word in words:
		word_value = 0
		for char in word:
			word_value += alpha_values[char]
		i = 0
		if word_value in list_of_tri_nums:
			special_words.append(word)

	print(special_words) 
	print(len(special_words))