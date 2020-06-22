import random
from collections import defaultdict, deque
import networkx as nx

with open('input/15.txt') as f:
    opcodes = [int(x) for x in f.read().strip().split(',')]
    opcodes = defaultdict(int, enumerate(map(int, opcodes)))


def machine():
    output = []
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


WALL = 0
SUCCESSFUL_MOVE = 1
OXYGEN = 2

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4


def get_opposite(move):
    return {NORTH: SOUTH, SOUTH: NORTH, WEST: EAST, EAST: WEST}.get(move)


def make_move(position, direction):
    moves = {NORTH: (0, 1), SOUTH: (0, -1), WEST: (-1, 0), EAST: (1, 0)}
    return tuple(map(sum, zip(position, moves.get(direction))))


def get_neighbours(pos):
    return [make_move(pos, direction) for direction in range(1, 5)]


def get_ship_map():
    m = machine()
    next(m)
    pos = (0, 0)
    ship_map = {}
    moves = []

    # contains directions (value) we haven't attempted for each
    # coordinate (key)
    unexplored = {}

    while True:
        if pos not in unexplored:
            unexplored[pos] = [1, 2, 3, 4]

        if unexplored[pos]:
            back_tracking = False
            move = unexplored[pos].pop()
        else:
            back_tracking = True

            if not moves:  # backtracked to start
                return ship_map

            prev = moves.pop()
            move = get_opposite(prev)

        status = m.send(move)
        ss = next(m)

        if status in (SUCCESSFUL_MOVE, OXYGEN):
            pos = make_move(pos, move)
            ship_map[pos] = status

            if not back_tracking:
                moves.append(move)


def shortest_path(graph, start, target):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if graph.get(node) == target:
            return len(path) - 1

        if node not in visited:
            visited.add(node)
            for neighbour in get_neighbours(node):
                if graph.get(node, 0) == 1:
                    new_path = path.copy()
                    new_path.append(neighbour)
                    queue.append(new_path)


droid_map = get_ship_map()
print(shortest_path(droid_map, start=(0, 0), target=OXYGEN))


def flood(ship_map, pos, step=0):
    if ship_map.get(pos, "#") == "#":
        return step - 1

    ship_map[pos] = "#"
    n1, n2, n3, n4 = get_neighbours(pos)

    return max(flood(ship_map, n1, step + 1),
               flood(ship_map, n2, step + 1),
               flood(ship_map, n3, step + 1),
               flood(ship_map, n4, step + 1))


oxygen_location = None
for coordinate in droid_map:
    if droid_map[coordinate] == OXYGEN:
        oxygen_location = coordinate

print(flood(droid_map, oxygen_location))
