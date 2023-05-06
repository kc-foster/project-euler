#! python3

MAX = 28124

def get_abundant_numbers():

    divisors_sum = [0] * MAX
    for i in range(1, MAX):
        for j in range(i * 2, MAX, i):
            divisors_sum[j] += i

    return [k for k, v in enumerate(divisors_sum) if v > k]

abundant_nums = get_abundant_numbers()

array = [False] * MAX

for i in abundant_nums:
    for j in abundant_nums:
        if (i + j) < MAX:
            array[(i + j)] = True
        else:
            break

result = [k for (k, v) in enumerate(array) if v != True]

print(sum(result))