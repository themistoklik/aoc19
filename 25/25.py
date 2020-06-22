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

def readASCII(proc):
    s = ''
    try:
        q = next(proc)
        while q!=None:
            if s==10:
                print(s)
                s = ''
            else:
                s += chr(q)
            q = next(proc)
    except StopIteration:
        print('stopped')
        pass

    if len(s)>0:
        print(s)
        s = ''

    return q

def sendASCII(proc, txt):
    print(txt)
    out = ''
    s = ''
    try:
        for c in txt:
            q = proc.send(ord(c))
        while q!=None:
            out += chr(q)
            if q==10:
                print(s)
                s = ''
            else:
                if q>0x110000:
                    print('got number', q)
                else:
                    s += chr(q)
            q = next(proc)
    except StopIteration:
        print('stopped')
        pass

    if len(s)>0:
        print(s)
        s = ''
    return q or out

drops = """drop dark matter
drop whirled peas
drop weather machine
drop prime number
drop antenna
drop fixed point
drop astrolabe
drop coin
"""

cs="""east
east
east
east
east
take dark matter
west
west
west
west
west
north
take fixed point
north
take weather machine
south
south
east
take whirled peas
north
take coin
south
east
north
take prime number
south
west
north
west
south
take antenna
north
north
west
take astrolabe
east
south
east
south
west
north
north
east
south
"""+drops+"""south
take whirled peas
take fixed point
take prime number
take antenna
south
"""

inv = """coin
whirled peas
fixed point
prime number
antenna
weather machine
"""
# from itertools import combinations
# cc = combinations(inv.splitlines(), 4)
# ccc=[]
# for c in cc:
#   print(''.join(list(map(lambda x:'take '+x+'\n',c))))


n=6
combos=[]

m = machine(opcodes.copy())

readASCII(m)
# css = cmds+['south\n']
for c in cs.splitlines():
  q=sendASCII(m,c+'\n')
  if not isinstance(q,str):
      break

for i in range(0, 1<<n):
    gray=i^(i>>1)
    combos.append("{0:0{1}b}".format(gray,n))

action = {'0':'drop ','1':'take '}
item = {i:e for i,e in enumerate(inv.splitlines())}

cmds = [action[y]+item[x]+'\n' for x,y in enumerate('011110')]

# for c in combos:
  # cmds = [action[y]+item[x]+'\n' for x,y in enumerate(c)]
#   m = machine(opcodes.copy())

#   readASCII(m)
#   css = cmds+['south\n']
#   for c in cs.splitlines()+:
#     q=sendASCII(m,c+'\n')
#     if not isinstance(q,str):
#         break




















# take whirled peas
# take fixed point
# take prime number
# take weather machine

# take whirled peas
# take fixed point
# take antenna
# take weather machine

# take whirled peas
# take prime number
# take antenna
# take weather machine

# take fixed point
# take prime number
# take antenna
# take weather machine

#heccin gray dont work but it produces valid ops.oh well hybrid bruteforced it!!!!11!11