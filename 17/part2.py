from collections import defaultdict

with open('input/17.txt') as f:
    opcodes = [int(x) for x in f.read().strip().split(',')]
    opcodes = defaultdict(int, enumerate(map(int, opcodes)))


def machine():
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


out = []
m = machine()
ss = next(m)
sss = []
while ss and ss < 255:
    sss.append(ss)
    ss = next(m)
sss = ''.join([chr(c) for c in sss])
path = [ord(c) for c in "A,B,A,C,A,B,A,C,B,C\n"]
A = [ord(c) for c in "R,4,L,12,L,8,R,4\n"]
B = [ord(c) for c in "L,8,R,10,R,10,R,6\n"]
C = [ord(c) for c in "R,4,R,10,L,12\n"]
feed = [ord(c) for c in "n\n"]
inputs = [path, A, B, C, feed]
oo = []
for inp in inputs:
    for i in inp:
        o = m.send(i)
        if o is not None:
            ssss = ""
            while o is not None:
                try:
                    o = next(m)
                    oo.append(o if o is not None else 1)
                    ssss = ''.join([chr(c) for c in oo])
                except StopIteration:
                    print(ssss)
                    break



print(out, o)
