from collections import defaultdict

with open('input/13.txt') as f:
    opcodes = [int(x) for x in f.read().strip().split(',')]
    opcodes = defaultdict(int, enumerate(map(int, opcodes)))
    opcodes[0] = 2


def machine():
    output = []
    p = opcodes  # grab a fresh one + extra mem ghetto way
    ip = 0
    rel_base = 0
    while True:
        cmd = p[ip]
        op = cmd % 100
        # C B A .. modes can be 0 1 or 2
        mode = [cmd // 100 % 10, cmd // 1000 % 10, cmd // 10000 % 10]
        values = [0, 0, 0]
        # positions of A B C
        pos = [p[i] for i in range(ip + 1, ip + 4)]

        # this is from reddit too. Making it a generator and abstracting or the if else out of every op is the lawd's work
        for i in range(3):
            if mode[i] == 0:
                values[i] = p[pos[i]]
            elif mode[i] == 2:
                pos[i] = rel_base + pos[i]
                values[i] = p[pos[i]]
            else:
                values[i] = pos[i]
                pos[i] = ip + i + 1

        a, b, c = values

        if op == 1:
            p[pos[2]] = a + b
            ip += 4
        elif op == 2:
            p[pos[2]] = a * b
            ip += 4
        elif op == 3:
            p[pos[0]] = yield  # wait for input, so state-machiney
            ip += 2
        elif op == 4:
            output.append(a)
            ip += 2
            if len(output) == 3:
                res = output[:]
                output = []
                yield res
        elif op == 5:
            if a != 0:
                ip = b
            else:
                ip += 3
        elif op == 6:
            if a == 0:
                ip = b
            else:
                ip += 3
        elif op == 7:
            p[pos[2]] = 1 if a < b else 0
            ip += 4
        elif op == 8:
            p[pos[2]] = 1 if a == b else 0
            ip += 4
        elif op == 9:
            rel_base += a
            ip += 2
        elif op == 99:
            break


m = machine()
outputs = []
tile_ids = {0: ' ', 1: '|', 2: '#', 3: '~', 4: '@'}


def display(grid):
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)
    # print(max_x, max_y)
    screen = [[' ' for i in range(max_x + 1)] for j in range(max_y + 1)]
    for k, v in grid.items():
        x, y = k
        screen[y][x] = tile_ids[v]
    for line in screen:
        print(''.join(line))


while True:  # part1
    try:
        outputs.append(next(m))
    except StopIteration:
        break
display({(o[0], o[1]): o[2] for o in outputs})
# print(len([o for o in outputs if o[-1] == 2]))  # ans1
