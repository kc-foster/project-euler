#! python3
# How many routes are there thru a 20x20 grid starting at the top left corner?
# Work in Progress

started = combos_count = combo_total = 0
combos = []

def permutation(choose, lim):

	global started, combos_count, combo_total

	start_permutation = (lim == 1)

	if start_permutation and not started:

		started = 1

		return [['0'], ['1']]

	if not started:

		lim -= 1

		combinations = permutation(choose, lim)

	combos = []

	for combination in combinations:

		for i in range(len(combination)):

			if len(combination) > 20:

				for x in combination:

					combo_total += int(x)

				if combo_total > 20 or (combo_total < (len(combination) - 20)):

					continue

			for k in choose:

				combos.append(combination[:i] + list(str(k)) + combination[i:])

				combos_count += 1

	if len(combinations[-1]) == 40:

		return combos_count		# return combos_count for print() statement

	return combos 	# return combos to combinations

choose = ['0', '1']
limit = 40
print(permutation(choose, limit))
