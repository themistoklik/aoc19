from collections import Counter
from functools import reduce

with open('input/8.txt') as f:
    pixels = f.readlines()[0].strip()


def resolve_layer(first, second):
    for i in range(len(first)):
        if first[i] == '2':
            if second[i] != '2':
                first[i] = second[i]
    return "".join(first)


# frames are 25wide 6 tall
width = 25
height = 6
index = 0
max_zeros = 1234567890
ans1 = 0
frames = []
while index < len(pixels):
    frame = []
    total_zeros = 0
    for _ in range(height):
        row = [pixels[index:index + width]]
        total_zeros += Counter(row[0])['0']
        frame.append(row)
        index = index + width
    if total_zeros <= max_zeros:
        max_zeros = total_zeros
        total_counter = reduce(lambda x, y: x + y, map(lambda x: Counter(x[0]), frame))
        ans1 = total_counter['1'] * total_counter['2']
    frames.append(frame)

print(ans1)

for i in range(1, len(frames)):
    frames[0] = [resolve_layer(list(f[0]), list(s[0])) for f, s in zip(frames[0], frames[i])]
    frames[0] = list(map(lambda x: [x], frames[0]))

# ans2
[print(frame[0].replace('0', ' '), ) for frame in frames[0]]
