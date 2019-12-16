from functools import reduce
from itertools import cycle

with open('input/16.txt') as f:
    digits = [int(d) for d in f.readline().strip()]


def rotate(l, n):
    return l[n:] + l[:n]


def construct_pattern(n):
    pattern = [0, 1, 0, -1]
    return rotate(list(reduce(lambda x, y: x + y, [p for p in zip(*(n + 1) * [pattern])])), 1)


new_digits = []
for phase in range(100):
    for i in range(len(digits)):
        res = abs(sum([(p[0] * p[1]) for p in zip(digits, cycle(construct_pattern(i)))])) % 10
        new_digits.append(res)
    digits = new_digits[:]
    new_digits = []

print(''.join([str(x) for x in digits])[:8])  # part 1
