from itertools import permutations

P = list(map(int, open('input/7.txt').read().strip().split(',')))

#this is similar to my day 5 but if you replace return with yield then magic happens!
def run_amplifier():
    p = P[:]  # grab a fresh one
    ip = 0
    while True:
        cmd = p[ip]
        op = cmd % 100
        if op == 1:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = a1 + a2
            ip += 4
        elif op == 2:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = a1 * a2
            ip += 4
        elif op == 3:
            p[p[ip + 1]] = yield  # wait for input, so state-machiney
            ip += 2
        elif op == 4:
            yield p[p[ip + 1]]
            ip += 2
        elif op == 5:
            a = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            if a != 0:
                ip = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            else:
                ip += 3
        elif op == 6:
            a = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            if a == 0:
                ip = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            else:
                ip += 3
        elif op == 7:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = 1 if a1 < a2 else 0
            ip += 4
        elif op == 8:
            a1 = p[ip + 1] if cmd // 100 % 10 == 1 else p[p[ip + 1]]
            a2 = p[ip + 2] if cmd // 1000 % 10 == 1 else p[p[ip + 2]]
            p[p[ip + 3]] = 1 if a1 == a2 else 0
            ip += 4
        elif op == 99:
            break


m = 0
for phase_perm in permutations(range(5, 10)):
    amp_states = []
    for phase in phase_perm:
        amp = run_amplifier()
        next(amp)
        amp.send(phase)
        amp_states.append(amp)
    signal = 0
    while True:
        for amp in amp_states:
            signal = amp.send(signal)
        try:
            for amp in amp_states:
                next(amp)
        except StopIteration:
            break #no more, halted
    m = max(m, signal)
print(m)
