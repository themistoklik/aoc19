from collections import defaultdict


def machine():
    with open('input/19.txt') as f:
        opcodes = [int(x) for x in f.read().strip().split(',')]
        opcodes = defaultdict(int, enumerate(map(int, opcodes)))

    p = opcodes
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
            p[pos[0]] = yield
            ip += 2
        elif op == 4:
            yield a
            ip += 2
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


def send_drone(x, y):
    m = machine()
    next(m)
    m.send(x)
    return m.send(y)


grid = {}
for x in range(50):
    for y in range(50):
        grid[(x, y)] = send_drone(x, y)

print(sum(grid.values()))  # part1

x, y = 0, 0
while not send_drone(x + 99, y):
    y += 1
    if not send_drone(x, y + 99): # first tall enough(y++) boundary will be met by moving right
        x += 1

print(x*10000+y) #ans2
