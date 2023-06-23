#! python3
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Finished

with open("pe13_num.txt", "r") as file:
	content = file.read()

	integers = [[0] for _ in range(100)]
	pos = 0
	for character in content:
		if character == '\n':
			pos += 1
			continue
		integers[pos].append(int(character))

for pos in range(100):
	integers[pos].pop(0)

large_nums = []
for integer_list in integers:
	large_nums.append(int("".join(str(i) for i in integer_list)))

print(sum(large_nums))