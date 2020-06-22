inp = """#####
.#.##
#...#
..###
#.##.
"""


def get_neighbors(bugs, point):
    n = 0
    x, y, level = point
    # get simple cross first
    for p in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        xx = x + p[0]
        yy = y + p[1]
        if x == y == 2 or (xx not in range(0, 5) and yy not in range(0, 5)): continue
        if (xx, yy, level) in bugs: n += 1

    # neighbors of level -1 (whole cells)
    if x == 0 and (1, 2, level - 1) in bugs: n += 1
    if x == 4 and (3, 2, level - 1) in bugs: n += 1
    if y == 0 and (2, 1, level - 1) in bugs: n += 1
    if y == 4 and (2, 3, level - 1) in bugs: n += 1

    # neighbors of middle cell in level+1
    if (x, y) == (1, 2):
        n += sum([(0, y, level + 1) in bugs for y in range(5)])  # whole first row
    elif (x, y) == (2, 1):
        n += sum([(x, 0, level + 1) in bugs for x in range(5)])  # whole first col
    elif (x, y) == (3, 2):
        n += sum([(4, y, level + 1) in bugs for y in range(5)])  # whole last row
    elif (x, y) == (2, 3):  # whole last col
        n += sum([(x, 4, level + 1) in bugs for x in range(5)])

    return n


def evolve(bugs):
    nbugs = set()
    min_level = min(bugs, key=lambda x: x[2])[-1]
    max_level = max(bugs, key=lambda x: x[2])[-1]

    for level in range(min_level - 1, max_level + 2):
        for x in range(5):
            for y in range(5):
                if x == y == 2: continue
                ns = get_neighbors(bugs, (x, y, level))
                if (x, y, level) in bugs:
                    if ns == 1: nbugs.add((x, y, level))
                elif ns in [1, 2]:
                    nbugs.add((x, y, level))
    return nbugs


inp = inp.splitlines()
bugs = set()
h, w = len(inp), len(inp[0])

# init
for x in range(h):
    for y in range(w):
        if inp[x][y] == '#': bugs.add((x, y, 0))

for _ in range(200):
    bugs = evolve(bugs)
print(len(bugs))