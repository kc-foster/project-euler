#! python3
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# Work in Progress

def number_combinations(n):
    # Base case: If n is a single-digit number, return it as a list of single-digit strings
    if n < 10:
        return [str(n)]

    # Recursive case: Split the number into its last digit and the remaining digits
    last_digit = n % 10
    remaining_digits = n // 10

    # Recursive call to generate combinations of the remaining digits
    combinations = number_combinations(remaining_digits)

    # Generate combinations by adding the last digit to each combination
    result = []
    for combination in combinations:
        for i in range(len(combination) + 1):
            combo = (combination[:i] + str(last_digit) + combination[i:])
            result.append(combo)

    return result

newlist = number_combinations(1234567890)
newlist.sort()
print(newlist[999999])