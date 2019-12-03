# dumb solution for now
# notice that bumping position 1 by one for example gives greater increase than position 2
# we can heuristically binary search based on ^

def fresh_opcodes():
    with open('input/1.txt') as f:
        return list(map(lambda x: int(x), f.read().split(',')))


ops = {1: lambda x, y: x + y, 2: lambda x, y: x * y}


def calc(opcodes):
    index = 0

    while index < len(opcodes):
        if opcodes[index] == 99:
            break
        opcodes[opcodes[index + 3]] = ops[opcodes[index]](opcodes[opcodes[index + 2]], opcodes[opcodes[index + 1]])
        index += 4

    return opcodes[0]


def solve2():
    target = 19690720

    for i in range(0, 100):
        for j in range(0, 100):
            opcodes = fresh_opcodes()
            opcodes[1] = i
            opcodes[2] = j
            if calc(opcodes) == target:
                return (i, j)


print(solve2())
