from collections import defaultdict

with open('input/11.txt') as f:
    opcodes = [int(x) for x in f.read().strip().split(',')]
    opcodes = defaultdict(int, enumerate(map(int, opcodes)))

plate = [[' '] * 110 for _ in range(110)]


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
            if len(output) == 2:
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


points = {}
facing = {'R': {'R': 'D', 'L': 'U'}, 'L': {'R': 'U', 'L': 'D'}, 'U': {'R': 'R', 'L': 'L'}, 'D': {'R': 'L', 'L': 'R'}}
move_to = {'R': lambda x: (x[0] + 1, x[1]), 'L': lambda x: (x[0] - 1, x[1]), 'U': lambda x: (x[0], x[1] - 1),
           'D': lambda x: (x[0], x[1] + 1)}
points[(0, 0)] = 1  # start @ black for part 1 @ white for part 2

at_point = (0, 0)
curr_direction = 'U'
robot = machine()
next(robot)
while True:
    try:
        try:
            color, next_dir = robot.send(points[at_point])
            next(robot)
        except KeyError:
            points[at_point] = color
            color, next_dir = robot.send(0)
            next(robot)
        points[at_point] = color
        curr_direction = facing[curr_direction]['L' if next_dir == 0 else 'R']
        at_point = move_to[curr_direction](at_point)
    except StopIteration:
        break
print(len(points))

for p in sorted(points.keys()):
    plate[p[1] + 10][p[0] + 10] = '#' if points[p] == 1 else '.'
for p in plate:
    print(''.join(p))
