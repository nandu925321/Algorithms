# Uses python3
import sys
def dp_min_ops(n):
    all_parents = [None] * (n + 1)
    all_min_ops = [0] + [None] * n

    for k in range(1, n + 1):
        curr_parent = k - 1
        curr_min_ops = all_min_ops[curr_parent] + 1

        if k % 3 == 0:
            parent = k // 3
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                curr_parent, curr_min_ops = parent, num_ops

        if k % 2 == 0:
            parent = k // 2
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                curr_parent, curr_min_ops = parent, num_ops

        all_parents[k], all_min_ops[k] = curr_parent, curr_min_ops

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = all_parents[k]
    numbers.reverse()

    return  numbers


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(dp_min_ops(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
