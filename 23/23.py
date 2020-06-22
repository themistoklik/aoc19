from collections import defaultdict, deque
from itertools import count

with open('in.txt') as f:
    opcodes = [int(x) for x in f.read().strip().split(',')]
    opcodes = defaultdict(int, enumerate(map(int, opcodes)))


def machine(m):
    p = m
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
            # inp = -1
            # if talk[id][-1]:
            #   inp=talk[id].pop()
            #   print(inp,id)
            p[pos[0]] = yield
            ip += 2
        elif op == 4:
            # output.append(a)
            yield a
            ip += 2
            # if len(output) == 3:
            #     res = output[:]
            #     output = []
            #     print(res)
            #     talk[res[0]] = (res[1],res[2])
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


qs = [deque() for _ in range(50)]
machines = []
nat = [0, 0]
last_seen_nat = [-111, -111]
for i in range(50):
    m = machine(opcodes.copy())
    machines.append(m)
    next(m)
    m.send(i)
run = True
while run:
    for i, q in enumerate(qs):
        p = machines[i]  # it is in input state
        if len(q) >= 2:
            v = p.send(q.popleft())
            v = p.send(q.popleft())
        else:
            v = p.send(-1)
        while v is not None:
            addr = v
            x, y, v = next(p), next(p), next(p)
            if addr == 255:
                nat = [x, y]
                continue
                # print(x,y) #for part1
                # run = False
                # break
            qs[addr].append(x)
            qs[addr].append(y)

    if any(qs): continue
    if last_seen_nat[1] == nat[1]: print(nat[1])
    last_seen_nat = nat
    qs[0].append(nat[0])
    qs[0].append(nat[1])